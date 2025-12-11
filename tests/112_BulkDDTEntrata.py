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

    def cambia_stato(self):
        self.navigateTo("Ddt in entrata")
        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select('//button[@data-toggle="dropdown"]', option_xpath='//a[@data-op="change_status"]')
        self.wait_for_dropdown_and_select('//span[@id="select2-id_stato-container"]', option_text='Evaso')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        stato = self.find(By.XPATH, '//tbody//tr//td[11]').text
        self.assertEqual(stato, "Evaso")

    def fattura_ddt_entrata(self):
        self.navigateTo("Ddt in entrata")
        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        self.send_keys_and_wait(search_input, "1", False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select('//button[@data-toggle="dropdown"]', option_xpath='//a[@data-op="create_invoice"]')
        self.wait_for_dropdown_and_select('//span[@id="select2-raggruppamento-container"]', option_text='Cliente')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.navigateTo("Ddt in entrata")
        self.wait_for_element_and_click('//tbody//tr//td')
        self.clear_filters()

        self.expandSidebar("Acquisti")
        self.navigateTo("Fatture di acquisto")
        ragione_sociale = self.find(By.XPATH, '//tbody//tr//td[4]').text
        self.assertEqual(ragione_sociale, "Cliente")

        self.expandSidebar("Magazzino")

    def elimina_selezionati(self):        
        self.navigateTo("Ddt in entrata")
        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select('//button[@data-toggle="dropdown"]', option_xpath='//a[@data-op="delete_bulk"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        self.send_keys_and_wait(search_input, '2', False)
        scritta = self.find(By.XPATH, '//tbody//tr').text
        self.assertEqual(scritta, "La ricerca non ha portato alcun risultato.")
        self.clear_filters()