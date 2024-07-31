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

    def test_impostazioni_fatturazione_elettronica(self):
        # Regime fiscale (4)
        self.regime_fiscale()

        # Tipo cassa previdenziale (5)
        self.tipo_cassa_previdenziale()

    def regime_fiscale(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Vendite")   #test con impostazioni preselezionate
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Test")    #scrivo "Test" come descrizione della riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1") #scrivo 1 come prezzo unitario
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idstatodocumento-container"]').click() #cambia stato
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idstatodocumento-results"]//li[2]').click()  #seleziona stato "Emessa"
        sleep(1)

        self.find(By.XPATH, '//button[@id="save"]').click() #click su salva
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-xs btn-info"]').click()   #visualizza fattura elettronica
        sleep(1)

        regime=self.find(By.XPATH, '(//div[@class="headContent"]//span)[3]').text   #check regime fiscale
        self.assertEqual(regime, "RF01")
        self.find(By.XPATH, '//button[@class="close"]').click() #chiudi
        sleep(1)

        self.find(By.XPATH, '//a[@id="elimina"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-10"]').click() #apro Fatturazione Elettronica
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting73-container"]').click()    #cambia regime fiscale
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-setting73-results"]//li[2]').click() #imposta il regime fiscale RF02
        sleep(2)

        self.expandSidebar("Vendite")   #test con impostazioni diverse
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Test")    #scrivo "Test" come descrizione della riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1") #scrivo 1 come prezzo unitario
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idstatodocumento-container"]').click() #cambia stato
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idstatodocumento-results"]//li[2]').click()  #seleziona stato "Emessa"
        sleep(1)

        self.find(By.XPATH, '//button[@id="save"]').click() #click su salva
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-xs btn-info"]').click()   #visualizza fattura elettronica
        sleep(1)

        regime=self.find(By.XPATH, '(//div[@class="headContent"]//span)[3]').text   #check regime fiscale
        self.assertEqual(regime, "RF02")
        self.find(By.XPATH, '//button[@class="close"]').click() #chiudi
        sleep(1)

        self.find(By.XPATH, '//a[@id="elimina"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-10"]').click() #apro Fatturazione Elettronica
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting73-container"]').click()    #cambia regime fiscale
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-setting73-results"]//li[1]').click() #imposta il regime fiscale RF01
        sleep(2)

    def tipo_cassa_previdenziale(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-10"]').click() #apro Fatturazione Elettronica
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting74-container"]').click()    #seleziono cassa previdenziale
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-setting74-results"]//li[1]').click() #seleziono cassa TC01
        sleep(2)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Test")    #scrivo "Test" come descrizione della riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1") #scrivo 1 come prezzo unitario
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idstatodocumento-container"]').click() #cambia stato
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idstatodocumento-results"]//li[2]').click()  #seleziona stato "Emessa"
        sleep(1)

        self.find(By.XPATH, '//button[@id="save"]').click() #click su salva
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-xs btn-info"]').click()   #visualizza fattura elettronica
        sleep(1)

        cassa=self.find(By.XPATH, '(//table[@class="tbFoglio"]//span)[1]').text #check se è stata impostata la cassa previdenziale
        self.assertEqual(cassa, "TC01")
        self.find(By.XPATH, '//button[@class="close"]').click() #chiudi
        sleep(1)

        self.find(By.XPATH, '//a[@id="elimina"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-10"]').click() #apro Fatturazione Elettronica
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting74-container"]//span').click()    #tolgo cassa previdenziale
        sleep(2)


