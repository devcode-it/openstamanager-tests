from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Relazioni(Test):
    def setUp(self):
        super().setUp()

        self.navigateTo("Anagrafiche")
        self.navigateTo("Relazioni")

    def test_creazione_relazioni(self):
        self.creazione_relazioni(descrizione= "Prova1",colore="#9d2929")

    def creazione_relazioni(self, descrizione=str, colore=str):

        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Colore').setValue(colore)

        self.input(modal, 'Descrizione').setValue(descrizione)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
