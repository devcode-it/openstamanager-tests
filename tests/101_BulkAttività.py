from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Attivita(Test):
    def setUp(self):
        super().setUp()

    def test_bulk_attivita(self):      
        self.cambio_stato()
        self.duplica()
        self.elimina_selezionati()
        #TODO: Esporta
        #self.esporta_selezionati()
        self.fattura_attivita()
        self.firma_interventi()
        self.stampa_riepilogo()
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')
        
    def cambio_stato(self):
        self.navigateTo('Attività')
        search_input = self.wait_for_element_and_click('//th[@id="th_Numero"]/input')
        self.send_keys_and_wait(search_input, '1', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="change_status"]'
        )

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_stato-container"]',
            option_text='Da programmare'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        stato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[7]'))
        ).text
        self.assertEqual(stato, 'Da programmare')
        self.wait_for_element_and_click('//tbody//tr//td')
        self.clear_filters()

    def duplica(self):
        self.navigateTo('Attività')
        search_input = self.wait_for_element_and_click('//th[@id="th_Numero"]/input')
        self.send_keys_and_wait(search_input, '1', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="copy_bulk"]'
        )

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-idstatointervento-container"]',
            option_text='Da programmare'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')
        self.clear_filters()

        search_input = self.wait_for_element_and_click('//th[@id="th_Numero"]/input')
        self.send_keys_and_wait(search_input, '2', wait_modal=False)
        numero = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[2]'))
        ).text
        self.assertEqual(numero, '2')
        self.clear_filters()

    def elimina_selezionati(self):
        self.navigateTo('Attività')
        search_input = self.wait_for_element_and_click('//th[@id="th_Numero"]/input')
        self.send_keys_and_wait(search_input, '2', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="delete_bulk"]'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        scritta = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td'))
        ).text
        self.assertEqual(scritta, 'Nessun dato presente nella tabella')
        self.clear_filters()

    def fattura_attivita(self):
        self.navigateTo('Attività')
        search_input = self.wait_for_element_and_click('//th[@id="th_Numero"]/input')
        self.send_keys_and_wait(search_input, '2', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="create_invoice"]'
        )

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-raggruppamento-container"]',
            option_text='Cliente'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        stato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[7]'))
        ).text
        self.assertEqual(stato, 'Fatturato')

        self.expandSidebar('Vendite')
        self.navigateTo('Fatture di vendita')
        self.click_first_result()
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask "]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.navigateTo('Attività')
        self.clear_filters()

    def firma_interventi(self):
        importi = RowManager.list()
        self.attivita('Cliente', '2', '1', importi[0])

        self.navigateTo('Attività')
        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="firma-intervento"]'
        )

        self.wait_for_element_and_click('//button[@id="firma"]')
        firma_input = self.wait_for_element_and_click('//input[@id="firma_nome"]')
        firma_input.send_keys('firma')
        self.wait_for_element_and_click('//button[@class="btn btn-success pull-right"]')

        self.click_first_result()
        self.wait_for_element_and_click('(//div[@class="text-center row"]//div)[3]')

    def stampa_riepilogo(self):
        self.navigateTo('Attività')
        search_input = self.wait_for_element_and_click('//th[@id="th_Numero"]/input')
        self.send_keys_and_wait(search_input, '2', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="print_summary"]'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.driver.switch_to.window(self.driver.window_handles[1])
        prezzo = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="viewer"]//span)[39]'))).text
        self.assertEqual(prezzo, '0,00')

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.click_first_result()
        self.wait_for_element_and_click('//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
