from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class CausaliMovimenti(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")
        self.navigateTo("Causali movimenti")

    def test_creazione_causalimovimenti(self):
        self.creazione_causalimovimenti(nome="Causale movimento Prova", descrizione="Descrizione causale movimento prova", tipo="Carico")

    def creazione_causalimovimenti(self, nome=str, descrizione=str, tipo=str):

        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)

        select = self.input(modal, 'Tipo movimento')
        select.setByText(tipo)

        self.input(modal, 'Descrizione').setValue(descrizione)
    
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()