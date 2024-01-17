import tkinter as tk
from tkinter import ttk
from ReminderAppDL.ReminderManager import ReminderManager
from ReminderAppUI.Aanpassen import Aanpassen
from datetime import datetime

class ScrollableFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.canvas = tk.Canvas(self, borderwidth=0, background="#424242", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#424242")

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

class SchermAanpassen(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.master = master
        self.title("Reminder Aanpassen")

        self.geometry("800x460")
        self.resizable(width=False, height=False)  
        self.protocol("WM_DELETE_WINDOW", self.on_close)     

        # Main Frame aanmaken en instellen:
        self.frame = tk.Frame(self, bg="#727272")
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame = tk.Frame(self.frame, bg="#424242")
        self.main_frame.pack(padx=30, pady=30, fill=tk.BOTH, expand=True)

        label_titel = tk.Label(self.main_frame, text="Reminder aanpassen", font=("Inter", 14, "bold"), bg="#FF4141", fg="white")
        label_titel.pack(pady=20)

        # Scrollable Frame aanmaken en instellen:
        scrollable_frame = ScrollableFrame(self.main_frame, bg="#424242")
        scrollable_frame.pack(padx=20, pady=(0,20), fill=tk.BOTH, expand=True)

        kolom_titels = ["Naam", "Beschrijving", "Datum", "Uur", "Dagen", "Pas aan"]
        for col, titel in enumerate(kolom_titels):
            if titel == "Pas aan":
                label_titels = tk.Label(scrollable_frame.scrollable_frame, text=titel, font=("Inter", 10, "bold"), bg="#FF4141", fg="white", width=15, anchor="w", padx=5)
                label_titels.grid(row=0, column=col, pady=(0, 5))
            elif titel == "Dagen":
                label_titels = tk.Label(scrollable_frame.scrollable_frame, text=titel, font=("Inter", 10, "bold"), bg="#FF4141", fg="white", width=12)
                label_titels.grid(row=0, column=col, pady=(0, 5))
            else:
                label_titels = tk.Label(scrollable_frame.scrollable_frame, text=titel, font=("Inter", 10, "bold"), bg="#FF4141", fg="white", width=15)
                label_titels.grid(row=0, column=col, pady=(0, 5))

        reminder_manager = ReminderManager()
        reminders = reminder_manager.geef_reminders()

        sorted_reminders = sorted(reminders, key=lambda reminder: reminder.datum)

        for row, reminder in enumerate(sorted_reminders, start=1):
            tk.Label(scrollable_frame.scrollable_frame, text=reminder.naam, width=15, anchor="w").grid(row=row, column=0, padx=5, pady=5)
            tk.Label(scrollable_frame.scrollable_frame, text=reminder.beschrijving, width=15, anchor="w").grid(row=row, column=1, padx=5, pady=5)
            tk.Label(scrollable_frame.scrollable_frame, text=reminder.datum, width=15).grid(row=row, column=2, padx=5, pady=5)
            
            uur_label = tk.Label(scrollable_frame.scrollable_frame, text=self.format_time(reminder.uur), width=15)
            uur_label.grid(row=row, column=3, padx=5, pady=5)
            
            tk.Label(scrollable_frame.scrollable_frame, text=reminder.meldingsdag, width=12).grid(row=row, column=4, padx=5, pady=5)
            
            button = tk.Button(scrollable_frame.scrollable_frame, text="Pas aan", command=lambda r=reminder: self.pas_reminder_aan(r), width=9, bg="#FF4141", fg="white", bd=0)
            button.grid(row=row, column=5, pady=5, sticky="w")
    
    def format_time(self, time_str):
        try:
            dt_obj = datetime.strptime(time_str, "%H:%M:%S.%f")
            return dt_obj.strftime("%H:%M:%S.%f")[:-3] if dt_obj.microsecond else dt_obj.strftime("%H:%M:%S")
        except ValueError:
            try:
                return datetime.strptime(time_str, "%H:%M:%S").strftime("%H:%M:%S")
            except ValueError:
                return time_str

    def pas_reminder_aan(self, reminder):
        self.withdraw()
        Aanpassen(self.master, reminder)

    def on_close(self):
        self.destroy()
        self.master.deiconify()