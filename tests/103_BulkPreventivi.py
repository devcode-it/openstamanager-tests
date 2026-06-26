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
        self.duplica()

    def cambia_stato(self):
        self.navigate_to_and_wait("Preventivi")

        self.search_by_th("th_Numero", "1")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="change_status"]'
        )

        self.select_state('Bozza')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        stato = self.get_table_text(1, 6)
        self.assertEqual(stato, "Bozza")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="change_status"]'
        )

        self.select_state('Accettato')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.clear_filters()

    def fattura_preventivi(self):
        self.navigate_to_and_wait("Preventivi")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="create_invoice"]'
        )

        self.wait_for_dropdown_and_select('//span[@id="select2-raggruppamento-container"]', option_text='Cliente')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.click_first_table_row()

        self.wait_for_dropdown_and_select('//span[@id="select2-id_stato-container"]', option_text='In lavorazione')
        self.wait_for_element_and_click('//button[@id="save"]')

    def duplica(self):
        self.navigate_to_and_wait("Preventivi")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="copy_bulk"]'
        )

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.clear_filters()
        self.send_keys_and_wait(self.driver.find_element(By.XPATH, '//th[@id="th_Numero"]/input'), "2", wait_modal=False)
