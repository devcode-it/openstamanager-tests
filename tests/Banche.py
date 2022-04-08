from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Banche(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")
        self.navigateTo("Banche")

    def test_creazione_banca(self):
        self.creazione_banca(anagrafica="Cliente", nome="banca banca", iban="IT11C1234512345678912345679", bic="12345678")

    def creazione_banca(self, anagrafica: str, nome: str, iban: str, bic: str):
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        select = self.input(modal, 'Anagrafica')
        select.setByText(anagrafica)

        self.input(modal, 'Nome').setValue(nome)

        self.input(modal, 'IBAN').setValue(iban)

        self.input(modal, 'BIC').setValue(bic)
        

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
