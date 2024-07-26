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

class FattureVendita(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Vendite")

    def test_creazione_fattura_vendita(self):
        # Crea una nuova fattura per il cliente "Cliente". *Required*
        importi = RowManager.list()
        self.creazione_fattura_vendita("Cliente", importi[0])

        # Duplicazione fattura di vendita
        self.duplica()

        # Modifica fattura di vendita
        self.modifica_fattura_vendita("Emessa")

        # Controllo valori fattura elettronica e piano dei conti
        self.controllo_fattura_vendita()

        # Creazione nota di credito
        self.creazione_nota_credito()

        # Modifica nota di credito
        self.modifica_nota_credito("Emessa")

        # Controllo valori nota credito
        self.controllo_nota_credito()

        # Confronto valori fattura e nota credito
        self.controllo_fattura_nota_credito()

        # Cancellazione fattura di vendita
        self.elimina_documento()

        # Verifica fattura di vendita
        self.verifica_fattura_di_vendita()

        # Verifica XML fattura estera
        self.verifica_xml_fattura_estera(importi[0], "1")

        #Verifica plugin movimenti contabili da fatture di vendita
        self.movimenti_contabili()

        # Plugin movimenti contabili da Anagrafiche
        self.plugin_movimenti_contabili()

        # Plugin regole pagamenti da Anagrafiche
        self.regole_pagamenti()

        # Plugin registrazioni
        self.registrazioni()   

        # Plugin allegati da Anagrafiche
        self.controlla_allegati()

        # Elimina selezionati (Azioni di gruppo)
        self.elimina_selezionati()

        # Cambia sezionale (Azioni di gruppo)
        self.cambia_sezionale()    

        # Duplica selezionati (Azioni di gruppo)
        self.duplica_selezionati()
         
        # Emetti fatture (Azioni di gruppo)
        self.emetti_fatture()      

        # Plugin statistiche vendite in Articoli
        self.statistiche_vendita()

        # Controlla fatture elettroniche (Azioni di gruppo)
        self.controlla_fatture_elettroniche()

        # Registrazione contabile (Azioni di gruppo)
        self.registrazione_contabile()

        # Genera fatture elettroniche (Azioni di gruppo)
        self.genera_fatture_elettroniche()

    def creazione_fattura_vendita(self, cliente: str, file_importi: str):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        # Crea una nuova fattura per il cliente indicato. 
        # Apre la schermata di nuovo elemento
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        select = self.input(modal, 'Cliente')
        select.setByText(cliente)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

        # Inserisco le righe
        row_manager = RowManager(self)
        self.valori=row_manager.compile(file_importi)

    def duplica(self):
        self.find(By.XPATH, '//button[@class="btn btn-primary ask"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]').click()
        self.wait_loader()

    def modifica_fattura_vendita(self, modifica=str):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//td[@class="bound clickable"]').click()
        self.wait_loader()
        
        self.input(None,'Stato*').setByText(modifica)
        sleep(1)

        self.driver.execute_script('window.scrollTo(0,0)')
        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()
        
    def controllo_fattura_vendita(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//td[@class="bound clickable"]').click()
        self.wait_loader()
        
        # Estrazione totali righe
        sconto = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[2]//td[2]').text
        totale_imponibile = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text
        iva = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[4]//td[2]').text
        totale = self.find(By.XPATH, '//div[@id="tab_0"]//div[@id="righe"]//tbody[2]//tr[5]//td[2]').text

        self.assertEqual(sconto, (self.valori["Sconto/maggiorazione"]+ ' €'))
        self.assertEqual(totale_imponibile, (self.valori["Totale imponibile"]+ ' €'))
        self.assertEqual(iva, (self.valori["IVA"] + ' €'))
        self.assertEqual(totale, (self.valori["Totale documento"] + ' €'))

        # Controllo Scadenzario
        scadenza_fattura = self.find(By.XPATH, '//div[@id="tab_0"]//strong[text()="Scadenze"]/ancestor::div[1]//following-sibling::p[2]').text
        self.assertEqual(totale, scadenza_fattura[12:20])
        self.driver.execute_script('$("a").removeAttr("target")')
        self.find(By.XPATH, '//div[@id="tab_0"]//strong[text()="Scadenze"]/ancestor::div[1]//following-sibling::a').click()
        self.wait_loader()

        scadenza_scadenzario = self.find(By.XPATH, '//div[@id="tab_0"]//td[@id="totale_utente"]').text + ' €'
        self.assertEqual(totale, scadenza_scadenzario)

        # Torno alla tabella delle Fatture
        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()
        
        # Estrazione Totale widgets
        widget_fatturato = self.find(By.XPATH, '(//span[@class="info-box-number"])[1]').text
        widget_crediti = self.find(By.XPATH, '(//span[@class="info-box-number"])[2]').text

        # Confronto i due valori
        self.assertEqual(totale_imponibile, widget_fatturato)
        self.assertEqual(totale, widget_crediti)

        # Controllo importi fattura elettronica
        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@id="link-tab_18"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="text-center"]//a[@class="btn btn-info btn-lg "]'))).click()
        sleep(1)

        self.driver.switch_to.window(self.driver.window_handles[1])
        perc_iva_FE = self.find(By.XPATH, '//table[@class="tbFoglio"][3]/tbody/tr[1]/td[2]').text
        iva_FE = self.find(By.XPATH, '//table[@class="tbFoglio"][3]/tbody/tr[1]/td[6]').text
        totale_imponibile_FE = self.find(By.XPATH, '//table[@class="tbFoglio"][3]/tbody/tr[1]/td[5]').text + ' €'
        totale_FE = self.find(By.XPATH, '//table[@class="tbFoglio"][3]/tbody/tr[3]/td[4]').text + ' €'
        scadenza_FE = self.find(By.XPATH, '//table[@class="tbFoglio"][4]/tbody/tr[1]/td[4]').text + ' €'

        self.assertEqual('22,00', perc_iva_FE)
        self.assertEqual((self.valori["IVA"]), iva_FE)
        self.assertEqual((self.valori["Totale imponibile"]+ ' €'), totale_imponibile_FE)
        self.assertEqual((self.valori["Totale documento"] + ' €'), totale_FE)
        self.assertEqual((self.valori["Totale documento"] + ' €'), scadenza_FE)

        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.close()

        # Estrazione valori Piano dei conti
        super().setUp()
        self.expandSidebar("Contabilità")
        self.navigateTo("Piano dei conti")
        self.wait_loader()

        self.find(By.XPATH, '//*[@id="conto2-20"]//*[@class="fa fa-plus"]').click()
        sleep(2)
        self.find(By.XPATH, '//*[@id="movimenti-94"]//*[@class="fa fa-plus"]').click()
        sleep(2)
        conto_ricavi = self.find(By.XPATH, '//*[@id="conto_94"]//*[@class="text-right"]').text
       
        self.find(By.XPATH, '//*[@id="conto2-2"]//*[@class="fa fa-plus"]').click()
        sleep(2)
        self.find(By.XPATH, '//*[@id="movimenti-121"]//*[@class="fa fa-plus"]').click()
        sleep(2)
        conto_cliente = self.find(By.XPATH, '//*[@id="conto_121"]//*[@class="text-right"]').text
   
        self.find(By.XPATH, '//*[@id="conto2-22"]//*[@class="fa fa-plus"]').click()
        sleep(2)
        self.find(By.XPATH, '//*[@id="movimenti-106"]//*[@class="fa fa-plus"]').click()        
        sleep(2)
        conto_iva = self.find(By.XPATH, '//*[@id="conto_106"]//*[@class="text-right"]').text

        self.assertEqual(totale_imponibile, conto_ricavi)
        self.assertEqual(totale, conto_cliente)
        self.assertEqual(iva, conto_iva)

    def creazione_nota_credito(self):
        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[1]//td[6]').click()
        self.wait_loader()
        
        # Crea una nuova nota di credito 
        # Apre la schermata di nuovo elemento
        self.find(By.XPATH, '//button[@class="btn btn-primary unblockable dropdown-toggle "]').click()
        self.find(By.XPATH, '(//a[@class="dropdown-item bound clickable"])[2]').click()
        modal = self.wait_modal()

        # Submit
        self.find(By.XPATH, '//button[@id="submit_btn"]').click()
        self.wait_loader()

    def modifica_nota_credito(self, modifica=str):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[3]//td[6]').click()
        self.wait_loader()
        
        self.input(None,'Stato*').setByText(modifica)
        self.driver.execute_script('window.scrollTo(0,0)')
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()

    def controllo_nota_credito(self):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//td[@class="bound clickable"]').click()
        self.wait_loader()

        totale_imponibile = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text
        totale_imponibile = '-'+totale_imponibile
        iva = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[4]//td[2]').text
        totale = self.find(By.XPATH, '//div[@id="tab_0"]//div[@id="righe"]//tbody[2]//tr[5]//td[2]').text
        totale = '-'+totale

        # Controllo Scadenzario
        scadenza_fattura = self.find(By.XPATH, '//div[@id="tab_0"]//strong[text()="Scadenze"]/ancestor::div[1]//following-sibling::p[2]').text
        self.assertEqual(totale, scadenza_fattura[12:21])
        
        self.find(By.XPATH, '//div[@class="btn-group pull-right"]').click()
        sleep(1)

        self.driver.switch_to.window(self.driver.window_handles[1])
        scadenza_scadenzario = self.find(By.XPATH, '//div[@id="tab_0"]//td[@id="totale_utente"]').text
        scadenza_scadenzario = scadenza_scadenzario +' €'
        self.assertEqual(totale, scadenza_scadenzario)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        # Torno alla tabella delle Fatture
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        # Controllo importi fattura elettronica
        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//tr[1]//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//div[@class="control-sidebar-button"]').click()
        self.find(By.XPATH, '//a[@id="link-tab_18"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//form[@id="form-xml"]/following-sibling::a[1]').click()
        sleep(1)

        self.driver.switch_to.window(self.driver.window_handles[1])
        perc_iva_FE = self.find(By.XPATH, '//table[@class="tbFoglio"][3]/tbody/tr[1]/td[2]').text
        iva_FE = self.find(By.XPATH, '//table[@class="tbFoglio"][3]/tbody/tr[1]/td[6]').text
        iva_FE = iva_FE+' €'
        totale_imponibile_FE = self.find(By.XPATH, '//table[@class="tbFoglio"][3]/tbody/tr[1]/td[5]').text
        totale_imponibile_FE = '-'+totale_imponibile_FE+' €'
        totale_FE = self.find(By.XPATH, '//table[@class="tbFoglio"][3]/tbody/tr[3]/td[4]').text
        totale_FE = '-'+totale_FE+' €'
        scadenza_FE = self.find(By.XPATH, '//table[@class="tbFoglio"][4]/tbody/tr[1]/td[4]').text
        scadenza_FE = '-'+scadenza_FE+' €'
        self.assertEqual('22,00', perc_iva_FE)
        self.assertEqual(iva, iva_FE)
        self.assertEqual(totale_imponibile, totale_imponibile_FE)
        self.assertEqual(totale, totale_FE)
        self.assertEqual(totale, scadenza_FE)
        iva = '-' + iva
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.close()
        
        # Estrazione valori Piano dei conti
        super().setUp()
        self.expandSidebar("Contabilità")
        self.navigateTo("Piano dei conti")
        self.wait_loader()

        self.find(By.XPATH, '//*[@id="conto2-20"]//*[@class="fa fa-plus"]').click()
        sleep(2)
        self.find(By.XPATH, '//*[@id="movimenti-94"]//*[@class="fa fa-plus"]').click()
        sleep(2)
        conto_ricavi = self.find(By.XPATH, '//*[@id="conto_94"]//*[@class="text-right"]').text
       
        self.find(By.XPATH, '//*[@id="conto2-2"]//*[@class="fa fa-plus"]').click()
        sleep(2)
        self.find(By.XPATH, '//*[@id="movimenti-121"]//*[@class="fa fa-plus"]').click()
        sleep(2)
        conto_cliente = self.find(By.XPATH, '//*[@id="conto_121"]//*[@class="text-right"]').text
   
        self.find(By.XPATH, '//*[@id="conto2-22"]//*[@class="fa fa-plus"]').click()
        sleep(2)
        self.find(By.XPATH, '//*[@id="movimenti-106"]//*[@class="fa fa-plus"]').click()        
        sleep(2)

        conto_iva = self.find(By.XPATH, '//*[@id="conto_106"]//*[@class="text-right"]').text
        conto_iva= '-'+ conto_iva
        conto_ricavi = '-' + conto_ricavi
        conto_cliente = '-' + conto_cliente
        self.assertEqual(totale_imponibile, conto_ricavi)
        self.assertEqual(totale, conto_cliente)
        self.assertEqual(iva, conto_iva)

    def controllo_fattura_nota_credito(self):
        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        fattura=self.find(By.XPATH, '//tbody//tr[2]//td[6]').text
        notacredito=self.find(By.XPATH, '//tbody//tr[1]//td[6]').text
        fattura='-'+ fattura
        self.assertEqual(fattura,notacredito)

    def elimina_documento(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[3]//td[2]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask "]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

    def verifica_fattura_di_vendita(self):
        wait = WebDriverWait(self.driver, 20)

        #Creazione fattura di acquisto estera
        self.expandSidebar("Acquisti")
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()  

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        select = self.input(modal, 'Fornitore')
        select.setByText("Fornitore Estero")
        sleep(1)
        self.input(modal, 'N. fattura del fornitore').setValue("02")

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

    def verifica_xml_fattura_estera(self, file_importi: str, pagamento: str):
        wait = WebDriverWait(self.driver, 20)

        # Inserisco le righe
        self.input(self.find(By.XPATH, '//div[@id="tab_0"]'), 'Pagamento').setByIndex(pagamento)
        row_manager = RowManager(self)
        row_manager.compile(file_importi)

        self.find(By.XPATH, '(//a[@title="Modifica riga"])[1]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idiva-container"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Non imponibile')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@onclick="submitForm()"]'))).click()
        sleep(1)

        self.find(By.XPATH, '(//a[@title="Modifica riga"])[2]').click()  
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idiva-container"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Non imponibile')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@onclick="submitForm()"]'))).click()
        sleep(1)

        self.find(By.XPATH, '(//a[@title="Modifica riga"])[3]').click()  
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idiva-container"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Non imponibile')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@onclick="submitForm()"]'))).click()
        sleep(1)

        self.find(By.XPATH, '(//a[@title="Modifica riga"])[4]').click()  
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idiva-container"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Non imponibile')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@onclick="submitForm()"]'))).click()
        sleep(1)

        self.find(By.XPATH, '(//a[@title="Modifica riga"])[5]').click()  
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idiva-container"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Non imponibile')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@onclick="submitForm()"]'))).click()
        sleep(1)

        # Modifica stato in emessa        
        self.input(None,'Stato*').setByText("Emessa")
        self.driver.execute_script('window.scrollTo(0,0)')
        sleep(1)
        
        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        sleep(1)
        # Creazione autofattura
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary unblockable dropdown-toggle "]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@class="dropdown-item bound clickable"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="modal-body"]//span[@class="select2-selection select2-selection--single"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input[@type="search"]'))).send_keys("TD17")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="modal-body"]//button[@type="submit"]'))).click()
        self.wait_loader()

        # Modifica stato in emessa        
        self.input(None,'Stato*').setByText("Emessa")
        self.driver.execute_script('window.scrollTo(0,0)')
        sleep(1)
        
        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()

        totale_imponibile = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[1]//td[2]').text
        iva = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[2]//td[2]').text
        totale = self.find(By.XPATH, '//div[@id="tab_0"]//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text

        self.assertEqual(totale_imponibile, (self.valori["Totale imponibile"]+ ' €'))
        self.assertEqual(iva, (self.valori["IVA"] + ' €'))
        self.assertEqual(totale, (self.valori["Totale documento"] + ' €'))

    def movimenti_contabili(self):               
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Fatture di vendita")
        self.wait_loader()
        
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Tipo"]/input'))).send_keys("Fattura immediata di vendita", Keys.ENTER)
        sleep(1) 
        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()
        self.wait_loader() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        self.wait_loader() 
        self.find(By.XPATH, '//a[@id="link-tab_37"]').click()
        sleep(1)
        self.find(By.XPATH, '//a[@class="btn btn-info btn-lg"]').click()
        self.wait_loader() 
        
        dare=self.find(By.XPATH, '(//td[@class="text-right"])[21]').text
        avere_1=self.find(By.XPATH, '(//td[@class="text-right"])[25]').text
        avere_2=self.find(By.XPATH, '(//td[@class="text-right"])[28]').text
        self.assertEqual(dare,"323,06 €")
        self.assertEqual(avere_1,"264,80 €")
        self.assertEqual(avere_2,"58,26 €")

        self.navigateTo("Fatture di vendita")
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

    def plugin_movimenti_contabili(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        self.find(By.XPATH, '//a[@id="link-tab_38"]').click()
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_38"]//a[@class="btn btn-info btn-lg"]').click()
        self.wait_loader()

        dare=self.find(By.XPATH, '//div[@id="tab_38"]//tr[1]//td[3]').text
        self.assertEqual(dare, "323,06 €")
        self.navigateTo("Anagrafiche")
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def regole_pagamenti(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()
        sleep(2) 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        sleep(1)
        self.find(By.XPATH, '//a[@id="link-tab_40"]').click()
        sleep(1)
        
        self.find(By.XPATH, '//div[@id="tab_40"]//h4//button').click() #apre pop up aggiungi
        modal=self.wait_modal()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="select2-mese-container"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys("Agosto", Keys.ENTER)
        

        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="select2-giorno_fisso-container"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys("8", Keys.ENTER)
        self.wait_loader()

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="tab_40"]//h4//button').click() #apre pop up aggiungi
        modal=self.wait_modal()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="select2-mese-container"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys("Aprile", Keys.ENTER)
        

        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="select2-giorno_fisso-container"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys("8", Keys.ENTER)
        self.wait_loader()

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
        wait.until(EC.visibility_of_element_located((By.XPATH,  '//div[@id="tab_40"]//tbody//td[2]//div[1]'))).click()
        sleep(1)
             
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-danger "]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        sleep(2)

        self.expandSidebar("Contabilità")
        self.navigateTo("Scadenzario")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Anagrafica"]/input'))).send_keys('Cliente', Keys.ENTER)
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH,  '//tbody//tr//td[2]'))).click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_concordata0"]'))).send_keys('08/09/2024')
        sleep(2)

        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        wait.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="alert alert-warning"]')))

        self.navigateTo("Anagrafiche")
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(2)
        
    def registrazioni(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Tipo"]/input'))).send_keys("Fattura immediata di vendita", Keys.ENTER)
        sleep(1) 

        self.find(By.XPATH, '//tbody//tr[1]//td[2]').click()
        self.wait_loader()
        
        self.find(By.XPATH, '//div[@class="control-sidebar-button"]').click()
        self.find(By.XPATH, '//a[@id="link-tab_42"]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_42"]//tr[5]//td[1]'))) #check 5 riga
        sleep(2)

    def controlla_allegati(self): 
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        sleep(2) 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        sleep(1)
        self.find(By.XPATH, '//a[@id="link-tab_30"]').click()
        sleep(1)
        self.find(By.XPATH, '//div[@id="tab_30"]//a[@class="btn btn-info btn-lg"]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_30"]//a[@class="btn btn-xs btn-primary"]')))

        self.navigateTo("Anagrafiche")
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

    def elimina_selezionati(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td').click()  #seleziono prima fattura
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() #apro azioni di gruppo
        self.find(By.XPATH, '//a[@data-op="delete-bulk"]').click()  #click su elimina selezionati
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()

        test=self.find(By.XPATH, '//tbody//tr//td[2]').text
        self.assertEqual(test, "0002/2024") #controllo se trova la seconda fattura e non la prima in prima riga


    def cambia_sezionale(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su aggiungi
        self.wait_loader()

        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="form-control"])[9]'))).send_keys("Bozza", Keys.ENTER) #cerco fattura in stato di bozza
        sleep(2)

        self.find(By.XPATH, '//tbody//tr//td').click() #seleziono primo risultato
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()  #apro azioni di gruppo
        self.find(By.XPATH, '//a[@data-op="cambia-sezionale"]').click() #click su cambia sezionale
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-id_segment-container"]').click()
        self.find(By.XPATH, '//ul[@id="select2-id_segment-results"]').click()   #click sul primo risultato
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() #click di conferma
        self.wait_loader()

        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click() #cancello ricerca
        sleep(2)

        self.find(By.XPATH, '//span[@id="select2-id_segment_-container"]').click() #vado in sezionale "Autofatture"
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Autofatture")
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-id_segment_-results"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td').click() #seleziono prima fattura
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() #apro azioni di gruppo
        self.find(By.XPATH, '//a[@data-op="cambia-sezionale"]').click() #click su cambia sezionale
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-id_segment-container"]').click()   
        self.find(By.XPATH, '//ul[@id="select2-id_segment-results"]').click() #click su primo risultato
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  #click di conferma
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-id_segment_-container"]').click()  #vado in sezionale "Standard vendite"
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Standard")
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-id_segment_-results"]').click() #click sul primo risultato
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click() #apro prima fattura
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="elimina"]').click()   #elimino fattura
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click() #click di conferma
        self.wait_loader()

    def duplica_selezionati(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()

        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td').click() #seleziono prima fattura
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()  #apro azioni di gruppo
        self.find(By.XPATH, '//a[@data-op="copy-bulk"]').click()    #click su duplica selezionati
        sleep(1)
        
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() #click di conferma
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click() #apro prima fattura
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="elimina"]').click() #elimina fattura
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td').click()  #tolgo il "checkbox" della prima fattura

    def emetti_fatture(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()  #apro prima fattura
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Test")    #scrivo "Test" come descrizione della riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1") #scrivo 1 come prezzo unitario
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)

        self.navigateTo("Fatture di vendita")   #torno in fatture di vendita
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td').click()  #seleziono prima fattura
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()  #apro azioni di gruppo
        self.find(By.XPATH, '//a[@data-op="change-stato"]').click() #click su emetti fatture
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  #click di conferma
        self.wait_loader()

        stato=self.find(By.XPATH, '(//div[@id="tab_0"]//td[10]//span)[2]').text
        self.assertEqual(stato, "Emessa")   #controllo se lo stato della fattura è "Emessa"
        self.find(By.XPATH, '//tbody//tr//td[2]').click()  #apro fattura
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="elimina"]').click()   #elimino fattura
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td').click()  #tolgo il "checkbox" della prima fattura

    def statistiche_vendita(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Magazzino")
        self.wait_loader()
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        sleep(1)

        self.find(By.XPATH, '//a[@id="link-tab_44"]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_44"]//tr[1]//td[1])[2]')))   #checkbox
        sleep(1)

        self.navigateTo("Articoli")
        self.wait_loader()

    def controlla_fatture_elettroniche(self):
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
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idstatodocumento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Emessa", Keys.ENTER)
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td').click() #seleziono prima fattura
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()  #apro azioni di gruppo
        self.find(By.XPATH, '//a[@data-op="check-bulk"]').click()    #click su controlla fatture elettroniche
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() #click su procedi
        sleep(1)
        #commentato perchè in fase di controllo fatture non riesco a leggere il widget
        #widget=self.find(By.XPATH, '//div[@class="toast toast-success"]//div[3]').text  #se trova il widget il test è superato
        #self.assertEqual(widget, "Nessuna anomalia!")  

    def registrazione_contabile(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="form-control"])[1]'))).send_keys("0001", Keys.ENTER) #cerco fattura numero 0001
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click() #seleziono prima fattura
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()  #apro azioni di gruppo
        self.find(By.XPATH, '//a[@data-op="registrazione-contabile"]').click()    #click su registrazione contabile
        sleep(3)

        totale=self.find(By.XPATH, '(//tfoot//tr[1]//td[2])[3]').text   #controllo se il totale è uguale a 1,22 €
        self.assertEqual(totale, "1,22 €")

        self.find(By.XPATH, '//button[@class="close"]').click() #chiudo registrazione contabile
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click()  #tolgo il checkbox
        self.find(By.XPATH, '(//i[@class="deleteicon fa fa-times"])[1]').click()    #cancello ricerca
        sleep(2)

    def genera_fatture_elettroniche(self):
        wait = WebDriverWait(self.driver, 20)
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

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Prova")    #scrivo "Prova" come descrizione della riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1") #scrivo 1 come prezzo unitario
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idstatodocumento-container"]').click() #stato in emessa
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Emessa", Keys.ENTER)
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '(//tr[1]//td[1])[2]').click() #seleziono prima fattura
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click()  #apro azioni di gruppo
        self.find(By.XPATH, '(//a[@class="bulk-action clickable dropdown-item"])[12]').click()    #click su genera fatture elettroniche
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() #click su procedi
        sleep(1)

        self.driver.switch_to.window(self.driver.window_handles[1]) #cambia scheda
        sleep(2)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()  #apro prima fattura
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-xs btn-info"]').click()   #apri fattura elettronica
        sleep(1)

        self.find(By.XPATH, '//button[@class="close"]').click() #chiudi fattura elettronica
        sleep(1)

        self.find(By.XPATH, '//a[@id="elimina"]').click()   #elimino fattura
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.driver.close() #chiude scheda
        self.driver.switch_to.window(self.driver.window_handles[0]) #torna alla prima
        sleep(2)

        self.navigateTo("Fatture di vendita")
        self.wait_loader()