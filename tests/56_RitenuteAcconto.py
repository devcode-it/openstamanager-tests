from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class RitenuteAcconto(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")
        self.navigateTo("Ritenute acconto")

    def test_creazione_ritenuteacconto(self):
        self.creazione_ritenuteacconto(descrizione= "Ritenuta acconto di prova", percentuale="80,00", percentualeimp="60,00")

    def creazione_ritenuteacconto(self, descrizione=str, percentuale=str, percentualeimp=str):

        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Descrizione').setValue(descrizione)
        self.input(modal, 'Percentuale').setValue(percentuale)
        self.input(modal, 'Percentuale imponibile').setValue(percentualeimp)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()