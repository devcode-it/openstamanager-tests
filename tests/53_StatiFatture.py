from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class StatiFatture(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")

    def test_creazione_stati_fatture(self):
        self.modifica_stati_fatture("fa fa-file-text text-muted")
        self.verifica_stati_fatture()
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')
        
    def modifica_stati_fatture(self, modifica = str):
        self.navigateTo("Stati fatture")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Bozza', wait_modal=False)
        self.click_first_result()

        self.input(None,'Icona').setValue(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.navigateTo("Stati fatture")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]')

    def verifica_stati_fatture(self):
        self.navigateTo("Stati fatture")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, "Bozza", wait_modal=False)
        modificato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[3]'))).text
        self.assertEqual("fa fa-file-text text-muted", modificato)
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')