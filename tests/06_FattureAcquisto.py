from common.Test import Test
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class FattureAcquisto(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Acquisti")

    def test_creazione_fattura_acquisto(self):
        importi = RowManager.list()
        self.creazione_fattura_acquisto("Fornitore", "1", "1", importi[0])
        self.modifica_fattura_acquisto("Emessa")
        self.controllo_fattura_acquisto()
        self.elimina_documento()
        self.verifica_fattura_acquisto()
        self.verifica_xml_autofattura(importi[0], "1")


    def creazione_fattura_acquisto(self, fornitore: str, numero: str, pagamento: str, file_importi: str):
        self.navigateTo("Fatture di acquisto")
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'N. fattura del fornitore').setValue(numero)
        select = self.input(modal, 'Fornitore')
        select.setByText(fornitore)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

        select = self.input(self.find(By.XPATH, '//div[@id="tab_0"]'), 'Pagamento')
        select.setByIndex(pagamento)
        row_manager = RowManager(self)
        self.valori = row_manager.compile(file_importi)

    def modifica_fattura_acquisto(self, modifica = str):
        self.navigateTo("Fatture di acquisto")
        self.click_first_result()

        self.wait_for_dropdown_and_select('//span[@id="select2-idstatodocumento-container"]', option_text='Emessa')
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

    def controllo_fattura_acquisto(self):
        self.navigateTo("Fatture di acquisto")
        self.click_first_result()

        sconto = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="righe"]//tbody[2]//tr[2]//td[2]'))
        ).text
        totale_imponibile = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]'))
        ).text
        iva = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="righe"]//tbody[2]//tr[4]//td[2]'))
        ).text
        totale = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//div[@id="righe"]//tbody[2]//tr[5]//td[2]'))
        ).text

        self.assertEqual(sconto, self.valori["Sconto/maggiorazione"] + ' €')
        self.assertEqual(totale_imponibile, self.valori["Totale imponibile"] + ' €')
        self.assertEqual(iva, self.valori["IVA"] + ' €')
        self.assertEqual(totale, self.valori["Totale documento"] + ' €')

        scadenza_fattura = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//strong[text()="Scadenze"]/ancestor::div[1]//following-sibling::p[2]'))
        ).text
        self.assertEqual(totale, scadenza_fattura[12:21])
        self.driver.execute_script('$("a").removeAttr("target")')
        self.wait_for_element_and_click('//div[@id="tab_0"]//strong[text()="Scadenze"]/ancestor::div[1]//following-sibling::a')

        totale = '-' + totale
        scadenza_scadenzario = (self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//td[@id="totale_utente"]'))
        ).text + ' €')
        self.assertEqual(totale, scadenza_scadenzario)

        self.expandSidebar("Acquisti")
        self.navigateTo("Fatture di acquisto")
        widget_fatturato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//span[@class="info-box-number"])[1]'))
        ).text
        widget_crediti = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//span[@class="info-box-number"])[2]'))
        ).text
        widget_crediti = '-' + widget_crediti

        self.assertEqual(totale_imponibile, widget_fatturato)
        self.assertEqual(totale, widget_crediti)

        self.expandSidebar("Contabilità")
        self.navigateTo("Piano dei conti")

        self.wait_for_element_and_click('//*[@id="conto2-14"]//*[@class="fa fa-plus"]')
        self.wait_for_expanded_element('//*[@id="conto2-14"]')
        self.wait_for_element_and_click('//*[@id="movimenti-55"]//*[@class="fa fa-plus"]')
        self.wait_for_expanded_element('//*[@id="conto_55"]')
        conto_costi = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="conto_55"]//*[@class="text-right"]'))
        ).text

        self.wait_for_element_and_click('//*[@id="conto2-8"]//*[@class="fa fa-plus"]')
        self.wait_for_expanded_element('//*[@id="conto2-8"]')
        self.wait_for_element_and_click('//*[@id="movimenti-126"]//*[@class="fa fa-plus"]')
        self.wait_for_expanded_element('//*[@id="conto_126"]')
        conto_fornitore = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="conto_126"]//*[@class="text-right"]'))
        ).text
        conto_fornitore = '-' + conto_fornitore

        self.wait_for_element_and_click('//*[@id="conto2-22"]//*[@class="fa fa-plus"]')
        self.wait_for_expanded_element('//*[@id="conto2-22"]')
        self.wait_for_element_and_click('//*[@id="movimenti-107"]//*[@class="fa fa-plus"]')
        self.wait_for_expanded_element('//*[@id="conto_107"]')
        conto_iva = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="conto_107"]//*[@class="text-right"]'))
        ).text

        self.assertEqual(totale_imponibile, conto_costi)
        self.assertEqual(totale, conto_fornitore)
        self.assertEqual(iva, conto_iva)

        self.expandSidebar("Acquisti")

    def elimina_documento(self):
        self.navigateTo("Fatture di acquisto")
        self.click_first_result()

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask "]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

    def verifica_fattura_acquisto(self):
        self.navigateTo("Fatture di acquisto")
        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        self.send_keys_and_wait(search_input, "1", False)

        eliminato = self.driver.find_element(By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)
        self.clear_filters()

    def verifica_xml_autofattura(self, file_importi: str, pagamento: str):
        importi = RowManager.list()
        self.creazione_fattura_acquisto("Fornitore Estero", "01", "1", importi[0])

        self.wait_for_element_and_click('//input[@id="check_all"]')
        self.wait_for_element_and_click('//button[@id="modifica_iva_righe"]')
        self.wait_for_dropdown_and_select('//span[@id="select2-iva_id-container"]', option_text='258 - Non imponibile - cessioni verso San Marino')
        self.wait_for_element_and_click('(//button[@class="btn btn-primary"])[2]')

        self.wait_for_dropdown_and_select('//span[@id="select2-idstatodocumento-container"]', option_text='Emessa')
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.wait_for_dropdown_and_select('//button[@class="btn btn-primary unblockable dropdown-toggle "]', option_xpath='//a[@class="btn dropdown-item bound clickable"]')
        self.wait_for_dropdown_and_select('//div[@class="modal-body"]//span[@class="select2-selection select2-selection--single"]', option_text='TD17')
        self.wait_for_element_and_click('(//button[@type="submit"])[4]')

        self.driver.execute_script('window.scrollTo(0,0)')
        self.input(None,'Stato*').setByText('Emessa')
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        totale_imponibile = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[1]//td[2]').text
        totale = self.find(By.XPATH, '//div[@id="tab_0"]//div[@id="righe"]//tbody[2]//tr[2]//td[2]').text

        self.assertEqual(totale_imponibile, ('264,80 €'))
        self.assertEqual(totale, ('58,26 €'))
