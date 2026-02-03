from common.Test import Test, get_html
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Impostazioni(Test):
    def setUp(self):
        super().setUp()

    def test_impostazioni_contratti(self):
        # Test Condizioni generali di fornitura contratti
        self.condizioni_generali_contratti()

        # Test Crea contratto rinnovabile di default
        self.crea_contratto_rinnovabile()

        # Test Giorni di preavviso di default
        self.giorni_preavviso()

        ## TODO: cambia automaticamente stato contratti fatturati

    def condizioni_generali_contratti(self):
                self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Contratti"]'))
        ).click()

        element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Condizioni generali di fornitura contratti"))
        )]//iframe')
        element.click()
        element.send_keys('Prova')

        self.expandSidebar("Vendite")
        self.navigateTo("Contratti")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys("Manutenzione")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_accettazione"]'))).send_keys("01/01/2025")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_conclusione"]'))).send_keys("31/12/2025")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()
        self.wait_loader()
        
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="print-button_p"]'))
        ).click()

        self.driver.switch_to.window(self.driver.window_handles[1])

        test = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//div[@class="page"])[2]//span[26]'))
        ).text
        self.assertEqual(test, "Prova")
        self.driver.close() 
        self.driver.switch_to.window(self.driver.window_handles[0])

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()  
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Contratti"]'))
        ).click()

        element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Condizioni generali di fornitura contratti"))
        )]//iframe')
        element.click()
        element.send_keys(Keys.BACKSPACE * 5)
        
    def crea_contratto_rinnovabile(self):
        wait = self.wait_driver  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Contratti"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Crea contratto rinnovabile di default"))
        )]//div//label').click()

        self.expandSidebar("Vendite")
        self.navigateTo("Contratti")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-tool"]'))
        ).click()

        stato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//label[@class="btn btn-default active"]//span[1]'))
        ).text 
        self.assertEqual(stato, "Attivato")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="close"]'))
        ).click()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Contratti"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Crea contratto rinnovabile di default"))
        )]//div//label').click()

    def giorni_preavviso(self):
        wait = self.wait_driver  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Contratti"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Giorni di preavviso di default"))
        )]//input').send_keys('3,00')

        self.expandSidebar("Vendite")
        self.navigateTo("Contratti")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-tool"]'))
        ).click()

        giorni_element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="giorni_preavviso_rinnovo_add"]'))
        )  
        giorni = giorni_element.get_attribute("value")
        self.assertEqual(giorni, "3,00")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="close"]'))
        ).click()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Contratti"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Giorni di preavviso di default"))
        )]//input').send_keys('2,00')