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


class Attivita(Test):
    def setUp(self):
        super().setUp()

       
    def test_attivita(self):
        # Crea un nuovo intervento. *Required*
        importi = RowManager.list()
        self.attivita("Cliente", "1", "2", importi[0])

        # Duplica attività
        self.duplica_attività()

        # Modifica intervento
        self.modifica_attività("3")

        # Cancellazione intervento
        self.elimina_attività()

        # Controllo righe
        self.controllo_righe()

        # Verifica attività
        self.verifica_attività()

        # Controllo storico attività plugin in Anagrafica
        self.storico_attivita()
        
        # Cambio stato (Azioni di gruppo)
        self.cambio_stato()

        # Duplica attività (Azioni di gruppo)
        self.duplica()

        # Elimina selezionati (Azioni di gruppo)
        self.elimina_selezionati()

    def attivita(self, cliente: str, tipo: str, stato: str, file_importi: str):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attività")

        # Crea un nuovo intervento. 
        # Apre la schermata di nuovo elemento
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        self.input(modal, 'Cliente').setByText(cliente)
        self.input(modal, 'Tipo').setByIndex(tipo)

        self.find(By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]').click()  
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).send_keys("Test")
        self.find(By.XPATH, '//div[@class="col-md-12 text-right"]//button[@type="button"]').click()
        self.wait_loader()

        row_manager = RowManager(self)
        self.valori=row_manager.compile(file_importi)


    def duplica_attività(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="pulsanti"]//button[1]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_stato-container"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-results"]//li[2]'))).click()
        self.find(By.XPATH, '//div[@class="modal-content"]//button[@type="submit"]').click()
        self.wait_loader()
    
    def modifica_attività(self, modifica:str):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attività")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys('1', Keys.ENTER)        
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        
        self.input(None,'Stato').setValue(modifica)
        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

    def elimina_attività(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attività")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys('2', Keys.ENTER)        
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()
        
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

    def controllo_righe(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attività")
        self.wait_loader()  
        
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys('1', Keys.ENTER)
        sleep(1)
        
        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        sleep(1)

        imponibile = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[1]//td[2]').text
        sconto = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[2]//td[2]').text
        totale = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text

        self.assertEqual(imponibile, (self.valori["Imponibile"] + ' €'))
        self.assertEqual(sconto, (self.valori["Sconto/maggiorazione"]+ ' €'))
        self.assertEqual(totale, (self.valori["Totale imponibile"]+ ' €'))


        imponibilefinale=self.find(By.XPATH, '//div[@id="costi"]//tbody[2]//tr[1]//td[2]').text
        scontofinale=self.find(By.XPATH, '//div[@id="costi"]//tbody[2]//tr[2]//td[2]').text
        totaleimpfinale=self.find(By.XPATH, '//div[@id="costi"]//tbody[2]//tr[3]//td[2]').text
        IVA=self.find(By.XPATH, '//div[@id="costi"]//tbody[2]//tr[4]//td[2]').text
        totalefinale=self.find(By.XPATH, '//div[@id="costi"]//tbody[2]//tr[5]//td[2]').text

        self.assertEqual(imponibilefinale,imponibile)
        self.assertEqual(scontofinale,sconto)
        self.assertEqual(totaleimpfinale,totale)
        self.assertEqual(IVA, (self.valori["IVA"] + ' €'))
        self.assertEqual(totalefinale, (self.valori["Totale documento"] + ' €'))

        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

    def verifica_attività(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attività")
        self.wait_loader()    

        #verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys("1", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[7]').text
        self.assertEqual("Fatturato",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

        #verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys("2", Keys.ENTER)
        sleep(1)
        
        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

    

    def storico_attivita(self):  
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        sleep(1) 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        sleep(1)
        self.find(By.XPATH, '//a[@id="link-tab_28"]').click() #apre pagina con tutte le attività
        self.find(By.XPATH, '//div[@id="tab_28"]//tbody//tr[1]//td[1]') #se rileva il checkbox della attività il test è superato

        self.navigateTo("Anagrafiche")
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

    def cambio_stato(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attività")
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys("1", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '(//div[@id="tab_0"]//tr[1]//td[1])[2]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//a[@class="bulk-action clickable dropdown-item"])[4]'))).click()
        self.find(By.XPATH, '//span[@id="select2-id_stato-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Da programmare")
        sleep(2)

        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()
        self.wait_loader()

        stato=self.find(By.XPATH, '(//div[@id="tab_0"]//tr[1]//td[7]//div)[2]').text
        self.assertEqual(stato, "Da programmare")
        #ritorno come era prima
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//a[@class="bulk-action clickable dropdown-item"])[4]'))).click()
        self.find(By.XPATH, '//span[@id="select2-id_stato-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Programmato")
        sleep(2)

        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()
        self.wait_loader()

        nuovo_stato=self.find(By.XPATH, '(//div[@id="tab_0"]//tr[1]//td[7]//div)[2]').text
        self.assertEqual(nuovo_stato, "Programmato")
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

    def duplica(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attività")
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys("1", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '(//div[@id="tab_0"]//tr[1]//td[1])[2]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//a[@class="bulk-action clickable dropdown-item"])[5]'))).click()
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idstatointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Da programmare")
        sleep(2)

        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys("2", Keys.ENTER)
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_0"]//tr[1]//td[2])[2]')))
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

    def elimina_selezionati(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attività")
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys("2", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '(//div[@id="tab_0"]//tr[1]//td[1])[2]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//a[@class="bulk-action clickable dropdown-item"])[1]'))).click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        scritta=self.find(By.XPATH, '(//div[@id="tab_0"]//tr[1])[4]').text
        self.assertEqual(scritta, "La ricerca non ha portato alcun risultato.")
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(2)