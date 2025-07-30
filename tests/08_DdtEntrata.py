from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from common.functions import (
    wait_for_dropdown_and_select,
    wait_for_element_and_click,
    send_keys_and_wait,
    wait_loader,
    search_entity,
    click_first_result,
    clear_filters,
    wait_for_search_results
)
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
        self.cambia_stato()
        self.fattura_ddt_entrata()
        self.duplica_ddt_entrata()
        self.elimina_selezionati()

    def creazione_ddt_entrata(self, fornitore: str, causale: str, file_importi: str):
        self.navigateTo("Ddt in entrata")
        wait_for_element_and_click(self.driver, self.wait_driver, '//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        select = self.input(modal, 'Mittente')
        select.setByText(fornitore)
        select = self.input(modal, 'Causale trasporto')
        select.setByIndex(causale)
        wait_for_element_and_click(self.driver, self.wait_driver, 'button[type="submit"]', By.CSS_SELECTOR)

        row_manager = RowManager(self)
        self.valori = row_manager.compile(file_importi)

    def duplica_ddt_entrata(self):
        self.navigateTo("Ddt in entrata")
        click_first_result(self.driver, self.wait_driver)

        self.driver.execute_script('window.scrollTo(0,0)')
        wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="btn btn-primary ask"]')
        wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="swal2-confirm btn btn-lg btn-primary"]')

    def modifica_ddt(self, modifica):
        self.navigateTo("Ddt in entrata")
        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        send_keys_and_wait(self.driver, self.wait_driver, search_input, '1', False)
        click_first_result(self.driver, self.wait_driver)

        wait_for_dropdown_and_select(self.driver, self.wait_driver, '//span[@id="select2-idstatoddt-container"]', option_text='Evaso')

        sconto = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[2]//td[2]').text
        totale_imponibile = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text
        iva = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[4]//td[2]').text
        totale = self.find(By.XPATH, '//div[@id="tab_0"]//div[@id="righe"]//tbody[2]//tr[5]//td[2]').text

        self.assertEqual(sconto, (self.valori["Sconto/maggiorazione"] + ' €'))
        self.assertEqual(totale_imponibile, (self.valori["Totale imponibile"] + ' €'))
        self.assertEqual(iva, (self.valori["IVA"] + ' €'))
        self.assertEqual(totale, (self.valori["Totale documento"] + ' €'))

        wait_for_element_and_click(self.driver, self.wait_driver, '//div[@id="tab_0"]//button[@id="save"]')
        self.navigateTo("Ddt in entrata")
        clear_filters(self.driver, self.wait_driver)

    def elimina_ddt(self):
        self.navigateTo("Ddt in entrata")
        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        send_keys_and_wait(self.driver, self.wait_driver, search_input, '2', False)
        click_first_result(self.driver, self.wait_driver)

        wait_for_element_and_click(self.driver, self.wait_driver, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        clear_filters(self.driver, self.wait_driver)

    def verifica_ddt(self):
        self.navigateTo("Ddt in entrata")
        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        send_keys_and_wait(self.driver, self.wait_driver, search_input, "1", False)
        modificato = self.driver.find_element(By.XPATH, '//tbody//tr[1]//td[11]').text
        self.assertEqual("Evaso", modificato)
        clear_filters(self.driver, self.wait_driver)

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        send_keys_and_wait(self.driver, self.wait_driver, search_input, "2", False)
        eliminato = self.driver.find_element(By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)
        clear_filters(self.driver, self.wait_driver)

    def cambia_stato(self):
        self.navigateTo("Ddt in entrata")
        wait_for_element_and_click(self.driver, self.wait_driver, '//tbody//tr//td')
        wait_for_dropdown_and_select(self.driver, self.wait_driver, '//button[@data-toggle="dropdown"]', option_xpath='//a[@data-op="change_status"]')
        wait_for_dropdown_and_select(self.driver, self.wait_driver, '//span[@id="select2-id_stato-container"]', option_text='Evaso')
        wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        stato = self.find(By.XPATH, '//tbody//tr//td[11]').text
        self.assertEqual(stato, "Evaso")

    def fattura_ddt_entrata(self):
        self.navigateTo("Ddt in entrata")
        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        send_keys_and_wait(self.driver, self.wait_driver, search_input, "1", False)

        wait_for_element_and_click(self.driver, self.wait_driver, '//tbody//tr//td')
        wait_for_dropdown_and_select(self.driver, self.wait_driver, '//button[@data-toggle="dropdown"]', option_xpath='//a[@data-op="create_invoice"]')
        wait_for_dropdown_and_select(self.driver, self.wait_driver, '//span[@id="select2-raggruppamento-container"]', option_text='Cliente')
        wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.navigateTo("Ddt in entrata")
        wait_for_element_and_click(self.driver, self.wait_driver, '//tbody//tr//td')
        clear_filters(self.driver, self.wait_driver)

        self.expandSidebar("Acquisti")
        self.navigateTo("Fatture di acquisto")
        ragione_sociale = self.find(By.XPATH, '//tbody//tr//td[4]').text
        self.assertEqual(ragione_sociale, "Cliente")

        self.expandSidebar("Magazzino")

    def elimina_selezionati(self):
        self.navigateTo("Ddt in entrata")
        wait_for_element_and_click(self.driver, self.wait_driver, '//tbody//tr//td')
        wait_for_dropdown_and_select(self.driver, self.wait_driver, '//button[@data-toggle="dropdown"]', option_xpath='//a[@data-op="delete_bulk"]')
        wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        send_keys_and_wait(self.driver, self.wait_driver, search_input, '2', False)
        scritta = self.find(By.XPATH, '//tbody//tr').text
        self.assertEqual(scritta, "La ricerca non ha portato alcun risultato.")
        clear_filters(self.driver, self.wait_driver)