from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Attivita(Test):
    def setUp(self):
        super().setUp()

    def test_plugin_attivita(self):      
        self.mostra_su_mappa()
        self.impianti()


    def mostra_su_mappa(self):
        self.navigate_to_and_wait("Attività")

        self.wait_for_element_and_click('//a[@id="link-tab_46"]')
        self.wait_for_element_and_click('//a[@class="btn btn-primary btn-lg btn-large"]')

        tasto = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary btn-lg btn-large"]'))
        )

    def impianti(self):
        self.navigate_to_and_wait("Attività")
        self.click_first_result()

        self.input(None, 'Stato*').setByText("Programmato")
        self.driver.execute_script('window.scrollTo(0,0)')
        self.click_save_button()

        self.wait_for_element_and_click('//a[@id="link-tab_2"]')

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_impianto_add-container"]',
            option_text='03'
        )

        self.wait_for_element_and_click('(//button[@class="btn btn-primary tip tooltipstered"])[2]')

        impianto_nome = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="righe-impianti"]//tr//td[3]'))
        ).text
        self.assertEqual("Impianto di Prova", impianto_nome)