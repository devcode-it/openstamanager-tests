from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Eventi(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")
        self.navigateTo("Eventi")

    def test_creazione_eventi(self):
        self.creazione_eventi(nome="Prova Evento 1", nazione= "IT - Italia")

    def creazione_eventi(self, nome=str, nazione=str):

        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
    
        select = self.input(modal, 'Nazione')
        select.setByText(nazione)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
