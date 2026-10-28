from common.Test import Test, get_html
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

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
        ## TODO: conto predefinito per le spese d'incasso
        ## TODO: descrizione aggiuntiva personalizzata in fatturazione

    def iva_predefinita(self):
        wait = self.wait_driver
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click()

        self.wait_for_dropdown_and_select(
            '//div[@class="form-group" and contains(., "Iva predefinita")]//div//span',
            option_text='Aliq. Iva 10'
        )

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_for_element_and_click('//span[@id="select2-id_anagrafica_add-container"]')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[contains(normalize-space(.), "00000004")]'))).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[@type="submit"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@data-title="Aggiungi riga"]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="modals"]//textarea[@id="descrizione_riga"]'))).send_keys("test")
        iva = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="modals"]//span[@id="select2-id_iva-container"]'))
        ).text
        self.assertIn("10 - Aliq. Iva 10%", iva)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="modals"]//button[@class="close"]'))
        ).click()

        self.wait_for_element_and_click('//a[@id="elimina"]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click()

        self.wait_for_dropdown_and_select(
            '//div[@class="form-group" and contains(., "Iva predefinita")]//div//span',
            option_text='Aliq. Iva 22'
        )

    def tipo_pagamento_predefinito(self):
        wait = self.wait_driver
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click()

        self.wait_for_dropdown_and_select(
            '//div[@class="form-group" and contains(., "Tipo di pagamento predefinito")]//div//span',
            option_text='Rimessa diretta'
        )

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_for_element_and_click('//span[@id="select2-id_anagrafica_add-container"]')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[contains(normalize-space(.), "00000004")]'))).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[@type="submit"]'))
        ).click()
        self.wait_loader()

        tipo = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_pagamento-container"]'))
        ).text
        self.assertIn("MP01 - Rimessa diretta", tipo)
        self.wait_for_element_and_click('//a[@id="elimina"]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click()

        self.wait_for_dropdown_and_select(
            '//div[@class="form-group" and contains(., "Tipo di pagamento predefinito")]//div//span',
            option_text='Bonifico 30gg d.f.f.m.'
        )

    def ritenuta_acconto_predefinita(self):
        wait = self.wait_driver
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click()

        self.wait_for_dropdown_and_select(
            '//div[@class="form-group" and contains(., "Ritenuta d\'acconto predefinita")]//div//span',
            option_text='Ritenuta Acconto di Prova'
        )

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_for_element_and_click('//span[@id="select2-id_anagrafica_add-container"]')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[contains(normalize-space(.), "00000004")]'))).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[@type="submit"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@data-title="Aggiungi riga"]'))
        ).click()

        ritenuta = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="modals"]//span[@id="select2-id_ritenuta_acconto-container"]'))
        ).text
        self.assertIn("Ritenuta Acconto di Prova", ritenuta)

        self.wait_loader()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="modals"]//button[@class="close"]'))
        ).click()

        self.wait_for_element_and_click('//a[@id="elimina"]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click()

        # ripristino: il setting torna vuoto (stato originale) via API select2
        self.wait_driver.until(
            EC.presence_of_element_located((By.ID, 'setting8'))
        )
        self.driver.execute_script("$('#setting8').val(null).trigger('change');")
        self.wait_ajax()

    def cassa_previdenziale_predefinita(self):
        wait = self.wait_driver
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click()

        self.wait_for_dropdown_and_select(
            '//div[@class="form-group" and contains(., "Cassa previdenziale predefinita")]//div//span',
            option_text='Cassa Previdenziale di Prova'
        )

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_for_element_and_click('//span[@id="select2-id_anagrafica_add-container"]')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[contains(normalize-space(.), "00000004")]'))).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[@type="submit"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@data-title="Aggiungi riga"]'))
        ).click()

        cassa_previdenziale = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="modals"]//span[@id="select2-id_rivalsa_inps-container"]'))
        ).text
        self.assertIn("Cassa Previdenziale di Prova", cassa_previdenziale)

        self.wait_loader()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="modals"]//button[@class="close"]'))
        ).click()

        self.wait_for_element_and_click('//a[@id="elimina"]')

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click()

        # ripristino: il setting torna vuoto (stato originale) via API select2
        self.wait_driver.until(
            EC.presence_of_element_located((By.ID, 'setting9'))
        )
        self.driver.execute_script("$('#setting9').val(null).trigger('change');")
        self.wait_ajax()

    def importo_marca_bollo(self):
        wait = self.wait_driver

        # Fase 1: importo corrente (2,00)
        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")
        self.crea_fattura_con_riga_test()

        riga_bollo = self.wait_driver.until(
            EC.presence_of_element_located((By.XPATH, '//tr[td[starts-with(normalize-space(.), "Marca da bollo")]]'))
        )
        totale = riga_bollo.get_attribute('textContent')
        self.assertIn("2,00", totale)

        self.wait_for_element_and_click('//a[@id="elimina"]')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        # Cambio l'importo a 3,00
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click()

        element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Importo marca da bollo")]//input'))
        )
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys('3,00')
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change', {bubbles: true}));", element)
        self.wait_ajax()

        # Fase 2: importo 3,00
        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")
        self.crea_fattura_con_riga_test()

        riga_bollo = self.wait_driver.until(
            EC.presence_of_element_located((By.XPATH, '//tr[td[starts-with(normalize-space(.), "Marca da bollo")]]'))
        )
        totale = riga_bollo.get_attribute('textContent')
        self.assertIn("3,00", totale)

        self.wait_for_element_and_click('//a[@id="elimina"]')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        # Ripristino l'importo a 2,00
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click()

        element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Importo marca da bollo")]//input'))
        )
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys('2,00')
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change', {bubbles: true}));", element)
        self.wait_ajax()

    def crea_fattura_con_riga_test(self, prezzo='80'):
        wait = self.wait_driver

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_for_element_and_click('//span[@id="select2-id_anagrafica_add-container"]')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[contains(normalize-space(.), "00000004")]'))).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[@type="submit"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@data-title="Aggiungi riga"]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="modals"]//textarea[@id="descrizione_riga"]'))).send_keys("test")
        prezzo_unitario = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="modals"]//input[@id="prezzo_unitario"]')))
        prezzo_unitario.send_keys(Keys.CONTROL, 'a')
        prezzo_unitario.send_keys(prezzo)

        # la marca da bollo si applica solo a righe esenti con natura Fe N2/N3/N4
        self.wait_for_dropdown_and_select(
            '//div[@id="modals"]//span[@id="select2-id_iva-container"]',
            option_text='Esente art. 10'
        )

        self.wait_loader()
        self.wait_for_element_and_click('//div[@id="modals"]//button[@onclick="submitForm()"]')
        self.wait_loader()

        # la lista righe ricaricata via AJAX omette la riga auto-generata della
        # marca da bollo: serve un ricaricamento completo della pagina
        self.driver.refresh()
        self.wait_loader()

    def soglia_minima_marca_bollo(self):
        wait = self.wait_driver

        # Fase 1: prezzo 80 > soglia 77,47 -> bollo applicato
        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")
        self.crea_fattura_con_riga_test()

        riga_bollo = self.wait_driver.until(
            EC.presence_of_element_located((By.XPATH, '//tr[td[starts-with(normalize-space(.), "Marca da bollo")]]'))
        )
        self.assertIn("2,00", riga_bollo.get_attribute('textContent'))

        self.wait_for_element_and_click('//a[@id="elimina"]')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        # Soglia a 40
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click()

        element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Soglia minima per l\'applicazione della marca da bollo")]//input'))
        )
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys('40')
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change', {bubbles: true}));", element)
        self.wait_ajax()

        # Fase 2: prezzo 45 > soglia 40 -> bollo applicato
        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")
        self.crea_fattura_con_riga_test(prezzo='45')

        riga_bollo = self.wait_driver.until(
            EC.presence_of_element_located((By.XPATH, '//tr[td[starts-with(normalize-space(.), "Marca da bollo")]]'))
        )
        self.assertIn("2,00", riga_bollo.get_attribute('textContent'))

        self.wait_for_element_and_click('//a[@id="elimina"]')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        # Ripristino la soglia a 77,47
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click()

        element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Soglia minima per l\'applicazione della marca da bollo")]//input'))
        )
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys('77,47')
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change', {bubbles: true}));", element)
        self.wait_ajax()


    def conto_predefinito_vendita(self):
        wait = self.wait_driver
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click()

        self.wait_for_dropdown_and_select(
            '//div[@class="form-group" and contains(., "Conto predefinito fatture di vendita")]//div//span',
            option_text='Ricavi vendita prestazione servizi'
        )

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_for_element_and_click('//span[@id="select2-id_anagrafica_add-container"]')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[contains(normalize-space(.), "00000004")]'))).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[@type="submit"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@data-title="Aggiungi riga"]'))
        ).click()

        conto = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="modals"]//span[@id="select2-id_conto-container"]'))
        ).text
        self.assertIn("700.000020 Ricavi vendita prestazione servizi", conto)

        self.wait_loader()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="modals"]//button[@class="close"]'))
        ).click()

        self.wait_for_element_and_click('//a[@id="elimina"]')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click()

        self.wait_for_dropdown_and_select(
            '//div[@class="form-group" and contains(., "Conto predefinito fatture di vendita")]//div//span',
            option_text='Ricavi merci c/to vendite'
        )


    def conto_predefinito_acquisto(self):
        wait = self.wait_driver
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click()

        self.wait_for_dropdown_and_select(
            '//div[@class="form-group" and contains(., "Conto predefinito fatture di acquisto")]//div//span',
            option_text='Costi merci c/acquisto di produzione'
        )

        self.expandSidebar("Acquisti")
        self.navigate_to_and_wait("Fatture di acquisto")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="numero_esterno"]'))).send_keys("05")
        self.wait_for_element_and_click('//span[@id="select2-id_anagrafica_add-container"]')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Fornitore")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[contains(normalize-space(.), "00000006")]'))).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[@type="submit"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@data-title="Aggiungi riga"]'))
        ).click()

        conto = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="modals"]//span[@id="select2-id_conto-container"]'))
        ).text
        self.assertIn("600.000020 Costi merci c/acquisto di produzione", conto)

        self.wait_loader()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="modals"]//button[@class="close"]'))
        ).click()

        self.wait_for_element_and_click('//a[@id="elimina"]')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click()

        self.wait_for_dropdown_and_select(
            '//div[@class="form-group" and contains(., "Conto predefinito fatture di acquisto")]//div//span',
            option_text='Costi merci c/acquisto di rivendita'
        )


    def dicitura_fissa_fattura(self):
        wait = self.wait_driver
        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")

        self.wait_and_click_table_row(1, 2)
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="print-button_p"]'))
        ).click()

        wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        wait.until(lambda d: '196/2003' in d.find_element(By.ID, 'viewer').text)

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        # imposto la dicitura a "Test"
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click()

        # attesa che il CKEditor del setting sia caricato
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//iframe[@class="cke_wysiwyg_frame cke_reset"]'))
        )
        # il valore viene impostato via API CKEditor: la digitazione lunga
        # viene troncata dal processing dell'editor
        self.driver.execute_script("""
            var key = Object.keys(CKEDITOR.instances).find(function(k){ return k.indexOf('setting') === 0; });
            CKEDITOR.instances[key].setData('Test');
            document.getElementById(key).value = 'Test';
            $(document.getElementById(key)).trigger('change');
        """)

        try:
            self.wait_ajax()
        except Exception:
            time.sleep(2)

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")

        self.wait_and_click_table_row(1, 2)
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="print-button_p"]'))
        ).click()

        wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        wait.until(lambda d: 'Test' in d.find_element(By.ID, 'viewer').text)

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        # ripristino la dicitura originale
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//iframe[@class="cke_wysiwyg_frame cke_reset"]'))
        )
        self.driver.execute_script("""
            var key = Object.keys(CKEDITOR.instances).find(function(k){ return k.indexOf('setting') === 0; });
            CKEDITOR.instances[key].setData(arguments[0]);
            document.getElementById(key).value = arguments[0];
            $(document.getElementById(key)).trigger('change');
        """, "Ai sensi del D.Lgs. 196/2003 Vi informiamo che i Vs. dati saranno utilizzati esclusivamente per i fini connessi ai rapporti commerciali tra di noi in essere. Contributo CONAI assolto ove dovuto - Vi preghiamo di controllare i Vs. dati anagrafici, la P. IVA e il Cod. Fiscale. Non ci riteniamo responsabili di eventuali errori.")

        try:
            self.wait_ajax()
        except Exception:
            time.sleep(2)


    def ritenuta_previdenziale_predefinita(self):
        wait = self.wait_driver
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click()

        self.wait_for_dropdown_and_select(
            '//div[@class="form-group" and contains(., "Ritenuta previdenziale predefinita")]//div//span',
            option_text='Ritenuta Previdenziale di Prova'
        )

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_for_element_and_click('//span[@id="select2-id_anagrafica_add-container"]')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[contains(normalize-space(.), "00000004")]'))).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[@type="submit"]'))
        ).click()
        self.wait_loader()

        ritenuta_element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_ritenuta_contributi-container"]'))
        )
        ritenuta = (ritenuta_element.get_attribute("title") or '') + ' ' + ritenuta_element.text
        self.assertIn("Ritenuta Previdenziale di Prova", ritenuta)

        self.wait_for_element_and_click('//a[@id="elimina"]')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click()

        # ripristino: il setting torna vuoto (stato originale) via API select2
        self.wait_driver.until(
            EC.presence_of_element_located((By.ID, 'setting82'))
        )
        self.driver.execute_script("$('#setting82').val(null).trigger('change');")
        self.wait_ajax()

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_for_element_and_click('//span[@id="select2-id_anagrafica_add-container"]')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[contains(normalize-space(.), "00000004")]'))).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal") and contains(@class,"show")]//button[@type="submit"]'))
        ).click()
        self.wait_loader()

        ritenuta_element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_ritenuta_contributi-container"]'))
        )
        ritenuta = (ritenuta_element.get_attribute("title") or '') + ' ' + ritenuta_element.text
        self.assertNotIn("Ritenuta Previdenziale di Prova", ritenuta)

        self.wait_for_element_and_click('//a[@id="elimina"]')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()


    def descrizione_marca_bollo(self):
        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() 
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("test")
        prezzo_unitario = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))
        )
        prezzo_unitario.clear()
        prezzo_unitario.send_keys("80")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idiva-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idiva-results"]//li[20]'))
        ).click()  
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click()  
        self.wait_loader()

        descrizione = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[2]//td[3]'))
        ).text
        self.assertEqual(descrizione[31:61], "Marca da bollo")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click() 
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click()

        element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Descrizione addebito bollo")]//input'))
        )
        element.clear()
        element.send_keys('Descrizione test', Keys.ENTER)

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() 
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("test")
        prezzo_unitario = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))
        )
        prezzo_unitario.clear()
        prezzo_unitario.send_keys("80")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idiva-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idiva-results"]//li[20]'))
        ).click()   
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click()  
        self.wait_loader()

        descrizione = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[2]//td[3]'))
        ).text
        self.assertEqual(descrizione[31:47], "Descrizione test")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()  
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click()

        element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Descrizione addebito bollo")]//input'))
        )
        element.clear()
        element.send_keys('Marca da bollo', Keys.ENTER)

    def conto_marca_bollo(self):
        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() 
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("test")
        prezzo_unitario = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))
        )
        prezzo_unitario.clear()
        prezzo_unitario.send_keys("80")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idiva-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idiva-results"]//li[20]'))
        ).click()  
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click()  
        self.wait_loader()
        conto = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[2]//td[3]//small'))
        ).text 
        self.assertEqual(conto, "Rimborso spese marche da bollo")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click() 
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Conto predefinito per la marca da bollo")]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-setting90-results"]//li[1]'))
        ).click()

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() 
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("test")
        prezzo_unitario = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))
        )
        prezzo_unitario.clear()
        prezzo_unitario.send_keys("80")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idiva-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idiva-results"]//li[20]'))
        ).click()  
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click()   
        self.wait_loader()

        conto = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[2]//td[3]//small'))
        ).text 
        self.assertEqual(conto, "Ricavi merci c/to vendite")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()   
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Conto predefinito per la marca da bollo")]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-setting90-results"]//li[6]'))
        ).click()

    def iva_lettere_intento(self):
        self.navigate_to_and_wait("Anagrafiche") 

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)

        self.wait_and_click_table_row(1, 2) 

        
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="link-tab_25"]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_25"]//i[@class="fa fa-plus"]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="numero_protocollo"]'))).send_keys("012345678901234567890123")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_protocollo"]'))).send_keys("06/11/2026")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="numero_progressivo"]'))).send_keys("001")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_inizio"]'))).send_keys("06/11/2026")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_fine"]'))).send_keys("06/12/2026")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="massimale"]'))).send_keys("50000")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_emissione"]'))).send_keys("06/11/2026", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-primary"])[2]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click() 
        self.wait_modal()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("prova per dichiarazione")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="qta"]'))).send_keys("100")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click()

        iva = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe"]//tr[1]//td[8]//small'))
        ).text
        self.assertEqual(iva, "Non imp. art. 8 c.1 lett. c DPR 633/1972 (I) (N3.5)")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.navigate_to_and_wait("Anagrafiche") 

        self.wait_and_click_table_row(1, 2) 

        
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="link-tab_25"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_25"]//tr[1]//td[2])[2]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask "]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Iva per lettere d\'intento")]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-setting94-results"]//li[1]'))
        ).click()

        self.navigate_to_and_wait("Anagrafiche") 

        self.wait_and_click_table_row(1, 2) 

        
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="link-tab_25"]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_25"]//i[@class="fa fa-plus"]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="numero_protocollo"]'))).send_keys("012345678901234567890123")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_protocollo"]'))).send_keys("06/11/2026")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="numero_progressivo"]'))).send_keys("001")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_inizio"]'))).send_keys("06/11/2026")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_fine"]'))).send_keys("06/12/2026")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="massimale"]'))).send_keys("50000")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_emissione"]'))).send_keys("06/11/2026", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn-primary"])[2]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click() 
        self.wait_modal()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("prova per dichiarazione")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="qta"]'))).send_keys("100")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click()

        iva = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe"]//tr[1]//td[8]//small'))
        ).text
        self.assertEqual(iva, "Art. 2 c. 2, n. 4 DPR 633/1972 (I) (N3.6)")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.navigate_to_and_wait("Anagrafiche") 

        self.wait_and_click_table_row(1, 2) 

        
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="link-tab_25"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_25"]//tr[1]//td[2])[2]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask "]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.navigate_to_and_wait("Anagrafiche") 

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]//i'))
        ).click()  

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Iva per lettere d\'intento")]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-setting94-results"]//li[9]'))
        ).click()

    def prezzi_vendita_comprensivi_iva(self):
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Utilizza prezzi di vendita comprensivi di IVA")]'))
        ).click()

        self.expandSidebar("Magazzino")
        self.navigate_to_and_wait("Articoli")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione"]'))).send_keys("Prova") 

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//div[@id="modals"]//i[@class="fa fa-plus"])[3]'))
        ).click()
        modal = self.wait_modal()

        self.input(modal, 'Quantità iniziale').setValue('1')
        self.submit_modal(modal)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_vendita"]'))).send_keys("12") 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica_add-container"]'))
        ).click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click() 
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_articolo-container"]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Prova")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]'))
        ).click()

        prezzo = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody[2]//tr[1]//td[2]'))
        ).text
        self.assertEqual(prezzo, "12,00 €")

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Utilizza prezzi di vendita comprensivi di IVA")]'))
        ).click()

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")

        self.wait_and_click_table_row(3, 2) 
        self.wait_loader()

        prezzo_element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody[2]//tr[1]//td[2]'))
        ).text
        self.assertEqual(prezzo, "12,00 €")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click()  
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click() 
        self.wait_loader()

        self.expandSidebar("Magazzino")
        self.navigate_to_and_wait("Articoli")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Prova', Keys.ENTER)

        self.click_first_table_row()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]'))
        ).click()

        self.expandSidebar("Strumenti")

    def liquidazione_iva(self):
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Liquidazione iva")]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-setting128-results"]//li[2]'))
        ).click()

        self.navigate_to_and_wait("Contabilità")
        self.navigate_to_and_wait("Stampe contabili")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//div[@class="row"]//div[3]//button)[1]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-periodo-container"]'))
        ).click()

        periodo = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-periodo-results"]//li[2]'))
        ).text
        self.assertEqual(periodo, "1° Trimestre 2024")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="close"]'))
        ).click()

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Liquidazione iva")]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-setting128-results"]//li[1]'))
        ).click()

        self.navigate_to_and_wait("Contabilità")
        self.navigate_to_and_wait("Stampe contabili")
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//div[@class="row"]//div[3]//button)[1]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-periodo-container"]'))
        ).click()

        periodo = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-periodo-results"]//li[2]'))
        ).text
        self.assertEqual(periodo, "gennaio 2024")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="close"]'))
        ).click()

    def descrizione_fattura_pianificata(self):
        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Contratti")

        self.wait_and_click_table_row(2, 2) 
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="link-tab_26"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_26"]//tbody//tr//td[2]//a'))
        ).click() 
        
        self.driver.switch_to.window(self.driver.window_handles[1]) 
        self.wait_loader()

        descrizione = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//textarea[@id="note"]'))
        ).text  
        self.assertEqual(descrizione, "Canone 1 del contratto numero 2")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="close"]'))
        ).click()
        
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="ask btn btn-danger pull-right tip tooltipstered"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click()

        descrizione = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Descrizione fattura pianificata")]//input'))
        ).click()
        descrizione.clear() 
        descrizione.send_keys("prova")

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Contratti")

        self.wait_and_click_table_row(2, 2)  
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="link-tab_26"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="pianifica"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//div[@class="nav-tabs-custom"]//a)[2]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="btn_procedi"]'))
        ).click() 
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary btn-sm "]'))
        ).click()

        descrizione = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//textarea[@id="note"]'))
        ).text 
        self.assertEqual(descrizione, "prova")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="close"]'))
        ).click()
        
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="ask btn btn-danger pull-right tip tooltipstered"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()
        
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click()

        descrizione = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="form-group" and contains(., "Descrizione fattura pianificata")]//input'))
        ).click()
        descrizione.clear() 
        descrizione.send_keys("Canone {rata} del contratto numero {numero}")

    def fattura_attivita_collegate_contratti(self):
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click() #apro Fatturazione

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[4]'))
        ).click()    #attivo impostazione

        #crea contratto
        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Contratti")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys("Prova")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_accettazione"]'))).send_keys("01/01/2026")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_conclusione"]'))).send_keys("31/12/2026")
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()
        self.wait_loader()
        #aggiungi riga
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-primary"]'))
        ).click() #click su aggiungi riga

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))).send_keys("Test")    #scrivo "Test" come descrizione della riga
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))).send_keys("1") #scrivo 1 come prezzo unitario
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary pull-right"]'))
        ).click() #click su aggiungi

        #cambio stato
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstato-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idstato-results"]//li[6]'))
        ).click() #imposto stato "In lavorazione"
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click() #click su salva
        self.wait_loader()

        #crea attività
        self.navigate_to_and_wait("Attività")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()  #click su +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys("Cliente")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys(Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtipointervento-container"]'))
        ).click() #seleziono Generico come tipo di intervento
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Generico")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--selectable select2-results__option--highlighted"]'))
        ).click()  #click su primo risultato
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).send_keys("Test")   #scrivo "Test" come richiesta
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idcontratto-container"]'))
        ).click()  #aggiungi contratto

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idcontratto-results"]//li[2]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()   #click su Aggiungi
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-nuovo_tecnico-container"]'))
        ).click()    #aggiungi sessione

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-nuovo_tecnico-results"]//li[2]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary btn-block"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatointervento-container"]'))
        ).click()    #click su stato

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[3]'))
        ).send_keys("Completato", Keys.ENTER) #seleziono Completato come nuovo stato

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click() #click su salva
        self.wait_loader()

        self.navigate_to_and_wait("Attività")
        
        self.wait_and_click_table_row(1, 1)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@data-toggle="dropdown"]'))
        ).click() #apro azioni di gruppo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-op="crea_fattura"]'))).click()    #click su crea fattura

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-raggruppamento-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")    #seleziono cliente
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-raggruppamento-results"]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]'))
        ).click()  #click di conferma
        self.wait_loader()

        stato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[7]//div'))
        ).text    #controllo se l'attività è stata fatturata
        self.assertEqual(stato, "Fatturato")
        self.wait_and_click_table_row(1, 2)    #apro attività
        self.wait_loader()
        #elimino attività
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()
        #elimino fattura
        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")

        self.wait_and_click_table_row(1, 2) #apro prima fattura
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click() #elimina fattura
        self.wait_loader()

        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click() #apro Fatturazione

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[4]'))
        ).click()    #disattivo impostazione

        #crea attività
        self.navigate_to_and_wait("Attività")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()  #click su +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys("Cliente")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys(Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtipointervento-container"]'))
        ).click() #seleziono Generico come tipo di intervento
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Generico")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--selectable select2-results__option--highlighted"]'))
        ).click()  #click su primo risultato
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).send_keys("Test")   #scrivo "Test" come richiesta
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idcontratto-container"]'))
        ).click()  #aggiungi contratto

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idcontratto-results"]//li[2]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()   #click su Aggiungi
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-nuovo_tecnico-container"]'))
        ).click()    #aggiungi sessione

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-nuovo_tecnico-results"]//li[2]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary btn-block"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatointervento-container"]'))
        ).click()    #click su stato

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[3]'))
        ).send_keys("Completato", Keys.ENTER) #seleziono Completato come nuovo stato

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click() #click su salva
        self.wait_loader()

        self.navigate_to_and_wait("Attività")
        
        self.wait_and_click_table_row(1, 1)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@data-toggle="dropdown"]'))
        ).click() #apro azioni di gruppo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-op="crea_fattura"]'))).click()    #click su crea fattura

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-raggruppamento-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")    #seleziono cliente
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-raggruppamento-results"]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]'))
        ).click()  #click di conferma
        self.wait_loader()

        stato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[7]//div'))
        ).text    #controllo se l'attività non è stata fatturata
        self.assertEqual(stato, "Completato")
        self.wait_and_click_table_row(1, 2)    #apro attività
        self.wait_loader()
        #elimino attività
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()
        #elimino contratto
        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Contratti")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]//input'))).send_keys("Prova", Keys.ENTER)

        self.wait_and_click_table_row(2, 2)    #apro contratto
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()  #elimina contratto 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]//i'))
        ).click()   #cancella ricerca

    def fattura_attivita_collegate_ordini(self):
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click() #apro Fatturazione

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[6]'))
        ).click()    #attivo impostazione

        #crea ordine
        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Ordini cliente")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su tasto +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click()     #scelta di "Cliente" come anagrafica per l'ordine
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Cliente')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()   #click su tasto aggiungi
        self.wait_loader()
        #aggiungi articolo
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_articolo-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]'))
        ).click() #click su aggiungi
        #cambio stato
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_stato-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Accettato", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()
        #crea attività
        self.navigate_to_and_wait("Attività")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()  #click su +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys("Cliente")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys(Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtipointervento-container"]'))
        ).click() #seleziono Generico come tipo di intervento
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Generico")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--selectable select2-results__option--highlighted"]'))
        ).click()  #click su primo risultato
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).send_keys("Test")   #scrivo "Test" come richiesta
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idordine-container"]'))
        ).click() #aggiungo ordine

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idordine-results"]//li[2]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()   #click su Aggiungi
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-nuovo_tecnico-container"]'))
        ).click()    #aggiungi sessione

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-nuovo_tecnico-results"]//li[2]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary btn-block"]'))
        ).click()
    
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatointervento-container"]'))
        ).click()    #click su stato

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[3]'))
        ).send_keys("Completato", Keys.ENTER) #seleziono Completato come nuovo stato
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()

        self.navigate_to_and_wait("Attività")

        self.wait_and_click_table_row(1, 1) #seleziono attività 
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@data-toggle="dropdown"]'))
        ).click() #apro azioni di gruppo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-op="crea_fattura"]'))).click()    #click su crea fattura

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-raggruppamento-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")    #seleziono cliente
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-raggruppamento-results"]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]'))
        ).click()  #click di conferma
        self.wait_loader()

        stato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[7]'))
        ).text #controllo se lo stato è passato a "Fatturato"
        self.assertEqual(stato, "Fatturato")
        #elimina fattura
        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")

        self.wait_and_click_table_row(1, 2)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()   #click di conferma
        self.wait_loader()
        #elimina ordine
        self.navigate_to_and_wait("Ordini cliente")

        self.wait_and_click_table_row(1, 2) 
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()
        
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigate_to_and_wait("Impostazioni")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-title="Fatturazione"]'))
        ).click() #apro Fatturazione

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//label[@class="btn btn-default active"])[6]'))
        ).click()    #disattivo impostazione

        #crea ordine
        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Ordini cliente")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()   #click su tasto +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click()     #scelta di "Cliente" come anagrafica per l'ordine
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Cliente')

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()   #click su tasto aggiungi
        self.wait_loader()
        #aggiungi articolo
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_articolo-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="select2-results__options select2-results__options--nested"]//li[1]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]'))
        ).click() #click su aggiungi
        #cambio stato
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_stato-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Accettato", Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()
        #crea attività
        self.navigate_to_and_wait("Attività")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//i[@class="fa fa-plus"]'))
        ).click()  #click su +

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idanagrafica-container"]'))
        ).click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys("Cliente")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-dropdown select2-dropdown--below"]//input'))).send_keys(Keys.ENTER)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idtipointervento-container"]'))
        ).click() #seleziono Generico come tipo di intervento
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input'))).send_keys("Generico")

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--selectable select2-results__option--highlighted"]'))
        ).click()  #click su primo risultato
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).send_keys("Test")   #scrivo "Test" come richiesta
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idordine-container"]'))
        ).click() #aggiungo ordine

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-idordine-results"]//li[2]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))
        ).click()   #click su Aggiungi
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-nuovo_tecnico-container"]'))
        ).click()    #aggiungi sessione

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-nuovo_tecnico-results"]//li[2]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-primary btn-block"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idstatointervento-container"]'))
        ).click()    #click su stato

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[3]'))
        ).send_keys("Completato", Keys.ENTER) #seleziono Completato come nuovo stato
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()

        #fattura attività
        self.navigate_to_and_wait("Attività")

        self.wait_and_click_table_row(1, 1)
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@data-toggle="dropdown"]'))
        ).click() #apro azioni di gruppo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-op="crea_fattura"]'))).click()    #click su crea fattura

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-raggruppamento-container"]'))
        ).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente")    #seleziono cliente
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@id="select2-raggruppamento-results"]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-primary"]'))
        ).click()  #click di conferma
        self.wait_loader()

        stato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[7]'))
        ).text #controllo se lo stato è passato a "Fatturato"
        self.assertEqual(stato, "Fatturato")
        #elimina ordine
        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Ordini cliente") 

        self.wait_for_element_and_click('//tbody//tr[1//td[2]') 
        self.wait_loader()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()
        #elimina fattura
        self.navigate_to_and_wait("Fatture di vendita")

        self.wait_and_click_table_row(1, 2)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@id="elimina"]'))
        ).click() #elimina fattura

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()   #click di conferma
        self.wait_loader()
        #elimina attività
        self.navigate_to_and_wait("Attività")
        
        self.wait_and_click_table_row(1, 2)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger ask"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))
        ).click()
        self.wait_loader()

