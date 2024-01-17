from datetime import datetime, timedelta
from tkinter import messagebox
import time
import os

class Reminder:
    def __init__(self, naam, beschrijving, datum, uur, meldingsdag):
        self.naam = naam
        self.beschrijving = beschrijving
        self.datum = datum
        self.uur = uur
        self.meldingsdag = meldingsdag

    @staticmethod
    def check_inputs(naam, beschrijving, datum, uur, meldingsdag):
        if not naam or not beschrijving or not datum or not uur or not meldingsdag:
            messagebox.showerror("Error", "Vul alle velden in!")
            return False

        try:
            datum = datetime.strptime(datum, '%m-%d-%Y')
        except ValueError:
            messagebox.showerror("Error", "Datum is incorrect! (Gebruik mm-dd-yyyy)")
            return False
        
        try:
            uur = datetime.strptime(uur, '%H:%M')
        except ValueError:
            messagebox.showerror("Error", "Uur is incorrect! (Gebruik hh-mm)")
            return False
        
        datum_vandaag = datetime.now()
        datum = datetime.combine(datum, uur.time())
        if datum < datum_vandaag:
            messagebox.showerror("Error", "Datum mag niet in het verleden liggen!")
            return False

        try:
            int_meldingsdag = int(meldingsdag)
        except ValueError:
            messagebox.showerror("Error", "Ingegeven dagen moet een getal zijn!")
            return False

        if (datum - timedelta(days=int_meldingsdag)) < datum_vandaag:
            messagebox.showerror("Error", "Dagen op voorhand valt in het verleden!")
            return False

        return True
    
    def herinnering_melding(self, root):
        datum_datetime = datetime.strptime(self.datum, '%m-%d-%Y').date()
        uur_datetime = datetime.strptime(self.uur, '%H:%M').time()

        einddatum_en_uur = datetime.combine(datum_datetime, uur_datetime)

        meldingsdag = int(self.meldingsdag)

        herinnering_datum = einddatum_en_uur - timedelta(days=meldingsdag)

        nu = datetime.now()

        verschil = herinnering_datum - nu

        self.einddatum_en_uur = einddatum_en_uur

        root.after(int(verschil.total_seconds() * 1000), lambda: self.toon_herinnering())

    def toon_herinnering(self):
        if os.name == 'nt':
            melding = '{} - {} - Eindigt op {}'.format(self.naam, self.beschrijving, self.einddatum_en_uur.strftime('%d-%m-%Y %H:%M'))
            os.system('msg * /time:5 "{}"'.format(melding))