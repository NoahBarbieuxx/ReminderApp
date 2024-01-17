from ReminderAppDL.ReminderManager import ReminderManager
from ReminderAppBL.Reminder import Reminder
from datetime import datetime, timedelta
from tkinter import messagebox
import tkinter as tk

class Aanpassen(tk.Toplevel):
    def __init__(self, master, reminder):
        tk.Toplevel.__init__(self, master)
        self.master = master
        self.reminder = reminder
        self.title("Reminder Aanpassen")

        self.geometry("800x460")
        self.resizable(width=False, height=False)  
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        # Main Frame aanmaken:
        self.frame = tk.Frame(self, bg="#727272")
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Bovenste Frame aanmaken en instellen:
        self.bovenste_frame = tk.Frame(self.frame, bg="#424242")
        self.bovenste_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        label_titel = tk.Label(self.bovenste_frame, text="Huidige Reminder", font=("Inter", 14, "bold"), bg="#FF4141", fg="white")
        label_titel.pack(pady=15)

        inhoud_frame = tk.Frame(self.bovenste_frame, bg="#424242")
        inhoud_frame.pack(padx=20, fill=tk.BOTH, expand=True)

        kolom_titels = ["Naam", "Beschrijving", "Datum", "Uur", "Meldingsdag"]
        for col, titel in enumerate(kolom_titels):
            breedte = 25 if titel == "Beschrijving" else 15
            label = tk.Label(inhoud_frame, text=titel, font=("Inter", 10, "bold"), bg="#FF4141", fg="white", width=breedte)
            label.grid(row=0, column=col, pady=(0, 5))

        tk.Label(inhoud_frame, text=reminder.naam, width=15, anchor="w").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(inhoud_frame, text=reminder.beschrijving, width=25, anchor="w").grid(row=1, column=1, padx=5, pady=5)
        tk.Label(inhoud_frame, text=reminder.datum, width=15).grid(row=1, column=2, padx=5, pady=5)
        tk.Label(inhoud_frame, text=reminder.uur, width=15).grid(row=1, column=3, padx=5, pady=5)
        tk.Label(inhoud_frame, text=reminder.meldingsdag, width=15).grid(row=1, column=4, padx=5, pady=5)

        # Onderste Frame aanmaken en instellen:
        self.onderste_frame = tk.Frame(self.frame, bg="#424242")
        self.onderste_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0,20))

        label_titel = tk.Label(self.onderste_frame, text="Pas Reminder Aan", font=("Inter", 14, "bold"), bg="#FF4141", fg="white")
        label_titel.pack(pady=15)

        update_frame = tk.Frame(self.onderste_frame, bg="#424242")
        update_frame.pack(padx=20, fill=tk.BOTH, expand=True)

        kolom_titels = ["Naam", "Beschrijving", "Datum", "Uur", "Meldingsdag"]
        for col, titel in enumerate(kolom_titels):
            breedte = 25 if titel == "Beschrijving" else 15
            label = tk.Label(update_frame, text=titel, font=("Inter", 10, "bold"), bg="#FF4141", fg="white", width=breedte)
            label.grid(row=0, column=col, pady=(0, 5))

        self.naam_var = tk.StringVar(value=reminder.naam)
        self.beschrijving_var = tk.StringVar(value=reminder.beschrijving)
        self.datum_var = tk.StringVar(value=reminder.datum)
        self.uur_var = tk.StringVar(value=reminder.uur)
        self.dagen_var = tk.StringVar(value=reminder.meldingsdag)

        self.naam_entry = tk.Entry(update_frame, textvariable=self.naam_var, width=15)
        self.naam_entry.grid(row=1, column=0, padx=5, pady=5)

        self.beschrijving_entry = tk.Entry(update_frame, textvariable=self.beschrijving_var, width=25)
        self.beschrijving_entry.grid(row=1, column=1, padx=5, pady=5)

        self.datum_entry = tk.Entry(update_frame, textvariable=self.datum_var, width=15)
        self.datum_entry.grid(row=1, column=2, padx=5, pady=5)

        self.uur_entry = tk.Entry(update_frame, textvariable=self.uur_var, width=15)
        self.uur_entry.grid(row=1, column=3, padx=5, pady=5)

        self.meldingsdag = tk.Entry(update_frame, textvariable=self.dagen_var, width=15)
        self.meldingsdag.grid(row=1, column=4, padx=5, pady=5)

        self.opslaan_button = tk.Button(update_frame, text="Opslaan", command=lambda: self.opslaan(reminder), bg="#FF4141", fg="white", bd=0, width=20)
        self.opslaan_button.grid(row=2, column=0, columnspan=5, pady=20)


    def opslaan(self, reminder):
        naam = self.naam_var.get()
        beschrijving = self.beschrijving_var.get()
        datum = self.datum_var.get()
        uur = self.uur_var.get()
        meldingsdag = self.meldingsdag.get()

        if not Reminder.check_inputs(naam, beschrijving, datum, uur, meldingsdag):
            return
        
        reminder_manager = ReminderManager()
        if reminder_manager.bestaat_reminder(naam, beschrijving, datum, uur, meldingsdag):
            messagebox.showerror("Error", "Deze reminder bestaat al!")
            return 

        if reminder_manager.bestaat_reminder(naam, beschrijving, datum, uur, meldingsdag):
            messagebox.showerror("Error", "Deze reminder bestaat al!")
            return

        reminder_manager.update_reminder(reminder, naam, beschrijving, datum, uur, meldingsdag)

        messagebox.showinfo("Succes", "Reminder succesvol aangepast!")

    def on_close(self):
        self.destroy()
        self.master.deiconify()