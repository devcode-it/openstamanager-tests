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
        
    def attivita(self, cliente: str, tipo: str, stato: str, file_importi: str):
        self.navigateTo("Attività")

        # Crea un nuovo intervento. 
        # Apre la schermata di nuovo elemento
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Cliente').setByText(cliente)
        self.input(modal, 'Tipo').setByIndex(tipo)
        self.input(modal, 'Stato').setByIndex(stato)
        
        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary"]').click()
        self.wait_loader()

        #toast = self.driver.find_elements(By.CLASS_NAME, 'toast-message')
        #self.assertIn('Aggiunto intervento', toast)
        sleep(1)
        row_manager = RowManager(self)
        row_manager.compile(file_importi)

    def duplica_attività(self):
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="pulsanti-modulo"]//button[1]').click()
        sleep(2)
        self.find(By.XPATH, '//span[@id="select2-id_stato-container"]').click()
        sleep(1)
        self.find(By.XPATH, '//span[@class="select2-results"]//li[2]').click()
        sleep(1)

        self.find(By.XPATH, '//div[@class="modal-content"]//button[@type="submit"]').click()
        self.wait_loader()
    
    def modifica_attività(self, modifica:str):
        self.navigateTo("Attività")
        self.wait_loader()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Numero"]/input')
        element.send_keys('1')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        
        self.input(None,'Stato').setValue(modifica)

        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Attività")
        self.wait_loader()  
        self.find(By.XPATH, '//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def elimina_attività(self):
        self.navigateTo("Attività")
        self.wait_loader()  

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Numero"]/input')
        element.send_keys('2')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys(Keys.ENTER)

        sleep(2)
        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]').click()
        self.wait_loader()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        
        self.navigateTo("Attività")
        self.wait_loader()  
        self.find(By.XPATH, '//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def controllo_righe(self):
        self.navigateTo("Attività")
        self.wait_loader()  
        
        element=self.driver.find_element(By.XPATH,'//th[@id="th_Numero"]/input')
        element.send_keys('1')

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys(Keys.ENTER)
        sleep(2)
        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()

        imponibilerighe=('{:,.2f} €'.format(332)).replace('.',',')
        scontorighe='{:,.2f} €'.format(2*15+150*20/100+272*10/100).replace('.',',')
        totalerighe='{:,.2f} €'.format(332-87.20).replace('.',',')

        imponibile = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[1]//td[2]').text
        sconto = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[2]//td[2]').text
        totale = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text

        self.assertEqual(imponibile, imponibilerighe)
        self.assertEqual(sconto, scontorighe)
        self.assertEqual(totale, totalerighe)


        IVARIGHE='{:,.2f} €'.format(0.44+2.20*15+1.76*15-5.98).replace('.',',')
        totalefinalerighe='{:,.2f} €'.format(244.80+53.86).replace('.',',')

        imponibilefinale=self.find(By.XPATH, '//div[@id="costi"]//tbody[2]//tr[1]//td[2]').text
        scontofinale=self.find(By.XPATH, '//div[@id="costi"]//tbody[2]//tr[2]//td[2]').text
        totaleimpfinale=self.find(By.XPATH, '//div[@id="costi"]//tbody[2]//tr[3]//td[2]').text
        IVA=self.find(By.XPATH, '//div[@id="costi"]//tbody[2]//tr[4]//td[2]').text
        totalefinale=self.find(By.XPATH, '//div[@id="costi"]//tbody[2]//tr[5]//td[2]').text

        self.assertEqual(imponibilefinale,imponibile)
        self.assertEqual(scontofinale,sconto)
        self.assertEqual(totaleimpfinale,totale)
        self.assertEqual(IVA, IVARIGHE)
        self.assertEqual(totalefinale, totalefinalerighe)

        self.navigateTo("Attività")
        self.wait_loader()  
        self.find(By.XPATH, '//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def verifica_attività(self):
        self.navigateTo("Attività")
        self.wait_loader()    

        #verifica elemento modificato
        element=self.driver.find_element(By.XPATH,'//th[@id="th_Numero"]/input')
        element.send_keys("1")
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys(Keys.ENTER)
        sleep(1)
        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[7]').text
        self.assertEqual("Fatturato",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times fa-2x"]').click()
        sleep(1)

        #verifica elemento eliminato
        element=self.driver.find_element(By.XPATH,'//th[@id="th_Numero"]/input')
        element.send_keys("2")
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys(Keys.ENTER)
        sleep(1)
        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)