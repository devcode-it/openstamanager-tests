from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class MansioniReferenti(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")
        self.navigateTo("Mansioni referenti")

    def test_creazione_mansionireferenti(self):
        self.creazione_mansionireferenti(mansione="Mansione prova")

    def creazione_mansionireferenti(self, mansione= str):

        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Mansione').setValue(mansione)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()