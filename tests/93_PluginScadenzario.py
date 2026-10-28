from common.Test import Test
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Scadenzario(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Contabilità")

    def test_plugin_scadenzario(self):
        self.presentazioni_bancarie()

    def presentazioni_bancarie(self):
        
        self.navigate_to_and_wait("Scadenzario")
        self.search_by_th("th_Anagrafica", "Cliente")

        self.wait_for_element_and_click('//tbody//tr[1]//td[1]')
        self.wait_for_element_and_click('//a[@id="link-tab_39"]')

        self.wait_for_element_and_click('//button[@class="btn btn-primary "]')
        self.wait_for_element_and_click('//button[@onclick="esporta(this)"]')