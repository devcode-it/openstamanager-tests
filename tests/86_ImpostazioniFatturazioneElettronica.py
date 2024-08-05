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

        # Causale ritenuta d'acconto (6)
        self.causale_ritenuta_acconto()

        # Riferimento dei documenti in fattura elettronica (10)
        self.riferimento_documenti_fattura_elettronica()

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

    def causale_ritenuta_acconto(self):
        wait = WebDriverWait(self.driver, 20)
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
        self.find(By.XPATH, '//span[@id="select2-id_ritenuta_acconto-container"]').click()  #ritenuta d'acconto
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-id_ritenuta_acconto-results"]//li[1]').click()
        self.find(By.XPATH, '//span[@id="select2-calcolo_ritenuta_acconto-container"]').click() #calcola ritenuta su imponibile
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-calcolo_ritenuta_acconto-results"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idstatodocumento-container"]').click() #cambia stato
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idstatodocumento-results"]//li[2]').click()  #seleziona stato "Emessa"
        sleep(1)

        self.find(By.XPATH, '//button[@id="save"]').click() #click su salva
        self.wait_loader()

        self.find(By.XPATH, '(//button[@class="btn btn-info dropdown-toggle dropdown-toggle-split"])[1]').click()   #apro fattura elettronica
        sleep(1)

        self.find(By.XPATH, '//a[@id="print-button_1"]').click()
        sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda
        sleep(1)
        
        causale=self.find(By.XPATH, '(//div[@id="viewer"]//span)[97]').text #check causale
        self.assertNotEqual(causale[0], "A")    #controllo se non è stata selezionata nessuna delle causali disponibili
        self.assertNotEqual(causale[0], "B")
        self.assertNotEqual(causale[0], "C")
        self.assertNotEqual(causale[0], "D")
        self.assertNotEqual(causale[0], "E")
        self.assertNotEqual(causale[0], "F")
        self.assertNotEqual(causale[0], "G")
        self.assertNotEqual(causale[0], "I")
        self.assertNotEqual(causale[0], "L")
        self.assertNotEqual(causale[0:1], "L1")
        self.assertNotEqual(causale[0], "M")
        self.assertNotEqual(causale[0:1], "M1")
        self.assertNotEqual(causale[0:1], "M2")
        self.assertNotEqual(causale[0], "N")
        self.assertNotEqual(causale[0], "O")
        self.assertNotEqual(causale[0:1], "01")
        self.assertNotEqual(causale[0], "P")
        self.assertNotEqual(causale[0], "Q")
        self.assertNotEqual(causale[0], "R")
        self.assertNotEqual(causale[0], "S")
        self.assertNotEqual(causale[0], "T")
        self.assertNotEqual(causale[0], "U")
        self.assertNotEqual(causale[0], "V")
        self.assertNotEqual(causale[0:1], "V1")
        self.assertNotEqual(causale[0:1], "V2")
        self.assertNotEqual(causale[0], "W")
        self.assertNotEqual(causale[0], "X")
        self.assertNotEqual(causale[0], "Y")
        self.assertNotEqual(causale[0:1], "ZO")
        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima
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

        self.find(By.XPATH, '//span[@id="select2-setting75-container"]').click()    #scelgo causale A
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-setting75-results"]//li[1]').click()
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
        self.find(By.XPATH, '//span[@id="select2-id_ritenuta_acconto-container"]').click()  #ritenuta d'acconto
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-id_ritenuta_acconto-results"]//li[1]').click()
        self.find(By.XPATH, '//span[@id="select2-calcolo_ritenuta_acconto-container"]').click() #calcola ritenuta su imponibile
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-calcolo_ritenuta_acconto-results"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idstatodocumento-container"]').click() #cambia stato
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idstatodocumento-results"]//li[2]').click()  #seleziona stato "Emessa"
        sleep(1)

        self.find(By.XPATH, '//button[@id="save"]').click() #click su salva
        self.wait_loader()

        self.find(By.XPATH, '(//button[@class="btn btn-info dropdown-toggle dropdown-toggle-split"])[1]').click()   #apro fattura elettronica
        sleep(1)

        self.find(By.XPATH, '//a[@id="print-button_1"]').click()
        sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda
        sleep(1)

        causale=self.find(By.XPATH, '(//div[@id="viewer"]//span)[97]').text #check causale
        self.assertEqual(causale, "A (decodiﬁca come da modello CU)")

        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima
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

        self.find(By.XPATH, '//span[@id="select2-setting75-container"]//span').click()  #togli causale
        sleep(2)

    def riferimento_documenti_fattura_elettronica(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()
        #aggiungi preventivo
        self.find(By.XPATH, '//button[@class="btn btn-primary dropdown-toggle"]').click() #click su altro
        sleep(1)

        self.find(By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right show"]//a[4]').click()
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-id_documento-container"]').click()
        sleep(2)

        self.find(By.XPATH, '//ul[@id="select2-id_documento-results"]//li[1]').click()
        sleep(2)

        self.find(By.XPATH, '//input[@id="import_all"]').click()    #deseleziona tutte le righe
        sleep(1)

        self.find(By.XPATH, '//input[@id="checked_3"]').click() #seleziono solo la riga del articolo
        self.find(By.XPATH, '//button[@id="submit_btn"]').click()   #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-idstatodocumento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Emessa")
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()
        #stampa fattura elettronica
        self.find(By.XPATH, '//button[@class="btn btn-info dropdown-toggle dropdown-toggle-split"]').click()
        sleep(1)

        self.find(By.XPATH, '//a[@id="print-button_1"]').click()
        sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda
        sleep(2)

        riferimento=self.find(By.XPATH, '(//div[@id="viewer"]//span)[50]').text
        self.assertEqual(riferimento[10:32], "Rif. preventivo num. 1")

        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima
        sleep(2)

        #elimina fattura
        self.find(By.XPATH, '//a[@id="elimina"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()
        
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-10"]').click() #apro Fatturazione Elettronica
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[4]').click()    #disattiva impostazione
        sleep(2)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()
        #aggiungi preventivo
        self.find(By.XPATH, '//button[@class="btn btn-primary dropdown-toggle"]').click() #click su altro
        sleep(1)

        self.find(By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right show"]//a[4]').click()
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-id_documento-container"]').click()
        sleep(2)

        self.find(By.XPATH, '//ul[@id="select2-id_documento-results"]//li[1]').click()
        sleep(2)

        self.find(By.XPATH, '//input[@id="import_all"]').click()    #deseleziona tutte le righe
        sleep(1)

        self.find(By.XPATH, '//input[@id="checked_3"]').click() #seleziono solo la riga del articolo
        self.find(By.XPATH, '//button[@id="submit_btn"]').click()   #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-idstatodocumento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Emessa")
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()
        #stampa fattura elettronica
        self.find(By.XPATH, '//button[@class="btn btn-info dropdown-toggle dropdown-toggle-split"]').click()
        sleep(1)

        self.find(By.XPATH, '//a[@id="print-button_1"]').click()
        sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda
        sleep(2)

        riferimento=self.find(By.XPATH, '(//div[@id="viewer"]//span)[50]').text
        self.assertNotEqual(riferimento[10:32], "Rif. preventivo num. 1")

        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima
        sleep(2)

        #elimina fattura
        self.find(By.XPATH, '//a[@id="elimina"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-10"]').click() #apro Fatturazione Elettronica
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[4]').click()    #attiva impostazione
        sleep(2)



