from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from common.Test import Test, get_text
import time

class Combinazioni(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Magazzino")
        self.navigateTo("Combinazioni")

    def test_creazione_combinazioni(self):
        self.creazione_combinazioni(codice="00001", nome="NomeProva", categoria="Componenti", attributi="NomeProva")

    def creazione_combinazioni(self, codice: str, nome: str, categoria: str, attributi: str):
        
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Codice').setValue(codice)
        self.input(modal, 'Nome').setValue(nome)

        select = self.input(modal, 'Categoria')
        select.setByText(categoria)

        select = self.input(modal, 'Attributi')
        select.setByText(attributi)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
       