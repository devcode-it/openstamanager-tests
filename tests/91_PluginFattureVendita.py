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

    def movimenti_contabili(self):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Tipo"]/input')))
        self.send_keys_and_wait(search_input, "Fattura immediata di vendita", False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//a[@id="link-tab_37"]')
        self.wait_for_element_and_click('//a[@class="btn btn-info btn-lg"]')

        dare_1 = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_37"]//tbody//td)[3]'))).text
        dare_2 = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_37"]//tbody//td)[23]'))).text
        avere_1 = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_37"]//tbody//td)[9]'))).text
        avere_2 = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_37"]//tbody//td)[14]'))).text
        avere_3 = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_37"]//tbody//td)[19]'))).text
        avere_4 = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_37"]//tbody//td)[29]'))).text
        avere_5 = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_37"]//tbody//td)[34]'))).text

        self.assertEqual(dare_1, "305,98 €")
        self.assertEqual(dare_2, "27,20 €")
        self.assertEqual(avere_1, "2,00 €")
        self.assertEqual(avere_2, "150,00 €")
        self.assertEqual(avere_3, "120,00 €")
        self.assertEqual(avere_4, "6,00 €")
        self.assertEqual(avere_5, "55,18 €")

        self.navigateTo("Fatture di vendita")
        self.wait_loader()
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

    def registrazioni(self):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Tipo"]/input')))
        self.send_keys_and_wait(search_input, "Fattura immediata di vendita", False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//a[@id="link-tab_42"]')
        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_42"]//tr[5]//td')))

        self.navigateTo("Fatture di vendita")
        self.wait_loader()
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

