from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class OrdiniCliente(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Vendite")

    def test_bulk_ordine_cliente(self):
        self.cambia_stato()
        self.fattura_ordini_clienti()
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')
        
    def cambia_stato(self):
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))), '01', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_status"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_stato-container"]', option_text='Accettato')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        stato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//tbody//tr[1]//td[7]//span)[2]'))
        ).text
        self.assertEqual(stato, "Accettato")

        self.wait_for_element_and_click('//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]')

    def fattura_ordini_clienti(self):
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="create_invoice"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-raggruppamento-container"]', option_text='Cliente')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        tipo = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[3]//td[5]'))
        ).text
        self.assertEqual(tipo, "Fattura immediata di vendita")

        self.wait_for_element_and_click('//tbody//tr//td[4]')
        self.wait_for_element_and_click('//a[@id="elimina"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
