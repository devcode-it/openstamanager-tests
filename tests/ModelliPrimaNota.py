from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class ModelliPrimaNota(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")
        self.navigateTo("Modelli prima nota")

    def test_creazione_modelliprimanota(self):
        self.creazione_modelliprimanota(nome="Prova modello prima nota", causale="Prova anticipo fattura num. {numero} del {data}")

    def creazione_modelliprimanota(self, nome=str, causale=str):

        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        self.input(modal, 'Causale').setValue(causale)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()