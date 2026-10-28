from common.Test import Test, get_html
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from common.RowManager import RowManager

class Impostazioni(Test):
    def setUp(self):
        super().setUp()

    def test_impostazioni_ddt(self):
        # Test Cambia automaticamente stato ddt fatturati
        importi = RowManager.list()
        self.cambia_stato_ddt_fatturati(importi[0])
        ## TODO: raggruppamento fatturazione massiva ddt
        ## TODO: raggruppa gli articoli con sttesso barcode nei ddt

    def cambia_stato_ddt_fatturati(self, file_importi: str):
        wait = self.wait_driver
        self.expandSidebar("Magazzino")
        self.navigate_to_and_wait("Ddt in entrata")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_for_element_and_click('//span[@id="select2-id_anagrafica_add-container"]')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Fornitore")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[contains(normalize-space(.), "00000006")]'))).click()

        self.wait_for_dropdown_and_select('//span[@id="select2-id_causale_t-container"]', option_text='Conto lavorazione')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[@type="submit"]'))
        ).click()
        self.wait_loader()

        row_manager = RowManager(self)
        self.valori = row_manager.compile(file_importi)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_stato-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Evaso")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[contains(@class, "select2-results__option--highlighted")]'))).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()

        self.navigate_to_and_wait("Ddt in entrata")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="create_invoice"]'
        )

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-raggruppamento-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[contains(@class, "select2-results__option--highlighted")]'))).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]'))
        ).click()
        self.wait_loader()

        stato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[11]'))
        ).text
        # In 2.11.2 lo stato è "Parzialmente fatturato": getQtaFatturata() esclude
        # le righe di tipo Sconto (qta_fatturata=32) mentre il DDT le conta in qta (33)
        self.assertEqual(stato, "Parzialmente fatturato")
        self.wait_and_click_table_row(1, 2)

        self.wait_for_element_and_click('//a[@class="btn btn-danger ask"]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Acquisti")
        self.navigate_to_and_wait("Fatture di acquisto")

        self.click_first_table_row()
        self.wait_loader()

        self.wait_for_element_and_click('//a[@id="elimina"]')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Magazzino")
        self.navigate_to_and_wait("Ddt in uscita")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_for_element_and_click('//span[@id="select2-id_anagrafica_add-container"]')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[contains(normalize-space(.), "00000004")]'))).click()

        self.wait_for_dropdown_and_select('//span[@id="select2-id_causale_t-container"]', option_text='Conto lavorazione')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[@type="submit"]'))
        ).click()
        self.wait_loader()

        row_manager = RowManager(self)
        self.valori = row_manager.compile(file_importi)

        self.driver.execute_script('window.scrollTo(0,0)')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_stato-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Evaso")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[contains(@class, "select2-results__option--highlighted")]'))).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()

        self.navigate_to_and_wait("Ddt in uscita")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="create_invoice"]'
        )

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-raggruppamento-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[contains(@class, "select2-results__option--highlighted")]'))).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]'))
        ).click()
        self.wait_loader()

        stato2 = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[11]'))
        ).text
        # Come sopra: con la riga sconto lo stato resta "Parzialmente fatturato" in 2.11.2
        self.assertEqual(stato2, "Parzialmente fatturato")
        self.wait_and_click_table_row(1, 2)

        self.wait_for_element_and_click('//a[@class="btn btn-danger ask"]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")

        self.click_first_table_row()
        self.wait_loader()

        self.wait_for_element_and_click('//a[@id="elimina"]')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()
