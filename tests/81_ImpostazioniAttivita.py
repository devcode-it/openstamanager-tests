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
    
    def test_impostazioni_attivita(self):
        # Test impostazione Mostra i prezzi al tecnico
        self.mostra_prezzi_tecnico()

        # Test impostazione Stampa per anteprima e firma
        self.stampa_anteprima_firma()   

        # Test impostazione Permetti inserimento sessioni degli altri tecnici
        self.inserimento_sessioni_tecnici()

        # Test impostazione Giorni lavorativi
        self.giorni_lavorativi()

        # Test impostazione Notifica al tecnico l'aggiunta della sessione nell'attività
        self.notifica_tecnico_aggiunta_sessione()

        # Test impostazione Notifica al tecnico la rimozione della sessione dall'attività
        self.notifica_tecnico_rimozione_sessione()

        # Test impostazione Stato dell’attività dopo la firma
        self.stato_attivita_firma()

        # Test impostazione Espandi automaticamente la sezione “Dettagli aggiuntivi”
        self.espandi_barra_dettagli_aggiuntivi()

        # Test impostazione Alert occupazione tecnici
        self.alert_occupazione_tecnici()

        # Test impostazione Verifica numero intervento
        self.verifica_numero_intervento()

        # Test impostazione Formato ore in stampa
        self.formato_ore_stampa()

        # Test impostazione Notifica al tecnico l'assegnazione all'attività
        self.notifica_tecnico_assegnazione()

        # Test impostazione Notifica al tecnico la rimozione dell'assegnazione dall'attività
        self.notifica_tecnico_rimozione_assegnazione()

        # Test impostazione Descrizione personalizzata in fatturazione
        self.descrizione_attivita()

        # Test impostazione Stato predefinito dell'attività da Dashboard
        self.stato_predefinito_attivita_dashboard()

        # Test impostazione Stato predefinito dell'attività
        self.stato_predefinito_attivita()

        ## TODO: numero di minuti di avanzamento delle sessioni delle attività

        ## TODO: cambia automaticamente stato attività fatturate


    def mostra_prezzi_tecnico(self):
        wait = WebDriverWait(self.driver, 20)      
        self.navigateTo("Utenti e permessi")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Gruppo"]//input'))).send_keys('Tecnici', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()           

        self.find(By.XPATH, '//a[@data-title="Aggiungi utente"]').click()
        sleep(1)

        user=self.find(By.XPATH, '//input[@id="username"]') 
        user.clear()
        user.send_keys(self.getConfig('tests.tecnico_user'))
        self.find(By.XPATH, '//span[@id="select2-idanag-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys('Tecnico')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys(Keys.ENTER)
        password=self.find(By.XPATH, '//input[@id="password"]') 
        password.clear()
        password.send_keys(self.getConfig('tests.tecnico_password'))
        self.find(By.XPATH, '//button[@id="submit-button"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[17]//td[2]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Lettura e scrittura')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        sleep(1)

        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Attività"]').click()
        sleep(1)

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Mostra i prezzi al tecnico")]//div//label').click() 
        sleep(1)

        self.find(By.XPATH, '//a[@class="nav-link bg-danger"]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys(self.getConfig('tests.tecnico_user'))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys(self.getConfig('tests.tecnico_password')) 
        self.find(By.XPATH, '//button[@class="btn btn-danger btn-block btn-flat"]').click() 
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click() 
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Articolo 1')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click()
        sleep(1)

        wait.until(EC.invisibility_of_element_located((By.XPATH, '//thead//tr[1]//th[7]'))) 

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="nav-link bg-danger"]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys(self.getConfig('login.username'))   
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys(self.getConfig('login.password'))
        self.find(By.XPATH, '//button[@class="btn btn-danger btn-block btn-flat"]').click() 
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Attività"]').click()
        sleep(1)

        self.find(By.XPATH, '//label[@class="btn btn-default active"]').click()
        sleep(1)

        self.find(By.XPATH, '//a[@class="nav-link bg-danger"]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys(self.getConfig('tests.tecnico_user'))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys(self.getConfig('tests.tecnico_password')) 
        self.find(By.XPATH, '//button[@class="btn btn-danger btn-block btn-flat"]').click() 
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click() 
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Articolo 1')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//thead//tr[1]//th[7]'))) 

        self.find(By.XPATH, '//a[@class="nav-link bg-danger"]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys(self.getConfig('login.username'))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys(self.getConfig('login.password')) 
        self.find(By.XPATH, '//button[@class="btn btn-danger btn-block btn-flat"]').click() 
        self.wait_loader()

    def stampa_anteprima_firma(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()
        self.wait_loader()

        self.find(By.XPATH, '(//button[@class="btn btn-primary "])[2]').click()
        sleep(1)

        self.find_elements(By.XPATH, '//div[@id="viewer"]//span[71]//text()')
        self.find(By.XPATH, '//button[@class="close"]').click()
        sleep(1)
        
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Attività"]').click() 
        sleep(1)

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Stampa per anteprima e firma")]//span').click()
        sleep(1)

        self.find(By.XPATH, '(//input[@class="select2-search__field"])[2]').send_keys("Intervento (senza prezzi)", Keys.ENTER)
        sleep(1)

        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '(//button[@class="btn btn-primary "])[2]').click() 
        sleep(1)

        wait.until(EC.invisibility_of_element_located((By.XPATH, '(//div[@id="viewer"]//span)[69]')))
        self.find(By.XPATH, '//button[@class="close"]').click()
        sleep(1)

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Attività"]').click() 
        sleep(1)

        elemento=self.find(By.XPATH, '//div[@class="form-group" and contains(., "Stampa per anteprima e firma")]//span[@class="select2-selection__clear"]').click()
        self.find(By.XPATH, '//li[@class="select2-results__option"]').click()
        sleep(1)

    def inserimento_sessioni_tecnici(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Attività"]').click() 
        sleep(1)

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Permetti inserimento sessioni degli altri tecnici")]//div//label').click() 
        sleep(1)

        self.find(By.XPATH, '//a[@class="nav-link bg-danger"]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys(self.getConfig('tests.tecnico_user'))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys(self.getConfig('tests.tecnico_password')) 
        self.find(By.XPATH, '//button[@class="btn btn-danger btn-block btn-flat"]').click() 
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click() 
        sleep(1)

        self.find(By.XPATH, '(//button[@class="btn btn-tool"])[4]').click()
        sleep(1)

        self.find(By.XPATH, '(//ul[@class="select2-selection__rendered"]//li)[3]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-tecnici_assegnati-results"]//li[2]'))) 
        self.find(By.XPATH, '(//button[@class="btn btn-tool"])[5]').click()
        sleep(1)

        self.find(By.XPATH, '(//ul[@class="select2-selection__rendered"])[4]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[1]'))) 
        self.find(By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[1]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="close"]').click()
        sleep(1)

        self.find(By.XPATH, '//a[@class="nav-link bg-danger"]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys(self.getConfig('login.username'))   
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys(self.getConfig('login.password'))
        self.find(By.XPATH, '//button[@class="btn btn-danger btn-block btn-flat"]').click() 
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Attività"]').click()
        sleep(1)

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Permetti inserimento sessioni degli altri tecnici")]//div//label').click() 
        sleep(1)

    def giorni_lavorativi(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Dashboard")
        self.wait_loader() 

        wait.until(EC.invisibility_of_element_located((By.XPATH, '(//div[@class="fc-event fc-event-start fc-event-future fc-bg-event"])[3]'))) 
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Attività"]').click() 
        sleep(1)

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Giorni lavorativi")]//span//li [contains(., "Venerdì")]//span').click()
        sleep(1)

        self.navigateTo("Dashboard")
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@class="fc-event fc-event-start fc-event-future fc-bg-event"])[3]'))) 
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Attività"]').click()
        sleep(1)

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Giorni lavorativi")]//li[@class="select2-search select2-search--inline"]').click() 
        sleep(1)

        self.find(By.XPATH, '//li[contains(., "Venerdì")]').click()
        sleep(1)

    def notifica_tecnico_aggiunta_sessione(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Anagrafiche")
        self.wait_loader()
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Tecnico", Keys.ENTER)
        sleep(1)
 
        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()
        sleep(1)

        self.input(None, 'Email').setValue(self.getConfig('tests.email_receiver'))
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click() 
        sleep(1)

        self.navigateTo("Attività")
        self.wait_loader()
 
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click() 
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')

        self.find(By.XPATH, '//span[@id="select2-id-container"]').click()
        sleep(1)
 
        self.find(By.XPATH, '//ul[@id="select2-id-results"]//li[4]').click() 

        self.find(By.XPATH, '(//button[@class="btn btn-tool"])[5]').click()
        sleep(1)
 
        self.find(By.XPATH, '(//ul[@class="select2-selection__rendered"])[4]').click()
        sleep(1)
 
        self.find(By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[2]').click()
        sleep(1)
 
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()  
        self.wait_loader()

        wait.until(EC.invisibility_of_element_located((By.XPATH, '(//div[@class="toast-message"])[2]')))
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()
 
        self.find(By.XPATH, '//div[@title="Attività"]').click()
        sleep(1)
 
        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Notifica al tecnico l\'aggiunta della sessione nell\'attività")]//div//label').click() 
        sleep(1)
 
        self.navigateTo("Attività")
        self.wait_loader()
 
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click() 
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
  
        self.find(By.XPATH, '//span[@id="select2-id-container"]').click()
        sleep(1)
 
        self.find(By.XPATH, '//ul[@id="select2-id-results"]//li[4]').click()   

        self.find(By.XPATH, '(//button[@class="btn btn-tool"])[5]').click()
        sleep(1)
 
        self.find(By.XPATH, '(//ul[@class="select2-selection__rendered"])[4]').click()
        sleep(1)
 
        self.find(By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[2]').click()
        sleep(1)
 
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()  
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@class="toast-message"])[2]')))
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()
 
        self.find(By.XPATH, '//div[@title="Attività"]').click() 
        sleep(1)
 
        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Notifica al tecnico l\'aggiunta della sessione nell\'attività")]//div//label').click() 
        sleep(1)

    def notifica_tecnico_rimozione_sessione(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attività")
        self.wait_loader()
 
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click() 
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
   
        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')

        self.find(By.XPATH, '//span[@id="select2-id-container"]').click()
        sleep(1)
 
        self.find(By.XPATH, '//ul[@id="select2-id-results"]//li[4]').click()  

        self.find(By.XPATH, '(//button[@class="btn btn-tool"])[5]').click()
        sleep(1)
 
        self.find(By.XPATH, '(//ul[@class="select2-selection__rendered"])[4]').click()
        sleep(1)
 
        self.find(By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[2]').click()
        sleep(1)
 
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   
        self.wait_loader()

        self.find(By.XPATH, '//td[@class="text-center"]//button[3]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@id="save"]').click() 
        self.wait_loader()

        self.navigateTo("Attività")
        self.wait_loader()

        invio=self.find(By.XPATH, '//tbody//tr//td[14]').text
        self.assertNotEqual(invio, 'Inviata via email')
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Attività"]').click()
        sleep(1)

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Notifica al tecnico la rimozione della sessione dall\'attività")]//div//label').click() 
        sleep(1)

        self.navigateTo("Attività")
        self.wait_loader()
 
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')

        self.find(By.XPATH, '//span[@id="select2-id-container"]').click()
        sleep(1)
 
        self.find(By.XPATH, '//ul[@id="select2-id-results"]//li[4]').click()
        self.find(By.XPATH, '(//button[@class="btn btn-tool"])[5]').click()
        sleep(1)
 
        self.find(By.XPATH, '(//ul[@class="select2-selection__rendered"])[4]').click()
        sleep(1)
 
        self.find(By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[2]').click()
        sleep(1)
 
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//td[@class="text-center"]//button[3]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        self.expandSidebar("Gestione email")
        self.navigateTo("Coda di invio")
        self.wait_loader()

        messaggio=self.find(By.XPATH, '//tbody//tr[1]//td[5]//div').text 
        self.assertEqual(messaggio, "Notifica rimozione intervento")
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader()


        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Attività"]').click() 
        sleep(1)

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Notifica al tecnico la rimozione della sessione dall\'attività")]//div//label').click() 
        sleep(1)

    def stato_attivita_firma(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Attività"]').click()
        sleep(1)

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Stato dell\'attività dopo la firma ")]//div//span').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Stato di Attività di Prova")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click() 
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()  
        self.wait_loader()

        self.find(By.XPATH, '(//button[@class="btn btn-primary "])[2]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@id="firma"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="firma_nome"]'))).send_keys('Prova')
        self.find(By.XPATH,'//button[@class="btn btn-success pull-right"]').click()
        self.wait_loader()

        self.navigateTo("Attività")
        self.wait_loader()

        stato=self.find(By.XPATH, '//tbody//tr//td[7]').text
        self.assertEqual(stato, "Stato di Attività di Prova")   
        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Attività"]').click() 
        sleep(1)

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Stato dell\'attività dopo la firma ")]//div//span').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Completato")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        sleep(1)

    def espandi_barra_dettagli_aggiuntivi(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Attività"]').click()
        sleep(1)

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Espandi automaticamente la sezione")]//div//label').click() 
        sleep(1)

        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click() 
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_scadenza"]')))
        self.find(By.XPATH, '//button[@class="close"]').click()
        sleep(1)

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Attività"]').click()
        sleep(1)
        
        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Espandi automaticamente la sezione")]//div//label').click() 
        sleep(1)

    def alert_occupazione_tecnici(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click() 
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')

        self.find(By.XPATH, '//span[@id="select2-id-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Programmato')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.find(By.XPATH, '(//button[@class="btn btn-tool"])[5]').click()
        sleep(1)

        orario_inizio=self.find(By.XPATH, '//input[@id="orario_inizio"]')
        orario_inizio.clear()
        orario_inizio.send_keys("31/12/2024 09:00")    

        orario_fine=self.find(By.XPATH, '//input[@id="orario_fine"]')
        orario_fine.clear()
        orario_fine.send_keys("31/12/2024 10:00")    

        self.find(By.XPATH, '(//div[@class="card-body"]//span[@class="select2-selection select2-selection--multiple"])[2]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[2]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() 
        self.wait_loader()

        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click() 
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('prova')

        self.find(By.XPATH, '//span[@id="select2-id-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Programmato')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.find(By.XPATH, '(//button[@class="btn btn-tool"])[5]').click() 
        sleep(1)

        orario_inizio=self.find(By.XPATH, '//input[@id="orario_inizio"]')
        orario_inizio.clear()
        orario_inizio.send_keys("31/12/2024 09:00")    

        orario_fine=self.find(By.XPATH, '//input[@id="orario_fine"]')
        orario_fine.clear()
        orario_fine.send_keys("31/12/2024 10:00")    
        self.find(By.XPATH, '(//div[@class="card-body"]//span[@class="select2-selection select2-selection--multiple"])[2]').click() 
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[2]').click()
        sleep(1)

        scritta=self.find(By.XPATH, '//div[@class="card-header"]//h3').text
        self.assertEqual(scritta, "⚠️ Sono presenti dei conflitti con le sessioni di lavoro di alcuni tecnici")
        self.find(By.XPATH, '//button[@class="close"]').click() 
        sleep(1)

        self.expandSidebar("Strumenti")   
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Attività"]').click()
        sleep(1)

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Alert occupazione tecnici")]//div//label').click() 
        sleep(1)

        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        wait.until(EC.invisibility_of_element_located((By.XPATH, '/div[@class="card-header"]//h3')))
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader() 
        sleep(1)

        self.expandSidebar("Strumenti")   
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Attività"]').click()
        sleep(1)

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Alert occupazione tecnici")]//div//label').click() 
        sleep(1)

    def verifica_numero_intervento(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="alert alert-warning alert-dismissable"]')))

        self.expandSidebar("Strumenti")   
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Attività"]').click()
        sleep(1)

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Verifica numero intervento")]//div//label').click() 
        sleep(1)

        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        wait.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="alert alert-warning alert-dismissable"]')))

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click() 
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader() 

        self.expandSidebar("Strumenti")   
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Attività"]').click()
        sleep(1)

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Verifica numero intervento")]//div//label').click() 
        sleep(1)

    def formato_ore_stampa(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Attività"]').click() 
        sleep(1)

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Formato ore in stampa")]//div//span').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Sessantesimi")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click() 
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')

        self.find(By.XPATH, '(//button[@class="btn btn-tool"])[5]').click()
        sleep(1)

        self.find(By.XPATH, '(//ul[@class="select2-selection__rendered"])[4]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[1]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()  
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="print-button_p"]').click()  
        sleep(1)

        self.driver.switch_to.window(self.driver.window_handles[1]) 
        sleep(1)

        ore=self.find(By.XPATH, '//div[@id="viewer"]//span[57]').text
        self.assertEqual(ore, "1:00")
        self.driver.close() 
        self.driver.switch_to.window(self.driver.window_handles[0]) 
        sleep(1)

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Attività"]').click() 
        sleep(1)

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Formato ore in stampa")]//div//span').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Decimale")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="print-button_p"]').click()  
        sleep(1)

        self.driver.switch_to.window(self.driver.window_handles[1]) 
        sleep(1)

        ore=self.find(By.XPATH, '//div[@id="viewer"]//span[57]').text
        self.assertEqual(ore, "1,00")
        self.driver.close() 
        self.driver.switch_to.window(self.driver.window_handles[0]) 
        sleep(1)

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

    def notifica_tecnico_assegnazione(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attività")
        self.wait_loader()
 
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click() 
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')

        self.find(By.XPATH, '//span[@id="select2-id-container"]').click()
        sleep(1)
 
        self.find(By.XPATH, '//ul[@id="select2-id-results"]//li[4]').click() 
        self.find(By.XPATH, '(//button[@class="btn btn-tool"])[4]').click()
        sleep(1)

        self.find(By.XPATH, '(//span[@class="select2-selection select2-selection--multiple"])[3]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-tecnici_assegnati-results"]//li[2]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()  
        self.wait_loader()

        wait.until(EC.invisibility_of_element_located((By.XPATH, '(//div[@class="toast-message"])[2]')))

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Attività"]').click() 
        sleep(1)

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Notifica al tecnico l\'assegnazione all\'attività")]//div//label').click() 
        sleep(1)

        self.navigateTo("Attività")
        self.wait_loader()
 
        self.find(By.XPATH,'//tbody//tr//td[2]').click() 
        self.wait_loader()
        
        self.find(By.XPATH, '//span[@class="selection"]//ul//li//span').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-success"]').click()   
        self.wait_loader()

        self.find(By.XPATH, '//input[@class="select2-search__field"]').click()
        sleep(1)
        
        tecnico = self.find(By.XPATH, '//input[@class="select2-search__field"]')
        tecnico.send_keys('Tecnico')
        sleep(1)
        tecnico.send_keys(Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-success"]').click()   
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@class="toast-message"])[2]')))
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()
 
        self.find(By.XPATH, '//div[@title="Attività"]').click()
        sleep(1)
        
        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Notifica al tecnico l\'assegnazione all\'attività")]//div//label').click() 
        sleep(1)

    def notifica_tecnico_rimozione_assegnazione(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attività")
        self.wait_loader()
 
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click() 
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')

        self.find(By.XPATH, '//span[@id="select2-id-container"]').click()
        sleep(1)
 
        self.find(By.XPATH, '//ul[@id="select2-id-results"]//li[4]').click()  
        self.find(By.XPATH, '(//button[@class="btn btn-tool"])[4]').click()
        sleep(1)

        self.find(By.XPATH, '(//span[@class="select2-selection select2-selection--multiple"])[3]').click()
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-tecnici_assegnati-results"]//li[2]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//span[@class="select2-selection__choice__remove"]').click() 
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        wait.until(EC.invisibility_of_element_located((By.XPATH, '(//div[@class="toast-message"])[2]')))

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Attività"]').click()
        sleep(1)

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Notifica al tecnico la rimozione dell\'assegnazione dall\'attività")]//div//label').click() 
        sleep(1)

        self.navigateTo("Attività")
        self.wait_loader()
 
        self.find(By.XPATH,'//tbody//tr//td[2]').click() 
        self.wait_loader()
        
        self.find(By.XPATH, '//input[@class="select2-search__field"]').click()
        sleep(1)
        
        tecnico = self.find(By.XPATH, '//input[@class="select2-search__field"]')
        tecnico.send_keys('Tecnico')
        sleep(1)
        tecnico.send_keys(Keys.ENTER)
        sleep(1)
        
        self.find(By.XPATH, '//button[@class="btn btn-success"]').click()   
        self.wait_loader()

        self.find(By.XPATH, '//span[@class="selection"]//ul//li//span').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="btn btn-success"]').click()   
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@class="toast-message"])[2]')))
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Attività"]').click() 
        sleep(1)

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Notifica al tecnico la rimozione dell\'assegnazione dall\'attività")]//div//label').click() 
        sleep(1)

    def descrizione_attivita(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Attività"]').click() 
        sleep(1)

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Descrizione personalizzata in fatturazione")]//textarea').send_keys('Test')
        sleep(1)

        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click() 
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Generico")
        sleep(1)

        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).send_keys("Test")   
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()  
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()  
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Test") 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1") 
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()  
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idstatointervento-container"]').click() 
        sleep(1)

        self.find(By.XPATH, '(//input[@class="select2-search__field"])[3]').send_keys("Completato", Keys.ENTER) 
        sleep(1)

        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="back"]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td').click() 
        self.find(By.XPATH, '//button[@data-toggle="dropdown"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-op="crea_fattura"]'))).click() 
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-raggruppamento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")    
        self.find(By.XPATH, '//ul[@id="select2-raggruppamento-results"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  
        self.wait_loader()

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")  
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[3]//td[2]').click()  
        self.wait_loader()

        descrizione=self.find(By.XPATH, '//tbody//tr//td[3]').text  
        self.assertEqual(descrizione[8:13], "Test")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask "]'))).click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[2]//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Attività"]').click() 
        sleep(1)

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Descrizione personalizzata in fatturazione")]//textarea').clear()
        sleep(1)
        
    def stato_predefinito_attivita_dashboard(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Attività"]').click()
        sleep(1)

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Stato predefinito dell\'attività da Dashboard")]//div//span').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Stato di Attività di Prova")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.navigateTo("Dashboard")
        self.wait_loader()

        actions = webdriver.common.action_chains.ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH,'//div[@id="calendar"]')).move_by_offset(300,100).click().perform()
        modal = self.wait_modal()

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')

        self.find(By.XPATH, '(//ul[@class="select2-selection__rendered"])[4]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[2]'))) 
        self.find(By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[2]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() 
        self.wait_loader()
        sleep(1)

        self.navigateTo("Attività")
        self.wait_loader()

        stato=self.find(By.XPATH, '//tbody//tr//td[7]').text
        self.assertEqual(stato, "Stato di Attività di Prova")

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader() 

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Attività"]').click()
        sleep(1)
        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Stato predefinito dell\'attività da Dashboard")]//div//span').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Programmato")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        sleep(1)

    def stato_predefinito_attivita(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Attività"]').click()
        sleep(1)

        self.find(By.XPATH, '(//div[@class="form-group" and contains(., "Stato predefinito dell\'attività")]//div//span)[8]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Stato di Attività di Prova")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        sleep(1)
        
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click() 
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.find(By.XPATH, '//div[@id="cke_1_contents"]//iframe').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() 
        self.wait_loader()

        self.navigateTo("Attività")
        self.wait_loader()

        stato=self.find(By.XPATH, '(//tr[1]//td[7])[2]').text
        self.assertEqual(stato, "Stato di Attività di Prova")

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader() 

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@title="Attività"]').click() 
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting171-container"]').click()  
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Da programmare')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        
