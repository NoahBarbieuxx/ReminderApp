import tkinter as tk
from ReminderAppUI.SchermToevoegen import SchermToevoegen
from ReminderAppUI.SchermVerwijderen import SchermVerwijderen
from ReminderAppUI.SchermBekijken import SchermBekijken
from ReminderAppUI.SchermAanpassen import SchermAanpassen

class Homepagina:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, bg="#727272")
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.master.resizable(width=False, height=False)

        self.left_frame = tk.Frame(self.frame, bg="#424242")
        self.left_frame.pack(side=tk.LEFT, padx=(30, 5), pady=30, fill=tk.BOTH, expand=True)

        self.right_frame = tk.Frame(self.frame, bg="#424242")
        self.right_frame.pack(side=tk.RIGHT, padx=(30, 30), pady=30, fill=tk.BOTH, expand=True)

        # Linkerkant
        button_config = {
            "width": 13,
            "font": ("Inter", int(14.25), "bold"),
            "bg": "#FF4141",
            "fg": "white",
            "bd": 0
        }

        buttons = [
            ("OVERZICHT", {"pady": (30, 0)}),
            ("Toevoegen", {"pady": (46, 0)}),
            ("Verwijderen", {"pady": (10, 0)}),
            ("Aanpassen", {"pady": (10, 0)}),
            ("Bekijken", {"pady": (10, 0)}),
            ("REMINDER APP", {"pady": (55, 0)}),
        ]

        for text, pack_options in buttons:
            tk.Button(self.left_frame, text=text, command=lambda t=text: self.open_scherm(t), **button_config).pack(**pack_options)

        # Rechterkant
        tk.Label(self.right_frame, text="Dit is de graduaatsproef van Noah Barbieux:", font=("Inter", 14, "bold"), bg="#FF4141", fg="white").pack(pady=(30, 0))

        image_path = "images/logo.png"
        self.logo_image = tk.PhotoImage(file=image_path)
        tk.Label(self.right_frame, image=self.logo_image).pack(pady=(40, 0))

        tk.Label(self.right_frame, text="© 2023 HoGent", font=("Inter", 10, "bold"), fg="white", bg="#FF4141", anchor="w", justify="left").pack(pady=(62, 0))

    def open_scherm(self, scherm_naam):
        if scherm_naam == "Toevoegen":
            self.master.withdraw()
            SchermToevoegen(self.master)
        elif scherm_naam == "Verwijderen":
            self.master.withdraw()
            SchermVerwijderen(self.master)
        elif scherm_naam == "Aanpassen":
            self.master.withdraw()
            SchermAanpassen(self.master)
        elif scherm_naam == "Bekijken":
            self.master.withdraw()
            SchermBekijken(self.master)

    def on_close(self):
        self.master.deiconify()