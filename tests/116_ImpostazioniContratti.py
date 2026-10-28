from common.Test import Test, get_html
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
        ## TODO: raggruppamento fatturazione massiva contratti

    def condizioni_generali_contratti(self):
        wait = self.wait_driver
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Contratti"]'))
        ).click()

        element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Condizioni generali di fornitura contratti")]//iframe'))
        )
        element.click()
        element.send_keys('Prova')

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Contratti")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys("Manutenzione")
        self.wait_for_dropdown_and_select('//span[@id="select2-id_anagrafica-container"]', option_text='Cliente')
        data_accettazione = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_accettazione"]')))
        data_accettazione.send_keys("01/01/2026")
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change', {bubbles: true}));", data_accettazione)
        data_conclusione = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_conclusione"]')))
        data_conclusione.send_keys("31/12/2026")
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change', {bubbles: true}));", data_conclusione)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[@type="submit"]'))
        ).click()
        self.wait_loader()
        
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="print-button_p"]'))
        ).click()

        wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])

        wait.until(lambda d: 'Prova' in d.find_element(By.ID, 'viewer').text)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.wait_for_element_and_click('//a[@class="btn btn-danger ask"]')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Contratti"]'))
        ).click()

        element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Condizioni generali di fornitura contratti")]//iframe'))
        )
        element.click()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACKSPACE)

        # blur per far scattare il salvataggio AJAX del setting
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Contratti"]'))
        ).click()
        self.wait_ajax()

    def crea_contratto_rinnovabile(self):
        wait = self.wait_driver
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Contratti"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Crea contratto rinnovabile di default")]//div//label'))
        ).click()

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Contratti")

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
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Contratti"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Crea contratto rinnovabile di default")]//div//label'))
        ).click()

    def giorni_preavviso(self):
        wait = self.wait_driver
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Contratti"]'))
        ).click()

        giorni_setting = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Giorni di preavviso di default")]//input'))
        )
        giorni_setting.send_keys(Keys.CONTROL, 'a')
        giorni_setting.send_keys('3')

        # blur per far scattare il salvataggio AJAX del setting
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Contratti"]'))
        ).click()
        self.wait_ajax()

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Contratti")

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
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Contratti"]'))
        ).click()

        giorni_setting = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Giorni di preavviso di default")]//input'))
        )
        giorni_setting.send_keys(Keys.CONTROL, 'a')
        giorni_setting.send_keys('2')

        # blur per far scattare il salvataggio AJAX del setting
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Contratti"]'))
        ).click()
        self.wait_ajax()