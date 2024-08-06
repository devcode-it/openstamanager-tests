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

    
    def test_impostazioni_attivita(self):
        # Mostra i prezzi al tecnico (1)
        self.mostra_prezzi_tecnico()

        # Stampa per anteprima e firma (2)
        self.stampa_anteprima_firma()   #da finire

        # Permetti inserimento sessioni degli altri tecnici (3)
        self.inserimento_sessioni_tecnici()

        # Giorni lavorativi (4)
        self.giorni_lavorativi()

        # Notifica al tecnico l'aggiunta della sessione nell'attività (5)
        self.notifica_tecnico_aggiunta_sessione()

        # Notifica al tecnico la rimozione della sessione dall'attività (6)
        self.notifica_tecnico_rimozione_sessione()

        # Stato dell’attività dopo la firma (7)
        self.stato_attivita_firma()

        # Espandi automaticamente la sezione “Dettagli aggiuntivi” (8)
        self.espandi_barra_dettagli_aggiuntivi()

        # Alert occupazione tecnici (9)
        self.alert_occupazione_tecnici()

        # Verifica numero intervento (10)
        self.verifica_numero_intervento()

        # Formato ore in stampa (11)
        self.formato_ore_stampa()

        # Notifica al tecnico l'assegnazione all'attività(12)
        self.notifica_tecnico_assegnazione()

        # Notifica al tecnico la rimozione dell'assegnazione dall'attività (13)
        self.notifica_tecnico_rimozione_assegnazione()

        # Descrizione personalizzata in fatturazione (14)
        self.descrizione_attivita()

        # Stato predefinito dell'attività da Dashboard (15)
        self.stato_predefinito_attivita_dashboard()

        # Stato predefinito dell'attività (16)
        self.stato_predefinito_attivita()


    def mostra_prezzi_tecnico(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Strumenti")  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '//label[@class="btn btn-default active"]').click() #disattivo impostazione mostra prezzi al tecnico
        sleep(1)

        self.navigateTo("Utenti e permessi")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Gruppo"]//input'))).send_keys('Tecnici', Keys.ENTER)   #cerca utente tecnici
        sleep(2)

        self.find(By.XPATH, '//tbody//tr//td[2]').click() #apro primo risultato
        self.wait_loader()           

        self.find(By.XPATH, '//a[@class="pull-right btn btn-primary bound clickable"]').click() #aggiungi utente
        sleep(1)
        #imposto user
        user=self.find(By.XPATH, '//input[@id="username"]') 
        user.clear()
        user.send_keys("tecnicotest")
        #collego anagrafica
        self.find(By.XPATH, '//span[@id="select2-idanag-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys('Tecnico')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys(Keys.ENTER)
        #imposto password
        password=self.find(By.XPATH, '//input[@id="password"]') 
        password.clear()
        password.send_keys("tecnicotest")
        self.find(By.XPATH, '//button[@id="submit-button"]').click()
        self.wait_loader()

        self.find(By.XPATH, '(//tbody//tr[17]//span)[2]').click() #aggiungo permessi
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Lettura e scrittura')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        sleep(2)

        #logout
        self.find(By.XPATH, '//a[@class="nav-link bg-danger"]').click()
        self.wait_loader()
        sleep(2)

        #login
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys('tecnicotest')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys('tecnicotest') 
        self.find(By.XPATH, '//button[@class="btn btn-danger btn-block btn-flat"]').click() 
        sleep(2)
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #creo nuova attività
        sleep(1)
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #tipo
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #richiesta
        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click() #aggiungi articolo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Articolo 1')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click()
        sleep(1)

        wait.until(EC.invisibility_of_element_located((By.XPATH, '//thead//tr[1]//th[7]')))  #controllo se non c'è la colonna degli importi
        #elimino attività
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        #logout
        self.find(By.XPATH, '//a[@class="nav-link bg-danger"]').click()
        self.wait_loader()
        sleep(2)

        #login
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys(self.getConfig('login.username'))   
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys('') #password da inserire al momento del test
        self.find(By.XPATH, '//button[@class="btn btn-danger btn-block btn-flat"]').click() 
        sleep(2)
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '//label[@class="btn btn-default active"]').click() #attivo impostazione mostra prezzi al tecnico
        sleep(1)

    def stampa_anteprima_firma(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #creo nuova attività
        sleep(1)
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #tipo
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #richiesta
        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()

        self.find(By.XPATH, '(//button[@class="btn btn-primary "])[2]').click() #anteprima e stampa
        sleep(2)

        #non trova l'elemento
        prezzo = self.find_elements(By.XPATH, '//div[@id="viewer"]//span[59]').value
        self.assertEqual(prezzo, "0,00 €")
        self.find(By.XPATH, '//button[@class="close"]').click() #chiudi
        sleep(1)
        
        #elimina attività
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting79-container"]').click()    #imposta "Intervento (senza prezzi)"
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-setting79-results"]//li[1]').click()
        sleep(2)

        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #creo nuova attività
        sleep(1)
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #tipo
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #richiesta
        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()

        self.find(By.XPATH, '(//button[@class="btn btn-primary "])[2]').click() #anteprima e stampa
        sleep(2)

        wait.until(EC.invisibility_of_element_located((By.XPATH, '(//div[@id="viewer"]//span)[69]')))
        self.find(By.XPATH, '//button[@class="close"]').click() #chiudi
        sleep(1)
        #elimina attività
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting79-container"]').click()    #imposta "Intervento (senza prezzi)"
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-setting79-results"]//li[2]').click()
        sleep(2)


    def inserimento_sessioni_tecnici(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[2]').click() #attiva impostazione inserimento sessioni tecnici
        sleep(1)

        #logout
        self.find(By.XPATH, '//a[@class="nav-link bg-danger"]').click()
        self.wait_loader()
        sleep(2)

        #login
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys('tecnicotest')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys('tecnicotest') 
        self.find(By.XPATH, '//button[@class="btn btn-danger btn-block btn-flat"]').click() 
        sleep(2)
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #click su +
        sleep(1)

        #apro assegnazione tecnici
        self.find(By.XPATH, '(//button[@class="btn btn-tool"])[4]').click()
        sleep(1)

        self.find(By.XPATH, '(//ul[@class="select2-selection__rendered"]//li)[3]').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-tecnici_assegnati-results"]//li[2]'))) #controlla se appare tra le opzioni di scelta il tecnico
        #apro sessioni di lavoro
        self.find(By.XPATH, '(//button[@class="btn btn-tool"])[5]').click()
        sleep(1)

        self.find(By.XPATH, '(//ul[@class="select2-selection__rendered"])[4]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[1]'))) #controlla se appare tra le opzioni di scelta il tecnico
        self.find(By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[1]').click()
        sleep(1)

        #chiudo
        self.find(By.XPATH, '//button[@class="close"]').click()
        sleep(2)

        #logout
        self.find(By.XPATH, '//a[@class="nav-link bg-danger"]').click()
        self.wait_loader()
        sleep(2)

        #login
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys(self.getConfig('login.username'))   
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys('') #password da inserire al momento del test
        self.find(By.XPATH, '//button[@class="btn btn-danger btn-block btn-flat"]').click() 
        sleep(2)
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[2]').click() #disattiva impostazione inserimento sessioni tecnici
        sleep(1)

    def giorni_lavorativi(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Dashboard")
        self.wait_loader() 

        wait.until(EC.invisibility_of_element_located((By.XPATH, '(//div[@class="fc-event fc-event-start fc-event-future fc-bg-event"])[3]')))  #controlla se il quinto giorno è lavorativo
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '(//li[@class="select2-selection__choice"]//span)[5]').click() #tolgo il venerdì dai giorni lavorativi
        sleep(2)

        self.navigateTo("Dashboard")
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@class="fc-event fc-event-start fc-event-future fc-bg-event"])[3]')))  #controlla se il quinto giorno è lavorativo
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '//span[@class="select2-selection select2-selection--multiple" ]').click()  #seleziono venerdì come giorno lavorativo
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-setting109-results"]//li[5]').click()
        sleep(2)

    def notifica_tecnico_aggiunta_sessione(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Anagrafiche")
        self.wait_loader()
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Tecnico", Keys.ENTER)
        sleep(1)
 
        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()   #aggiungo email a "Tecnico"
        sleep(1)

        self.input(None, 'Email').setValue(self.getConfig('tests.tecnico_email'))
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click() #elimino ricerca
        sleep(2)

        self.navigateTo("Attività")
        self.wait_loader()
 
        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #creo nuova attività
        sleep(1)
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #tipo
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #richiesta
        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        #stato
        self.find(By.XPATH, '//span[@id="select2-id-container"]').click()
        sleep(1)
 
        self.find(By.XPATH, '//ul[@id="select2-id-results"]//li[4]').click()    #stato programmato
        #aggiungo sessione
        self.find(By.XPATH, '(//button[@class="btn btn-tool"])[5]').click()
        sleep(1)
 
        self.find(By.XPATH, '(//ul[@class="select2-selection__rendered"])[4]').click()
        sleep(1)
 
        self.find(By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[2]').click()
        sleep(1)
 
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()

        wait.until(EC.invisibility_of_element_located((By.XPATH, '(//div[@class="toast-message"])[2]')))    #check se non appare la notifica
        #elimino attività
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()
 
        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)
 
        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[3]').click() #attivo impostazione
        sleep(2)
 
        self.navigateTo("Attività")
        self.wait_loader()
 
        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #creo nuova attività
        sleep(1)
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #tipo
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #richiesta
        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        #stato
        self.find(By.XPATH, '//span[@id="select2-id-container"]').click()
        sleep(1)
 
        self.find(By.XPATH, '//ul[@id="select2-id-results"]//li[4]').click()    #stato programmato
        #aggiungo sessione
        self.find(By.XPATH, '(//button[@class="btn btn-tool"])[5]').click()
        sleep(1)
 
        self.find(By.XPATH, '(//ul[@class="select2-selection__rendered"])[4]').click()
        sleep(1)
 
        self.find(By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[2]').click()
        sleep(1)
 
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@class="toast-message"])[2]')))#check se arriva la notifica di invio della mail
        #elimino attività
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()
 
        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)
 
        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[3]').click() #disattivo impostazione
        sleep(2)

    def notifica_tecnico_rimozione_sessione(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attività")
        self.wait_loader()
 
        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #creo nuova attività
        sleep(2)
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #tipo
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #richiesta
        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        #stato
        self.find(By.XPATH, '//span[@id="select2-id-container"]').click()
        sleep(1)
 
        self.find(By.XPATH, '//ul[@id="select2-id-results"]//li[4]').click()    #stato programmato
        #aggiungo sessione
        self.find(By.XPATH, '(//button[@class="btn btn-tool"])[5]').click()
        sleep(1)
 
        self.find(By.XPATH, '(//ul[@class="select2-selection__rendered"])[4]').click()
        sleep(1)
 
        self.find(By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[2]').click()
        sleep(1)
 
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()

        #elimina sessione
        self.find(By.XPATH, '//td[@class="text-center"]//button[3]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]').click()
        sleep(2)

        self.find(By.XPATH, '//button[@id="save"]').click() #click su salva
        self.wait_loader()

        self.expandSidebar("Gestione email")
        self.navigateTo("Coda di invio")
        self.wait_loader()

        messaggio=self.find(By.XPATH, '//tbody//tr[1]//td').text    #check se non è stata inviata la mail
        self.assertEqual(messaggio, "Nessun dato presente nella tabella")
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click() #apro attività
        self.wait_loader()

        #elimino attività
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[4]').click() #attivo impostazione
        sleep(2)

        self.navigateTo("Attività")
        self.wait_loader()
 
        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #creo nuova attività
        sleep(1)
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #tipo
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #richiesta
        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        #stato
        self.find(By.XPATH, '//span[@id="select2-id-container"]').click()
        sleep(1)
 
        self.find(By.XPATH, '//ul[@id="select2-id-results"]//li[4]').click()    #stato programmato
        #aggiungo sessione
        self.find(By.XPATH, '(//button[@class="btn btn-tool"])[5]').click()
        sleep(1)
 
        self.find(By.XPATH, '(//ul[@class="select2-selection__rendered"])[4]').click()
        sleep(1)
 
        self.find(By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[2]').click()
        sleep(1)
 
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()

        #elimina sessione
        self.find(By.XPATH, '//td[@class="text-center"]//button[3]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]').click()
        sleep(2)

        self.find(By.XPATH, '//button[@id="save"]').click() #click su salva
        self.wait_loader()

        self.expandSidebar("Gestione email")
        self.navigateTo("Coda di invio")
        self.wait_loader()

        messaggio=self.find(By.XPATH, '//tbody//tr[1]//td[5]//div').text    #controllo se non è presente la mail in coda di invio
        self.assertEqual(messaggio, "Notifica rimozione intervento")
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click() #apro attività
        self.wait_loader()

        #elimino attività
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[4]').click() #attivo impostazione
        sleep(2)

    def stato_attivita_firma(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting123-container"]').click() #seleziono stato "Fatturato"
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Fatturato")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        sleep(2)

        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #creo nuova attività
        sleep(1)
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #tipo
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #richiesta
        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()

        self.find(By.XPATH, '(//button[@class="btn btn-primary "])[2]').click() #firma
        sleep(1)

        self.find(By.XPATH, '//button[@id="firma"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="firma_nome"]'))).send_keys('Prova')
        self.find(By.XPATH,'//button[@class="btn btn-success pull-right"]').click()
        self.wait_loader()

        stato=self.find(By.XPATH, '(//tr[1]//td[7]//div)[2]').text
        self.assertEqual(stato, "Fatturato")    #check se il stato è cambiato in fatturato
        self.find(By.XPATH, '//tbody//tr//td[2]').click()  #elimino attività
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting123-container"]').click() #seleziono stato "Completato"
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Completato")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        sleep(2)


    def espandi_barra_dettagli_aggiuntivi(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[5]').click() #attivo impostazione espandi automaticamente Dettagli aggiuntivi
        sleep(1)

        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #click su +
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_scadenza"]')))    #controllo se gli elementi della barra sono visibili
        self.find(By.XPATH, '//button[@class="close"]').click() #chiudo
        sleep(1)

        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)
        
        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[5]').click() #disattivo impostazione espandi automaticamente Dettagli aggiuntivi
        sleep(1)

    def alert_occupazione_tecnici(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #creo nuova attività
        sleep(1)
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #tipo
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #richiesta
        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        #cambio lo stato in "Programmato"
        self.find(By.XPATH, '//span[@id="select2-id-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Programmato')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #sessione di lavoro
        self.find(By.XPATH, '(//button[@class="btn btn-tool"])[5]').click() #apro sessione di lavoro
        sleep(1)

        #orario inizio
        orario_inizio=self.find(By.XPATH, '//input[@id="orario_inizio"]')
        orario_inizio.clear()
        orario_inizio.send_keys("31/12/2024 09:00")     #data di inizio 31/12/2024 09:00
        #orario fine
        orario_fine=self.find(By.XPATH, '//input[@id="orario_fine"]')
        orario_fine.clear()
        orario_fine.send_keys("31/12/2024 10:00")     #data di fine 31/12/2024 10:00
        #tencico assegnato
        self.find(By.XPATH, '(//div[@class="card-body"]//span[@class="select2-selection select2-selection--multiple"])[2]').click()
        sleep(2)

        self.find(By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[2]').click() #assegno il tecnico "Tecnico"
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()

        self.navigateTo("Attività")
        self.wait_loader()
        #faccio un'altra attività uguale
        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #creo nuova attività
        sleep(1)
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #tipo
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #richiesta
        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('prova')
        #cambio lo stato in "Programmato"
        self.find(By.XPATH, '//span[@id="select2-id-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Programmato')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #sessione di lavoro
        self.find(By.XPATH, '(//button[@class="btn btn-tool"])[5]').click() #apro sessione di lavoro
        sleep(1)

        #orario inizio
        orario_inizio=self.find(By.XPATH, '//input[@id="orario_inizio"]')
        orario_inizio.clear()
        orario_inizio.send_keys("31/12/2024 09:00")     #data di inizio 31/12/2024 09:00
        #orario fine
        orario_fine=self.find(By.XPATH, '//input[@id="orario_fine"]')
        orario_fine.clear()
        orario_fine.send_keys("31/12/2024 10:00")     #data di fine 31/12/2024 10:00
        self.find(By.XPATH, '(//div[@class="card-body"]//span[@class="select2-selection select2-selection--multiple"])[2]').click() #tencico assegnato
        sleep(2)
        #assegno il tecnico "Tecnico"
        self.find(By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[2]').click()
        sleep(2)
        #controllo se appare l'alert
        scritta=self.find(By.XPATH, '//div[@class="card-header"]//h3').text
        self.assertEqual(scritta, "⚠️ Sono presenti dei conflitti con le sessioni di lavoro di alcuni tecnici")
        self.find(By.XPATH, '//button[@class="close"]').click() #esco
        sleep(1)
        #elimino prima attività
        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader() 
        sleep(1)

    def verifica_numero_intervento(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #creo nuova attività
        sleep(1)
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #tipo
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #richiesta
        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()

        codice=self.find(By.XPATH, '//input[@id="codice"]') #cambio codice
        codice.clear()
        codice.send_keys("9")
        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="alert alert-warning alert-dismissable"]'))) #check se appare l'alert
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click() #elimino attività
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader() 

    def formato_ore_stampa(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting142-container"]').click()   #seleziono formato in sessantesimi
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-setting142-results"]').click()
        sleep(2)

        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #creo nuova attività
        sleep(1)
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #tipo
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #richiesta
        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        #sessioni di lavoro
        self.find(By.XPATH, '(//button[@class="btn btn-tool"])[5]').click()
        sleep(1)

        self.find(By.XPATH, '(//ul[@class="select2-selection__rendered"])[4]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[1]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="print-button_p"]').click()    #stampa intervento
        sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda
        sleep(2)

        ore=self.find(By.XPATH, '//span[@style="left: 17.35%; top: 40.11%; font-size: calc(var(--scale-factor)*9.00px); font-family: sans-serif; transform: scaleX(0.996142);"]').text
        self.assertEqual(ore, "1:00")
        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima
        sleep(1)

        #elimina attività
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting142-container"]').click()   #seleziono formato in decimi
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-setting142-results"]').click()
        sleep(2)

    def notifica_tecnico_assegnazione(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attività")
        self.wait_loader()
 
        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #creo nuova attività
        sleep(1)
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #tipo
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #richiesta
        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        #stato
        self.find(By.XPATH, '//span[@id="select2-id-container"]').click()
        sleep(1)
 
        self.find(By.XPATH, '//ul[@id="select2-id-results"]//li[4]').click()    #stato programmato
        #assegnazione
        self.find(By.XPATH, '(//button[@class="btn btn-tool"])[4]').click()
        sleep(1)

        self.find(By.XPATH, '(//span[@class="select2-selection select2-selection--multiple"])[3]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-tecnici_assegnati-results"]//li[2]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su aggiungi
        self.wait_loader()

        wait.until(EC.invisibility_of_element_located((By.XPATH, '(//div[@class="toast-message"])[2]')))#check se arriva la notifica di invio della mail
        #elimino attività
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[8]').click()    #attiva impostazione
        sleep(1)

        self.navigateTo("Attività")
        self.wait_loader()
 
        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #creo nuova attività
        sleep(1)
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #tipo
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #richiesta
        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        #stato
        self.find(By.XPATH, '//span[@id="select2-id-container"]').click()
        sleep(1)
 
        self.find(By.XPATH, '//ul[@id="select2-id-results"]//li[4]').click()    #stato programmato
        #assegnazione
        self.find(By.XPATH, '(//button[@class="btn btn-tool"])[4]').click()
        sleep(1)

        self.find(By.XPATH, '(//span[@class="select2-selection select2-selection--multiple"])[3]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-tecnici_assegnati-results"]//li[2]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su aggiungi
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@class="toast-message"])[2]')))#check se arriva la notifica di invio della mail
        #elimino attività
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()
 
        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[8]').click()    #disattiva impostazione
        sleep(1)

    def notifica_tecnico_rimozione_assegnazione(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attività")
        self.wait_loader()
 
        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #creo nuova attività
        sleep(1)
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #tipo
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #richiesta
        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        #stato
        self.find(By.XPATH, '//span[@id="select2-id-container"]').click()
        sleep(1)
 
        self.find(By.XPATH, '//ul[@id="select2-id-results"]//li[4]').click()    #stato programmato
        #assegnazione
        self.find(By.XPATH, '(//button[@class="btn btn-tool"])[4]').click()
        sleep(1)

        self.find(By.XPATH, '(//span[@class="select2-selection select2-selection--multiple"])[3]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-tecnici_assegnati-results"]//li[2]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//span[@class="select2-selection__choice__remove"]').click() #rimuovi assegnazione
        self.find(By.XPATH, '//button[@id="save"]').click() #click su salva
        self.wait_loader()

        self.expandSidebar("Gestione email")
        self.navigateTo("Coda di invio")
        self.wait_loader()

        messaggio=self.find(By.XPATH, '//tbody//tr[1]//td').text    #check se non è stata inviata la mail
        self.assertEqual(messaggio, "Nessun dato presente nella tabella")
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click() #apro attività
        self.wait_loader()

        #elimino attività
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[9]').click()    #attiva impostazione
        sleep(1)

        self.navigateTo("Attività")
        self.wait_loader()
 
        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #creo nuova attività
        sleep(1)
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #tipo
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #richiesta
        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        #stato
        self.find(By.XPATH, '//span[@id="select2-id-container"]').click()
        sleep(1)
 
        self.find(By.XPATH, '//ul[@id="select2-id-results"]//li[4]').click()    #stato programmato
        #assegnazione
        self.find(By.XPATH, '(//button[@class="btn btn-tool"])[4]').click()
        sleep(1)

        self.find(By.XPATH, '(//span[@class="select2-selection select2-selection--multiple"])[3]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-tecnici_assegnati-results"]//li[2]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//span[@class="select2-selection__choice__remove"]').click() #rimuovi assegnazione
        self.find(By.XPATH, '//button[@id="save"]').click() #click su salva
        self.wait_loader()

        self.expandSidebar("Gestione email")
        self.navigateTo("Coda di invio")
        self.wait_loader()

        messaggio=self.find(By.XPATH, '//tbody//tr[1]//td[5]//div').text    #controllo se è presente la mail in coda di invio
        self.assertEqual(messaggio, "Notifica rimozione intervento")
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click() #apro attività
        self.wait_loader()

        #elimino attività
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[9]').click()    #disattiva impostazione
        sleep(2)


    def descrizione_attivita(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="setting155"]'))).send_keys('Attività num. {numero} in stato {stato}')
        sleep(1)

        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()  #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click() #seleziono Generico come tipo di intervento
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Generico")
        sleep(1)

        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()  #click sul primo risultato
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).send_keys("Test")   #scrivo "Test" come richiesta
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()    #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Test") #scrivo "Test" come descrizione riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1") #scrivo 1 come prezzo unitario
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()    #click su aggiungi
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idstatointervento-container"]').click()    #click su stato
        sleep(1)

        self.find(By.XPATH, '(//input[@class="select2-search__field"])[3]').send_keys("Completato", Keys.ENTER) #seleziono Completato come nuovo stato
        sleep(1)

        self.find(By.XPATH, '//button[@id="save"]').click() #click su salva
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="back"]').click() #torno in attività
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys("4", Keys.ENTER)  #cerco attività numero 4
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click() #seleziono attività 
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() #apro azioni di gruppo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-op="crea_fattura"]'))).click()    #click su crea fattura
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-raggruppamento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")    #seleziono cliente
        self.find(By.XPATH, '//ul[@id="select2-raggruppamento-results"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  #click di conferma
        self.wait_loader()

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")  
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()   #click sulla prima fattura
        self.wait_loader()

        descrizione=self.find(By.XPATH, '(//tbody//tr[1]//td[3])[1]').text  #controlla se appare la descrizione personalizzata
        self.assertEqual(descrizione[8:43], "Attività num. 4 in stato Completato")
        #elimina fattura
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask "]'))).click() #elimina fattura
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click() #apro attività
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click() #elimino attività
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        testo=self.find(By.XPATH, '//textarea[@id="setting155"]')
        testo.clear()
        sleep(1)

        self.navigateTo("Impostazioni")
        self.wait_loader()
        
    def stato_predefinito_attivita_dashboard(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting170-container"]').click()   #cambio lo stato predefinito a completato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Completato')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.navigateTo("Dashboard")
        self.wait_loader()

        self.find(By.XPATH, '(//td[@class="fc-timegrid-slot fc-timegrid-slot-lane fc-timegrid-slot-minor"])[41]').click()   #click in calendario
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #tipo
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #richiesta
        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        #aggiunta tecnico
        self.find(By.XPATH, '(//ul[@class="select2-selection__rendered"])[4]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[2]'))) #controlla se appare tra le opzioni di scelta il tecnico
        self.find(By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[2]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()
        sleep(1)

        self.navigateTo("Attività")
        self.wait_loader()

        stato=self.find(By.XPATH, '(//tr[1]//td[7])[2]').text
        self.assertEqual(stato, "Completato")
        #elimino attività
        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader() 

        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting170-container"]').click()   #cambio lo stato predefinito a Programmato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Programmato')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        sleep(1)

    def stato_predefinito_attivita(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting171-container"]').click()   #cambio lo stato predefinito a completato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Completato')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        sleep(1)
        
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click() #creo nuova attività
        sleep(1)
        #cliente
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #tipo
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        #richiesta
        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()

        self.navigateTo("Attività")
        self.wait_loader()

        stato=self.find(By.XPATH, '(//tr[1]//td[7])[2]').text
        self.assertEqual(stato, "Completato")
        #elimino attività
        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader() 

        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-4"]').click() #apro Attività
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting171-container"]').click()   #cambio lo stato predefinito a Da Programmare
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Da programmare')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        
