import tkinter as tk
from tkinter import ttk, messagebox
from ReminderAppDL.ReminderManager import ReminderManager

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

class SchermVerwijderen(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.master = master
        self.title("Reminder Verwijderen")
        self.reminder_manager = ReminderManager()

        self.geometry("800x460")
        self.resizable(width=False, height=False)  
        self.protocol("WM_DELETE_WINDOW", self.on_close)  

        # Main Frame aanmaken:
        self.frame = tk.Frame(self, bg="#727272")
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Linker Frame aanmaken en instellen:
        self.linker_frame = tk.Frame(self.frame, bg="#424242")
        self.linker_frame.pack(side=tk.LEFT, padx=(30, 5), pady=30, fill=tk.Y, expand=False)

        label_titel = tk.Label(self.linker_frame, text="Reminder Verwijderen", font=("Inter", 14, "bold"), bg="#FF4141", fg="white")
        label_titel.pack(padx=20, pady=20)

        label_zoekterm = tk.Label(self.linker_frame, text="Zoek op naam/beschrijving:", bg="#FF4141", fg="white", width=26, font=("Inter", 10, "bold"))
        label_zoekterm.pack(pady=(20,5))

        self.zoekterm_var = tk.StringVar()
        self.zoekterm_entry = tk.Entry(self.linker_frame, textvariable=self.zoekterm_var, width=35).pack()

        button_reset = tk.Button(self.linker_frame, text="Reset", command=self.laad_reminders, width=15, bg="#FF4141", fg="white", bd=0, font=("Inter", 10, "bold"))
        button_reset.pack(side=tk.BOTTOM, pady=(0,20))

        button_zoek = tk.Button(self.linker_frame, text="Zoek", command=self.filter_reminders, width=15, bg="#FF4141", fg="white", bd=0, font=("Inter", 10, "bold"))
        button_zoek.pack(side=tk.BOTTOM, pady=8)
    
        # Rechter Frame aanmaken en instellen:
        self.rechter_frame = ScrollableFrame(self.frame, bg="#424242")
        self.rechter_frame.pack(side=tk.RIGHT, padx=(30, 30), pady=30, fill=tk.BOTH, expand=True)

        self.inhoud_frame = tk.Frame(self.rechter_frame.scrollable_frame, bg="#424242")
        self.inhoud_frame.pack(padx=(25,20), pady=20, fill=tk.BOTH, expand=True)

        kolom_titels = ["Naam", "Beschrijving", "Datum", "Verw."]
        for col, titel in enumerate(kolom_titels):
            label_titel = tk.Label(self.inhoud_frame, text=titel, font=("Inter", 10, "bold"), bg="#FF4141", fg="white", width=13)
            label_titel.grid(row=0, column=col, pady=(0, 5))

        self.laad_reminders()

    def laad_reminders(self):
        reminders = self.reminder_manager.geef_reminders()

        sorted_reminders = sorted(reminders, key=lambda reminder: reminder.datum)

        for row, reminder in enumerate(sorted_reminders, start=1):
            tk.Label(self.inhoud_frame, text=reminder.naam, width=13, anchor="w").grid(row=row, column=0, padx=5, pady=5)
            tk.Label(self.inhoud_frame, text=reminder.beschrijving, width=13, anchor="w").grid(row=row, column=1, padx=5, pady=5)
            tk.Label(self.inhoud_frame, text=reminder.datum, width=13).grid(row=row, column=2, padx=5, pady=5)

            button_verwijder = tk.Button(self.inhoud_frame, text="Verwijderen", command=lambda r=row, reminder=reminder: self.verwijder_reminder(r, reminder), width=13, bg="#FF4141", fg="white", bd=0, anchor="w")
            button_verwijder.grid(row=row, column=3, padx=5, pady=5)

    def filter_reminders(self):
        zoekterm = self.zoekterm_var.get().lower()
        self.clear_data_rows()

        reminders = self.reminder_manager.geef_reminders()

        for row, reminder in enumerate(reminders, start=1):
            if zoekterm in reminder.naam.lower() or zoekterm in reminder.beschrijving.lower():
                tk.Label(self.inhoud_frame, text=reminder.naam, width=13, anchor="w").grid(row=row, column=0, padx=5, pady=5)
                tk.Label(self.inhoud_frame, text=reminder.beschrijving, width=13, anchor="w").grid(row=row, column=1, padx=5, pady=5)
                tk.Label(self.inhoud_frame, text=reminder.datum, width=13).grid(row=row, column=2, padx=5, pady=5)

                button_verwijder = tk.Button(self.inhoud_frame, text="Verwijderen", command=lambda r=row, reminder=reminder: self.verwijder_reminder(r, reminder), width=13, bg="#FF4141", fg="white", bd=0, anchor="w")
                button_verwijder.grid(row=row, column=3, padx=5, pady=5)
        
    def clear_data_rows(self):
        for row in range(1, self.inhoud_frame.grid_size()[1]):
            for col in range(self.inhoud_frame.grid_size()[0]):
                for widget in self.inhoud_frame.grid_slaves(row=row, column=col):
                    widget.destroy()

    def verwijder_reminder(self, row, reminder):
        for col in range(self.inhoud_frame.grid_size()[0]):
            for widget in self.inhoud_frame.grid_slaves(row=row, column=col):
                widget.destroy()
        
        messagebox.showinfo("Succes", "Reminder succesvol verwijderd!")

        self.reminder_manager.verwijder_reminder(reminder)
        self.clear_data_rows()
        self.laad_reminders()

    def on_close(self):
        self.destroy()
        self.master.deiconify()