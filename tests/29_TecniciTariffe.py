from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TecniciTariffe(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Attività")
        
    def test_tecnici_tariffe(self):
        # Modifica Tariffe
        self.modifica_tariffe("28.00")

        # Verifica Tariffe
        self.verifica_tariffe()

    def modifica_tariffe(self, modifica):
                self.navigateTo("Tecnici e tariffe")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Tecnico', Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="input-group"]/input[@id="costo_ore1"]'))).send_keys(modifica)
            
        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()
        
        self.navigateTo("Tecnici e tariffe")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()

    def verifica_tariffe(self):
                self.navigateTo("Tecnici e tariffe")
        self.wait_loader()    

        # Verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Tecnico", Keys.ENTER)

        self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[2]').click()

        self.find(By.XPATH, '//div[@class="input-group"]/input[@id="costo_ore1"][@value="28.000000"]').click()
        modificato="28.000000"
        self.assertEqual("28.000000", modificato)

