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

        # Verifica plugin movimenti contabili da fatture di vendita
        self.movimenti_contabili()

        # Plugin movimenti contabili da Anagrafiche
        self.plugin_movimenti_contabili()

        # Plugin regole pagamenti da Anagrafiche
        self.regole_pagamenti()

        # Plugin registrazioni
        self.registrazioni()   

        # Plugin allegati da Anagrafiche
        self.controlla_allegati()

        # Duplica selezionati (Azioni di gruppo)
        self.duplica_selezionati()
         
        # Cambia sezionale (Azioni di gruppo)
        self.cambia_sezionale()    

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

        # Elimina selezionati (Azioni di gruppo)
        self.elimina_selezionati()

    def creazione_fattura_vendita(self, cliente: str, file_importi: str):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        # Crea una nuova fattura
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        select = self.input(modal, 'Cliente')
        select.setByText(cliente)
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

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

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
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

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
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
        sleep(1)
        self.find(By.XPATH, '//*[@id="movimenti-94"]//*[@class="fa fa-plus"]').click()
        sleep(1)
        conto_ricavi = self.find(By.XPATH, '//*[@id="conto_94"]//*[@class="text-right"]').text
       
        self.find(By.XPATH, '//*[@id="conto2-2"]//*[@class="fa fa-plus"]').click()
        sleep(1)
        self.find(By.XPATH, '//*[@id="movimenti-121"]//*[@class="fa fa-plus"]').click()
        sleep(1)
        conto_cliente = self.find(By.XPATH, '//*[@id="conto_121"]//*[@class="text-right"]').text
   
        self.find(By.XPATH, '//*[@id="conto2-22"]//*[@class="fa fa-plus"]').click()
        sleep(1)
        self.find(By.XPATH, '//*[@id="movimenti-106"]//*[@class="fa fa-plus"]').click()        
        sleep(1)
        conto_iva = self.find(By.XPATH, '//*[@id="conto_106"]//*[@class="text-right"]').text

        self.assertEqual(totale_imponibile, conto_ricavi)
        self.assertEqual(totale, conto_cliente)
        self.assertEqual(iva, conto_iva)

        self.expandSidebar("Vendite")

    def creazione_nota_credito(self):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()
        
        self.find(By.XPATH, '//button[@class="btn btn-primary unblockable dropdown-toggle "]').click()
        self.find(By.XPATH, '//a[@class="btn dropdown-item bound clickable"]').click()
        modal = self.wait_modal()

        self.find(By.XPATH, '//button[@id="submit_btn"]').click()
        self.wait_loader()

    def modifica_nota_credito(self, modifica=str):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[3]//td[2]').click()
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

        # Controllo Scadenzario
        scadenza_fattura = self.find(By.XPATH, '//div[@id="tab_0"]//strong[text()="Scadenze"]/ancestor::div[1]//following-sibling::p[2]').text
        self.assertEqual(totale, scadenza_fattura[12:21])
        self.find(By.XPATH, '//div[@class="btn-group pull-right"]').click()
        sleep(1)

        totale = '-'+totale
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
        sleep(1)
        self.find(By.XPATH, '//*[@id="movimenti-94"]//*[@class="fa fa-plus"]').click()
        sleep(1)
        conto_ricavi = self.find(By.XPATH, '//*[@id="conto_94"]//*[@class="text-right"]').text
       
        self.find(By.XPATH, '//*[@id="conto2-2"]//*[@class="fa fa-plus"]').click()
        sleep(1)
        self.find(By.XPATH, '//*[@id="movimenti-121"]//*[@class="fa fa-plus"]').click()
        sleep(1)
        conto_cliente = self.find(By.XPATH, '//*[@id="conto_121"]//*[@class="text-right"]').text
   
        self.find(By.XPATH, '//*[@id="conto2-22"]//*[@class="fa fa-plus"]').click()
        sleep(1)
        self.find(By.XPATH, '//*[@id="movimenti-106"]//*[@class="fa fa-plus"]').click()        
        sleep(1)

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

        wait.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="toast-message"]')))
        self.find(By.XPATH, '(//a[@title="Modifica riga"])[1]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idiva-container"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Non imponibile')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@onclick="submitForm()"]'))).click()
        sleep(1)

        wait.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="toast-message"]')))
        self.find(By.XPATH, '(//a[@title="Modifica riga"])[2]').click()  
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idiva-container"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Non imponibile')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@onclick="submitForm()"]'))).click()
        sleep(1)

        wait.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="toast-message"]')))
        self.find(By.XPATH, '(//a[@title="Modifica riga"])[3]').click()  
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idiva-container"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Non imponibile')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@onclick="submitForm()"]'))).click()
        sleep(1)

        wait.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="toast-message"]')))
        self.find(By.XPATH, '(//a[@title="Modifica riga"])[4]').click()  
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idiva-container"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Non imponibile')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@onclick="submitForm()"]'))).click()
        sleep(1)

        wait.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="toast-message"]')))
        self.find(By.XPATH, '(//a[@title="Modifica riga"])[5]').click()  
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idiva-container"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Non imponibile')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@onclick="submitForm()"]'))).click()
        sleep(1)

        self.input(None,'Stato*').setByText("Emessa")
        self.driver.execute_script('window.scrollTo(0,0)')
        sleep(1)
        
        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        sleep(1)

        # Creazione autofattura
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary unblockable dropdown-toggle "]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@class="btn dropdown-item bound clickable"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="modal-body"]//span[@class="select2-selection select2-selection--single"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input[@type="search"]'))).send_keys("TD17")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="modal-body"]//button[@type="submit"]'))).click()
        self.wait_loader()
    
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

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader() 

        self.find(By.XPATH, '//a[@id="link-tab_37"]').click()
        self.find(By.XPATH, '//a[@class="btn btn-info btn-lg"]').click()
        self.wait_loader() 
        
        # Verifica movimenti contabili
        dare=self.find(By.XPATH, '(//td[@class="text-right"])[21]').text
        avere_1=self.find(By.XPATH, '(//td[@class="text-right"])[25]').text
        avere_2=self.find(By.XPATH, '(//td[@class="text-right"])[28]').text
        self.assertEqual(dare,"323,06 €")
        self.assertEqual(avere_1,"264,80 €")
        self.assertEqual(avere_2,"58,26 €")

        self.navigateTo("Fatture di vendita")
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def plugin_movimenti_contabili(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader() 

        self.find(By.XPATH, '//a[@id="link-tab_38"]').click()
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

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader() 

        self.find(By.XPATH, '//a[@id="link-tab_40"]').click()        
        self.find(By.XPATH,'//div[@id="tab_40"]//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="select2-mese-container"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys("Agosto", Keys.ENTER)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="select2-giorno_fisso-container"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys("8", Keys.ENTER)
        self.wait_loader()

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

        self.find(By.XPATH,'//div[@id="tab_40"]//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="select2-mese-container"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys("Aprile", Keys.ENTER)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="select2-giorno_fisso-container"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))).send_keys("8", Keys.ENTER)
        self.wait_loader()

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH,  '//div[@id="tab_40"]//tbody//tr//td[2]'))).click()
        self.wait_loader()
             
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-danger "]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        sleep(1)

        self.expandSidebar("Contabilità")
        self.navigateTo("Scadenzario")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Anagrafica"]/input'))).send_keys('Cliente', Keys.ENTER)
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH,  '//tbody//tr//td[2]'))).click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_concordata0"]'))).send_keys('13/08/2025')
        sleep(1)

        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="alert alert-warning"]')))

        element = self.find(By.XPATH, '//input[@id="data_concordata0"]')
        element.clear()
        element.send_keys('20/01/2025')
        sleep(1)

        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        wait.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="alert alert-warning"]')))

        self.navigateTo("Anagrafiche")
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

        self.expandSidebar("Vendite")
        
    def registrazioni(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Tipo"]/input'))).send_keys("Fattura immediata di vendita", Keys.ENTER)
        sleep(1) 

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()
        

        self.find(By.XPATH, '//a[@id="link-tab_42"]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_42"]//tr[5]//td'))) 
        sleep(1)

        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def controlla_allegati(self): 
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader() 

        self.find(By.XPATH, '//a[@id="link-tab_30"]').click()
        self.find(By.XPATH, '//div[@id="tab_30"]//a[@class="btn btn-info btn-lg"]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_30"]//a[@class="btn btn-xs btn-primary"]')))

        self.navigateTo("Anagrafiche")
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

        self.expandSidebar("Vendite")

    def duplica_selezionati(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td').click() 
        self.find(By.XPATH, '//button[@data-toggle="dropdown"]').click()  
        self.find(By.XPATH, '//a[@data-op="copy-bulk"]').click()   
        sleep(1)
        
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td').click()  

    def cambia_sezionale(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td').click()
        self.find(By.XPATH, '//button[@data-toggle="dropdown"]').click() 
        self.find(By.XPATH, '//a[@data-op="cambia-sezionale"]').click() 
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-id_segment-container"]').click()
        self.find(By.XPATH, '//ul[@id="select2-id_segment-results"]').click()  
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-id_segment_-container"]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Autofatture")
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-id_segment_-results"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td').click() 
        self.find(By.XPATH, '//button[@data-toggle="dropdown"]').click() 
        self.find(By.XPATH, '//a[@data-op="cambia-sezionale"]').click() 
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-id_segment-container"]').click()   
        self.find(By.XPATH, '//ul[@id="select2-id_segment-results"]').click() 
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-id_segment_-container"]').click() 
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Standard")
        sleep(1)

        self.find(By.XPATH, '//ul[@id="select2-id_segment_-results"]').click() 
        self.wait_loader()


    def emetti_fatture(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td').click() 

        self.find(By.XPATH, '//button[@data-toggle="dropdown"]').click()
        self.find(By.XPATH, '//a[@data-op="change-stato"]').click() 
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() 
        self.wait_loader()

        stato=self.find(By.XPATH, '//tbody//tr//td[11]').text
        self.assertEqual(stato, "Emessa")   

        self.find(By.XPATH, '//tbody//tr//td').click()  

    def statistiche_vendita(self):
        wait = WebDriverWait(self.driver, 20)
        self.expandSidebar("Magazzino")
        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="link-tab_44"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_44"]//tbody//tr//td'))) 
        sleep(1)

        self.expandSidebar("Vendite")

    def controlla_fatture_elettroniche(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td').click() 
        self.find(By.XPATH, '//button[@data-toggle="dropdown"]').click()  
        self.find(By.XPATH, '//a[@data-op="check-bulk"]').click()  
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click() 
        sleep(1)

        # Verifica successo operazione
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.find(By.XPATH, '//div[@class="toast toast-success"]').click()
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def registrazione_contabile(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys("0001", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click()
        self.find(By.XPATH, '//button[@data-toggle="dropdown"]').click()
        self.find(By.XPATH, '//a[@data-op="registrazione-contabile"]').click() 
        sleep(1)

        totale=self.find(By.XPATH, '//th[@id="totale_dare"]').text 
        self.assertEqual(totale, "323,06 €")

        # TODO aggiungere registrazione contabile e verificare importo in prima nota anzichè chiuderla

        self.find(By.XPATH, '//button[@class="close"]').click() 
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td').click() 
        self.find(By.XPATH, '(//i[@class="deleteicon fa fa-times"])[1]').click() 
        sleep(1)

    def genera_fatture_elettroniche(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td').click()
        self.find(By.XPATH, '//button[@data-toggle="dropdown"]').click()  
        self.find(By.XPATH, '//a[@data-op="genera-xml"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()
        sleep(1)

        self.driver.switch_to.window(self.driver.window_handles[1]) 
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-xs btn-info"]').click()  
        sleep(1)

        self.find(By.XPATH, '//button[@class="close"]').click() 
        sleep(1)

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(1)

        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td').click()  
        sleep(1)

    def elimina_selezionati(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td').click()  
        self.find(By.XPATH, '//button[@data-toggle="dropdown"]').click() 
        self.find(By.XPATH, '//a[@data-op="delete-bulk"]').click()  
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   
        sleep(1)

        test=self.find(By.XPATH, '//tbody//tr//td[2]').text
        self.assertEqual(test, "0002/2025")
