import tkinter as tk

class CTk(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("ReminderApp - \"Efficiënt Herinneren: Een Gebruiksvriendelijke Reminder Applicatie in Python\"")
        self.geometry("800x460")
        self.configure(bg="#727272")
        self.root = self