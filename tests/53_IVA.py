from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class IVA(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")
        self.navigateTo("IVA")

    def test_creazione_iva(self):
        self.creazione_iva(descrizione= "IVA Prova 1", percentuale="9,00", indetraibile="2,00", esigibilita="Scissione dei pagamenti")

    def creazione_iva(self, descrizione=str, percentuale=str, indetraibile=str, esigibilita=str):

        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Descrizione').setValue(descrizione)
        self.input(modal, 'Percentuale').setValue(percentuale)
        self.input(modal, 'Indetraibile').setValue(indetraibile)

        select = self.input(modal, 'Esigibilità')
        select.setByText(esigibilita)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
