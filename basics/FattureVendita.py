from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class FattureVendita(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")

    def test_creazione_fattura_vendita(self):
        # Crea una nuova fattura per il cliente "Cliente". 
        importi = RowManager.list()
        self.creazione_fattura_vendita("Cliente", importi[0])

    def creazione_fattura_vendita(self, cliente: str, file_importi: str):
        # Crea una nuova fattura per il cliente indicato. 
        # Apre la schermata di nuovo elemento
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        select = self.input(modal, 'Cliente')
        select.setByText(cliente)

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
        iva = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[4]//td[2]').text
        iva = '-'+iva
        totale = self.find(By.XPATH, '//div[@id="tab_0"]//div[@id="righe"]//tbody[2]//tr[5]//td[2]').text

        # Controllo Scadenzario
        scadenza_fattura = self.find(By.XPATH, '//div[@id="tab_0"]//strong[text()="Scadenze"]/ancestor::div[1]//following-sibling::p[2]').text
        self.assertEqual(totale, scadenza_fattura[12:20])

        self.driver.execute_script('$("a").removeAttr("target")')
        self.find(By.XPATH, '//div[@id="tab_0"]//strong[text()="Scadenze"]/ancestor::div[1]//following-sibling::a').click()
        self.wait_loader()

        scadenza_scadenzario = self.find(By.XPATH, '//div[@id="tab_0"]//td[@id="totale_utente"]').text
        scadenza_scadenzario = scadenza_scadenzario+' €'
        print(scadenza_scadenzario)
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

        # Estrazione valori Piano dei conti
        self.expandSidebar("Contabilità")
        self.navigateTo("Piano dei conti")

        conto_ricavi = self.find(By.XPATH, '(//b[text() = "700 Ricavi"]/ancestor::h5[1]/following-sibling::div//td)[2]').text
        conto_cliente = self.find(By.XPATH, '(//b[text() = "110 Crediti clienti e crediti diversi"]/ancestor::h5[1]/following-sibling::div//button[@class="btn btn-xs btn-primary"]/preceding::td[1])[1]').text
        conto_iva = self.find(By.XPATH, '(//b[text() = "900 Conti transitori"]/ancestor::h5[1]/following-sibling::div//td)[2]').text
        

        self.assertEqual(totale_imponibile, conto_ricavi)
        self.assertEqual(totale, conto_cliente)
        self.assertEqual(iva, conto_iva)


       

