from ReminderAppBL.Ctk import CTk
from ReminderAppUI.Homepagina import Homepagina
from ReminderAppDL.ReminderManager import ReminderManager

if __name__ == "__main__":
    root = CTk()

    eerste_scherm = Homepagina(root)
    
    reminder_manager = ReminderManager()
    reminder_manager.create_table()

    root.mainloop()