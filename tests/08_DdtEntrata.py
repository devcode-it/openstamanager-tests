from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class DdtEntrata(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Magazzino")

    def test_creazione_ddt_entrata(self):
        importi = RowManager.list()
        self.creazione_ddt_entrata("Fornitore", "1", importi[0])
        self.duplica_ddt_entrata()
        self.modifica_ddt("Evaso")
        self.elimina_ddt()
        self.verifica_ddt()


    def creazione_ddt_entrata(self, fornitore: str, causale: str, file_importi: str):
        self.navigateTo("Ddt in entrata")
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        select = self.input(modal, 'Mittente')
        select.setByText(fornitore)
        select = self.input(modal, 'Causale trasporto')
        select.setByIndex(causale)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

        row_manager = RowManager(self)
        self.valori = row_manager.compile(file_importi)

    def duplica_ddt_entrata(self):
        self.navigateTo("Ddt in entrata")
        self.click_first_result()

        self.driver.execute_script('window.scrollTo(0,0)')
        self.wait_for_element_and_click('//button[@class="btn btn-primary ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-primary"]')

    def modifica_ddt(self, modifica):
        self.navigateTo("Ddt in entrata")
        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        self.send_keys_and_wait(search_input, '1', False)
        self.click_first_result()

        self.wait_for_dropdown_and_select('//span[@id="select2-idstatoddt-container"]', option_text='Evaso')

        sconto = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[2]//td[2]').text
        totale_imponibile = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text
        iva = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[4]//td[2]').text
        totale = self.find(By.XPATH, '//div[@id="tab_0"]//div[@id="righe"]//tbody[2]//tr[5]//td[2]').text

        self.assertEqual(sconto, (self.valori["Sconto/maggiorazione"] + ' €'))
        self.assertEqual(totale_imponibile, (self.valori["Totale imponibile"] + ' €'))
        self.assertEqual(iva, (self.valori["IVA"] + ' €'))
        self.assertEqual(totale, (self.valori["Totale documento"] + ' €'))

        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')
        self.navigateTo("Ddt in entrata")
        self.clear_filters()

    def elimina_ddt(self):
        self.navigateTo("Ddt in entrata")
        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        self.send_keys_and_wait(search_input, '2', False)
        self.click_first_result()

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.clear_filters()

    def verifica_ddt(self):
        self.navigateTo("Ddt in entrata")
        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        self.send_keys_and_wait(search_input, "1", False)
        modificato = self.driver.find_element(By.XPATH, '//tbody//tr[1]//td[11]').text
        self.assertEqual("Evaso", modificato)
        self.clear_filters()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        self.send_keys_and_wait(search_input, "2", False)
        eliminato = self.driver.find_element(By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)
        self.clear_filters()
