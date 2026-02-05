from common.Test import Test
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class FattureVendita(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Vendite")

    def test_plugin_fattura_vendita(self):
        self.movimenti_contabili()
        #TODO: Ricevute FE
        #self.ricevute_fe()
        #TODO: Fatturazione elettronica modulo
        #self.fatturazione_elettronica_modulo()
        self.registrazioni()
        #TODO: Importazione FE
        #self.importazione_fe()
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')
        
    def movimenti_contabili(self):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Tipo"]/input')))
        self.send_keys_and_wait(search_input, "Fattura immediata di vendita", wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//a[@id="link-tab_37"]')
        self.wait_for_element_and_click('//a[@class="btn btn-info btn-lg"]')

        dare_1 = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_37"]//tbody//td)[3]'))).text
        avere_1 = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_37"]//tbody//td)[9]'))).text
        avere_2 = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_37"]//tbody//td)[14]'))).text

        self.assertEqual(dare_1, "102,00 €")
        self.assertEqual(avere_1, "100,00 €")
        self.assertEqual(avere_2, "2,00 €")

        self.navigateTo("Fatture di vendita")
        self.wait_loader()
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

    def registrazioni(self):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Tipo"]/input')))
        self.send_keys_and_wait(search_input, "Fattura immediata di vendita", wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//a[@id="link-tab_42"]')
        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_42"]//tr[2]//td')))

        self.navigateTo("Fatture di vendita")
        self.wait_loader()
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

