from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Preventivi(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Vendite")

    def test_bulk_preventivo(self):
        self.cambia_stato()
        self.fattura_preventivi()


    def cambia_stato(self):
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))), "1", wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_status"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_stato-container"]', option_text='Bozza')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        stato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[6]'))
        ).text
        self.assertEqual(stato, "Bozza")

        self.wait_for_element_and_click('//tbody//tr//td')

        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_status"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_stato-container"]', option_text='Accettato')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

    def fattura_preventivi(self):
        self.navigateTo("Preventivi")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td[1]')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="create_invoice"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-raggruppamento-container"]', option_text='Cliente')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.wait_for_dropdown_and_select('//span[@id="select2-idstato-container"]', option_text='In lavorazione')
        self.wait_for_element_and_click('//button[@id="save"]')