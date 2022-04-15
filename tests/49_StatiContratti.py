from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class StatiContratti(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")
        self.navigateTo("Stati dei contratti")

    def test_creazione_staticontratti(self):
        self.creazione_staticontratti( descrizione= "Descrizione prova stato contratto", icona="fa fa-check text-success")

    def creazione_staticontratti(self, descrizione=str, icona=str):

        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Descrizione').setValue(descrizione)
        self.input(modal, 'Icona').setValue(icona)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
