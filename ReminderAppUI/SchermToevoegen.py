from ReminderAppBL.Reminder import Reminder
from ReminderAppDL.ReminderManager import ReminderManager
from tkinter import messagebox
import tkinter as tk

class SchermToevoegen(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.master = master
        self.title("Reminder Toevoegen")

        self.geometry("800x460")
        self.resizable(width=False, height=False)  
        self.protocol("WM_DELETE_WINDOW", self.on_close)  


        # Main Frame aanmaken:
        self.frame = tk.Frame(self, bg="#727272")
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Linker Frame aanmaken en instellen:
        self.linker_frame = tk.Frame(self.frame, bg="#424242")
        self.linker_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(30, 5), pady=30)

        label_titel = tk.Label(self.linker_frame, text="Voorbeeldgegevens", font=("Inter", 14, "bold"), bg="#FF4141", fg="white")
        label_titel.pack(pady=(20,30))

        label_naam = tk.Label(self.linker_frame, text="Voer een naam in:", font=("Inter", 10, "bold"), bg="#FF4141", fg="white", width=26)
        label_naam.pack(padx=20)
        label_naam_entry = tk.Label(self.linker_frame, text="Dit is een reminder", font=("Inter", 9), width=30, justify="left")
        label_naam_entry.pack(padx=20, pady=(5,10))

        label_beschrijving = tk.Label(self.linker_frame, text="Voer een beschrijving in:", font=("Inter", 10, "bold"), bg="#FF4141", fg="white", width=26)
        label_beschrijving.pack(padx=20)
        label_beschrijving_entry = tk.Label(self.linker_frame, text="Dit is een beschrijving", font=("Inter", 9), width=30, justify="left")
        label_beschrijving_entry.pack(padx=20, pady=(5,10))
    
        label_datum = tk.Label(self.linker_frame, text="Voer een datum in:", font=("Inter", 10, "bold"), bg="#FF4141", fg="white", width=26)
        label_datum.pack(padx=20)
        label_datum_entry = tk.Label(self.linker_frame, text="12-20-2023 (mm-dd-yyyy)", font=("Inter", 9), width=30, justify="left")
        label_datum_entry.pack(padx=20, pady=(5, 10))

        label_uur = tk.Label(self.linker_frame, text="Voer een uur in:", font=("Inter", 10, "bold"), bg="#FF4141", fg="white", width=26)
        label_uur.pack(padx=20)
        label_uur_entry = tk.Label(self.linker_frame, text="10:30 (hh-mm)", font=("Inter", 9), width=30, justify="left")
        label_uur_entry.pack(padx=20, pady=(5,10))

        label_meldingsdag = tk.Label(self.linker_frame, text="Voer de meldingsdag in:", font=("Inter", 10, "bold"), bg="#FF4141", fg="white", width=26)
        label_meldingsdag.pack(padx=20)
        label_meldingsdag_entry = tk.Label(self.linker_frame, text="4", font=("Inter", 9), width=30, justify="left")
        label_meldingsdag_entry.pack(padx=20, pady=(5,10))
    
        # Rechter Frame aanmaken en instellen:
        self.rechter_frame = tk.Frame(self.frame, bg="#424242")
        self.rechter_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(30, 30), pady=30)

        label_titel = tk.Label(self.rechter_frame, text="Reminder Toevoegen", font=("Inter", 14, "bold"), bg="#FF4141", fg="white")
        label_titel.pack(pady=(20,30), padx=20)

        label_naam = tk.Label(self.rechter_frame, text="Voer een naam in:", font=("Inter", 10, "bold"), bg="#FF4141", fg="white", width=26)
        label_naam.pack(padx=20)
        self.naam_entry = tk.Entry(self.rechter_frame, width=35)
        self.naam_entry.pack(padx=20, pady=(5,10))

        label_beschrijving = tk.Label(self.rechter_frame, text="Voer een beschrijving in:", font=("Inter", 10, "bold"), bg="#FF4141", fg="white", width=26)
        label_beschrijving.pack(padx=20)
        self.beschrijving_entry = tk.Entry(self.rechter_frame, width=35)
        self.beschrijving_entry.pack(padx=20, pady=(5,10))

        label_datum = tk.Label(self.rechter_frame, text="Voer een datum in:", font=("Inter", 10, "bold"), bg="#FF4141", fg="white", width=26)
        label_datum.pack(padx=20)
        self.datum_entry = tk.Entry(self.rechter_frame, width=35)
        self.datum_entry.pack(padx=20, pady=(5,10))

        label_uur = tk.Label(self.rechter_frame, text="Voer een uur in:", font=("Inter", 10, "bold"), bg="#FF4141", fg="white", width=26)
        label_uur.pack(padx=20)
        self.uur_entry = tk.Entry(self.rechter_frame, width=35)
        self.uur_entry.pack(padx=20, pady=(5,10))

        label_meldingsdag = tk.Label(self.rechter_frame, text="Voer de meldingsdag in:", font=("Inter", 10, "bold"), bg="#FF4141", fg="white", width=26)
        label_meldingsdag.pack(padx=20)
        self.meldingsdag_entry = tk.Entry(self.rechter_frame, width=35)
        self.meldingsdag_entry.pack(padx=20, pady=(5,10))

        tk.Button(self.rechter_frame, text="Toevoegen", command=self.reminder_toevoegen, width=15, font=("Inter", 10, "bold"), bg="#FF4141", fg="white", bd=0).pack()

    def reminder_toevoegen(self):
        naam = self.naam_entry.get()
        beschrijving = self.beschrijving_entry.get()
        datum = self.datum_entry.get()
        uur = self.uur_entry.get()
        meldingsdag = self.meldingsdag_entry.get()

        if not Reminder.check_inputs(naam, beschrijving, datum, uur, meldingsdag):
            return
        
        reminder_manager = ReminderManager()
        if reminder_manager.bestaat_reminder(naam, beschrijving, datum, uur, meldingsdag):
            messagebox.showerror("Error", "Deze reminder bestaat al!")
            return

        reminder = Reminder(naam, beschrijving, datum, uur, meldingsdag)
        reminder_manager.voeg_reminder_toe(reminder)
        reminder.herinnering_melding(self.master.root)
        messagebox.showinfo("Succes", "Reminder succesvol toegevoegd!")

    def on_close(self):
        self.destroy()
        self.master.deiconify()