from common.Test import Test
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Scadenzario(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Contabilità")

    def test_plugin_scadenzario(self):
        self.presentazioni_bancarie()

    def presentazioni_bancarie(self):
        self.navigate_to_and_wait("Scadenzario")

        self.search_by_th("th_Anagrafica", "Cliente")

        self.wait_for_element_and_click('//tbody//tr[1]//td[1]')
        self.wait_for_element_and_click('//a[@id="link-tab_39"]')
        self.wait_for_element_and_click('//i[@class="fa fa-external-link"]')


        self.driver.switch_to.window(self.driver.window_handles[1])

        self.click_add_button()
        modal = self.wait_modal()

        select = self.input(modal, 'Anagrafica')
        select.setByText('Cliente')
        self.input(modal, 'Nome').setValue('test')
        self.input(modal, 'IBAN').setValue('123123123123123123')
        self.input(modal, 'BIC').setValue('123456789')
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.wait_for_element_and_click('//i[@class="fa fa-external-link"]')

        self.driver.switch_to.window(self.driver.window_handles[1])

        self.click_add_button()
        modal = self.wait_modal()

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_anagrafica-container"]',
            option_xpath='//li[@id="select2-result-1"]'
        )

        self.input(modal, 'Nome').setValue('test2')
        self.input(modal, 'IBAN').setValue('123123123123123121')
        self.input(modal, 'BIC').setValue('123456781')
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.navigate_to_and_wait("Scadenzario")
        self.wait_for_element_and_click('//tbody//tr[1]//td[1]')
        self.wait_for_element_and_click('//a[@id="link-tab_39"]')

        self.wait_for_element_and_click('//button[@class="btn btn-primary "]')
        self.wait_for_element_and_click('//button[@onclick="esporta(this)"]')