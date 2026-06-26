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
        self.cambia_metodo_pagamento()
        self.fattura_contratti()
        self.rinnova_contratti()
        self.duplica_contratti()
    
    def cambia_stato(self):
        self.navigate_to_and_wait("Contratti")

        self.search_by_th("th_Numero", "1", wait_modal=False)


        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="change_status"]'
        )
        self.select_state('In lavorazione')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        stato = self.get_table_text(1, 5)
        self.assertEqual(stato, "In lavorazione")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.clear_filters()

    def cambia_metodo_pagamento(self):
        self.navigate_to_and_wait("Contratti")

        self.search_by_th("th_Numero", "1", wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="change_payment"]'
        )

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_pagamento-container"]',
            option_text='Bonifico 120gg d.f.'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.click_first_result()
        metodo_pagamento = self.wait_for_element_and_click('//span[@id="select2-id_pagamento-container"]').text
        self.assertEqual(metodo_pagamento, "MP05 - Bonifico 120gg d.f.")

        self.navigate_to_and_wait("Contratti")
        self.wait_for_element_and_click('//tbody//tr//td')
        self.clear_filters()

    def fattura_contratti(self):
        self.navigate_to_and_wait("Contratti")

        self.search_by_th("th_Numero", "1", wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="create_invoice"]'
        )

        self.wait_for_dropdown_and_select('//span[@id="select2-raggruppamento-container"]', option_text='Cliente')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.navigate_to_and_wait("Fatture di vendita")

        tipo = self.get_table_text(3, 5)
        self.assertEqual(tipo, "Fattura immediata di vendita")

        self.wait_and_click_table_row(3, 4)
        self.delete_current_and_clear()

        self.navigate_to_and_wait("Contratti")
        self.clear_filters()

    def rinnova_contratti(self):
        self.navigate_to_and_wait("Contratti")

        self.search_by_th("th_Numero", "1", wait_modal=False)

        self.click_first_table_row()

        self.send_keys_and_wait(self.driver.find_element(By.XPATH, '//input[@id="data_accettazione"]'), '01/01/2026')
        self.send_keys_and_wait(self.driver.find_element(By.XPATH, '//input[@id="data_conclusione"]'), '31/12/2026')
        self.wait_for_element_and_click('//div[@class="btn-group checkbox-buttons"]//label[@for="rinnovabile"]')
        self.wait_for_dropdown_and_select('//span[@id="select2-id_stato-container"]', option_text='Accettato')
        self.wait_for_element_and_click('//button[@id="save"]')

        self.navigate_to_and_wait("Contratti")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="renew_contract"]'
        )

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.clear_filters()

        self.send_keys_and_wait(self.driver.find_element(By.XPATH, '//th[@id="th_Numero"]/input'), "1", wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.click_first_table_row()
        self.delete_current_and_clear()

    def duplica_contratti(self):
        self.navigate_to_and_wait("Contratti")

        self.search_by_th("th_Numero", "1", wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="copy_bulk"]'
        )

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.clear_filters()
        self.send_keys_and_wait(self.driver.find_element(By.XPATH, '//th[@id="th_Numero"]/input'), "2", wait_modal=False)
