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

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")

    def test_impostazioni_dashboard(self):
        # Visualizzare domenica sul calendario (2)
        self.visualizzare_domenica_calendario()

        # Ora inizio sul calendario (4)
        self.ora_inizio_calendario()

        # Ora fine sul calendario (5)
        self.ora_fine_calendario()

        # Visualizza informazioni aggiuntive sul calendario (6)
        self.visualizza_informazioni_aggiuntive()


    def visualizzare_domenica_calendario(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-7"]').click() #apro Dashboard
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[2]').click() #disattiva impostazione
        sleep(2)

        self.navigateTo("Dashboard")
        self.wait_loader()

        wait.until(EC.invisibility_of_element_located((By.XPATH, '//tr[1]//th[8]')))    #check se non è visibile la domenica
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-7"]').click() #apro Dashboard
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[2]').click() #attiva impostazione
        sleep(2)

    def vista_dashboard(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-7"]').click() #apro Dashboard
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting50-container"]').click()    #seleziona vista per mese
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("mese")
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        sleep(2)

        self.navigateTo("Dashboard")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="fc-dayGridMonth-button fc-button fc-button-primary fc-button-active"]')))    #controlla se la vista è per mese
        sleep(1)
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-7"]').click() #apro Dashboard
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting50-container"]').click()    #seleziona vista per settimana
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("settimana")
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        sleep(2)

    def ora_inizio_calendario(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-7"]').click() #apro Dashboard
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="setting77"]'))).send_keys("01:00") #seleziono 01:00 come prima ora del calendario
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="setting77"]'))).send_keys(Keys.ENTER)
        sleep(2)

        self.navigateTo("Dashboard")
        self.wait_loader()

        ora=self.find(By.XPATH, '//tr[1]//div[@class="fc-timegrid-slot-label-cushion fc-scrollgrid-shrink-cushion"]').text  #controllo se la prima ora è quella inserita
        self.assertEqual(ora, "01:00")
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-7"]').click() #apro Dashboard
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="setting77"]'))).send_keys("00:00") #seleziono 00:00 come prima ora del calendario
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="setting77"]'))).send_keys(Keys.ENTER)
        sleep(2)

    def ora_fine_calendario(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-7"]').click() #apro Dashboard
        sleep(1)

        ora_fine=self.find(By.XPATH, '//input[@id="setting78"]')
        ora_fine.clear()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="setting78"]'))).send_keys("13:30") #seleziono 13:30 come ultima ora del calendario
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="setting78"]'))).send_keys(Keys.ENTER)
        sleep(2)

        self.navigateTo("Dashboard")
        self.wait_loader()

        wait.until(EC.invisibility_of_element_located((By.XPATH, '//tr[55]//div'))) #check se non trova le ore dopo le 13.30
        sleep(1)

        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-7"]').click() #apro Dashboard
        sleep(1)

        ora_fine=self.find(By.XPATH, '//input[@id="setting78"]')
        ora_fine.clear()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="setting78"]'))).send_keys("23:59") #seleziono 23:59 come ultima ora del calendario
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="setting78"]'))).send_keys(Keys.ENTER)
        sleep(2)

    def visualizza_informazioni_aggiuntive(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-7"]').click() #apro Dashboard
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[3]').click()    #attiva impostazione
        sleep(2)

        self.navigateTo("Dashboard")
        self.wait_loader()

        scritta=self.find(By.XPATH, '//tr[1]//td[@class="fc-timegrid-axis fc-scrollgrid-shrink"]').text
        self.assertEqual(scritta, "Tutto il giorno")    #check se appare impostazione
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-7"]').click() #apro Dashboard
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[3]').click()    #disattiva impostazione
        sleep(2)
