from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrdiniFornitore(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Acquisti")


    def test_creazione_ordine_fornitore(self):
        # Crea una nuovo ordine fornitore *Required*
        importi = RowManager.list()
        self.creazione_ordine_fornitore("Fornitore", importi[0])
        self.creazione_ordine_fornitore("Fornitore", importi[0])

        # Modifica ordine fornitore
        self.modifica_ordine_fornitore("Modifica di Prova")

        # Cancellazione ordine fornitore
        self.elimina_ordine_fornitore()
    
        # Verifica ordine fornitore
        self.verifica_ordine_fornitore()

        # Cambia stato (Azioni di gruppo)
        self.cambia_stato()

    def creazione_ordine_fornitore(self, fornitore: str, file_importi: str):
        self.navigateTo("Ordini fornitore")

        # Crea Ordine
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        select = self.input(modal, 'Fornitore')
        select.setByText(fornitore)
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

        row_manager = RowManager(self)
        self.valori=row_manager.compile(file_importi)

    def modifica_ordine_fornitore(self, modifica):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Ordini fornitore")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys('1', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        self.driver.execute_script('window.scrollTo(0,0)')
        sleep(1)
        
        self.find(By.XPATH, '//span[@aria-labelledby="select2-idstatoordine-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input[@type="search"]'))).send_keys("Accettato")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//button[@id="save"]'))).click()
        sleep(1)

        # Estrazione totali righe
        sconto = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[2]//td[2]').text
        totale_imponibile = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text
        iva = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[4]//td[2]').text
        totale = self.find(By.XPATH, '//div[@id="tab_0"]//div[@id="righe"]//tbody[2]//tr[5]//td[2]').text

        self.assertEqual(sconto, (self.valori["Sconto/maggiorazione"]+ ' €'))
        self.assertEqual(totale_imponibile, (self.valori["Totale imponibile"]+ ' €'))
        self.assertEqual(iva, (self.valori["IVA"] + ' €'))
        self.assertEqual(totale, (self.valori["Totale documento"] + ' €'))

        self.navigateTo("Ordini fornitore")
        self.wait_loader()  

        self.find(By.XPATH, '//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def elimina_ordine_fornitore(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Ordini fornitore")
        self.wait_loader()  

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys('2', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def verifica_ordine_fornitore(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Ordini fornitore")
        self.wait_loader()  

        # Verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_icon_title_Stato"]/input'))).send_keys("Accettato", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[6]').text
        self.assertEqual("Accettato",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

        # Verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys("2", Keys.ENTER)
        sleep(1)

        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)
        self.find(By.XPATH, '//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def cambia_stato(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Ordini fornitore")
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys("1", Keys.ENTER) 
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click() 
        self.find(By.XPATH, '//button[@data-toggle="dropdown"]').click()  
        self.find(By.XPATH, '//a[@data-op="cambia_stato"]').click() 
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-id_stato-container"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Evaso")
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-id_stato-results"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() 
        self.wait_loader()

        stato=self.find(By.XPATH, '//tbody//tr//td[6]').text
        self.assertEqual(stato, "Evaso")  

        self.find(By.XPATH, '//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]').click() 
        sleep(1)
