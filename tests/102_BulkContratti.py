from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Contratti(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Vendite")

    def test_bulk_contratto(self):
        self.cambia_stato()
        #TODO: cambia metodo di pagamento
        #self.cambia_metodo_pagamento()
        self.fattura_contratti()
        self.rinnova_contratti()
        #TODO: duplica contratti
    
    def cambia_stato(self):
        self.navigate_to_and_wait("Contratti")

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))), "2", wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_status"]')

        self.select_state('In lavorazione')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        stato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[5]'))
        ).text
        self.assertEqual(stato, "In lavorazione")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.clear_filters()

    def fattura_contratti(self):
        self.navigate_to_and_wait("Contratti")

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))), "2", wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="create_invoice"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-raggruppamento-container"]', option_text='Cliente')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.navigate_to_and_wait("Fatture di vendita")

        tipo = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[5]'))
        ).text
        self.assertEqual(tipo, "Fattura immediata di vendita")

        self.wait_and_click_table_row(2, 4)
        self.delete_current_and_clear()

        self.navigate_to_and_wait("Contratti")
        self.clear_filters()

    def rinnova_contratti(self):
        self.navigate_to_and_wait("Contratti")

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))), "1", wait_modal=False)

        self.click_first_table_row()

        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_accettazione"]'))).send_keys("01/01/2026")
        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_conclusione"]'))).send_keys("31/12/2026")
        self.wait_for_dropdown_and_select('//span[@id="select2-idstato-container"]', option_text='Accettato')
        self.wait_for_element_and_click('//button[@id="save"]')

        self.navigate_to_and_wait("Contratti")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="renew_contract"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.wait_for_element_and_click('(//i[@class="deleteicon fa fa-times"])[1]')

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))), "3", wait_modal=False)

        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[2]')))
        self.click_first_table_row()
        self.delete_current_and_clear()