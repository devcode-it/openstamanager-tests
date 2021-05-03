from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class FattureVenditaNotaCredito(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")

    def test_creazione_fattura_vendita_nota_credito(self):
        # Crea una nuova nota di credito per il cliente "Cliente". 
        importi = RowManager.list()
        self.creazione_fattura_vendita_nota_credito("Cliente", importi[0])

    def creazione_fattura_vendita_nota_credito(self, cliente: str, file_importi: str):
        # Crea una nuova nota di credito per il cliente indicato. 
        # Apre la schermata di nuovo elemento
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        select = self.input(modal, 'Cliente')
        select.setByText(cliente)

        select = self.input(modal, 'Tipo documento')
        select.setByText("TD04 - Nota di credito")

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

        #toast = self.driver.find_elements(By.CLASS_NAME, 'toast-message')
        #self.assertIn('Aggiunto fattura', toast)

        # Inserisco le righe
        row_manager = RowManager(self)
        row_manager.compile(file_importi)

        # Cambio stato a Emessa
        select = self.input(self.find(By.XPATH, '//div[@id="tab_0"]'), 'Stato*')
        select.setByText("Emessa")

        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        self.wait_loader()

        # Estrazione totali righe
        totale_imponibile = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text
        totale_imponibile = '-'+totale_imponibile
        iva = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[4]//td[2]').text
        totale = self.find(By.XPATH, '//div[@id="tab_0"]//div[@id="righe"]//tbody[2]//tr[5]//td[2]').text
        totale = '-'+totale

        # Controllo Scadenzario
        scadenza_fattura = self.find(By.XPATH, '//div[@id="tab_0"]//strong[text()="Scadenze"]/ancestor::div[1]//following-sibling::p[2]').text
        self.assertEqual(totale, scadenza_fattura[12:21])

        self.driver.execute_script('$("a").removeAttr("target")')
        self.find(By.XPATH, '//div[@id="tab_0"]//strong[text()="Scadenze"]/ancestor::div[1]//following-sibling::a').click()
        self.wait_loader()

        scadenza_scadenzario = self.find(By.XPATH, '//div[@id="tab_0"]//td[@id="totale_utente"]').text
        scadenza_scadenzario = scadenza_scadenzario+' €'
        self.assertEqual(totale, scadenza_scadenzario)

        # Torno alla tabella delle Fatture
        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")

        # Estrazione Totale widgets
        widget_fatturato = self.find(By.XPATH, '(//span[@class="info-box-number"])[1]').text
        widget_crediti = self.find(By.XPATH, '(//span[@class="info-box-number"])[2]').text

        # Confronto i due valori
        self.assertEqual(totale_imponibile, widget_fatturato)
        self.assertEqual(totale, widget_crediti)
        
        # Controllo importi fattura elettronica
        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@id="link-tab_18"]').click()
        self.find(By.XPATH, '//form[@id="form-xml"]/descendant::button').click()
        time.sleep(8)

        self.driver.execute_script('$("a").removeAttr("target")')
        self.find(By.XPATH, '//form[@id="form-xml"]/following-sibling::a[1]').click()
        time.sleep(4)

        perc_iva_FE = self.find(By.XPATH, '//table[@class="tbFoglio"][3]/tbody/tr[1]/td[2]').text
        iva_FE = self.find(By.XPATH, '//table[@class="tbFoglio"][3]/tbody/tr[1]/td[6]').text
        iva_FE ='-'+iva_FE+' €'
        totale_imponibile_FE = self.find(By.XPATH, '//table[@class="tbFoglio"][3]/tbody/tr[1]/td[5]').text
        totale_imponibile_FE = totale_imponibile_FE+' €'
        totale_FE = self.find(By.XPATH, '//table[@class="tbFoglio"][3]/tbody/tr[3]/td[4]').text
        totale_FE = totale_FE+' €'
        scadenza_FE = self.find(By.XPATH, '//table[@class="tbFoglio"][4]/tbody/tr[1]/td[4]').text
        scadenza_FE = scadenza_FE+' €'

        self.assertEqual('22,00', perc_iva_FE)
        self.assertEqual(iva, iva_FE)
        self.assertEqual(totale_imponibile, totale_imponibile_FE)
        self.assertEqual(totale, totale_FE)
        self.assertEqual(totale, scadenza_FE)

        # Estrazione valori Piano dei conti
        super().setUp()
        self.expandSidebar("Contabilità")
        self.navigateTo("Piano dei conti")

        conto_ricavi = self.find(By.XPATH, '(//b[text() = "700 Ricavi"]/ancestor::h5[1]/following-sibling::div//td)[2]').text
        conto_cliente = self.find(By.XPATH, '(//b[text() = "110 Crediti clienti e crediti diversi"]/ancestor::h5[1]/following-sibling::div//button[@class="btn btn-xs btn-primary"]/preceding::td[1])[1]').text
        conto_iva = self.find(By.XPATH, '(//b[text() = "900 Conti transitori"]/ancestor::h5[1]/following-sibling::div//td)[2]').text
        

        self.assertEqual(totale_imponibile, conto_ricavi)
        self.assertEqual(totale, conto_cliente)
        self.assertEqual(iva, conto_iva)

        # Cancellazione fattura
        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]').click()
        self.wait_loader()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
       

