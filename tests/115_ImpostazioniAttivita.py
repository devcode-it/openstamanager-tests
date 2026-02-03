from common.Test import Test, get_html
from selenium.webdriver.common.by import By
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
        wait = self.wait_driver      
        self.navigateTo("Utenti e permessi")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Gruppo"]//input'))).send_keys('Tecnici', Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td[2]')           

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@data-title="Aggiungi utente"]'))
        ).click()

        user = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="username"]'))
        ) 
        user.clear()
        user.send_keys(self.getConfig('tests.tecnico_user'))
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanag-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys('Tecnico')

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys(Keys.ENTER)
        password = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))
        ) 
        password.clear()
        password.send_keys(self.getConfig('tests.tecnico_password'))
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="submit-button"]'))
        ).click()
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[18]//td[2]')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Lettura e scrittura')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)

        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Mostra i prezzi al tecnico"))
        )]//div//label').click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="nav-link bg-danger"]'))
        ).click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys(self.getConfig('tests.tecnico_user'))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys(self.getConfig('tests.tecnico_password')) 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-danger btn-block btn-flat"]'))
        ).click() 
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtipointervento-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_articolo-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Articolo 1')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]'))
        ).click()

        wait.until(EC.invisibility_of_element_located((By.XPATH, '//thead//tr[1]//th[7]'))) 

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="nav-link bg-danger"]'))
        ).click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys(self.getConfig('login.username'))   
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys(self.getConfig('login.password'))
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-danger btn-block btn-flat"]'))
        ).click() 
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//label[@class="btn btn-default active"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="nav-link bg-danger"]'))
        ).click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys(self.getConfig('tests.tecnico_user'))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys(self.getConfig('tests.tecnico_password')) 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-danger btn-block btn-flat"]'))
        ).click() 
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtipointervento-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_articolo-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Articolo 1')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//thead//tr[1]//th[7]'))) 

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="nav-link bg-danger"]'))
        ).click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys(self.getConfig('login.username'))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys(self.getConfig('login.password')) 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-danger btn-block btn-flat"]'))
        ).click() 
        self.wait_loader()

    def stampa_anteprima_firma(self):
        self.navigateTo("Attività")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtipointervento-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-primary "])[2]'))
        ).click()

        self.find_elements(By.XPATH, '//div[@id="viewer"]//span[71]//text()')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="close"]'))
        ).click()
        
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Stampa per anteprima e firma"))
        )]//span').click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))
        ).send_keys("Intervento (senza prezzi)", Keys.ENTER)

        self.navigateTo("Attività")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-primary "])[2]'))
        ).click()

        wait.until(EC.invisibility_of_element_located((By.XPATH, '(//div[@id="viewer"]//span)[69]')))
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="close"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        elemento = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Stampa per anteprima e firma"))
        )]//span[@class="select2-selection__clear"]').click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option"]'))
        ).click()

    def inserimento_sessioni_tecnici(self):
        wait = self.wait_driver  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Permetti inserimento sessioni degli altri tecnici"))
        )]//div//label').click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="nav-link bg-danger"]'))
        ).click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys(self.getConfig('tests.tecnico_user'))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys(self.getConfig('tests.tecnico_password')) 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-danger btn-block btn-flat"]'))
        ).click() 
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-tool"])[4]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//ul[@class="select2-selection__rendered"]//li)[3]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-tecnici_assegnati-results"]//li[2]'))) 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-tool"])[5]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//ul[@class="select2-selection__rendered"])[4]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[1]'))) 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[1]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="close"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="nav-link bg-danger"]'))
        ).click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys(self.getConfig('login.username'))   
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys(self.getConfig('login.password'))
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-danger btn-block btn-flat"]'))
        ).click() 
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Permetti inserimento sessioni degli altri tecnici"))
        )]//div//label').click()

    def giorni_lavorativi(self):
        self.navigateTo("Dashboard")
        self.wait_loader() 

        wait.until(EC.invisibility_of_element_located((By.XPATH, '(//div[@class="fc-event fc-event-start fc-event-future fc-bg-event"])[3]'))) 
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Giorni lavorativi"))
        )]//span//li [contains(., "Venerdì")]//span').click()

        self.navigateTo("Dashboard")
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@class="fc-event fc-event-start fc-event-future fc-bg-event"])[3]'))) 
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Giorni lavorativi"))
        )]//li[@class="select2-search select2-search--inline"]').click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//li[contains(., "Venerdì"))
        )]').click()

    def notifica_tecnico_aggiunta_sessione(self):
        wait = self.wait_driver  
        self.navigateTo("Anagrafiche")
        self.wait_loader()
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Tecnico", Keys.ENTER)
 
        self.wait_for_element_and_click('//tbody//td[2]//div[1]')

        self.input(None, 'Email').setValue(self.getConfig('tests.email_receiver'))
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()

        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="deleteicon fa fa-times"]'))
        ).click()

        self.navigateTo("Attività")
        self.wait_loader()
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtipointervento-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id-container"]'))
        ).click()
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id-results"]//li[4]'))
        ).click() 

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-tool"])[5]'))
        ).click()
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//ul[@class="select2-selection__rendered"])[4]'))
        ).click()
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[2]'))
        ).click()
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()  
        self.wait_loader()

        wait.until(EC.invisibility_of_element_located((By.XPATH, '(//div[@class="toast-message"])[2]')))
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Notifica al tecnico l\'aggiunta della sessione nell\'attività"))
        )]//div//label').click()
 
        self.navigateTo("Attività")
        self.wait_loader()
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtipointervento-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
  
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id-container"]'))
        ).click()
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id-results"]//li[4]'))
        ).click()   

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-tool"])[5]'))
        ).click()
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//ul[@class="select2-selection__rendered"])[4]'))
        ).click()
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[2]'))
        ).click()
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()  
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@class="toast-message"])[2]')))
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Notifica al tecnico l\'aggiunta della sessione nell\'attività"))
        )]//div//label').click()

    def notifica_tecnico_rimozione_sessione(self):
        self.navigateTo("Attività")
        self.wait_loader()
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtipointervento-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
   
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id-container"]'))
        ).click()
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id-results"]//li[4]'))
        ).click()  

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-tool"])[5]'))
        ).click()
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//ul[@class="select2-selection__rendered"])[4]'))
        ).click()
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[2]'))
        ).click()
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()   
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//td[@class="text-center"]//button[3]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click() 
        self.wait_loader()

        self.navigateTo("Attività")
        self.wait_loader()

        invio = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[14]'))
        ).text
        self.assertNotEqual(invio, 'Inviata via email')
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]') 
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Notifica al tecnico la rimozione della sessione dall\'attività"))
        )]//div//label').click()

        self.navigateTo("Attività")
        self.wait_loader()
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtipointervento-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id-container"]'))
        ).click()
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id-results"]//li[4]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-tool"])[5]'))
        ).click()
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//ul[@class="select2-selection__rendered"])[4]'))
        ).click()
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[2]'))
        ).click()
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//td[@class="text-center"]//button[3]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Gestione email")
        self.navigateTo("Coda di invio")
        self.wait_loader()

        messaggio = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[5]//div'))
        ).text 
        self.assertEqual(messaggio, "Notifica rimozione intervento")
        self.navigateTo("Attività")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Notifica al tecnico la rimozione della sessione dall\'attività"))
        )]//div//label').click()

    def stato_attivita_firma(self):
        wait = self.wait_driver  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Stato dell\'attività dopo la firma "))
        )]//div//span').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Stato di Attività di Prova")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.navigateTo("Attività")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtipointervento-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()  
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-primary "])[2]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="firma"]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="firma_nome"]'))).send_keys('Prova')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-success pull-right"]'))
        ).click()
        self.wait_loader()

        self.navigateTo("Attività")
        self.wait_loader()

        stato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[7]'))
        ).text
        self.assertEqual(stato, "Stato di Attività di Prova")   
        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Stato dell\'attività dopo la firma "))
        )]//div//span').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Completato")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

    def espandi_barra_dettagli_aggiuntivi(self):
        wait = self.wait_driver  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Espandi automaticamente la sezione"))
        )]//div//label').click()

        self.navigateTo("Attività")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_scadenza"]')))
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="close"]'))
        ).click()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()
        
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Espandi automaticamente la sezione"))
        )]//div//label').click()

    def alert_occupazione_tecnici(self):
        wait = self.wait_driver  
        self.navigateTo("Attività")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtipointervento-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Programmato')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-tool"])[5]'))
        ).click()

        orario_inizio = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="orario_inizio"]'))
        )
        orario_inizio.clear()
        orario_inizio.send_keys("31/12/2025 09:00")    

        orario_fine = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="orario_fine"]'))
        )
        orario_fine.clear()
        orario_fine.send_keys("31/12/2025 10:00")    

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//div[@class="card-body"]//span[@class="select2-selection select2-selection--multiple"])[2]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[2]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() 
        self.wait_loader()

        self.navigateTo("Attività")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtipointervento-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('prova')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Programmato')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-tool"])[5]'))
        ).click()

        orario_inizio = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="orario_inizio"]'))
        )
        orario_inizio.clear()
        orario_inizio.send_keys("31/12/2025 09:00")    

        orario_fine = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="orario_fine"]'))
        )
        orario_fine.clear()
        orario_fine.send_keys("31/12/2025 10:00")    
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//div[@class="card-body"]//span[@class="select2-selection select2-selection--multiple"])[2]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[2]'))
        ).click()

        scritta = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="card-header"]//h3'))
        ).text
        self.assertEqual(scritta, "⚠️ Sono presenti dei conflitti con le sessioni di lavoro di alcuni tecnici")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="close"]'))
        ).click()

        self.expandSidebar("Strumenti")   
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Alert occupazione tecnici"))
        )]//div//label').click()

        self.navigateTo("Attività")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        wait.until(EC.invisibility_of_element_located((By.XPATH, '/div[@class="card-header"]//h3')))
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")   
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Alert occupazione tecnici"))
        )]//div//label').click()

    def verifica_numero_intervento(self):
        wait = self.wait_driver  
        self.navigateTo("Attività")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="alert alert-warning alert-dismissable"]')))

        self.expandSidebar("Strumenti")   
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Verifica numero intervento"))
        )]//div//label').click()

        self.navigateTo("Attività")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        wait.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="alert alert-warning alert-dismissable"]')))

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader() 

        self.expandSidebar("Strumenti")   
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Verifica numero intervento"))
        )]//div//label').click()

    def formato_ore_stampa(self):
        wait = self.wait_driver  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Formato ore in stampa"))
        )]//div//span').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Sessantesimi")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.navigateTo("Attività")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtipointervento-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-tool"])[5]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//ul[@class="select2-selection__rendered"])[4]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[1]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()  
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="print-button_p"]'))
        ).click()

        self.driver.switch_to.window(self.driver.window_handles[1])

        ore = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="viewer"]//span[57]'))
        ).text
        self.assertEqual(ore, "1:00")
        self.driver.close() 
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Formato ore in stampa"))
        )]//div//span').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Decimale")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.navigateTo("Attività")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="print-button_p"]'))
        ).click()

        self.driver.switch_to.window(self.driver.window_handles[1])

        ore = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="viewer"]//span[57]'))
        ).text
        self.assertEqual(ore, "1,00")
        self.driver.close() 
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

    def notifica_tecnico_assegnazione(self):
        self.navigateTo("Attività")
        self.wait_loader()
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtipointervento-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id-container"]'))
        ).click()
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id-results"]//li[4]'))
        ).click() 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-tool"])[4]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//span[@class="select2-selection select2-selection--multiple"])[3]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-tecnici_assegnati-results"]//li[2]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()  
        self.wait_loader()

        wait.until(EC.invisibility_of_element_located((By.XPATH, '(//div[@class="toast-message"])[2]')))

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Notifica al tecnico l\'assegnazione all\'attività"))
        )]//div//label').click()

        self.navigateTo("Attività")
        self.wait_loader()
 
        self.wait_for_element_and_click('//tbody//tr//td[2]') 
        self.wait_loader()
        
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@class="selection"]//ul//li//span'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-success"]'))
        ).click()   
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))
        ).click()
        
        tecnico = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))
        )
        tecnico.send_keys('Tecnico')
        tecnico.send_keys(Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-success"]'))
        ).click()   
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@class="toast-message"])[2]')))
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()
        
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Notifica al tecnico l\'assegnazione all\'attività"))
        )]//div//label').click()

    def notifica_tecnico_rimozione_assegnazione(self):
        self.navigateTo("Attività")
        self.wait_loader()
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtipointervento-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id-container"]'))
        ).click()
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id-results"]//li[4]'))
        ).click()  
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-tool"])[4]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//span[@class="select2-selection select2-selection--multiple"])[3]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-tecnici_assegnati-results"]//li[2]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() 
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-selection__choice__remove"]'))
        ).click() 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()

        wait.until(EC.invisibility_of_element_located((By.XPATH, '(//div[@class="toast-message"])[2]')))

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Notifica al tecnico la rimozione dell\'assegnazione dall\'attività"))
        )]//div//label').click()

        self.navigateTo("Attività")
        self.wait_loader()
 
        self.wait_for_element_and_click('//tbody//tr//td[2]') 
        self.wait_loader()
        
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))
        ).click()
        
        tecnico = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))
        )
        tecnico.send_keys('Tecnico')
        tecnico.send_keys(Keys.ENTER)
        
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-success"]'))
        ).click()   
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@class="selection"]//ul//li//span'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-success"]'))
        ).click()   
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@class="toast-message"])[2]')))
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Notifica al tecnico la rimozione dell\'assegnazione dall\'attività"))
        )]//div//label').click()

    def descrizione_attivita(self):
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Descrizione personalizzata in fatturazione"))
        )]//textarea').send_keys('Test')

        self.navigateTo("Attività")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys("Cliente", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtipointervento-container"]'))
        ).click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Generico")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))
        ).click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).send_keys("Test")   
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()  
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Test") 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1") 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatointervento-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[3]'))
        ).send_keys("Completato", Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="back"]'))
        ).click() 
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td') 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@data-toggle="dropdown"]'))
        ).click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-op="crea_fattura"]'))).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-raggruppamento-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")    
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-raggruppamento-results"]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]'))
        ).click()  
        self.wait_loader()

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")  
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[3]//td[2]')  
        self.wait_loader()

        descrizione = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[3]'))
        ).text  
        self.assertEqual(descrizione[8:20], "Test")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask "]'))).click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.navigateTo("Attività")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[2]//td[2]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Descrizione personalizzata in fatturazione"))
        )]//textarea').clear()
        
    def stato_predefinito_attivita_dashboard(self):
        wait = self.wait_driver  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Stato predefinito dell\'attività da Dashboard"))
        )]//div//span').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Stato di Attività di Prova")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.navigateTo("Dashboard")
        self.wait_loader()

        actions = webdriver.common.action_chains.ActionChains(self.driver)
        actions.move_to_element(self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="calendar"]'))
        )).move_by_offset(300,100).click().perform()
        modal = self.wait_modal()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtipointervento-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//ul[@class="select2-selection__rendered"])[4]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[2]'))) 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idtecnico-results"]//li[2]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() 
        self.wait_loader()

        self.navigateTo("Attività")
        self.wait_loader()

        stato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[7]'))
        ).text
        self.assertEqual(stato, "Stato di Attività di Prova")

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader() 

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Stato predefinito dell\'attività da Dashboard"))
        )]//div//span').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Programmato")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

    def stato_predefinito_attivita(self):
        wait = self.wait_driver  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//div[@class="form-group" and contains(., "Stato predefinito dell\'attività"))
        )]//div//span)[8]').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Stato di Attività di Prova")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        
        self.navigateTo("Attività")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Cliente')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtipointervento-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Generico')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() 
        self.wait_loader()

        self.navigateTo("Attività")
        self.wait_loader()

        stato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//tr[1]//td[7])[2]'))
        ).text
        self.assertEqual(stato, "Stato di Attività di Prova")

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader() 

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting171-container"]'))
        ).click()  
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys('Da programmare')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)
        
