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
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')
    
    def cambia_stato(self):
        self.navigateTo("Contratti")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))), "2", wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_status"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_stato-container"]', option_text='In lavorazione')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        stato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[5]'))
        ).text
        self.assertEqual(stato, "In lavorazione")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

    def fattura_contratti(self):
        self.navigateTo("Contratti")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))), "2", wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="create_invoice"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-raggruppamento-container"]', option_text='Cliente')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        tipo = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[5]'))
        ).text
        self.assertEqual(tipo, "Fattura immediata di vendita")

        self.wait_for_element_and_click('//tbody//tr[2]//td[4]')
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask "]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.navigateTo("Contratti")
        self.wait_loader()
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

    def rinnova_contratti(self):
        self.navigateTo("Contratti")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))), "1", wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_accettazione"]'))).send_keys("01/01/2026")
        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_conclusione"]'))).send_keys("31/12/2026")
        self.wait_for_dropdown_and_select('//span[@id="select2-idstato-container"]', option_text='Accettato')
        self.wait_for_element_and_click('//button[@id="save"]')

        self.navigateTo("Contratti")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="renew_contract"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.wait_for_element_and_click('(//i[@class="deleteicon fa fa-times"])[1]')

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))), "3", wait_modal=False)

        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[2]')))
        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.wait_for_element_and_click('(//i[@class="deleteicon fa fa-times"])[1]')
