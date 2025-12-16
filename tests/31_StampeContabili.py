from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class StampeContabili(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Contabilità")
        self.navigateTo("Stampe contabili")
        self.wait_loader()
    def test_stampecontabili(self):
        self.apri_stampe_contabili()

    def apri_stampe_contabili(self):
        self.wait_for_element_and_click('//button[@data-title="Stampa registro IVA vendite"]')
        self.wait_for_dropdown_and_select('//span[@id="select2-id_sezionale-container"]', '//ul[@id="select2-id_sezionale-results"]//li[1]')
        self.wait_for_dropdown_and_select('//span[@id="select2-format-container"]', '//ul[@id="select2-format-results"]//li[1]')
        self.wait_for_dropdown_and_select('//span[@id="select2-orientation-container"]', '//ul[@id="select2-orientation-results"]//li[1]')
        self.wait_for_element_and_click('//button[@class="btn btn-primary btn-lg"]')

        self.driver.switch_to.window(self.driver.window_handles[1])
        stampa = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="viewer"]//span[3]'))).text
        self.assertEqual(stampa, "REGISTRO IVA VENDITE DAL 01/01/2025 AL 31/12/2025 - STANDARD VENDITE")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.wait_for_element_and_click('//button[@data-title="Stampa registro IVA acquisti"]')
        self.wait_for_dropdown_and_select('//span[@id="select2-id_sezionale-container"]', '//ul[@id="select2-id_sezionale-results"]//li[1]')
        self.wait_for_element_and_click('//button[@class="btn btn-primary btn-lg"]')

        self.driver.switch_to.window(self.driver.window_handles[1])
        stampa = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="viewer"]//span[3]'))).text
        self.assertEqual(stampa, "REGISTRO IVA ACQUISTI DAL 01/01/2025 AL 31/12/2025 - STANDARD ACQUISTI")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.wait_for_element_and_click('//button[@data-title="Stampa liquidazione IVA"]')
        self.wait_for_element_and_click('//button[@class="btn btn-primary btn-lg"]')

        self.driver.switch_to.window(self.driver.window_handles[1])
        stampa = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="viewer"]//span)[1]'))).text
        self.assertEqual(stampa, "PROSPETTO LIQUIDAZIONE IVA DAL 01/01/2025 AL 31/12/2025")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.wait_for_element_and_click('//button[@data-title="Stampa Bilancio"]')
        self.wait_for_element_and_click('//button[@class="btn btn-primary btn-lg"]')

        self.driver.switch_to.window(self.driver.window_handles[1])
        stampa = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="viewer"]//span'))).text
        self.assertEqual(stampa, "STAMPA BILANCIO")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.wait_for_element_and_click('//button[@class="close"]')

        self.wait_for_element_and_click('//button[@class="btn btn-primary btn-block"]')

        self.driver.switch_to.window(self.driver.window_handles[1])
        stampa = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="viewer"]//span'))).text
        self.assertEqual(stampa, "STAMPA BILANCIO")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.wait_for_element_and_click('(//button[@class="btn btn-primary btn-block"])[2]')

        self.driver.switch_to.window(self.driver.window_handles[1])
        stampa = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="viewer"]//span)[1]'))).text
        self.assertEqual(stampa, "STAMPA BILANCIO")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.wait_for_element_and_click('(//button[@class="btn btn-primary btn-block"])[3]')

        self.driver.switch_to.window(self.driver.window_handles[1])
        stampa = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="viewer"]//span)[9]'))).text
        self.assertEqual(stampa, "FATTURATO MENSILE DAL 01/01/2025 AL 31/12/2025")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.wait_for_element_and_click('(//button[@class="btn btn-primary btn-block"])[4]')

        self.driver.switch_to.window(self.driver.window_handles[1])
        stampa = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="viewer"]//span)[9]'))).text
        self.assertEqual(stampa, "ACQUISTI MENSILI DAL 01/01/2025 AL 31/12/2025")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.wait_for_element_and_click('//button[@data-title="Libro giornale"]')
        self.wait_for_element_and_click('//button[@class="btn btn-primary btn-lg"]')

        self.driver.switch_to.window(self.driver.window_handles[1])
        stampa = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="viewer"]//span)[1]'))).text
        self.assertEqual(stampa, "STAMPA LIBRO GIORNALE")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.wait_for_element_and_click('//button[@data-title="Stampa scadenzario"]')
        self.wait_for_element_and_click('//button[@class="btn btn-primary btn-lg"]')

        self.driver.switch_to.window(self.driver.window_handles[1])
        stampa = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="viewer"]//span)[6]'))).text
        self.assertEqual(stampa, "SCADENZE DAL 01/01/2025 AL 31/12/2025")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
