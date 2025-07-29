from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from common.RowManager import RowManager
from common.functions import (
    wait_for_dropdown_and_select,
    wait_for_element_and_click,
    send_keys_and_wait,
    wait_loader,
    search_entity,
    click_first_result,
    clear_filters,
    wait_for_search_results
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
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
        self.registrazioni()
        self.movimenti_contabili()
        self.cambia_sezionale()
        self.duplica_selezionati()
        self.registrazione_contabile()
        self.elimina_selezionati()

    def creazione_fattura_acquisto(self, fornitore: str, numero: str, pagamento: str, file_importi: str):
        self.navigateTo("Fatture di acquisto")
        wait_for_element_and_click(self.driver, self.wait_driver, '//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'N. fattura del fornitore').setValue(numero)
        select = self.input(modal, 'Fornitore')
        select.setByText(fornitore)
        wait_for_element_and_click(self.driver, self.wait_driver, 'button[type="submit"]', By.CSS_SELECTOR)

        select = self.input(self.find(By.XPATH, '//div[@id="tab_0"]'), 'Pagamento')
        select.setByIndex(pagamento)
        row_manager = RowManager(self)
        self.valori = row_manager.compile(file_importi)

    def modifica_fattura_acquisto(self, modifica=str):
        self.navigateTo("Fatture di acquisto")
        click_first_result(self.driver, self.wait_driver)

        wait_for_dropdown_and_select(self.driver, self.wait_driver,
            '//span[@id="select2-idstatodocumento-container"]',
            option_text='Emessa')
        wait_for_element_and_click(self.driver, self.wait_driver, '//div[@id="tab_0"]//button[@id="save"]')

    def controllo_fattura_acquisto(self):
        self.navigateTo("Fatture di acquisto")
        click_first_result(self.driver, self.wait_driver)

        sconto = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[2]//td[2]').text
        totale_imponibile = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text
        iva = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[4]//td[2]').text
        totale = self.find(By.XPATH, '//div[@id="tab_0"]//div[@id="righe"]//tbody[2]//tr[5]//td[2]').text

        self.assertEqual(sconto, self.valori["Sconto/maggiorazione"] + ' €')
        self.assertEqual(totale_imponibile, self.valori["Totale imponibile"] + ' €')
        self.assertEqual(iva, self.valori["IVA"] + ' €')
        self.assertEqual(totale, self.valori["Totale documento"] + ' €')

        scadenza_fattura = self.find(By.XPATH, '//div[@id="tab_0"]//strong[text()="Scadenze"]/ancestor::div[1]//following-sibling::p[2]').text
        self.assertEqual(totale, scadenza_fattura[12:21])
        self.driver.execute_script('$("a").removeAttr("target")')
        wait_for_element_and_click(self.driver, self.wait_driver, '//div[@id="tab_0"]//strong[text()="Scadenze"]/ancestor::div[1]//following-sibling::a')

        totale = '-' + totale
        scadenza_scadenzario = (self.find(By.XPATH, '//div[@id="tab_0"]//td[@id="totale_utente"]').text + ' €')
        self.assertEqual(totale, scadenza_scadenzario)

        self.expandSidebar("Acquisti")
        self.navigateTo("Fatture di acquisto")
        widget_fatturato = self.find(By.XPATH, '(//span[@class="info-box-number"])[1]').text
        widget_crediti = self.find(By.XPATH, '(//span[@class="info-box-number"])[2]').text
        widget_crediti = '-' + widget_crediti

        self.assertEqual(totale_imponibile, widget_fatturato)
        self.assertEqual(totale, widget_crediti)

        self.expandSidebar("Contabilità")
        self.navigateTo("Piano dei conti")

        wait_for_element_and_click(self.driver, self.wait_driver, '//*[@id="conto2-14"]//*[@class="fa fa-plus"]')
        wait_for_element_and_click(self.driver, self.wait_driver, '//*[@id="movimenti-55"]//*[@class="fa fa-plus"]')
        conto_costi = self.find(By.XPATH, '//*[@id="conto_55"]//*[@class="text-right"]').text

        wait_for_element_and_click(self.driver, self.wait_driver, '//*[@id="conto2-8"]//*[@class="fa fa-plus"]')
        wait_for_element_and_click(self.driver, self.wait_driver, '//*[@id="movimenti-126"]//*[@class="fa fa-plus"]')
        conto_fornitore = self.find(By.XPATH, '//*[@id="conto_126"]//*[@class="text-right"]').text
        conto_fornitore = '-' + conto_fornitore

        wait_for_element_and_click(self.driver, self.wait_driver, '//*[@id="conto2-22"]//*[@class="fa fa-plus"]')
        wait_for_element_and_click(self.driver, self.wait_driver, '//*[@id="movimenti-107"]//*[@class="fa fa-plus"]')
        conto_iva = self.find(By.XPATH, '//*[@id="conto_107"]//*[@class="text-right"]').text

        self.assertEqual(totale_imponibile, conto_costi)
        self.assertEqual(totale, conto_fornitore)
        self.assertEqual(iva, conto_iva)

    def elimina_documento(self):
        self.expandSidebar("Acquisti")
        self.navigateTo("Fatture di acquisto")
        click_first_result(self.driver, self.wait_driver)

        wait_for_element_and_click(self.driver, self.wait_driver, '//div[@id="tab_0"]//a[@class="btn btn-danger ask "]')
        wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="swal2-confirm btn btn-lg btn-danger"]')

    def verifica_fattura_acquisto(self):
        self.navigateTo("Fatture di acquisto")
        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        send_keys_and_wait(self.driver, self.wait_driver, search_input, "1", False)

        eliminato = self.driver.find_element(By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)
        clear_filters(self.driver, self.wait_driver)

    def verifica_xml_autofattura(self, file_importi: str, pagamento: str):
        importi = RowManager.list()
        self.creazione_fattura_acquisto("Fornitore Estero", "01", "1", importi[0])
        wait_for_element_and_click(self.driver, self.wait_driver, '//input[@id="check_all"]')
        wait_for_element_and_click(self.driver, self.wait_driver, '//button[@id="modifica_iva_righe"]')
        wait_for_dropdown_and_select(self.driver, self.wait_driver,
            '//span[@id="select2-iva_id-container"]',
            option_text='258 - Non imponibile - cessioni verso San Marino')
        wait_for_element_and_click(self.driver, self.wait_driver, '(//button[@class="btn btn-primary"])[2]')

        wait_for_dropdown_and_select(self.driver, self.wait_driver,
            '//span[@id="select2-idstatodocumento-container"]',
            option_text='Emessa')
        wait_for_element_and_click(self.driver, self.wait_driver, '//div[@id="tab_0"]//button[@id="save"]')
        
        wait_for_dropdown_and_select(self.driver, self.wait_driver,
            '//button[@class="btn btn-primary unblockable dropdown-toggle "]',
            option_xpath='//a[@class="btn dropdown-item bound clickable"]')
        wait_for_dropdown_and_select(self.driver, self.wait_driver,
            '//div[@class="modal-body"]//span[@class="select2-selection select2-selection--single"]',
            option_text='TD17')
        wait_for_element_and_click(self.driver, self.wait_driver, '(//button[@type="submit"])[4]')

        self.driver.execute_script('window.scrollTo(0,0)')
        
        self.input(None,'Stato*').setByText('Emessa')
        wait_for_element_and_click(self.driver, self.wait_driver, '//div[@id="tab_0"]//button[@id="save"]')

        totale_imponibile = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[1]//td[2]').text
        totale = self.find(By.XPATH, '//div[@id="tab_0"]//div[@id="righe"]//tbody[2]//tr[2]//td[2]').text

        self.assertEqual(totale_imponibile, ('264,80 €'))
        self.assertEqual(totale, ('58,26 €'))

    def registrazioni(self):
        self.expandSidebar("Acquisti")
        self.navigateTo("Fatture di acquisto")
        click_first_result(self.driver, self.wait_driver)

        wait_for_element_and_click(self.driver, self.wait_driver, '//a[@id="link-tab_41"]')
        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_41"]//tr[5]//td[1]')))
    def movimenti_contabili(self):
        self.navigateTo("Fatture di acquisto")
        click_first_result(self.driver, self.wait_driver)

        wait_for_element_and_click(self.driver, self.wait_driver, '//a[@id="link-tab_36"]')
        wait_for_element_and_click(self.driver, self.wait_driver, '//a[@class="btn btn-info btn-lg"]')

        avere = self.find(By.XPATH, '//div[@id="tab_36"]//tr//td[4]').text
        self.assertEqual(avere, "251,60 €")

    def cambia_sezionale(self):
        self.navigateTo("Fatture di acquisto")
        wait_for_element_and_click(self.driver, self.wait_driver, '//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        numero_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="numero_esterno"]')))
        numero_input.send_keys("2")
        wait_for_dropdown_and_select(self.driver, self.wait_driver,
            '//span[@id="select2-idanagrafica_add-container"]',
            option_text='Fornitore')
        wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="btn btn-primary"]')

        self.navigateTo("Fatture di acquisto")
        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        send_keys_and_wait(self.driver, self.wait_driver, search_input, "2", False)

        wait_for_element_and_click(self.driver, self.wait_driver, '//tbody//tr//td')
        wait_for_dropdown_and_select(self.driver, self.wait_driver,
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="change_segment"]')

        wait_for_dropdown_and_select(self.driver, self.wait_driver,
            '//span[@id="select2-id_segment-container"]',
            option_text='Autofatture')
        wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="swal2-confirm btn btn-lg btn-warning"]')
        wait_for_dropdown_and_select(self.driver, self.wait_driver,
            '//span[@id="select2-id_segment_-container"]',
            option_text='Autofatture')

        clear_filters(self.driver, self.wait_driver)
        wait_for_element_and_click(self.driver, self.wait_driver, '//tbody//tr[1]//td[1]')
        wait_for_dropdown_and_select(self.driver, self.wait_driver,
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="change_segment"]')
        wait_for_dropdown_and_select(self.driver, self.wait_driver,
            '//span[@id="select2-id_segment-container"]',
            option_text='Standard')
        wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="swal2-confirm btn btn-lg btn-warning"]')
        wait_for_dropdown_and_select(self.driver, self.wait_driver,
            '//span[@id="select2-id_segment_-container"]',
            option_text='Standard')

    def duplica_selezionati(self):
        self.navigateTo("Fatture di acquisto")
        wait_for_element_and_click(self.driver, self.wait_driver, '//tbody//tr//td[1]')
        wait_for_dropdown_and_select(self.driver, self.wait_driver,
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="copy_bulk"]')
        wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        wait_for_element_and_click(self.driver, self.wait_driver, '//tbody//tr//td[2]')
        wait_for_element_and_click(self.driver, self.wait_driver, '//a[@id="elimina"]')
        wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="swal2-confirm btn btn-lg btn-danger"]')

    def registrazione_contabile(self):
        self.navigateTo("Fatture di acquisto")
        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        send_keys_and_wait(self.driver, self.wait_driver, search_input, "2", False)
        click_first_result(self.driver, self.wait_driver)

        self.driver.execute_script('window.scrollTo(0,0)')
        
        wait_for_dropdown_and_select(self.driver, self.wait_driver,
            '//span[@id="select2-idpagamento-container"]',
            option_text='Assegno')
            
        self.driver.execute_script('window.scrollTo(0,0)')
        
        numero_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="numero_esterno"]')))
        numero_input.send_keys("2")

        wait_for_element_and_click(self.driver, self.wait_driver, '//a[@class="btn btn-primary"]')

        descrizione_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]')))
        descrizione_input.send_keys("Prova")
        prezzo_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]')))
        prezzo_input.send_keys("1")
        wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="btn btn-primary pull-right"]')

        self.input(None,'Stato*').setByText('Emessa')
        wait_for_element_and_click(self.driver, self.wait_driver, '//button[@id="save"]')

        self.navigateTo("Fatture di acquisto")
        wait_for_element_and_click(self.driver, self.wait_driver, '//tbody//tr//td[1]')
        wait_for_element_and_click(self.driver, self.wait_driver, '//button[@data-toggle="dropdown"]')
        wait_for_element_and_click(self.driver, self.wait_driver, '//a[@data-op="registrazione_contabile"]')

        prezzo = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="totale_avere"]'))).text
        self.assertEqual(prezzo, "1,22 €")

        wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="close"]')
        clear_filters(self.driver, self.wait_driver)
        self.wait_loader()

    def elimina_selezionati(self):
        self.navigateTo("Fatture di acquisto")
        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]//input')))
        send_keys_and_wait(self.driver, self.wait_driver, search_input, "2", False)

        wait_for_element_and_click(self.driver, self.wait_driver, '//tbody//tr//td')
        wait_for_dropdown_and_select(self.driver, self.wait_driver,
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="delete_bulk"]')
        wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        scritta = self.find(By.XPATH, '//tbody//tr//td').text
        self.assertEqual(scritta, "La ricerca non ha portato alcun risultato.")
        clear_filters(self.driver, self.wait_driver)