from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Impostazioni(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")

    def test_impostazioni_mail_newsletter(self):
        return True
        ## TODO: Numero di giorni mantenimento coda di invio

        ## TODO: numero massimo di tentativi

        ## TODO: Numero email da inviare in contemporanea per account