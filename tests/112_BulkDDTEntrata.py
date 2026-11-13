from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class DdtEntrata(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Magazzino")

    def test_bulk_ddt_entrata(self):
        self.cambia_stato()
        self.fattura_ddt_entrata()
        self.elimina_selezionati()

    def deseleziona_tutto(self):
        self.wait_loader()
        self.wait_for_element_and_click('.btn-select-none', By.CSS_SELECTOR)
        
    def cambia_stato(self):
        self.navigate_to_and_wait("Ddt in entrata")
        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select('//button[@data-toggle="dropdown"]', option_xpath='//a[@data-op="change_status"]')
        self.select_state('Evaso')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-primary"]')

        stato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[11]'))
        ).text
        self.assertEqual(stato, "Evaso")

    def fattura_ddt_entrata(self):
        self.navigate_to_and_wait("Ddt in entrata")
        self.deseleziona_tutto()
        self.search_by_th("th_Ragione-sociale", "Cliente", wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td')

        self.wait_for_dropdown_and_select('//button[@data-toggle="dropdown"]', option_xpath='//a[@data-op="create_invoice"]')
        self.wait_for_dropdown_and_select('//span[@id="select2-raggruppamento-container"]', option_text='Cliente')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-primary"]')

        self.navigate_to_and_wait("Ddt in entrata")
        self.wait_for_element_and_click('//tbody//tr//td')
        self.clear_filters()

        self.expandSidebar("Acquisti")
        self.navigate_to_and_wait("Fatture di acquisto")
        ragione_sociale = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[4]'))
        ).text
        self.assertEqual(ragione_sociale, "Cliente")

        self.expandSidebar("Magazzino")
        self.deseleziona_tutto()

    def elimina_selezionati(self):
        self.navigate_to_and_wait("Ddt in entrata")
        self.search_by_th("th_Ragione-sociale", "Admin spa", wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select('//button[@data-toggle="dropdown"]', option_xpath='//a[@data-op="delete_bulk"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-primary"]')
        self.clear_filters()

        self.search_by_th("th_Ragione-sociale", 'Admin spa', wait_modal=False)
        scritta = self.get_empty_table_message()
        self.assertEqual(scritta, "Nessun dato presente nella tabella")
        self.clear_filters()