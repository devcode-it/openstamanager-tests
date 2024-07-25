from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Movimenti(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Magazzino")


    def test_creazione_movimento(self, modifica="Movimento di Prova"):
        # Crea movimento *Required*
        self.creazione_movimento("10", "Articolo di Prova", "Movimento di Prova")
        self.creazione_movimento("5", "Articolo di Prova", "Movimento di Prova da Eliminare")

        # Cancellazione movimento
        self.elimina_movimento()

        # Verifica movimento
        self.verifica_movimento()

        # Verifica movimenti documenti
        self.verifica_movimenti_documenti()

    def creazione_movimento(self, qta: str, articolo: str, descrizione:str):
        # Crea un nuovo movimento. 
        # Apre la schermata di nuovo elemento
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Movimenti")
        self.wait_loader()
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        self.find(By.XPATH,'//span[@id="select2-idarticolo-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(articolo, Keys.ENTER)

        self.input(modal, 'Quantità').setValue(qta)
        self.input(modal, 'Descrizione movimento').setValue(descrizione)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        sleep(2)
              
    def elimina_movimento(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Movimenti")
        self.wait_loader()  

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Movimento di Prova da Eliminare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger btn-xs ask"]/i[@class="fa fa-trash"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        sleep(1)

        self.navigateTo("Movimenti")
        self.wait_loader() 

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

    def verifica_movimento(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Movimenti")
        self.wait_loader()    

        #verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys("Movimento di prova da Eliminare", Keys.ENTER)
        sleep(1)
        
        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)
        sleep(2)
        
    def verifica_movimenti_documenti(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        #verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("001", Keys.ENTER)
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[2]'))).click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@id="link-tab_10"]'))).click()

        movimento = wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_10"]//tbody//td[1])[1]'))).text
        ddt_uscita = wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_10"]//tbody//td[1])[2]'))).text
        ddt_entrata = wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_10"]//tbody//td[1])[3]'))).text
        fattura_acquisto2 = wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_10"]//tbody//td[1])[4]'))).text
        fattura_acquisto = wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_10"]//tbody//td[1])[5]'))).text
        attività = wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_10"]//tbody//td[1])[6]'))).text
        eliminazioneserial = wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_10"]//tbody//td[1])[7]'))).text
        carico = wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_10"]//tbody//td[1])[8]'))).text

        self.assertEqual(movimento, "10,00")
        self.assertEqual(ddt_uscita, "-1,00")
        self.assertEqual(ddt_entrata, "1,00")
        self.assertEqual(fattura_acquisto2, "1,00")
        self.assertEqual(fattura_acquisto, "1,00")
        self.assertEqual(attività, "-1,00")
        self.assertEqual(eliminazioneserial, "-1,00")
        self.assertEqual(carico, "2,00")
