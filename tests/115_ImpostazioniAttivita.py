from common.Test import Test, get_html
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

import time

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
        ## TODO: raggruppamento fatturazione massiva attività
        ## TODO: permetti inserimento di allegati in attività completate
        ## TODO: limita conteggio ore ad oggi nell'intestazione
        ## TODO: applica diritto di chiamata una volta al giorno

    def mostra_prezzi_tecnico(self):
        wait = self.wait_driver
        self.expandSidebar("Gestione accessi")
        self.navigate_to_and_wait("Utenti e permessi")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Gruppo"]//input'))).send_keys('Tecnici', Keys.ENTER)

        self.click_first_table_row()           

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@data-title="Aggiungi utente"]'))
        ).click()

        user = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="username"]'))
        ) 
        user.clear()
        user.send_keys(self.getConfig('tests.tecnico_user'))
        self.wait_for_dropdown_and_select('//span[@id="select2-idanag-container"]', option_text='Tecnico')
        password = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))
        ) 
        password.clear()
        password.send_keys(self.getConfig('tests.tecnico_password'))
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="submit-button"]'))
        ).click()
        self.wait_loader()

        self.db_execute(
            "UPDATE zz_users SET options = %s WHERE username = %s",
            ('{"tours":[1,2,3,6,7,8,9,10,12,13,14,15,16,17,18,20,21,22,24,25,26,27,28,29,30,31,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112]}', self.getConfig('tests.tecnico_user'))
        )

        self.wait_for_element_and_click('//tbody//tr[td[1][normalize-space(.)="Attività"]]//td[2]')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Lettura e scrittura')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)

        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Mostra i prezzi al tecnico")]//div//label'))).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="nav-link bg-danger"]'))
        ).click()
        self.wait_loader()

        self.login(self.getConfig('tests.tecnico_user'), self.getConfig('tests.tecnico_password'))

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_for_dropdown_and_select('//span[@id="select2-id_anagrafica-container"]', option_text='Cliente')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_tipo_intervento-container"]', option_text='Generico')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[contains(@class, "btn-success") and contains(., "Aggiungi attività")]'))
        ).click()
        self.wait_loader()

        self.wait_for_dropdown_and_select('//span[@id="select2-id_articolo-container"]', option_text='Articolo 1')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//table//tbody//tr[td[contains(., "Articolo 1")]]')))

        self.wait_for_element_and_click('//a[@class="btn btn-danger ask"]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="nav-link bg-danger"]'))
        ).click()
        self.wait_loader()

        self.login(self.getConfig('login.username'), self.getConfig('login.password'))

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

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

        self.login(self.getConfig('tests.tecnico_user'), self.getConfig('tests.tecnico_password'))

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_for_dropdown_and_select('//span[@id="select2-id_anagrafica-container"]', option_text='Cliente')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_tipo_intervento-container"]', option_text='Generico')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[contains(@class, "btn-success") and contains(., "Aggiungi attività")]'))
        ).click()
        self.wait_loader()

        self.wait_for_dropdown_and_select('//span[@id="select2-id_articolo-container"]', option_text='Articolo 1')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//table//tbody//tr[td[contains(., "Articolo 1")]]')))

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="nav-link bg-danger"]'))
        ).click()
        self.wait_loader()

        self.login(self.getConfig('login.username'), self.getConfig('login.password'))

    def stampa_anteprima_firma(self):
        wait = self.wait_driver
        self.navigate_to_and_wait("Attività")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_for_dropdown_and_select('//span[@id="select2-id_anagrafica-container"]', option_text='Cliente')
        self.wait_for_dropdown_and_select('//span[@id="select2-id_tipo_intervento-container"]', option_text='Generico')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[contains(@class, "btn-success") and contains(., "Aggiungi attività")]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-primary "])[2]'))
        ).click()

        self.assertIn('TOTALE MANODOPERA', self.get_testo_stampa())

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[@class="close"]'))
        ).click()
        
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_for_dropdown_and_select('//span[@id="select2-setting79-container"]', option_text='Intervento (senza prezzi)')

        self.navigate_to_and_wait("Attività")

        self.click_first_table_row()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-primary "])[2]'))
        ).click()

        self.assertNotIn('TOTALE MANODOPERA', self.get_testo_stampa())
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[@class="close"]'))
        ).click()

        self.wait_for_element_and_click('//a[@class="btn btn-danger ask"]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-setting79-container"]',
            option_xpath='//li[contains(@class,"select2-results__option") and normalize-space(text())="Intervento"]'
        )


    def inserimento_sessioni_tecnici(self):
        wait = self.wait_driver  
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Permetti inserimento sessioni degli altri tecnici")]//div//label'))).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="nav-link bg-danger"]'))
        ).click()
        self.wait_loader()

        self.login(self.getConfig('tests.tecnico_user'), self.getConfig('tests.tecnico_password'))

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_for_element_and_click('//a[normalize-space(.)="Tecnici e sessioni"]')

        corrente = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_tecnico-container"]'))
        ).text
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_tecnico-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, f'//li[contains(@class,"select2-results__option") and not(contains(., "{corrente}"))]')))
        self.driver.switch_to.active_element.send_keys(Keys.ESCAPE)
        self.wait_for_element_and_click('//div[contains(@class,"modal") and contains(@class,"show")]//div[contains(@class,"modal-header")]//button')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="nav-link bg-danger"]'))
        ).click()
        self.wait_loader()

        self.login(self.getConfig('login.username'), self.getConfig('login.password'))

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Permetti inserimento sessioni degli altri tecnici")]//div//label'))
        ).click()

    def giorni_lavorativi(self):
        wait = self.wait_driver
        self.navigate_to_and_wait("Dashboard")

        wait.until(EC.invisibility_of_element_located((By.XPATH, '(//div[contains(@class,"fc-bg-event")])[3]')))
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Giorni lavorativi")]//span//li[contains(., "Venerdì")]//span'))
        ).click()

        self.navigate_to_and_wait("Dashboard")

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[contains(@class,"fc-bg-event")])[3]')))
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_for_dropdown_and_select('//ul[@id="select2-setting109-container"]', option_text='Venerdì')

    def notifica_tecnico_aggiunta_sessione(self):
        wait = self.wait_driver  
        self.navigate_to_and_wait("Anagrafiche")
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Tecnico", Keys.ENTER)
 
        self.wait_for_element_and_click('//tbody//td[2]//div[1]')

        self.input(None, 'Email').setValue(self.getConfig('tests.email_receiver'))
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()

        self.navigate_to_and_wait("Anagrafiche")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="deleteicon fa fa-times"]'))
        ).click()

        self.navigate_to_and_wait("Attività")
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_for_dropdown_and_select('//span[@id="select2-id_anagrafica-container"]', option_text='Cliente')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_tipo_intervento-container"]', option_text='Generico')

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

        self.wait_for_element_and_click('//a[normalize-space(.)="Tecnici e sessioni"]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtiposessione-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idtiposessione-results"]//li[1]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_tecnico-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id_tecnico-results"]//li[2]'))
        ).click()

        self.wait_for_element_and_click('//button[contains(@class, "btn-success") and contains(., "Aggiungi sessione")]')
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[contains(@class, "btn-success") and contains(., "Aggiungi attività")]'))
        ).click()  
        self.wait_loader()

        wait.until(EC.invisibility_of_element_located((By.XPATH, '(//div[@class="toast-message"])[2]')))
        self.wait_for_element_and_click('//a[@class="btn btn-danger ask"]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Notifica al tecnico l\'aggiunta della sessione nell\'attività")]//div//label'))
        ).click()
 
        self.navigate_to_and_wait("Attività")
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_for_dropdown_and_select('//span[@id="select2-id_anagrafica-container"]', option_text='Cliente')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_tipo_intervento-container"]', option_text='Generico')

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

        self.wait_for_element_and_click('//a[normalize-space(.)="Tecnici e sessioni"]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtiposessione-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idtiposessione-results"]//li[1]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_tecnico-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id_tecnico-results"]//li[2]'))
        ).click()

        self.wait_for_element_and_click('//button[contains(@class, "btn-success") and contains(., "Aggiungi sessione")]')
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[contains(@class, "btn-success") and contains(., "Aggiungi attività")]'))
        ).click()  
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@class="toast-message"])[2]')))
        self.wait_for_element_and_click('//a[@class="btn btn-danger ask"]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Notifica al tecnico l\'aggiunta della sessione nell\'attività")]//div//label'))
        ).click()

    def notifica_tecnico_rimozione_sessione(self):
        wait = self.wait_driver
        self.navigate_to_and_wait("Attività")
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_for_dropdown_and_select('//span[@id="select2-id_anagrafica-container"]', option_text='Cliente')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_tipo_intervento-container"]', option_text='Generico')
   
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

        self.wait_for_element_and_click('//a[normalize-space(.)="Tecnici e sessioni"]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtiposessione-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idtiposessione-results"]//li[1]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_tecnico-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id_tecnico-results"]//li[2]'))
        ).click()

        self.wait_for_element_and_click('//button[contains(@class, "btn-success") and contains(., "Aggiungi sessione")]')
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[contains(@class, "btn-success") and contains(., "Aggiungi attività")]'))
        ).click()
        self.wait_loader()

        self.wait_and_click_table_row(1, 2)
        self.wait_loader()

        self.wait_for_element_and_click('//table//tbody//tr//td//button[contains(@class, "btn-danger")]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()

        self.wait_for_element_and_click('//button[@id="save"]')
        self.wait_loader()

        self.navigate_to_and_wait("Attività")

        invio = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[14]'))
        ).text
        self.assertNotEqual(invio, 'Inviata via email')
        self.wait_loader()

        self.wait_and_click_table_row(1, 2) 
        self.wait_loader()

        self.wait_for_element_and_click('//a[@class="btn btn-danger ask"]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Notifica al tecnico la rimozione della sessione dall\'attività")]//div//label'))
        ).click()

        self.navigate_to_and_wait("Attività")
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_for_dropdown_and_select('//span[@id="select2-id_anagrafica-container"]', option_text='Cliente')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_tipo_intervento-container"]', option_text='Generico')

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
        self.wait_for_element_and_click('//a[normalize-space(.)="Tecnici e sessioni"]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtiposessione-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idtiposessione-results"]//li[1]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_tecnico-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id_tecnico-results"]//li[2]'))
        ).click()

        self.wait_for_element_and_click('//button[contains(@class, "btn-success") and contains(., "Aggiungi sessione")]')
 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[contains(@class, "btn-success") and contains(., "Aggiungi attività")]'))
        ).click()
        self.wait_loader()

        self.wait_and_click_table_row(1, 2)
        self.wait_loader()

        self.wait_for_element_and_click('//table//tbody//tr//td//button[contains(@class, "btn-danger")]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()

        self.wait_for_element_and_click('//button[@id="save"]')
        self.wait_loader()

        self.expandSidebar("Gestione email")
        self.navigate_to_and_wait("Coda di invio")

        messaggio = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[5]//div'))
        ).text 
        self.assertEqual(messaggio, "Notifica rimozione intervento")
        self.navigate_to_and_wait("Attività")

        self.wait_and_click_table_row(1, 2)

        self.wait_for_element_and_click('//a[@class="btn btn-danger ask"]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Notifica al tecnico la rimozione della sessione dall\'attività")]//div//label'))
        ).click()

    def stato_attivita_firma(self):
        wait = self.wait_driver
        self.db_execute("UPDATE in_stati_intervento SET is_bloccato = 1 WHERE name = %s AND deleted_at IS NULL", ('Stato di Attività di Prova',))

        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting123-container"]'))
        ).click()
        search = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[contains(@class,"select2-search")]//input')))
        search.send_keys('Stato di Attività di Prova')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-setting123-results"]//li[contains(., "Stato di Attività di Prova")]'))).click()

        self.navigate_to_and_wait("Attività")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_for_dropdown_and_select('//span[@id="select2-id_anagrafica-container"]', option_text='Cliente')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_tipo_intervento-container"]', option_text='Generico')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[contains(@class, "btn-success") and contains(., "Aggiungi attività")]'))
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

        self.navigate_to_and_wait("Attività")

        stato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[7]'))
        ).text
        self.assertEqual(stato, "Stato di Attività di Prova")   
        self.click_first_table_row()

        self.wait_for_element_and_click('//a[@class="btn btn-danger ask"]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting123-container"]'))
        ).click()
        search = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[contains(@class,"select2-search")]//input')))
        search.send_keys('Completato')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-setting123-results"]//li[contains(., "Completato")]'))).click()

    def alert_occupazione_tecnici(self):
        wait = self.wait_driver  
        self.navigate_to_and_wait("Attività")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_for_dropdown_and_select('//span[@id="select2-id_anagrafica-container"]', option_text='Cliente')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_tipo_intervento-container"]', option_text='Generico')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id-results"]//li[contains(., "Programmato")]'))).click()

        self.wait_for_element_and_click('//a[normalize-space(.)="Tecnici e sessioni"]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtiposessione-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idtiposessione-results"]//li[1]'))
        ).click()

        orario_inizio = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="orario_inizio"]'))
        )
        orario_inizio.clear()
        orario_inizio.send_keys("31/12/2026 09:00")    

        orario_fine = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="orario_fine"]'))
        )
        orario_fine.clear()
        orario_fine.send_keys("31/12/2026 10:00")    

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_tecnico-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id_tecnico-results"]//li[2]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[contains(@class, "btn-success") and contains(., "Aggiungi attività")]'))
        ).click() 
        self.wait_loader()

        self.navigate_to_and_wait("Attività")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_for_dropdown_and_select('//span[@id="select2-id_anagrafica-container"]', option_text='Cliente')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_tipo_intervento-container"]', option_text='Generico')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('prova')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id-results"]//li[contains(., "Programmato")]'))).click()

        self.wait_for_element_and_click('//a[normalize-space(.)="Tecnici e sessioni"]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtiposessione-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idtiposessione-results"]//li[1]'))
        ).click()

        orario_inizio = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="orario_inizio"]'))
        )
        orario_inizio.clear()
        orario_inizio.send_keys("31/12/2026 09:00")    

        orario_fine = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="orario_fine"]'))
        )
        orario_fine.clear()
        orario_fine.send_keys("31/12/2026 10:00")    
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_tecnico-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id_tecnico-results"]//li[2]'))
        ).click()

        scritta = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//h3[contains(@class, "card-title")][contains(text(), "conflitti")]'))
        ).text
        self.assertEqual(scritta.strip(), "⚠️ Sono presenti dei conflitti con le sessioni di lavoro di alcuni tecnici")
        self.wait_for_element_and_click('//div[contains(@class,"modal") and contains(@class,"show")]//div[contains(@class,"modal-header")]//button')

        self.expandSidebar("Strumenti")   
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Alert occupazione tecnici")]//div//label'))
        ).click()

        self.navigate_to_and_wait("Attività")

        self.click_first_table_row()

        wait.until(EC.invisibility_of_element_located((By.XPATH, '//h3[contains(@class, "card-title")][contains(text(), "conflitti")]')))
        self.wait_for_element_and_click('//a[@class="btn btn-danger ask"]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")   
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Alert occupazione tecnici")]//div//label'))
        ).click()

    def verifica_numero_intervento(self):
        wait = self.wait_driver

        # creo una nuova attività: il suo codice e' il successivo della numerazione
        self.navigate_to_and_wait("Attività")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_for_dropdown_and_select('//span[@id="select2-id_anagrafica-container"]', option_text='Cliente')
        self.wait_for_dropdown_and_select('//span[@id="select2-id_tipo_intervento-container"]', option_text='Generico')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[contains(@class, "btn-success") and contains(., "Aggiungi attività")]'))
        ).click()
        self.wait_loader()

        # elimino l'attività precedente per creare il buco di numerazione
        # che fa comparire l'alert di verifica
        id_nuova = self.driver.current_url.split('id_record=')[1].split('&')[0]
        precedenti = self.db_execute(
            "SELECT id FROM in_interventi WHERE id < %s ORDER BY id DESC LIMIT 1",
            (int(id_nuova),)
        )
        if precedenti:
            id_precedente = precedenti[0][0]
            self.db_execute("DELETE FROM in_righe_interventi WHERE id_intervento = %s", (id_precedente,))
            self.db_execute("DELETE FROM in_interventi_tecnici WHERE id_intervento = %s", (id_precedente,))
            self.db_execute("DELETE FROM in_interventi WHERE id = %s", (id_precedente,))

        self.navigate_to_and_wait("Attività")

        self.click_first_table_row()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="alert alert-warning alert-dismissable"]')))

        self.expandSidebar("Strumenti")   
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Verifica numero intervento")]//div//label'))
        ).click()

        self.navigate_to_and_wait("Attività")

        self.click_first_table_row()

        wait.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="alert alert-warning alert-dismissable"]')))

        self.wait_for_element_and_click('//a[@class="btn btn-danger ask"]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader() 

        self.expandSidebar("Strumenti")   
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Verifica numero intervento")]//div//label'))
        ).click()

    def formato_ore_stampa(self):
        wait = self.wait_driver
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        formato = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting142-container"]'))).text
        if 'Sessantesimi' not in formato:
            self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting142-container"]'))
            ).click()
            search = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[contains(@class,"select2-search")]//input')))
            search.send_keys('Sessantesimi')
            wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-setting142-results"]//li[contains(., "Sessantesimi")]'))).click()

        self.navigate_to_and_wait("Attività")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_for_dropdown_and_select('//span[@id="select2-id_anagrafica-container"]', option_text='Cliente')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_tipo_intervento-container"]', option_text='Generico')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')

        self.wait_for_element_and_click('//a[normalize-space(.)="Tecnici e sessioni"]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtiposessione-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idtiposessione-results"]//li[1]'))
        ).click()

        orario_inizio = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="orario_inizio"]'))
        )
        orario_inizio.clear()
        orario_inizio.send_keys(time.strftime('%d/%m/%Y') + ' 09:00')
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change', {bubbles: true}));", orario_inizio)

        orario_fine = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="orario_fine"]'))
        )
        orario_fine.clear()
        orario_fine.send_keys(time.strftime('%d/%m/%Y') + ' 10:00')
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change', {bubbles: true}));", orario_fine)
        time.sleep(1)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_tecnico-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id_tecnico-results"]//li[2]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[contains(@class, "btn-success") and contains(., "Aggiungi attività")]'))
        ).click()
        self.wait_loader()

        id_record = self.driver.current_url.split('id_record=')[-1]

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="print-button_p"]'))
        ).click()

        self.driver.switch_to.window(self.driver.window_handles[1])

        wait.until(lambda d: '1:00' in d.find_element(By.ID, 'viewer').text)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        formato = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting142-container"]'))).text
        if 'Decimale' not in formato:
            self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting142-container"]'))
            ).click()
            search = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[contains(@class,"select2-search")]//input')))
            search.send_keys('Decimale')
            wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-setting142-results"]//li[contains(., "Decimale")]'))).click()

        self.driver.get(self.getConfig('server') + '/editor.php?id_module=3&id_record=' + id_record)
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="print-button_p"]'))
        ).click()

        self.driver.switch_to.window(self.driver.window_handles[1])

        wait.until(lambda d: '1,00' in d.find_element(By.ID, 'viewer').text)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.wait_for_element_and_click('//a[@class="btn btn-danger ask"]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        formato = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting142-container"]'))).text
        if 'Sessantesimi' not in formato:
            self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting142-container"]'))
            ).click()
            search = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[contains(@class,"select2-search")]//input')))
            search.send_keys('Sessantesimi')
            wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-setting142-results"]//li[contains(., "Sessantesimi")]'))).click()

    def notifica_tecnico_assegnazione(self):
        wait = self.wait_driver
        self.navigate_to_and_wait("Attività")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_for_dropdown_and_select('//span[@id="select2-id_anagrafica-container"]', option_text='Cliente')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_tipo_intervento-container"]', option_text='Generico')

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

        self.wait_for_element_and_click('//a[normalize-space(.)="Tecnici e sessioni"]')

        ul = wait.until(EC.presence_of_element_located((By.XPATH, '//ul[@id="select2-tecnici_assegnati-container"]')))
        self.driver.execute_script("arguments[0].click();", ul)
        time.sleep(2)
        ta = wait.until(EC.presence_of_element_located((By.XPATH, '//ul[@id="select2-tecnici_assegnati-container"]/following-sibling::span[contains(@class,"select2-search--inline")]//textarea')))
        ta.send_keys('Tecnico')
        time.sleep(3)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-tecnici_assegnati-results"]//li[contains(., "Tecnico - 00000005")]'))).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[contains(@class, "btn-success") and contains(., "Aggiungi attività")]'))
        ).click()
        self.wait_loader()

        id_record = self.driver.current_url.split('id_record=')[-1]

        wait.until(EC.invisibility_of_element_located((By.XPATH, '(//div[@class="toast-message"])[2]')))

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Notifica al tecnico l\'assegnazione all\'attività")]//div//label'))
        ).click()

        self.driver.get(self.getConfig('server') + '/editor.php?id_module=3&id_record=' + id_record)
        self.wait_loader()

        # rimuove l'assegnazione
        self.wait_for_element_and_click('//ul[@id="select2-tecnici_assegnati-container"]//li[contains(@class,"select2-selection__choice")]//*[contains(@class,"choice__remove")]')

        self.wait_for_element_and_click('//button[@class="btn btn-success"]')
        self.wait_loader()

        # ri-assegna il tecnico
        ul = wait.until(EC.presence_of_element_located((By.XPATH, '//ul[@id="select2-tecnici_assegnati-container"]')))
        self.driver.execute_script("arguments[0].click();", ul)
        time.sleep(2)
        ta = wait.until(EC.presence_of_element_located((By.XPATH, '//ul[@id="select2-tecnici_assegnati-container"]/following-sibling::span[contains(@class,"select2-search--inline")]//textarea')))
        ta.send_keys('Tecnico')
        time.sleep(3)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-tecnici_assegnati-results"]//li[contains(., "Tecnico - 00000005")]'))).click()

        self.wait_for_element_and_click('//button[@class="btn btn-success"]')
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@class="toast-message"])[2]')))
        self.wait_for_element_and_click('//a[@class="btn btn-danger ask"]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Notifica al tecnico l\'assegnazione all\'attività")]//div//label'))
        ).click()

    def notifica_tecnico_rimozione_assegnazione(self):
        wait = self.wait_driver
        self.navigate_to_and_wait("Attività")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_for_dropdown_and_select('//span[@id="select2-id_anagrafica-container"]', option_text='Cliente')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_tipo_intervento-container"]', option_text='Generico')

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

        self.wait_for_element_and_click('//a[normalize-space(.)="Tecnici e sessioni"]')

        ul = wait.until(EC.presence_of_element_located((By.XPATH, '//ul[@id="select2-tecnici_assegnati-container"]')))
        self.driver.execute_script("arguments[0].click();", ul)
        time.sleep(2)
        ta = wait.until(EC.presence_of_element_located((By.XPATH, '//ul[@id="select2-tecnici_assegnati-container"]/following-sibling::span[contains(@class,"select2-search--inline")]//textarea')))
        ta.send_keys('Tecnico')
        time.sleep(3)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-tecnici_assegnati-results"]//li[contains(., "Tecnico - 00000005")]'))).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[contains(@class, "btn-success") and contains(., "Aggiungi attività")]'))
        ).click()
        self.wait_loader()

        id_record = self.driver.current_url.split('id_record=')[-1]

        # rimuove l'assegnazione (setting OFF: nessuna notifica)
        self.wait_for_element_and_click('//ul[@id="select2-tecnici_assegnati-container"]//li[contains(@class,"select2-selection__choice")]//*[contains(@class,"choice__remove")]')

        self.wait_for_element_and_click('//button[@class="btn btn-success"]')
        self.wait_loader()

        wait.until(EC.invisibility_of_element_located((By.XPATH, '(//div[@class="toast-message"])[2]')))

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Notifica al tecnico la rimozione dell\'assegnazione dall\'attività")]//div//label'))
        ).click()

        self.driver.get(self.getConfig('server') + '/editor.php?id_module=3&id_record=' + id_record)
        self.wait_loader()

        # assegna il tecnico
        ul = wait.until(EC.presence_of_element_located((By.XPATH, '//ul[@id="select2-tecnici_assegnati-container"]')))
        self.driver.execute_script("arguments[0].click();", ul)
        time.sleep(2)
        ta = wait.until(EC.presence_of_element_located((By.XPATH, '//ul[@id="select2-tecnici_assegnati-container"]/following-sibling::span[contains(@class,"select2-search--inline")]//textarea')))
        ta.send_keys('Tecnico')
        time.sleep(3)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-tecnici_assegnati-results"]//li[contains(., "Tecnico - 00000005")]'))).click()

        self.wait_for_element_and_click('//button[@class="btn btn-success"]')
        self.wait_loader()

        # rimuove l'assegnazione (setting ON: notifica)
        self.wait_for_element_and_click('//ul[@id="select2-tecnici_assegnati-container"]//li[contains(@class,"select2-selection__choice")]//*[contains(@class,"choice__remove")]')

        self.wait_for_element_and_click('//button[@class="btn btn-success"]')
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@class="toast-message"])[2]')))
        self.wait_for_element_and_click('//a[@class="btn btn-danger ask"]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Notifica al tecnico la rimozione dell\'assegnazione dall\'attività")]//div//label'))
        ).click()

    def descrizione_attivita(self):
        wait = self.wait_driver
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        textarea = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Descrizione personalizzata in fatturazione")]//textarea'))
        )
        textarea.clear()
        textarea.send_keys('Test')

        self.navigate_to_and_wait("Attività")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_for_dropdown_and_select('//span[@id="select2-id_anagrafica-container"]', option_text='Cliente')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_tipo_intervento-container"]', option_text='Generico')
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).send_keys("Test")   
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[contains(@class, "btn-success") and contains(., "Aggiungi attività")]'))
        ).click()
        self.wait_loader()

        id_record = self.driver.current_url.split('id_record=')[-1]
        numero = self.db_execute("SELECT codice FROM in_interventi WHERE id = %s", (id_record,))[0][0]

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Test") 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1") 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_stato-container"]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id_stato-results"]//li[contains(., "Completato")]'))).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="back"]'))
        ).click() 
        self.wait_loader()

        self.navigate_to_and_wait("Attività")

        self.search_by_th("th_Numero", numero)

        self.wait_for_element_and_click('//tbody//tr//td')

        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="create_invoice"]'
        )

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-raggruppamento-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")    
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-raggruppamento-results"]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")

        self.wait_and_click_table_row(1, 2)  
        self.wait_loader()

        descrizione = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[3]'))
        ).text  
        self.assertIn("Test", descrizione)

        # elimina la fattura intera
        self.wait_for_element_and_click('//a[@id="elimina"]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[contains(@class,"swal2-confirm")]'))
        ).click()
        self.wait_loader()

        self.driver.get(self.getConfig('server') + '/editor.php?id_module=3&id_record=' + id_record)
        self.wait_loader()

        self.wait_for_element_and_click('//a[@class="btn btn-danger ask"]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        textarea = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Descrizione personalizzata in fatturazione")]//textarea'))
        )
        textarea.clear()
        textarea.send_keys('Attività numero {numero} del {data}')
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change', {bubbles: true}));", textarea)
        
    def stato_predefinito_attivita_dashboard(self):
        wait = self.wait_driver  
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        stato_attuale = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting170-container"]'))).text
        if 'Stato di Attività di Prova' not in stato_attuale:
            self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Stato predefinito dell\'attività da Dashboard")]//div//span'))
            ).click()
            search = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[contains(@class,"select2-search")]//input')))
            search.send_keys('Stato di Attività di Prova')
            wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-setting170-results"]//li[contains(., "Stato di Attività di Prova")]'))).click()

        self.navigate_to_and_wait("Dashboard")

        actions = ActionChains(self.driver)
        actions.move_to_element(self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="calendar"]'))
        )).move_by_offset(300,100).click().perform()
        modal = self.wait_modal()

        self.wait_for_dropdown_and_select('//span[@id="select2-id_anagrafica-container"]', option_text='Cliente')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_tipo_intervento-container"]', option_text='Generico')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')

        self.wait_for_element_and_click('//a[normalize-space(.)="Tecnici e sessioni"]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_tecnico-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-id_tecnico-results"]//li[2]'))
        ).click()
        time.sleep(1)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[contains(@class, "btn-success") and contains(., "Aggiungi attività")]'))
        ).click()
        self.wait_loader()

        self.navigate_to_and_wait("Attività")

        stato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[7]'))
        ).text
        self.assertEqual(stato, "Stato di Attività di Prova")

        self.click_first_table_row()

        self.wait_for_element_and_click('//a[@class="btn btn-danger ask"]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader() 

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()
        stato_attuale = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting170-container"]'))).text
        if 'Programmato' not in stato_attuale:
            self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Stato predefinito dell\'attività da Dashboard")]//div//span'))
            ).click()
            search = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[contains(@class,"select2-search")]//input')))
            search.send_keys('Programmato')
            wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-setting170-results"]//li[contains(., "Programmato")]'))).click()

    def stato_predefinito_attivita(self):
        wait = self.wait_driver
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        stato_attuale = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting171-container"]'))).text
        if 'Stato di Attività di Prova' not in stato_attuale:
            self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting171-container"]'))
            ).click()
            search = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[contains(@class,"select2-search")]//input')))
            search.send_keys('Stato di Attività di Prova')
            wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-setting171-results"]//li[contains(., "Stato di Attività di Prova")]'))).click()

        self.navigate_to_and_wait("Attività")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_for_dropdown_and_select('//span[@id="select2-id_anagrafica-container"]', option_text='Cliente')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_tipo_intervento-container"]', option_text='Generico')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="cke_1_contents"]//iframe'))).send_keys('test')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[contains(@class, "btn-success") and contains(., "Aggiungi attività")]'))
        ).click()
        self.wait_loader()

        self.navigate_to_and_wait("Attività")

        stato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[7]'))
        ).text
        self.assertEqual(stato, "Stato di Attività di Prova")

        self.click_first_table_row()

        self.wait_for_element_and_click('//a[@class="btn btn-danger ask"]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Attività"]'))
        ).click()

        stato_attuale = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting171-container"]'))).text
        if 'Da programmare' not in stato_attuale:
            self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-setting171-container"]'))
            ).click()
            search = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[contains(@class,"select2-search")]//input')))
            search.send_keys('Da programmare')
            wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-setting171-results"]//li[contains(., "Da programmare")]'))).click()
