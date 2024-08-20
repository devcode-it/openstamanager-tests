from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DdtUscita(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Magazzino")


    def test_creazione_ddt_uscita(self):
        # Crea un nuovo ddt al cliente "Cliente". *Required*
        importi = RowManager.list()
        self.creazione_ddt_uscita("Cliente", "2", importi[0])

        # Duplica ddt uscita
        self.duplica_ddt_uscita()

        # Modifica Ddt
        self.modifica_ddt("Evaso")
        
        # Cancellazione Ddt
        self.elimina_ddt()

        # Verifica DDT
        self.verifica_ddt()

        # Verifica plugin DDT del cliente da Anagrafiche
        self.ddt_del_cliente()

        # Cambia stato (Azioni di gruppo)
        self.cambia_stato()

        # Fattura ddt in uscita (Azioni di gruppo)
        self.fattura_ddt_uscita()

        self.duplica_ddt_uscita()

        # Elimina selezionati (Azioni di gruppo)
        self.elimina_selezionati()

    def creazione_ddt_uscita(self, cliente: str, causale: str, file_importi: str):
        self.navigateTo("Ddt in uscita")

        # Crea DDT
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        select = self.input(modal, 'Destinatario')
        select.setByText(cliente)
        select = self.input(modal, 'Causale trasporto')
        select.setByIndex(causale)
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

        row_manager = RowManager(self)
        self.valori=row_manager.compile(file_importi)

    def duplica_ddt_uscita(self):
        self.navigateTo("Ddt in uscita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()  
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary ask"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]').click()
        sleep(1)

    def modifica_ddt(self, modifica):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Ddt in uscita")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys('01', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        self.driver.execute_script('window.scrollTo(0,0)')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatoddt-container"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input[@type="search"]'))).send_keys("Evaso")
        sleep(1)

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

        self.navigateTo("Ddt in uscita")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def elimina_ddt(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Ddt in uscita")
        self.wait_loader()    

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys('02', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)
        
    def verifica_ddt(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Ddt in uscita")
        self.wait_loader()    

        # Verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys("01", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[11]').text
        self.assertEqual("Evaso",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

        # Verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys("02", Keys.ENTER)
        sleep(1)

        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)

        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)


    def ddt_del_cliente(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
        self.wait_loader() 
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER) 
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click() 
        sleep(1) 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@id="link-tab_17"]'))).click()
        self.find(By.XPATH, '//tbody//tr[10]//td[2]').click()
        self.wait_loader()

    def cambia_stato(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Ddt in uscita")
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys("01", Keys.ENTER) 
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click() 
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() 
        self.find(By.XPATH, '//a[@data-op="cambia_stato"]').click() 
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-id_stato-container"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Evaso", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() 
        self.wait_loader()

        stato=self.find(By.XPATH, '(//tr[1]//td[11]//span)[2]').text
        self.assertEqual(stato, "Evaso")    
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def fattura_ddt_uscita(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Ddt in uscita")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys("01", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() 
        self.find(By.XPATH, '//a[@data-op="crea_fattura"]').click()  
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-raggruppamento-container"]').click()   
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")   
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  
        self.wait_loader()

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        tipo=self.find(By.XPATH, '//tbody//tr[3]//td[5]').text  
        self.assertEqual(tipo, "Cliente")

        self.find(By.XPATH, '//tbody//tr[3]//td[5]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask "]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.expandSidebar("Magazzino")
        self.navigateTo("Ddt in uscita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td').click()   

    def elimina_selezionati(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Ddt in uscita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td').click()   
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() 
        self.find(By.XPATH, '//a[@data-op="delete-bulk"]').click()   
        sleep(2)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys('2', Keys.ENTER)
        sleep(1)

        scritta=self.find(By.XPATH, '//tbody//tr').text
        self.assertEqual(scritta, "La ricerca non ha portato alcun risultato.") 

        self.find(By.XPATH, '//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]').click() 
        sleep(1)