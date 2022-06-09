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


class Preventivi(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Vendite")

    def test_creazione_preventivo(self):
        # Crea un nuovo preventivo *Required*
        importi = RowManager.list()
        self.creazione_preventivo("Preventivo di Prova","Cliente", "1","Bozza", importi[0])
        self.creazione_preventivo("Preventivo di Prova da Eliminare","Cliente", "1", "Bozza", importi[0])

        # Modifica preventivo *Required*
        self.modifica_preventivo("Accettato")

        # Cancellazione preventivo
        self.elimina_preventivo()

        # Creazione contratto da preventivo
        self.creazione_contratto()        

        # Creazione ordine cliente da preventivo
        self.creazione_ordine_cliente()

        # Creazione ordine fornitore da preventivo
        self.creazione_ordine_fornitore()

        # Creazione attività
        self.creazione_attività()

        # Creazione DDT in uscita
        self.creazione_ddt_uscita()

        # Creazione fattura
        self.creazione_fattura()

    def creazione_preventivo(self, nome:str, cliente:str, idtipo: str, stato:str, file_importi: str):
        self.navigateTo("Preventivi")
        self.wait_loader() 

        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        # Completamento dei campi per il nuovo elemento
        self.input(modal, 'Nome').setValue(nome)

        select = self.input(modal, 'Cliente')
        select.setByText(cliente)

        select = self.input(modal, 'Tipo di Attività')
        select.setByIndex(idtipo)

        select = self.input(modal, 'Stato')
        select.setByText(stato)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

        # Inserimento righe
        row_manager = RowManager(self)
        row_manager.compile(file_importi)

    def modifica_preventivo(self, stato:str):
        self.navigateTo("Preventivi")
        sleep(1)

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Nome"]/input')
        element.send_keys('=Preventivo di Prova')

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        
        # Modifica stato preventivo
        select = self.input(None, 'Stato')
        select.setByText(stato)

        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Preventivi")
        self.wait_loader()  

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def elimina_preventivo(self):
        self.navigateTo("Preventivi")
        self.wait_loader()  

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Nome"]/input')
        element.send_keys('Preventivo di Prova da Eliminare')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys(Keys.ENTER)

        sleep(1)
        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()

        # Cancellazione preventivo
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]').click()
        self.wait_loader()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.navigateTo("Preventivi")
        self.wait_loader()  

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def creazione_contratto(self):
        self.navigateTo("Preventivi")
        self.wait_loader()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Nome"]/input')
        element.send_keys('Preventivo di Prova')

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys(Keys.ENTER)

        sleep(1)
        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()

        totalepreventivo=self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text

        # Creazione contratto
        self.find(By.XPATH, '//button[@class="btn btn-info dropdown-toggle "]').click()
        self.wait_loader()
        self.find(By.XPATH, '//a[@class="bound clickable"][@data-title="Crea contratto"]').click()  
        sleep(1)
        self.find(By.XPATH, '//input[@id="checked_3"]').click()
        self.find(By.XPATH, '//button[@id="submit_btn"]').click()
        self.wait_loader()

        totalecontratto=self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text
        
        # Controllo valori righe preventivo
        self.assertEqual(totalecontratto,totalepreventivo)

        # Eliminazione contratto
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]').click()
        self.wait_loader()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.navigateTo("Preventivi")
        self.wait_loader()  

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def creazione_ordine_cliente(self):
        self.navigateTo("Preventivi")
        self.wait_loader()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Nome"]/input')
        element.send_keys('Preventivo di Prova')

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys(Keys.ENTER)

        sleep(2)
        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()

        totalepreventivo=self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text

        # Creazione ordine cliente
        self.find(By.XPATH, '//button[@class="btn btn-info dropdown-toggle "]').click()
        self.wait_loader()
        self.find(By.XPATH, '//a[@class="bound clickable"][@data-title="Crea ordine cliente"]').click()  
        sleep(1)
        self.find(By.XPATH, '//input[@id="checked_3"]').click()
        self.find(By.XPATH, '//button[@id="submit_btn"]').click()
        self.wait_loader()

        totaleordinecliente=self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text
        
        # Controllo valori righe preventivo
        self.assertEqual(totaleordinecliente,totalepreventivo)

        # Eliminazione ordine
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]').click()
        self.wait_loader()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.navigateTo("Preventivi")
        self.wait_loader()  

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def creazione_ordine_fornitore(self):
        self.navigateTo("Preventivi")
        self.wait_loader()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Nome"]/input')
        element.send_keys('Preventivo di Prova')

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys(Keys.ENTER)

        sleep(1)
        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()

        totalepreventivo=self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text
        # Creazione ordine fornitore
        self.find(By.XPATH, '//button[@class="btn btn-info dropdown-toggle "]').click()
        self.wait_loader()
        self.find(By.XPATH, '//a[@class="bound clickable"][@data-title="Crea ordine fornitore"]').click()  
        modal = self.wait_modal()
        self.find(By.XPATH, '//input[@id="checked_3"]').click()

        self.find(By.XPATH, '//div[@class="input-group has-feedback"]//span[@class="selection"]//span [@id="select2-idanagrafica-container"]').click() 
        sleep(1)
        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()
        self.find(By.XPATH, '//button[@id="submit_btn"]').click()
        self.wait_loader()

        totaleordinefornitore=self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text
        
        # Controllo valori righe preventivo
        self.assertEqual(totaleordinefornitore,totalepreventivo)

        # Eliminazione ordine
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]').click()
        self.wait_loader()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Vendite") 
        self.navigateTo("Preventivi")
        self.wait_loader()  

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def creazione_attività(self):
        self.navigateTo("Preventivi")
        self.wait_loader()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Nome"]/input')
        element.send_keys('Preventivo di Prova')

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys(Keys.ENTER)

        sleep(2)
        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()

        totalepreventivo=self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text

        # Creazione attività
        self.find(By.XPATH, '//button[@class="btn btn-info dropdown-toggle "]').click()
        self.wait_loader()
        self.find(By.XPATH, '//a[@class="bound clickable"][@data-title="Crea attività"]').click()  
        modal = self.wait_modal()
        self.find(By.XPATH, '//input[@id="checked_3"]').click()

        self.find(By.XPATH, '//span[@id="select2-id_tipo_intervento-container"]').click() 
        sleep(1)
        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()
        self.find(By.XPATH, '//button[@id="submit_btn"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-id_stato_intervento-container"]').click() 
        sleep(1)
        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()
        self.find(By.XPATH, '//button[@id="submit_btn"]').click()
        self.wait_loader()

        totaleattività=self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text
        
        # Controllo valori righe preventivo
        self.assertEqual(totaleattività,totalepreventivo)

        # Eliminazione attività
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]').click()
        self.wait_loader()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Vendite")        
        self.navigateTo("Preventivi")
        self.wait_loader()  

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def creazione_ddt_uscita(self):
        self.navigateTo("Preventivi")
        self.wait_loader()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Nome"]/input')
        element.send_keys('Preventivo di Prova')

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys(Keys.ENTER)

        sleep(2)
        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()

        totalepreventivo=self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text

        # Creazione ddt uscita
        self.find(By.XPATH, '//button[@class="btn btn-info dropdown-toggle "]').click()
        self.wait_loader()
        self.find(By.XPATH, '//a[@class="bound clickable"][@data-title="Crea ordine cliente"]//i[@class="fa fa-truck"]').click()  
        sleep(1)
        self.find(By.XPATH, '//input[@id="checked_3"]').click()

        self.find(By.XPATH, '//span[@id="select2-id_causale_trasporto-container"]').click() 
        sleep(1)
        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()
        self.find(By.XPATH, '//button[@id="submit_btn"]').click()
        self.wait_loader()

        sleep(1)
        totaleddtuscita=self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text
        
        # Controllo valori righe preventivo
        self.assertEqual(totaleddtuscita,totalepreventivo)

        # Eliminazione ddt uscita
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]').click()
        self.wait_loader()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        sleep(1)

        self.expandSidebar("Vendite")
        self.navigateTo("Preventivi")
        self.wait_loader()  

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def creazione_fattura(self):
        self.navigateTo("Preventivi")
        self.wait_loader()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Nome"]/input')
        element.send_keys('Preventivo di Prova')

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys(Keys.ENTER)

        sleep(2)
        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()

        totalepreventivo=self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text

        # Creazione fattura
        self.find(By.XPATH, '//button[@class="btn btn-info dropdown-toggle "]').click()
        self.wait_loader()
        self.find(By.XPATH, '//a[@class="bound clickable"][@data-title="Crea fattura"]').click()  
        sleep(1)
        self.find(By.XPATH, '//input[@id="checked_3"]').click()
        self.find(By.XPATH, '//button[@id="submit_btn"]').click()
        self.wait_loader()

        sleep(1)
        totalefattura=self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text
        
        # Controllo valori righe preventivo
        self.assertEqual(totalefattura,totalepreventivo)

        # Eliminazione fattura
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask "]').click()
        self.wait_loader()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.navigateTo("Preventivi")
        self.wait_loader()  

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times fa-2x"]').click()