from ReminderAppBL.Reminder import Reminder
import pyodbc

class ReminderManager:
    def __init__(self):
        self.connection_string = 'DRIVER={SQL Server};SERVER=LAPTOP-TJNUCBTN\\SQLEXPRESS;DATABASE=RemindersDb;Integrated Security=True;'
        self.connection = pyodbc.connect(self.connection_string)
        self.create_table()

    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''
            IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'reminders')
            BEGIN
                CREATE TABLE reminders (
                    id INT PRIMARY KEY IDENTITY(1,1),
                    naam NVARCHAR(255),
                    beschrijving NVARCHAR(255),
                    einddatum DATE,
                    einduur TIME,
                    dagenOpVoorhand INT
                );
            END
        ''')
        self.connection.commit()
    
    def voeg_reminder_toe(self, reminder):
        cursor = self.connection.cursor()        
        cursor.execute('''
            INSERT INTO reminders (naam, beschrijving, einddatum, einduur, dagenOpVoorhand)
            VALUES (?, ?, ?, ?, ?)
        ''', (reminder.naam, reminder.beschrijving, reminder.datum, reminder.uur, reminder.meldingsdag))
        self.connection.commit()

    def geef_reminders(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT naam, beschrijving, einddatum, einduur, dagenOpVoorhand FROM reminders')
        reminders = []

        for row in cursor.fetchall():
            naam, beschrijving, datum, uur, meldingsdag = row
            reminder = Reminder(naam, beschrijving, datum, uur, meldingsdag)
            reminders.append(reminder)

        return reminders
    
    def verwijder_reminder(self, reminder):
        cursor = self.connection.cursor()
        cursor.execute('''
            DELETE FROM reminders
            WHERE naam = ? AND beschrijving = ? AND einddatum = ? AND einduur = ? AND dagenOpVoorhand = ?
        ''', (reminder.naam, reminder.beschrijving, reminder.datum, reminder.uur, reminder.meldingsdag))
        self.connection.commit()

    def update_reminder(self, reminder, new_naam, new_beschrijving, new_datum, new_uur, new_meldingsdag):
        cursor = self.connection.cursor()
        cursor.execute('''
            UPDATE reminders
            SET naam = ?, beschrijving = ?, einddatum = ?, einduur = ?, dagenOpVoorhand = ?
            WHERE naam = ? AND beschrijving = ? AND einddatum = ? AND einduur = ? AND dagenOpVoorhand = ?
        ''', (new_naam, new_beschrijving, new_datum, new_uur, new_meldingsdag,
            reminder.naam, reminder.beschrijving, reminder.datum, reminder.uur, reminder.meldingsdag))
        self.connection.commit()

    def bestaat_reminder(self, naam, beschrijving, einddatum, einduur, dagen_op_voorhand):
        query = '''
            SELECT COUNT(*) AS count
            FROM reminders
            WHERE naam = ? AND beschrijving = ? AND einddatum = ? AND CONVERT(datetime, einduur, 108) = ? AND dagenOpVoorhand = ?
        '''

        with pyodbc.connect(self.connection_string) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (naam, beschrijving, einddatum, einduur, dagen_op_voorhand))
            result = cursor.fetchone()

        return result.count > 0