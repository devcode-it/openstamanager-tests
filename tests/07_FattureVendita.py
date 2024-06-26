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
        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
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