from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TipiDocumento(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")
        self.navigateTo("Tipi documento")

    def test_creazione_tipidocumento(self):
        self.creazione_tipidocumento(descrizione="Prova Documento 1", direzione="Entrata", codice="TD01 - Fattura" )

    def creazione_tipidocumento(self, descrizione=str, direzione=str, codice=str):

        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Descrizione').setValue(descrizione)
    
        select = self.input(modal, 'Direzione')
        select.setByText(direzione)

        select = self.input(modal, 'Codice tipo documento FE')
        select.setByText(codice)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
