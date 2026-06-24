from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Impianti(Test):
    def setUp(self):
        super().setUp()
        self.navigate_to_and_wait("Impianti")

    def test_plugin_impianti(self):
        self.interventi_svolti()
        self.componenti()

    def interventi_svolti(self):
        self.navigate_to_and_wait("Impianti")

        self.click_first_table_row()
        self.close_tour()
        
        self.wait_for_element_and_click('//a[@id="link-tab_8"]')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_8"]//i[@class="fa fa-external-link"]'))
        ).text

    def componenti(self):
        self.navigate_to_and_wait("Impianti")

        self.click_first_table_row()
        self.wait_for_element_and_click('//a[@id="link-tab_31"]')

        self.wait_for_element_and_click('//div[@id="tab_31"]//i[@class="fa fa-plus"]')

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_articolo_componente-container"]',
            option_text="Articolo 1"
        )
               
        self.wait_for_element_and_click('//div[@class="modal-footer"]//button[@class="btn btn-primary"]')

        componente = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_31"]//table//tr/td[2]'))
        ).text
        self.assertEqual("001 - Articolo 1\nNessun seriale selezionato", componente)