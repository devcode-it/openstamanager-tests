from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class StatiDDT(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")

    def test_creazione_stati_DDT(self):
        self.creazione_stato_DDT("Stato dei DDT di Prova", "fa fa-check text-success", "#9d2929" )
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')
        

    def creazione_stato_DDT(self, descrizione = str, icona = str, colore = str):
        self.navigateTo("Stati dei DDT")
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'Descrizione').setValue(descrizione)
        self.input(modal, 'Colore').setValue(colore)
        self.input(modal, 'Icona').setValue(icona)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)
