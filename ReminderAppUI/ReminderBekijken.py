import tkinter as tk

class ReminderBekijken(tk.Toplevel):
    def __init__(self, master, reminder):
        tk.Toplevel.__init__(self, master)
        self.master = master
        self.reminder = reminder
        self.title("Reminder Bekijken")

        self.geometry("800x460")
        self.resizable(width=False, height=False)
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        # Main Frame aanmaken en instellen:
        self.frame = tk.Frame(self, bg="#727272")
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame = tk.Frame(self.frame, bg="#424242")
        self.main_frame.pack(padx=30, pady=30, fill=tk.BOTH, expand=True)

        label_titel = tk.Label(self.main_frame, text="Specifieke Reminder Bekijken", font=("Inter", 14, "bold"), bg="#FF4141", fg="white")
        label_titel.pack(pady=20)

        label_naam_titel = tk.Label(self.main_frame, text="Naam:", font=("Inter", 11, "bold"), bg="#FF4141", fg="white", width=800)
        label_naam_titel.pack()
        label_naam = tk.Label(self.main_frame, text=reminder.naam, font=("Inter", 10), width=800, bg="#727272", fg="white")
        label_naam.pack()

        label_beschrijving_titel = tk.Label(self.main_frame, text="Beschrijving:", font=("Inter", 11, "bold"), bg="#FF4141", fg="white", width=800)
        label_beschrijving_titel.pack(pady=(20,0))
        label_beschrijving = tk.Label(self.main_frame, text=reminder.beschrijving, font=("Inter", 10), width=800, bg="#727272", fg="white")
        label_beschrijving.pack()

        label_datum_titel = tk.Label(self.main_frame, text="Einddatum:", font=("Inter", 11, "bold"), bg="#FF4141", fg="white", width=800)
        label_datum_titel.pack(pady=(20,0))
        label_datum = tk.Label(self.main_frame, text=reminder.datum, font=("Inter", 10), width=800, bg="#727272", fg="white")
        label_datum.pack()

        label_uur_titel = tk.Label(self.main_frame, text="Einduur:", font=("Inter", 11, "bold"), bg="#FF4141", fg="white", width=800)
        label_uur_titel.pack(pady=(20,0))
        label_uur = tk.Label(self.main_frame, text=reminder.uur, font=("Inter", 10), width=800, bg="#727272", fg="white")
        label_uur.pack()

        label_meldingsdag_titel = tk.Label(self.main_frame, text="Meldingsdag:", font=("Inter", 11, "bold"), bg="#FF4141", fg="white", width=800)
        label_meldingsdag_titel.pack(pady=(20,0))
        label_meldingsdag = tk.Label(self.main_frame, text=reminder.meldingsdag, font=("Inter", 10), width=800, bg="#727272", fg="white")
        label_meldingsdag.pack()

    def on_close(self):
        self.destroy()
        self.master.deiconify()