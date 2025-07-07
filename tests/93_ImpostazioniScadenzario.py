from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Impostazioni(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")

    def test_impostazioni_scadenzario(self):
        return True    
        ## TODO: Invio solleciti in automatico

        ## TODO: Template email primo sollecito

        ## TODO: Ritardo in giorni della scadenza della fattura per invio sollecito pagamento

        ## TODO: Ritardo in giorni dall'ultima email per invio sollecito pagamento

        ## TODO: Template email secondo sollecito

        ## TODO: Template email terzo sollecito

        ## TODO: Template emial mancato pagamento dopo i solleciti

        ## TODO: Indirizzo email mancato pagamento dopo i solleciti

        ## TODO: Template email promemoria scadenza

        ## TODO: Intervallo di giorni in anticipo per invio promemoria scadenza