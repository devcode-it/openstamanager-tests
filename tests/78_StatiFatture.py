from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class StatiFatture(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")
        

    def test_creazione_stati_fatture(self):
        # Modifica Stato delle fatture
        self.modifica_stati_fatture("fa fa-file-text text-muted")

        # Verifica Stato delle fatture
        self.verifica_stati_fatture()

    def modifica_stati_fatture(self, modifica = str):
                self.navigateTo("Stati fatture")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Bozza', Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td[2]')    

        self.driver.execute_script('window.scrollTo(0,0)')
        self.input(None,'Icona').setValue(modifica)
        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Stati fatture")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
    
    def verifica_stati_fatture(self):
                self.navigateTo("Stati fatture")
        self.wait_loader()    

        # Verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys("Bozza", Keys.ENTER)

        modificato = self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[3]').text
        self.assertEqual("fa fa-file-text text-muted", modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()