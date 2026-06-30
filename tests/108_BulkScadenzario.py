from common.Test import Test
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class Scadenzario(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Contabilità")

    def test_bulk_scadenzario(self):
        self.aggiorna_banca()
        self.info_distinta()
        self.invia_mail_sollecito()
        self.registrazione_contabile()


    def aggiorna_banca(self):
        self.navigate_to_and_wait("Scadenzario")
        self.search_by_th("th_Rif-Fattura", "0002/2026")
        self.wait_for_search_results()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="change_bank"]'
        )

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_banca-container"]',
            option_text="Test"
        )

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')
        self.clear_filters()

    def info_distinta(self):
        self.navigate_to_and_wait("Scadenzario")
        self.search_by_th("th_Rif-Fattura", "0002/2026")
        self.wait_for_search_results()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="change_distinta"]'
        )

        self.input(name='distinta').setValue('Test')

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')
        self.clear_filters()

    def invia_mail_sollecito(self):
        self.navigate_to_and_wait("Scadenzario")
        self.search_by_th("th_Rif-Fattura", "0002/2026")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="send_reminder"]'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')
        self.clear_filters()
    
    def registrazione_contabile(self):
        self.navigate_to_and_wait("Scadenzario")
        self.search_by_th("th_Rif-Fattura", "0002/2026")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="registrazione-contabile"]'
        )
        modal = self.wait_modal()

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-conto_add_1-container"]',
            option_text='Banca C/C'
        )

        self.wait_for_element_and_click('//button[@type="submit"]')

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")
        self.clear_filters()

