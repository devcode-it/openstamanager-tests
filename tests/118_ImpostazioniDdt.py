from common.Test import Test, get_html
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common.RowManager import RowManager

class Impostazioni(Test):
    def setUp(self):
        super().setUp()

    def test_impostazioni_ddt(self):
        # Test Cambia automaticamente stato ddt fatturati
        importi = RowManager.list()
        self.cambia_stato_ddt_fatturati(importi[0])

    def cambia_stato_ddt_fatturati(self, file_importi: str):
        wait = self.wait_driver 
        self.expandSidebar("Magazzino")
        self.navigateTo("Ddt in entrata")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Admin spa", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idcausalet-container"]'))
        ).click()   
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Conto lavorazione", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() 
        self.wait_loader()

        row_manager = RowManager(self)
        self.valori = row_manager.compile(file_importi)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatoddt-container"]'))
        ).click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Evaso", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()

        self.navigateTo("Ddt in entrata")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td')   
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@data-toggle="dropdown"]'))
        ).click() 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@data-op="crea_fattura"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-raggruppamento-container"]'))
        ).click()   
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]'))
        ).click() 
        self.wait_loader()

        stato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[11]'))
        ).text 
        self.assertEqual(stato, "Fatturato")
        self.wait_for_element_and_click('//tbody//tr[1]//td[2]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Acquisti")
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td[2]') 
        self.wait_loader()
    
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click()   
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()  
        self.wait_loader()

        self.expandSidebar("Magazzino")
        self.navigateTo("Ddt in uscita")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Admin spa")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idcausalet-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Conto lavorazione")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()
        self.wait_loader()

        row_manager = RowManager(self)
        self.valori = row_manager.compile(file_importi)

        self.driver.execute_script('window.scrollTo(0,0)')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatoddt-container"]'))
        ).click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Evaso", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()

        self.navigateTo("Ddt in uscita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td')    
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@data-toggle="dropdown"]'))
        ).click() 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@data-op="crea_fattura"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-raggruppamento-container"]'))
        ).click()   
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]'))
        ).click() 
        self.wait_loader()

        stato2 = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[11]'))
        ).text  
        self.assertEqual(stato2, "Fatturato")
        self.wait_for_element_and_click('//tbody//tr[1]//td[2]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td[2]')  
        self.wait_loader()
    
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click()  
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()  
        self.wait_loader()