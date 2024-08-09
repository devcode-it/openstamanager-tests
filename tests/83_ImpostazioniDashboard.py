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
        # Visualizzare domenica sul calendario (2)
        self.visualizzare_domenica_calendario()

        # Ora inizio sul calendario (4)
        self.ora_inizio_calendario()

        # Ora fine sul calendario (5)
        self.ora_fine_calendario()

        # Visualizza informazioni aggiuntive sul calendario (6)
        self.visualizza_informazioni_aggiuntive()

        # Visualizzazione colori sessioni (7)
        self.visualizza_colori_sessioni()


    def visualizzare_domenica_calendario(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-7"]').click() #apro Dashboard
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[2]').click() #disattiva impostazione
        sleep(1)

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
        sleep(1)

    def vista_dashboard(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-7"]').click() #apro Dashboard
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting50-container"]').click()    #seleziona vista per mese
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("mese")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        sleep(1)

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
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        sleep(1)

    def ora_inizio_calendario(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-7"]').click() #apro Dashboard
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="setting77"]'))).send_keys("01:00") #seleziono 01:00 come prima ora del calendario
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="setting77"]'))).send_keys(Keys.ENTER)
        sleep(1)

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
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="setting77"]'))).send_keys(Keys.ENTER)
        sleep(1)

    def ora_fine_calendario(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-7"]').click() #apro Dashboard
        sleep(1)

        ora_fine=self.find(By.XPATH, '//input[@id="setting78"]')
        ora_fine.clear()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="setting78"]'))).send_keys("13:30") #seleziono 13:30 come ultima ora del calendario
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="setting78"]'))).send_keys(Keys.ENTER)
        sleep(1)

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
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="setting78"]'))).send_keys(Keys.ENTER)
        sleep(1)

    def visualizza_informazioni_aggiuntive(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-7"]').click() #apro Dashboard
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[3]').click()    #attiva impostazione
        sleep(1)

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
        sleep(1)

    def visualizza_colori_sessioni(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-7"]').click() #apro Dashboard
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting153-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-setting153-results"]//li[2]').click()    #seleziono "Sfondo colore tecnico - bordo colore stato"
        sleep(1)

        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()  #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys("Cliente")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click() #seleziono Generico come tipo di intervento
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Generico")
        sleep(1)

        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()  #click su primo risultato
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).send_keys("Test")   #scrivo "Test" come richiesta
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-nuovo_tecnico-container"]').click()    #aggiungi sessione
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-nuovo_tecnico-results"]//li[2]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-block"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@id="save"]').click() #click su salva
        self.wait_loader()

        self.navigateTo("Dashboard")
        self.wait_loader()
        sleep(1)

        colori_element = self.find(By.XPATH, '//div[@class="fc-timegrid-event-harness fc-timegrid-event-harness-inset"]//a')
        colori = colori_element.get_attribute("style")  #check dei colori
        self.assertEqual(colori, "border-color: rgb(255, 239, 153); background-color: rgb(255, 255, 255);")
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-7"]').click() #apro Dashboard
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting153-container"]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-setting153-results"]//li[1]').click()    #seleziono "Sfondo colore stato - bordo colore tecnico"
        sleep(1)

        self.navigateTo("Dashboard")
        self.wait_loader()

        colori_element = self.find(By.XPATH, '//div[@class="fc-timegrid-event-harness fc-timegrid-event-harness-inset"]//a')
        colori = colori_element.get_attribute("style")  #check dei colori
        self.assertEqual(colori, "border-color: rgb(255, 255, 255); background-color: rgb(255, 239, 153);")
        #elimino attività
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click() #apro attività
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click() #elimino attività
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()


        