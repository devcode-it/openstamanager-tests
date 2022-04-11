from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class FasceOrarie(Test):
    def setUp(self):
        super().setUp()

        self.navigateTo("Attività")
        self.navigateTo("Stati di attività")

    def test_creazione_statiattivita(self):
        self.creazione_statiattivita(codice="0001", descrizione="Stato attività 1", colore="#9d2929")

    def creazione_statiattivita(self, codice= str, descrizione= str, colore= str):

        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Colore').setValue(colore)
        self.input(modal, 'Codice').setValue(codice)
        self.input(modal, 'Descrizione').setValue(descrizione)
        
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
