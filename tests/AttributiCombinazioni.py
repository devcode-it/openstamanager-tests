from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class AttributiCombinazioni(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Magazzino")
        self.navigateTo("Attributi Combinazioni")

    def test_creazione_attributi(self):
        self.creazione_attributi(nome="NomeProva", titolo="TitoloProva")

    def creazione_attributi(self, nome=str, titolo=str):

        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)

        self.input(modal, 'Titolo').setValue(titolo)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()