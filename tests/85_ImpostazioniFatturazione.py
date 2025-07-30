from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Impostazioni(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")

    def test_impostazioni_fatturazione(self):
        # Test Iva predefinita
        self.iva_predefinita()

        # Test Tipo di pagamento predefinito
        self.tipo_pagamento_predefinito()

        # Test Ritenuta d'acconto predefinita
        self.ritenuta_acconto_predefinita()

        # Test Cassa previdenziale predefinita
        self.cassa_previdenziale_predefinita()

        # Test Importo marca da bollo
        self.importo_marca_bollo()

        # Test Soglia minima per l'applicazione della marca da bollo
        self.soglia_minima_marca_bollo()

        ## TODO: conto aziendale predefinito

        # Test Conto predefinito fatture di vendita
        self.conto_predefinito_vendita()

        # Test Conto predefinito fatture di acquisto
        self.conto_predefinito_acquisto()

        # Test Dicitura fissa fattura
        self.dicitura_fissa_fattura() 

        ## TODO: metodologia calcolo ritenuta d'acconto predefinito

        # Test Ritenuta previdenziale predefinita 
        self.ritenuta_previdenziale_predefinita()

        # Test Descrizione addebito bollo 
        #self.descrizione_marca_bollo()  

        # Test Conto predefinito per la marca da bollo
        #self.conto_marca_bollo()

        # Test Iva per lettere d'intento
        #self.iva_lettere_intento()

        # Test Utilizza prezzi di vendita comprensivi di IVA
        #self.prezzi_vendita_comprensivi_iva()

        # Test Liquidazione iva
        #self.liquidazione_iva()

        ## TODO: conto anticipo clienti

        ## TODO: conto anticipo fornitori

        # Test Descrizione fattura pianificata
        #self.descrizione_fattura_pianificata()

        ## TODO: aggiorna info di acquisto

        ## TODO: bloccare i prezzi inferiori al minimo di vendita

        # Test Permetti fatturazione delle attività collegate a contratti
        #self.fattura_attivita_collegate_contratti()

        ## TODO: data emissione fattura automatica

        # Test Permetti fatturazione delle attività collegate a ordini
        #self.fattura_attivita_collegate_ordini()

        ## TODO: permetti fatturazione delle attività collegate a preventivi

        ## TODO: data inizio verifica contatore fatture di vendita

        ## TODO: raggruppa attività per tipologia in fattura

        ## TODO: metodo di importazione XML fatture di vendita

    def iva_predefinita(self):
                self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click()

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Iva predefinita")]//div//span').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Aliq. Iva 10")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()

        self.find(By.XPATH, '//textarea[@id="descrizione_riga"]').send_keys("test")
        iva = self.find(By.XPATH, '//span[@id="select2-idiva-container"]').text 
        self.assertEqual(iva[2:21], "10 - Aliq. Iva 10%")
        self.find(By.XPATH, '//button[@class="close"]').click()

        self.find(By.XPATH, '//a[@id="elimina"]').click()

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click()

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Iva predefinita")]//div//span').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Aliq. Iva 22")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

    def tipo_pagamento_predefinito(self):
                self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click()

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Tipo di pagamento predefinito")]//div//span').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Rimessa diretta")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() 
        self.wait_loader()

        tipo = self.find(By.XPATH, '//span[@id="select2-idpagamento-container"]').text
        self.assertEqual(tipo[2:24], "MP01 - Rimessa diretta")
        self.find(By.XPATH, '//a[@id="elimina"]').click()

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click() 
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click()

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Tipo di pagamento predefinito")]//div//span').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Bonifico 30gg d.f.f.m.")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

    def ritenuta_acconto_predefinita(self):
                self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click()

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Ritenuta d\'acconto predefinita")]//div//span').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Ritenuta Acconto di Prova")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click() 
        modal = self.wait_modal()

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()

        ritenuta = self.find(By.XPATH, '//span[@id="select2-id_ritenuta_acconto-container"]').text
        self.assertEqual(ritenuta[2:27], "Ritenuta Acconto di Prova")
        
        self.find(By.XPATH, '//div[@id="modals"]//button[@class="close"]').click()

        self.find(By.XPATH, '//a[@id="elimina"]').click()

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click() 
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click()

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Ritenuta d\'acconto predefinita")]//div//span[@class="select2-selection__clear"]').click()

    def cassa_previdenziale_predefinita(self):
                self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click()

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Cassa previdenziale predefinita")]//div//span').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Cassa Previdenziale di Prova")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys(Keys.ENTER)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()

        cassa_previdenziale = self.find(By.XPATH, '//span[@id="select2-id_rivalsa_inps-container"]').text 
        self.assertEqual(cassa_previdenziale[2:30], "Cassa Previdenziale di Prova")

        self.find(By.XPATH, '//button[@class="close"]').click()

        self.find(By.XPATH, '//a[@id="elimina"]').click()

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click() 
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click()

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Cassa previdenziale predefinita")]//div//span[@class="select2-selection__clear"]').click()

    def importo_marca_bollo(self):
                self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("test")

        prezzo_unitario = self.find(By.XPATH, '//input[@id="prezzo_unitario"]')
        prezzo_unitario.clear()
        prezzo_unitario.send_keys("80")

        self.find(By.XPATH, '//span[@id="select2-idiva-container"]').click()

        self.find(By.XPATH, '//ul[@id="select2-idiva-results"]//li[20]').click()  
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()  
        self.wait_loader()

        totale = self.find(By.XPATH, '//tbody//tr[2]//td[9]').text
        self.assertEqual(totale, "2,00 €")  

        self.find(By.XPATH, '//a[@id="elimina"]').click()

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click() 
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click()

        element = self.find(By.XPATH, '//div[@class="form-group" and contains(., "Importo marca da bollo")]//input')
        element.clear()
        element.send_keys('3,00', Keys.ENTER)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("test")

        prezzo_unitario = self.find(By.XPATH, '//input[@id="prezzo_unitario"]')
        prezzo_unitario.clear()
        prezzo_unitario.send_keys("80")

        self.find(By.XPATH, '//span[@id="select2-idiva-container"]').click()

        self.find(By.XPATH, '//ul[@id="select2-idiva-results"]//li[20]').click()  
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()   
        self.wait_loader()

        totale = self.find(By.XPATH, '//tbody//tr[2]//td[9]').text
        self.assertEqual(totale, "3,00 €", Keys.ENTER)   

        self.find(By.XPATH, '//a[@id="elimina"]').click()

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.navigateTo("Impianti")
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click()

        element = self.find(By.XPATH, '//div[@class="form-group" and contains(., "Importo marca da bollo")]//input')
        element.clear()
        element.send_keys('2,00', Keys.ENTER)

    def soglia_minima_marca_bollo(self):
                self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("test")

        prezzo_unitario = self.find(By.XPATH, '//input[@id="prezzo_unitario"]')
        prezzo_unitario.clear()
        prezzo_unitario.send_keys("80")

        self.find(By.XPATH, '//span[@id="select2-idiva-container"]').click()

        self.find(By.XPATH, '//ul[@id="select2-idiva-results"]//li[20]').click() 
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() 
        self.wait_loader()

        totale = self.find(By.XPATH, '//tbody//tr[2]//td[9]').text
        self.assertEqual(totale, "2,00 €")  

        self.find(By.XPATH, '//a[@id="elimina"]').click()

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click() 
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click()

        element = self.find(By.XPATH, '//div[@class="form-group" and contains(., "Soglia minima per l\'applicazione della marca da bollo")]//input')
        element.clear()
        element.send_keys('40')

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("test")

        prezzo_unitario = self.find(By.XPATH, '//input[@id="prezzo_unitario"]')
        prezzo_unitario.clear()
        prezzo_unitario.send_keys("45")   

        self.find(By.XPATH, '//span[@id="select2-idiva-container"]').click()

        self.find(By.XPATH, '//ul[@id="select2-idiva-results"]//li[20]').click()  
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()   
        self.wait_loader()

        totale = self.find(By.XPATH, '//tbody//tr[2]//td[9]').text
        self.assertEqual(totale, "2,00 €")   

        self.find(By.XPATH, '//a[@id="elimina"]').click()

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()  
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click()

        element = self.find(By.XPATH, '//div[@class="form-group" and contains(., "Soglia minima per l\'applicazione della marca da bollo")]//input')
        element.clear()
        element.send_keys('77,47')
        element.send_keys(Keys.ENTER)

    def conto_predefinito_vendita(self):
                self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click()

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Conto predefinito fatture di vendita")]').click()

        self.find(By.XPATH, '//ul[@id="select2-setting36-results"]//li[2]').click()

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()

        conto = self.find(By.XPATH, '//span[@id="select2-idconto-container"]').text   
        self.assertEqual(conto[2:47], "700.000020 Ricavi vendita prestazione servizi")
        self.find(By.XPATH, '//button[@class="close"]').click()

        #elimina fattura
        self.find(By.XPATH, '//a[@id="elimina"]').click()

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()  
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click()

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Conto predefinito fatture di vendita")]').click()

        self.find(By.XPATH, '//ul[@id="select2-setting36-results"]//li[1]').click()

    def conto_predefinito_acquisto(self):
                self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click()

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Conto predefinito fatture di acquisto")]').click()

        self.find(By.XPATH, '//ul[@id="select2-setting37-results"]//li[2]').click()

        self.expandSidebar("Acquisti")
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="numero_esterno"]'))).send_keys("05") 
        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Fornitore", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()  
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-idpagamento-container"]').click()

        self.find(By.XPATH, '//ul[@id="select2-idpagamento-results"]//li[1]').click()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()

        conto = self.find(By.XPATH, '//span[@id="select2-idconto-container"]').text
        self.assertEqual(conto[2:50], "600.000020 Costi merci c/acquisto di produzione")
        self.find(By.XPATH, '//button[@class="close"]').click()

        self.find(By.XPATH, '//a[@id="elimina"]').click()

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click()

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Conto predefinito fatture di acquisto")]').click()

        self.find(By.XPATH, '//ul[@id="select2-setting37-results"]//li[1]').click()

    def dicitura_fissa_fattura(self):
                self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]')  
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="print-button_p"]').click()

        self.driver.switch_to.window(self.driver.window_handles[1])

        dicitura = self.find(By.XPATH, '(//div[@id="viewer"]//span)[196]').text
        self.assertEqual(dicitura, "Ai sensi del D.Lgs. 196/2003 Vi informiamo che i Vs. dati saranno utilizzati esclusivamente per i ﬁni connessi ai rapporti commerciali tra di noi in essere. Contributo CONAI assolto ove dovuto - Vi")

        self.driver.close() 
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click()

        dicitura = self.find(By.XPATH, '//iframe[@class="cke_wysiwyg_frame cke_reset"]')
        self.driver.switch_to.frame(dicitura)
        self.driver.execute_script('document.body.innerHTML = ""')
        self.driver.execute_script('document.body.innerHTML = "Test"')
        self.driver.switch_to.default_content()
        dicitura.send_keys(Keys.ENTER)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]')  
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="print-button_p"]').click()

        self.driver.switch_to.window(self.driver.window_handles[1])

        dicitura = self.find(By.XPATH, '(//div[@id="viewer"]//span)[196]').text
        self.assertEqual(dicitura, "Test")

        self.driver.close() 
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click()

        dicitura = self.find(By.XPATH, '//iframe[@class="cke_wysiwyg_frame cke_reset"]')
        self.driver.switch_to.frame(dicitura)
        self.driver.execute_script('document.body.innerHTML = ""')
        self.driver.execute_script('document.body.innerHTML = "Ai sensi del D.Lgs. 196/2003 Vi informiamo che i Vs. dati saranno utilizzati esclusivamente per i fini connessi ai rapporti commerciali tra di noi in essere. Contributo CONAI assolto ove dovuto - Vi preghiamo di controllare i Vs. dati anagrafici, la P. IVA e il Cod. Fiscale. Non ci riteniamo responsabili di eventuali errori."')
        self.driver.switch_to.default_content()
        dicitura.send_keys(Keys.ENTER)

    def ritenuta_previdenziale_predefinita(self):
                self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click()

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Ritenuta previdenziale predefinita")]').click()

        self.find(By.XPATH, '//ul[@id="select2-setting82-results"]//li[1]').click()

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() 
        self.wait_loader()

        ritenuta_element = self.find(By.XPATH, '//span[@id="select2-id_ritenuta_contributi-container"]') 
        ritenuta = ritenuta_element.get_attribute("title")
        self.assertEqual(ritenuta, "Ritenuta Previdenziale di Prova - 80.00% sul 60.00% imponibile")

        self.find(By.XPATH, '//a[@id="elimina"]').click()

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click() 
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click()

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Ritenuta previdenziale predefinita")]//span[@class="select2-selection__clear"]').click()

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() 
        self.wait_loader()

        ritenuta_element = self.find(By.XPATH, '//span[@id="select2-id_ritenuta_contributi-container"]') 
        ritenuta = ritenuta_element.get_attribute("title")
        self.assertEqual(ritenuta, "")

        self.find(By.XPATH, '//a[@id="elimina"]').click()

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click() 
        self.wait_loader()

    def descrizione_marca_bollo(self):
                self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("test")
        prezzo_unitario = self.find(By.XPATH, '//input[@id="prezzo_unitario"]')
        prezzo_unitario.clear()
        prezzo_unitario.send_keys("80")

        self.find(By.XPATH, '//span[@id="select2-idiva-container"]').click()

        self.find(By.XPATH, '//ul[@id="select2-idiva-results"]//li[20]').click()  
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()  
        self.wait_loader()

        descrizione = self.find(By.XPATH, '//tbody//tr[2]//td[3]').text
        self.assertEqual(descrizione[31:61], "Marca da bollo")

        self.find(By.XPATH, '//a[@id="elimina"]').click()

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click() 
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click()

        element = self.find(By.XPATH, '//div[@class="form-group" and contains(., "Descrizione addebito bollo")]//input')
        element.clear()
        element.send_keys('Descrizione test', Keys.ENTER)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("test")
        prezzo_unitario = self.find(By.XPATH, '//input[@id="prezzo_unitario"]')
        prezzo_unitario.clear()
        prezzo_unitario.send_keys("80")

        self.find(By.XPATH, '//span[@id="select2-idiva-container"]').click()

        self.find(By.XPATH, '//ul[@id="select2-idiva-results"]//li[20]').click()   
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()  
        self.wait_loader()

        descrizione = self.find(By.XPATH, '//tbody//tr[2]//td[3]').text
        self.assertEqual(descrizione[31:47], "Descrizione test")

        self.find(By.XPATH, '//a[@id="elimina"]').click()

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()  
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click()

        element = self.find(By.XPATH, '//div[@class="form-group" and contains(., "Descrizione addebito bollo")]//input')
        element.clear()
        element.send_keys('Marca da bollo', Keys.ENTER)

    def conto_marca_bollo(self):
                self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("test")
        prezzo_unitario = self.find(By.XPATH, '//input[@id="prezzo_unitario"]')
        prezzo_unitario.clear()
        prezzo_unitario.send_keys("80")
        self.find(By.XPATH, '//span[@id="select2-idiva-container"]').click()

        self.find(By.XPATH, '//ul[@id="select2-idiva-results"]//li[20]').click()  
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()  
        self.wait_loader()
        conto = self.find(By.XPATH, '//tbody//tr[2]//td[3]//small').text 
        self.assertEqual(conto, "Rimborso spese marche da bollo")
        self.find(By.XPATH, '//a[@id="elimina"]').click()

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click() 
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click()

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Conto predefinito per la marca da bollo")]').click()

        self.find(By.XPATH, '//ul[@id="select2-setting90-results"]//li[1]').click()

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("test")
        prezzo_unitario = self.find(By.XPATH, '//input[@id="prezzo_unitario"]')
        prezzo_unitario.clear()
        prezzo_unitario.send_keys("80")
        self.find(By.XPATH, '//span[@id="select2-idiva-container"]').click()

        self.find(By.XPATH, '//ul[@id="select2-idiva-results"]//li[20]').click()  
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()   
        self.wait_loader()

        conto = self.find(By.XPATH, '//tbody//tr[2]//td[3]//small').text 
        self.assertEqual(conto, "Ricavi merci c/to vendite")
        self.find(By.XPATH, '//a[@id="elimina"]').click()

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click()

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Conto predefinito per la marca da bollo")]').click()

        self.find(By.XPATH, '//ul[@id="select2-setting90-results"]//li[6]').click()

    def iva_lettere_intento(self):
                self.navigateTo("Anagrafiche")
        self.wait_loader() 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]') 

        
        self.find(By.XPATH, '//a[@id="link-tab_25"]').click()
        self.find(By.XPATH, '//div[@id="tab_25"]//i[@class="fa fa-plus"]').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="numero_protocollo"]'))).send_keys("012345678901234567890123")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_protocollo"]'))).send_keys("06/11/2025")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="numero_progressivo"]'))).send_keys("001")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_inizio"]'))).send_keys("06/11/2025")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_fine"]'))).send_keys("06/12/2025")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="massimale"]'))).send_keys("50000")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_emissione"]'))).send_keys("06/11/2025", Keys.ENTER)
        self.find(By.XPATH, '(//button[@class="btn btn-primary"])[2]').click()
        self.wait_loader()

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//i[@class="fa fa-plus"]').click() 
        self.wait_modal()

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)

        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("prova per dichiarazione")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="qta"]'))).send_keys("100")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()

        iva = self.find(By.XPATH, '//tbody[@id="righe"]//tr[1]//td[8]//small').text
        self.assertEqual(iva, "Non imp. art. 8 c.1 lett. c DPR 633/1972 (I) (N3.5)")
        self.find(By.XPATH, '//a[@id="elimina"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.navigateTo("Anagrafiche")
        self.wait_loader() 

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]') 

        
        self.find(By.XPATH, '//a[@id="link-tab_25"]').click()

        self.find(By.XPATH, '(//div[@id="tab_25"]//tr[1]//td[2])[2]').click()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask "]').click()

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click()

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Iva per lettere d\'intento")]').click()

        self.find(By.XPATH, '//ul[@id="select2-setting94-results"]//li[1]').click()

        self.navigateTo("Anagrafiche")
        self.wait_loader() 

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]') 

        
        self.find(By.XPATH, '//a[@id="link-tab_25"]').click()
        self.find(By.XPATH, '//div[@id="tab_25"]//i[@class="fa fa-plus"]').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="numero_protocollo"]'))).send_keys("012345678901234567890123")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_protocollo"]'))).send_keys("06/11/2025")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="numero_progressivo"]'))).send_keys("001")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_inizio"]'))).send_keys("06/11/2025")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_fine"]'))).send_keys("06/12/2025")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="massimale"]'))).send_keys("50000")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_emissione"]'))).send_keys("06/11/2025", Keys.ENTER)
        self.find(By.XPATH, '(//button[@class="btn btn-primary"])[2]').click()
        self.wait_loader()

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//i[@class="fa fa-plus"]').click() 
        self.wait_modal()

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)

        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("prova per dichiarazione")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="qta"]'))).send_keys("100")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1")
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()

        iva = self.find(By.XPATH, '//tbody[@id="righe"]//tr[1]//td[8]//small').text
        self.assertEqual(iva, "Art. 2 c. 2, n. 4 DPR 633/1972 (I) (N3.6)")
        self.find(By.XPATH, '//a[@id="elimina"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.navigateTo("Anagrafiche")
        self.wait_loader() 

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]') 

        
        self.find(By.XPATH, '//a[@id="link-tab_25"]').click()

        self.find(By.XPATH, '(//div[@id="tab_25"]//tr[1]//td[2])[2]').click()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask "]').click()

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.navigateTo("Anagrafiche")
        self.wait_loader() 

        self.find(By.XPATH, '//th[@id="th_Ragione-sociale"]//i').click()  

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click()

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Iva per lettere d\'intento")]').click()

        self.find(By.XPATH, '//ul[@id="select2-setting94-results"]//li[9]').click()

    def prezzi_vendita_comprensivi_iva(self):
                self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click()

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Utilizza prezzi di vendita comprensivi di IVA")]').click()

        self.expandSidebar("Magazzino")
        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione"]'))).send_keys("Prova") 

        self.find(By.XPATH, '(//div[@id="modals"]//i[@class="fa fa-plus"])[3]').click()
        modal = self.wait_modal()

        self.input(modal, 'Quantità iniziale').setValue('1')
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_vendita"]'))).send_keys("12") 
        self.find(By.XPATH, '//button[@class="btn btn-success"]').click()
        self.wait_loader()

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Prova")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)

        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click()

        prezzo = self.find(By.XPATH, '//tbody[2]//tr[1]//td[2]').text
        self.assertEqual(prezzo, "12,00 €")

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click()

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Utilizza prezzi di vendita comprensivi di IVA")]').click()

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[3]//td[2]') 
        self.wait_loader()

        prezzo_element = self.find(By.XPATH, '//tbody[2]//tr[1]//td[2]').text
        self.assertEqual(prezzo, "12,00 €")

        self.find(By.XPATH, '//a[@id="elimina"]').click()  
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click() 
        self.wait_loader()

        self.expandSidebar("Magazzino")
        self.navigateTo("Articoli")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Prova', Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()

        self.expandSidebar("Strumenti")

    def liquidazione_iva(self):
                self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click()

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Liquidazione iva")]').click()

        self.find(By.XPATH, '//ul[@id="select2-setting128-results"]//li[2]').click()

        self.navigateTo("Contabilità")
        self.navigateTo("Stampe contabili")
        self.wait_loader()

        self.find(By.XPATH, '(//div[@class="row"]//div[3]//button)[1]').click()

        self.find(By.XPATH, '//span[@id="select2-periodo-container"]').click()

        periodo = self.find(By.XPATH, '//ul[@id="select2-periodo-results"]//li[2]').text
        self.assertEqual(periodo, "1° Trimestre 2024")
        self.find(By.XPATH, '//button[@class="close"]').click()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click()

        self.find(By.XPATH, '//div[@class="form-group" and contains(., "Liquidazione iva")]').click()

        self.find(By.XPATH, '//ul[@id="select2-setting128-results"]//li[1]').click()

        self.navigateTo("Contabilità")
        self.navigateTo("Stampe contabili")
        self.wait_loader()

        self.find(By.XPATH, '(//div[@class="row"]//div[3]//button)[1]').click()

        self.find(By.XPATH, '//span[@id="select2-periodo-container"]').click()

        periodo = self.find(By.XPATH, '//ul[@id="select2-periodo-results"]//li[2]').text
        self.assertEqual(periodo, "gennaio 2024")
        self.find(By.XPATH, '//button[@class="close"]').click()

    def descrizione_fattura_pianificata(self):
                self.expandSidebar("Vendite")
        self.navigateTo("Contratti")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[2]//td[2]') 
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="link-tab_26"]').click()

        self.find(By.XPATH, '//div[@id="tab_26"]//tbody//tr//td[2]//a').click() 
        
        self.driver.switch_to.window(self.driver.window_handles[1]) 
        self.wait_loader()

        descrizione = self.find(By.XPATH, '//textarea[@id="note"]').text  
        self.assertEqual(descrizione, "Canone 1 del contratto numero 2")
        self.find(By.XPATH, '//button[@class="close"]').click()
        
        self.find(By.XPATH, '//button[@class="ask btn btn-danger pull-right tip tooltipstered"]').click()

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click()

        descrizione = self.find(By.XPATH, '//div[@class="form-group" and contains(., "Descrizione fattura pianificata")]//input').click()
        descrizione.clear() 
        descrizione.send_keys("prova")

        self.expandSidebar("Vendite")
        self.navigateTo("Contratti")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[2]//td[2]')  
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="link-tab_26"]').click()

        self.find(By.XPATH, '//button[@id="pianifica"]').click()

        self.find(By.XPATH, '(//div[@class="nav-tabs-custom"]//a)[2]').click()

        self.find(By.XPATH, '//button[@id="btn_procedi"]').click() 
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary btn-sm "]').click()

        descrizione = self.find(By.XPATH, '//textarea[@id="note"]').text 
        self.assertEqual(descrizione, "prova")
        self.find(By.XPATH, '//button[@class="close"]').click()
        
        self.find(By.XPATH, '//button[@class="ask btn btn-danger pull-right tip tooltipstered"]').click()

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click()

        descrizione = self.find(By.XPATH, '//div[@class="form-group" and contains(., "Descrizione fattura pianificata")]//input').click()
        descrizione.clear() 
        descrizione.send_keys("Canone {rata} del contratto numero {numero}")

    def fattura_attivita_collegate_contratti(self):
                self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click() #apro Fatturazione

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[4]').click()    #attivo impostazione

        #crea contratto
        self.expandSidebar("Vendite")
        self.navigateTo("Contratti")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys("Prova")
        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_accettazione"]'))).send_keys("01/01/2025")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_conclusione"]'))).send_keys("31/12/2025")
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()
        self.wait_loader()
        #aggiungi riga
        self.find(By.XPATH, '//a[@class="btn btn-primary"]').click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Test")    #scrivo "Test" come descrizione della riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1") #scrivo 1 come prezzo unitario
        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click() #click su aggiungi

        #cambio stato
        self.find(By.XPATH, '//span[@id="select2-idstato-container"]').click()

        self.find(By.XPATH, '//ul[@id="select2-idstato-results"]//li[6]').click() #imposto stato "In lavorazione"
        self.find(By.XPATH, '//button[@id="save"]').click() #click su salva
        self.wait_loader()

        #crea attività
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()  #click su +

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys("Cliente")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click() #seleziono Generico come tipo di intervento
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Generico")

        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()  #click su primo risultato
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).send_keys("Test")   #scrivo "Test" come richiesta
        self.find(By.XPATH, '//span[@id="select2-idcontratto-container"]').click()  #aggiungi contratto

        self.find(By.XPATH, '//ul[@id="select2-idcontratto-results"]//li[2]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-nuovo_tecnico-container"]').click()    #aggiungi sessione

        self.find(By.XPATH, '//ul[@id="select2-nuovo_tecnico-results"]//li[2]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-block"]').click()

        self.find(By.XPATH, '//span[@id="select2-idstatointervento-container"]').click()    #click su stato

        self.find(By.XPATH, '(//input[@class="select2-search__field"])[3]').send_keys("Completato", Keys.ENTER) #seleziono Completato come nuovo stato

        self.find(By.XPATH, '//button[@id="save"]').click() #click su salva
        self.wait_loader()

        self.navigateTo("Attività")
        self.wait_loader()
        
        self.wait_for_element_and_click('//tbody//tr[1]//td[1]')
        self.find(By.XPATH, '//button[@data-toggle="dropdown"]').click() #apro azioni di gruppo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-op="crea_fattura"]'))).click()    #click su crea fattura

        self.find(By.XPATH, '//span[@id="select2-raggruppamento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")    #seleziono cliente
        self.find(By.XPATH, '//ul[@id="select2-raggruppamento-results"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  #click di conferma
        self.wait_loader()

        stato = self.find(By.XPATH, '//tbody//tr[1]//td[7]//div').text    #controllo se l'attività è stata fatturata
        self.assertEqual(stato, "Fatturato")
        self.wait_for_element_and_click('//tbody//tr[1]//td[2]')    #apro attività
        self.wait_loader()
        #elimino attività
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #elimino fattura
        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]') #apro prima fattura
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="elimina"]').click() #elimina fattura
        self.wait_loader()

        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click() #apro Fatturazione

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[4]').click()    #disattivo impostazione

        #crea attività
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()  #click su +

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys("Cliente")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click() #seleziono Generico come tipo di intervento
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Generico")

        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()  #click su primo risultato
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).send_keys("Test")   #scrivo "Test" come richiesta
        self.find(By.XPATH, '//span[@id="select2-idcontratto-container"]').click()  #aggiungi contratto

        self.find(By.XPATH, '//ul[@id="select2-idcontratto-results"]//li[2]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-nuovo_tecnico-container"]').click()    #aggiungi sessione

        self.find(By.XPATH, '//ul[@id="select2-nuovo_tecnico-results"]//li[2]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-block"]').click()

        self.find(By.XPATH, '//span[@id="select2-idstatointervento-container"]').click()    #click su stato

        self.find(By.XPATH, '(//input[@class="select2-search__field"])[3]').send_keys("Completato", Keys.ENTER) #seleziono Completato come nuovo stato

        self.find(By.XPATH, '//button[@id="save"]').click() #click su salva
        self.wait_loader()

        self.navigateTo("Attività")
        self.wait_loader()
        
        self.wait_for_element_and_click('//tbody//tr[1]//td[1]')
        self.find(By.XPATH, '//button[@data-toggle="dropdown"]').click() #apro azioni di gruppo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-op="crea_fattura"]'))).click()    #click su crea fattura

        self.find(By.XPATH, '//span[@id="select2-raggruppamento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")    #seleziono cliente
        self.find(By.XPATH, '//ul[@id="select2-raggruppamento-results"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  #click di conferma
        self.wait_loader()

        stato = self.find(By.XPATH, '//tbody//tr[1]//td[7]//div').text    #controllo se l'attività non è stata fatturata
        self.assertEqual(stato, "Completato")
        self.wait_for_element_and_click('//tbody//tr[1]//td[2]')    #apro attività
        self.wait_loader()
        #elimino attività
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #elimino contratto
        self.expandSidebar("Vendite")
        self.navigateTo("Contratti")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]//input'))).send_keys("Prova", Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr[2]//td[2]')    #apro contratto
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()  #elimina contratto 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Nome"]//i').click()   #cancella ricerca

    def fattura_attivita_collegate_ordini(self):
                self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click() #apro Fatturazione

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[6]').click()    #attivo impostazione

        #crea ordine
        self.expandSidebar("Vendite")
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()   #click su tasto +

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()     #scelta di "Cliente" come anagrafica per l'ordine
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Cliente')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su tasto aggiungi
        self.wait_loader()
        #aggiungi articolo
        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()

        self.find(By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click() #click su aggiungi
        #cambio stato
        self.find(By.XPATH, '//span[@id="select2-idstatoordine-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Accettato", Keys.ENTER)
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()
        #crea attività
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()  #click su +

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys("Cliente")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click() #seleziono Generico come tipo di intervento
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Generico")

        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()  #click su primo risultato
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).send_keys("Test")   #scrivo "Test" come richiesta
        self.find(By.XPATH, '//span[@id="select2-idordine-container"]').click() #aggiungo ordine

        self.find(By.XPATH, '//ul[@id="select2-idordine-results"]//li[2]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-nuovo_tecnico-container"]').click()    #aggiungi sessione

        self.find(By.XPATH, '//ul[@id="select2-nuovo_tecnico-results"]//li[2]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-block"]').click()
    
        self.find(By.XPATH, '//span[@id="select2-idstatointervento-container"]').click()    #click su stato

        self.find(By.XPATH, '(//input[@class="select2-search__field"])[3]').send_keys("Completato", Keys.ENTER) #seleziono Completato come nuovo stato
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Attività")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[1]//td[1]') #seleziono attività 
        self.find(By.XPATH, '//button[@data-toggle="dropdown"]').click() #apro azioni di gruppo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-op="crea_fattura"]'))).click()    #click su crea fattura

        self.find(By.XPATH, '//span[@id="select2-raggruppamento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")    #seleziono cliente
        self.find(By.XPATH, '//ul[@id="select2-raggruppamento-results"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  #click di conferma
        self.wait_loader()

        stato = self.find(By.XPATH, '//tbody//tr[1]//td[7]').text #controllo se lo stato è passato a "Fatturato"
        self.assertEqual(stato, "Fatturato")
        #elimina fattura
        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]')

        self.find(By.XPATH, '//a[@id="elimina"]').click()

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()
        #elimina ordine
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]') 
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@data-title="Fatturazione"]').click() #apro Fatturazione

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[6]').click()    #disattivo impostazione

        #crea ordine
        self.expandSidebar("Vendite")
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()   #click su tasto +

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click()     #scelta di "Cliente" come anagrafica per l'ordine
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Cliente')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su tasto aggiungi
        self.wait_loader()
        #aggiungi articolo
        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()

        self.find(By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click() #click su aggiungi
        #cambio stato
        self.find(By.XPATH, '//span[@id="select2-idstatoordine-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Accettato", Keys.ENTER)
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()
        #crea attività
        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()  #click su +

        self.find(By.XPATH, '//span[@id="select2-idanagrafica-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys("Cliente")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//span[@id="select2-idtipointervento-container"]').click() #seleziono Generico come tipo di intervento
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Generico")

        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()  #click su primo risultato
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).send_keys("Test")   #scrivo "Test" come richiesta
        self.find(By.XPATH, '//span[@id="select2-idordine-container"]').click() #aggiungo ordine

        self.find(By.XPATH, '//ul[@id="select2-idordine-results"]//li[2]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su Aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-nuovo_tecnico-container"]').click()    #aggiungi sessione

        self.find(By.XPATH, '//ul[@id="select2-nuovo_tecnico-results"]//li[2]').click()
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-block"]').click()

        self.find(By.XPATH, '//span[@id="select2-idstatointervento-container"]').click()    #click su stato

        self.find(By.XPATH, '(//input[@class="select2-search__field"])[3]').send_keys("Completato", Keys.ENTER) #seleziono Completato come nuovo stato
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        #fattura attività
        self.navigateTo("Attività")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[1]//td[1]')
        self.find(By.XPATH, '//button[@data-toggle="dropdown"]').click() #apro azioni di gruppo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-op="crea_fattura"]'))).click()    #click su crea fattura

        self.find(By.XPATH, '//span[@id="select2-raggruppamento-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")    #seleziono cliente
        self.find(By.XPATH, '//ul[@id="select2-raggruppamento-results"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  #click di conferma
        self.wait_loader()

        stato = self.find(By.XPATH, '//tbody//tr[1]//td[7]').text #controllo se lo stato è passato a "Fatturato"
        self.assertEqual(stato, "Fatturato")
        #elimina ordine
        self.expandSidebar("Vendite")
        self.navigateTo("Ordini cliente")
        self.wait_loader() 

        self.wait_for_element_and_click('//tbody//tr[1//td[2]') 
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #elimina fattura
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[1]//td[2]')

        self.find(By.XPATH, '//a[@id="elimina"]').click() #elimina fattura

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()   #click di conferma
        self.wait_loader()
        #elimina attività
        self.navigateTo("Attività")
        self.wait_loader()
        
        self.wait_for_element_and_click('//tbody//tr[1]//td[2]')

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

