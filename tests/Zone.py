from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Zone(Test):
    def setUp(self):
        super().setUp()

        self.navigateTo("Anagrafiche")
        self.navigateTo("Zone")

    def test_creazione_zone(self):
        self.creazione_zone(codice="0001", descrizione="ZonaProva")

    def creazione_zone(self, codice=str, descrizione=str):

        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Codice').setValue(codice)
        self.input(modal, 'Descrizione').setValue(descrizione)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()