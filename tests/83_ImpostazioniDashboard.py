from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Impostazioni(Test):
    def setUp(self):
        super().setUp()

    def test_impostazioni_dashboard(self):
        # Test Visualizzare domenica sul calendario 
        self.visualizzare_domenica_calendario()

        # Test Vista Dashboard
        self.vista_dashboard()

        # Test Ora inizio sul calendario 
        self.ora_inizio_calendario()

        # Test Ora fine sul calendario 
        self.ora_fine_calendario()

        # Test Visualizza informazioni aggiuntive sul calendario 
        self.visualizza_informazioni_aggiuntive()

        # Test Visualizzazione colori sessioni 
        self.visualizza_colori_sessioni()


    def visualizzare_domenica_calendario(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Dashboard"]').click()
        sleep(1)

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Visualizzare la domenica sul calendario")]//div//label').click() 
        sleep(1)

        self.navigateTo("Dashboard")
        self.wait_loader()

        wait.until(EC.invisibility_of_element_located((By.XPATH, '//tr[1]//th[8]')))   

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Dashboard"]').click()
        sleep(1)

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Visualizzare la domenica sul calendario")]//div//label').click() 
        sleep(1)

    def vista_dashboard(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Dashboard"]').click()
        sleep(1)

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Vista dashboard")]//div//span').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("mese")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.navigateTo("Dashboard")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="fc-dayGridMonth-button fc-button fc-button-primary fc-button-active"]')))  
        sleep(1)

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()
        self.find(By.XPATH, '//div[@title="Dashboard"]').click()
        sleep(1)

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Vista dashboard")]//div//span').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("settimana")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        sleep(1)

    def ora_inizio_calendario(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Dashboard"]').click()
        sleep(1)

        element=self.find(By.XPATH, '//div[@class="form-group" and contains(., "Ora inizio sul calendario")]//input')
        element.clear()
        element.send_keys('01:00')
        sleep(1)

        self.navigateTo("Dashboard")
        self.wait_loader()

        ora=self.find(By.XPATH, '//td[@role="presentation"]//tbody//tr//td').text 
        self.assertEqual(ora, "1:00")

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Dashboard"]').click()
        sleep(1)

        element=self.find(By.XPATH, '//div[@class="form-group" and contains(., "Ora inizio sul calendario")]//input')
        element.clear()
        element.send_keys('00:00')
        sleep(1)

    def ora_fine_calendario(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Dashboard"]').click()
        sleep(1)

        element=self.find(By.XPATH, '//div[@class="form-group" and contains(., "Ora fine sul calendario")]//input')
        element.clear()
        element.send_keys('13:30')
        sleep(1)

        self.navigateTo("Dashboard")
        self.wait_loader()

        wait.until(EC.invisibility_of_element_located((By.XPATH, '//tbody//tr[55]//td')))
        sleep(1)

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Dashboard"]').click()
        sleep(1)

        element=self.find(By.XPATH, '//div[@class="form-group" and contains(., "Ora fine sul calendario")]//input')
        element.clear()
        element.send_keys('23:59')
        sleep(1)


    def visualizza_informazioni_aggiuntive(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Dashboard"]').click()
        sleep(1)

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Visualizza informazioni aggiuntive sul calendario")]//span').click() 
        sleep(1)

        self.navigateTo("Dashboard")
        self.wait_loader()

        scritta=self.find(By.XPATH, '//tr[1]//td[@class="fc-timegrid-axis fc-scrollgrid-shrink"]').text
        self.assertEqual(scritta, "Tutto il giorno")

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Dashboard"]').click()
        sleep(1)

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Visualizza informazioni aggiuntive sul calendario")]//span').click() 
        sleep(1)


    def visualizza_colori_sessioni(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Dashboard"]').click()
        sleep(1)

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Visualizzazione colori sessioni")]//div//span').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("sfondo colore tecnico - bordo colore stato")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()  
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys("Cliente")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Generico")
        sleep(1)

        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).send_keys("Test")   
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()  
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-nuovo_tecnico-container"]').click()  
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-nuovo_tecnico-results"]//li[2]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-block"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@id="save"]').click() 
        self.wait_loader()

        self.navigateTo("Dashboard")
        self.wait_loader()

        colori_element = self.find(By.XPATH, '//td[@role="presentation"]//tbody//tr//td//a')
        colori = colori_element.get_attribute("style")
        self.assertEqual(colori, "border-color: rgb(153, 230, 255); background-color: rgb(255, 255, 255);")

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Dashboard"]').click()
        sleep(1)

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Visualizzazione colori sessioni")]//div//span').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("sfondo colore stato - bordo colore tecnico")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.navigateTo("Dashboard")
        self.wait_loader()

        colori_element = self.find(By.XPATH, '//div[@class="fc-timegrid-event-harness fc-timegrid-event-harness-inset"]//a')
        colori = colori_element.get_attribute("style")  
        self.assertEqual(colori, "border-color: rgb(255, 255, 255); background-color: rgb(153, 230, 255);")

        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click() 
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()


        