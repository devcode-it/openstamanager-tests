from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class OrdiniFornitore(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Acquisti")

    def test_bulk_ordine_fornitore(self):
        self.cambia_stato()
        self.duplica()
        self.invia_mail()
        
    def cambia_stato(self):
        self.navigate_to_and_wait("Ordini fornitore")

        self.search_by_th("th_Numero", "1")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="change_status"]'
        )
        self.select_state('Evaso')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        stato = self.get_table_text(1, 6)
        self.assertEqual(stato, "Evaso")
        self.clear_filters()

    def duplica(self):
        self.navigate_to_and_wait("Ordini fornitore")

        self.search_by_th("th_Numero", "1")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="copy_bulk"]'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.clear_filters()

        numero = self.get_table_text(2, 2)
        self.assertEqual(numero, "2")


    def invia_mail(self):
        self.navigate_to_and_wait("Ordini fornitore")

        self.search_by_th("th_Numero", "1")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="send_mail"]'
        )
        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_template-container"]',
            option_text='Ordine'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')
        self.clear_filters()