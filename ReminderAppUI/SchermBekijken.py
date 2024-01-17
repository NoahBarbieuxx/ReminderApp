from ReminderAppDL.ReminderManager import ReminderManager
from ReminderAppUI.ReminderBekijken import ReminderBekijken
import tkinter as tk

class SchermBekijken(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.master = master
        self.title("Reminders Bekijken")

        self.geometry("800x460")
        self.resizable(width=False, height=False)  
        self.protocol("WM_DELETE_WINDOW", self.on_close)     
 
        # Main frame aanmaken en instellen:
        self.frame = tk.Frame(self, bg="#727272")
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame = tk.Frame(self.frame, bg="#424242")
        self.main_frame.pack(padx=30, pady=30, fill=tk.BOTH, expand=True)

        label_titel = tk.Label(self.main_frame, text="Reminders Bekijken", font=("Inter", 14, "bold"), bg="#FF4141", fg="white")
        label_titel.pack(pady=20)

        # Inhoud Frame aanmaken en instellen:
        inhoud_frame = tk.Frame(self.main_frame, bg="#424242")
        inhoud_frame.pack(padx=20, pady=(0,20), fill=tk.BOTH, expand=True)

        kolom_titels = ["Naam", "Beschrijving", "Einddatum", "Einduur", "Dagen", "Bekijk"]
        for col, titel in enumerate(kolom_titels):
            if titel == "Bekijk":
                label = tk.Label(inhoud_frame, text=titel, font=("Inter", 10, "bold"), bg="#FF4141", fg="white", width=15, anchor="w", padx=5)
                label.grid(row=0, column=col, pady=(0, 5))
            else:
                label = tk.Label(inhoud_frame, text=titel, font=("Inter", 10, "bold"), bg="#FF4141", fg="white", width=15)
                label.grid(row=0, column=col, pady=(0, 5))

        reminder_manager = ReminderManager()
        reminders = reminder_manager.geef_reminders()

        for row, reminder in enumerate(reminders, start=1):
            tk.Label(inhoud_frame, text=reminder.naam, width=15, anchor="w").grid(row=row, column=0, padx=5, pady=5)
            tk.Label(inhoud_frame, text=reminder.beschrijving, width=15, anchor="w").grid(row=row, column=1, padx=5, pady=5)
            tk.Label(inhoud_frame, text=reminder.datum, width=15).grid(row=row, column=2, padx=5, pady=5)
            tk.Label(inhoud_frame, text=reminder.uur, width=15).grid(row=row, column=3, padx=5, pady=5)
            tk.Label(inhoud_frame, text=reminder.meldingsdag, width=15).grid(row=row, column=4, padx=5, pady=5)
            button = tk.Button(inhoud_frame, text="Bekijk", command=lambda reminder=reminder: self.bekijk_reminder(reminder), width=10,  bg="#FF4141", fg="white", bd=0)
            button.grid(row=row, column=5, pady=5, sticky="w")


    def bekijk_reminder(self, reminder):
        self.withdraw()
        ReminderBekijken(self.master, reminder)

    def on_close(self):
        self.destroy()
        self.master.deiconify()