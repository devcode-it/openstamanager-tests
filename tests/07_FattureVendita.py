from common.Test import Test
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class FattureVendita(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Vendite")

    def test_creazione_fattura_vendita(self):
        importi = RowManager.list()

        self.creazione_fattura_vendita("Cliente", importi[0])
        self.duplica()
        self.modifica_fattura_vendita("Emessa")
        #self.controllo_fattura_vendita()

        self.creazione_nota_credito()
        self.modifica_nota_credito("Emessa")
        #self.controllo_nota_credito()
        self.controllo_fattura_nota_credito()

        self.elimina_documento()
        self.verifica_fattura_di_vendita()
        self.verifica_xml_fattura_estera(importi[0], "1")

        self.movimenti_contabili()
        self.plugin_movimenti_contabili()
        self.regole_pagamenti()
        self.registrazioni()
        self.controlla_allegati()

        self.duplica_selezionati()
        self.cambia_sezionale()
        self.emetti_fatture()
        self.statistiche_vendita()
        self.controlla_fatture_elettroniche()
        self.registrazione_contabile()
        self.genera_fatture_elettroniche()
        self.elimina_selezionati()

    def creazione_fattura_vendita(self, cliente: str, file_importi: str):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        select = self.input(modal, 'Cliente')
        select.setByText(cliente)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

        row_manager = RowManager(self)
        self.valori = row_manager.compile(file_importi)

    def duplica(self):
        self.wait_for_element_and_click('//button[@class="btn btn-primary ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-primary"]')

    def modifica_fattura_vendita(self, modifica = str):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.click_first_result()
        self.input(None, 'Stato*').setByText(modifica)
        self.driver.execute_script('window.scrollTo(0,0)')
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

    def controllo_fattura_vendita(self):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()
        self.click_first_result()

        sconto = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="righe"]//tbody[2]//tr[2]//td[2]'))).text
        totale_imponibile = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]'))).text
        iva = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="righe"]//tbody[2]//tr[4]//td[2]'))).text
        totale = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//div[@id="righe"]//tbody[2]//tr[5]//td[2]'))).text

        self.assertEqual(sconto, (self.valori["Sconto/maggiorazione"] + ' €'))
        self.assertEqual(totale_imponibile, (self.valori["Totale imponibile"] + ' €'))
        self.assertEqual(iva, (self.valori["IVA"] + ' €'))
        self.assertEqual(totale, (self.valori["Totale documento"] + ' €'))

        scadenza_fattura = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//strong[text()="Scadenze"]/ancestor::div[1]//following-sibling::p[2]'))).text
        self.assertEqual(totale, scadenza_fattura[12:20])

        self.driver.execute_script('$("a").removeAttr("target")')
        self.wait_for_element_and_click('//div[@id="tab_0"]//strong[text()="Scadenze"]/ancestor::div[1]//following-sibling::a')

        scadenza_scadenzario = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//td[@id="totale_utente"]'))).text + ' €'
        self.assertEqual(totale, scadenza_scadenzario)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        widget_fatturato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//span[@class="info-box-number"])[1]'))).text
        widget_crediti = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//span[@class="info-box-number"])[2]'))).text
        self.assertEqual(totale_imponibile, widget_fatturato)
        self.assertEqual(totale, widget_crediti)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//a[@id="link-tab_18"]')
        self.wait_for_element_and_click('//div[@class="text-center"]//a[@class="btn btn-info btn-lg "]')

        self.driver.switch_to.window(self.driver.window_handles[1])
        perc_iva_FE = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//table[@class="tbFoglio"][3]/tbody/tr[1]/td[2]'))).text
        iva_FE = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//table[@class="tbFoglio"][3]/tbody/tr[1]/td[6]'))).text
        totale_imponibile_FE = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//table[@class="tbFoglio"][3]/tbody/tr[1]/td[5]'))).text + ' €'
        totale_FE = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//table[@class="tbFoglio"][3]/tbody/tr[3]/td[4]'))).text + ' €'
        scadenza_FE = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//table[@class="tbFoglio"][4]/tbody/tr[1]/td[4]'))).text + ' €'

        self.assertEqual('22,00', perc_iva_FE)
        self.assertEqual((self.valori["IVA"]), iva_FE)
        self.assertEqual((self.valori["Totale imponibile"]+ ' €'), totale_imponibile_FE)
        self.assertEqual((self.valori["Totale documento"] + ' €'), totale_FE)
        self.assertEqual((self.valori["Totale documento"] + ' €'), scadenza_FE)

        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.close()

        super().setUp()
        self.expandSidebar("Contabilità")
        self.navigateTo("Piano dei conti")
        self.wait_loader()

        self.wait_for_element_and_click('//*[@id="conto2-20"]//*[@class="fa fa-plus"]')
        self.wait_for_element_and_click('//*[@id="movimenti-94"]//*[@class="fa fa-plus"]')
        conto_ricavi = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="conto_94"]//*[@class="text-right"]'))).text

        self.wait_for_element_and_click('//*[@id="conto2-2"]//*[@class="fa fa-plus"]')
        self.wait_for_element_and_click('//*[@id="movimenti-125"]//*[@class="fa fa-plus"]')
        conto_cliente = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="conto_125"]//*[@class="text-right"]'))).text

        self.wait_for_element_and_click('//*[@id="conto2-22"]//*[@class="fa fa-plus"]')
        self.wait_for_element_and_click('//*[@id="movimenti-106"]//*[@class="fa fa-plus"]')
        conto_iva = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="conto_106"]//*[@class="text-right"]'))).text

        self.assertEqual(totale_imponibile, conto_ricavi)
        self.assertEqual(totale, conto_cliente)
        self.assertEqual(iva, conto_iva)
        self.expandSidebar("Vendite")

    def creazione_nota_credito(self):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_dropdown_and_select(
            '//button[@class="btn btn-primary unblockable dropdown-toggle "]',
            option_xpath='//a[@class="btn dropdown-item bound clickable"]'
        )
        modal = self.wait_modal()
        self.wait_for_element_and_click('//button[@id="submit_btn"]')

    def modifica_nota_credito(self, modifica = str):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[3]//td[2]')
        self.input(None,'Stato*').setByText(modifica)
        self.driver.execute_script('window.scrollTo(0,0)')
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

    def controllo_nota_credito(self):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()
        self.wait_for_element_and_click('//td[@class="bound clickable"]')

        totale_imponibile = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]'))).text
        totale_imponibile = '-'+totale_imponibile
        iva = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="righe"]//tbody[2]//tr[4]//td[2]'))).text
        totale = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//div[@id="righe"]//tbody[2]//tr[5]//td[2]'))).text

        scadenza_fattura = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//strong[text()="Scadenze"]/ancestor::div[1]//following-sibling::p[2]'))).text
        self.assertEqual(totale, scadenza_fattura[12:21])

        self.wait_for_element_and_click('//div[@class="btn-group pull-right"]')

        self.driver.switch_to.window(self.driver.window_handles[1])
        scadenza_scadenzario = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//body//tr//td)[5]'))).text
        self.assertEqual(totale, scadenza_scadenzario)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//div[@id="tab_0"]//tbody//tr[1]//td[2]')
        self.wait_for_element_and_click('//a[@id="link-tab_18"]')
        self.wait_for_element_and_click('//form[@id="form-xml"]/following-sibling::a[1]')

        self.driver.switch_to.window(self.driver.window_handles[1])
        perc_iva_FE = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//table[@class="tbFoglio"][3]/tbody/tr[1]/td[2]'))).text
        iva_FE = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//table[@class="tbFoglio"][3]/tbody/tr[1]/td[6]'))).text
        iva_FE = iva_FE+' €'
        totale_imponibile_FE = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//table[@class="tbFoglio"][3]/tbody/tr[1]/td[5]'))).text
        totale_imponibile_FE = '-'+totale_imponibile_FE+' €'
        totale_FE = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//table[@class="tbFoglio"][3]/tbody/tr[3]/td[4]'))).text
        totale_FE = totale_FE+' €'
        scadenza_FE = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//table[@class="tbFoglio"][4]/tbody/tr[1]/td[4]'))).text
        scadenza_FE = scadenza_FE+' €'

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

        super().setUp()
        self.expandSidebar("Contabilità")
        self.navigateTo("Piano dei conti")
        self.wait_loader()

        self.wait_for_element_and_click('//*[@id="conto2-20"]//*[@class="fa fa-plus"]')
        self.wait_for_element_and_click('//*[@id="movimenti-94"]//*[@class="fa fa-plus"]')
        conto_ricavi = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="conto_94"]//*[@class="text-right"]'))).text

        self.wait_for_element_and_click('//*[@id="conto2-2"]//*[@class="fa fa-plus"]')
        self.wait_for_element_and_click('//*[@id="movimenti-125"]//*[@class="fa fa-plus"]')
        conto_cliente = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="conto_125"]//*[@class="text-right"]'))).text

        self.wait_for_element_and_click('//*[@id="conto2-22"]//*[@class="fa fa-plus"]')
        self.wait_for_element_and_click('//*[@id="movimenti-106"]//*[@class="fa fa-plus"]')
        conto_iva = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="conto_106"]//*[@class="text-right"]'))).text

        conto_iva= '-'+ conto_iva
        conto_ricavi = '-' + conto_ricavi

        self.assertEqual(totale_imponibile, conto_ricavi)
        self.assertEqual(totale, conto_cliente)
        self.assertEqual(iva, conto_iva)

        self.expandSidebar("Vendite")

    def controllo_fattura_nota_credito(self):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        fattura = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[2]//td[6]'))).text
        notacredito = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[6]'))).text
        fattura = '-'+ fattura
        self.assertEqual(fattura, notacredito)

    def elimina_documento(self):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr[3]//td[2]')
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask "]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

    def verifica_fattura_di_vendita(self):
        self.expandSidebar("Acquisti")
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        select = self.input(modal, 'Fornitore')
        select.setByText("Fornitore Estero")
        self.input(modal, 'N. fattura del fornitore').setValue("02")
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def verifica_xml_fattura_estera(self, file_importi: str, pagamento: str):
        self.input(self.find(By.XPATH, '//div[@id="tab_0"]'), 'Pagamento').setByIndex(pagamento)
        row_manager = RowManager(self)
        row_manager.compile(file_importi)

        self.wait_for_element_and_click('//input[@id="check_all"]')
        self.wait_for_element_and_click('//button[@id="modifica_iva_righe"]')
        self.wait_for_dropdown_and_select(
            '//span[@id="select2-iva_id-container"]',
            option_text='258 - Non imponibile - cessioni verso San Marino')
        self.wait_for_element_and_click('(//button[@class="btn btn-primary"])[2]')

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-idstatodocumento-container"]',
            option_text='Emessa')
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.wait_for_element_and_click('//button[@class="btn btn-primary unblockable dropdown-toggle "]')
        self.wait_for_element_and_click('//a[@class="btn dropdown-item bound clickable"]')
        self.wait_for_element_and_click('//div[@class="modal-body"]//span[@class="select2-selection select2-selection--single"]')
        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input[@type="search"]'))), "TD17", False)
        self.wait_for_element_and_click('//div[@class="modal-body"]//button[@type="submit"]')

        self.input(None,'Stato*').setByText("Emessa")
        self.driver.execute_script('window.scrollTo(0,0)')
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        totale_imponibile = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="righe"]//tbody[2]//tr[1]//td[2]'))).text
        iva = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="righe"]//tbody[2]//tr[2]//td[2]'))).text
        totale = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//div[@id="righe"]//tbody[2]//tr[3]//td[2]'))).text

        self.assertEqual(totale_imponibile, '264,80 €')
        self.assertEqual(iva, '58,26 €')
        self.assertEqual(totale, '323,06 €')

    def movimenti_contabili(self):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Tipo"]/input')))
        self.send_keys_and_wait(search_input, "Fattura immediata di vendita", False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//a[@id="link-tab_37"]')
        self.wait_for_element_and_click('//a[@class="btn btn-info btn-lg"]')

        dare_1 = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_37"]//tbody//td)[3]'))).text
        dare_2 = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_37"]//tbody//td)[23]'))).text
        avere_1 = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_37"]//tbody//td)[9]'))).text
        avere_2 = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_37"]//tbody//td)[14]'))).text
        avere_3 = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_37"]//tbody//td)[19]'))).text
        avere_4 = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_37"]//tbody//td)[29]'))).text
        avere_5 = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_37"]//tbody//td)[34]'))).text

        self.assertEqual(dare_1, "305,98 €")
        self.assertEqual(dare_2, "27,20 €")
        self.assertEqual(avere_1, "2,00 €")
        self.assertEqual(avere_2, "150,00 €")
        self.assertEqual(avere_3, "120,00 €")
        self.assertEqual(avere_4, "6,00 €")
        self.assertEqual(avere_5, "55,18 €")

        self.navigateTo("Fatture di vendita")
        self.wait_loader()
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

    def plugin_movimenti_contabili(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.search_entity("Cliente")
        self.click_first_result()

        self.wait_for_element_and_click('//a[@id="link-tab_38"]')
        self.wait_for_element_and_click('//div[@id="tab_38"]//a[@class="btn btn-info btn-lg"]')

        dare = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_38"]//tr[1]//td[3]'))).text
        self.assertEqual(dare, "305,98 €")

        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

    def regole_pagamenti(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.search_entity("Cliente")
        self.click_first_result()

        self.wait_for_element_and_click('//a[@id="link-tab_40"]')
        self.wait_for_element_and_click('//div[@id="tab_40"]//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.wait_for_dropdown_and_select(
            '//*[@id="select2-mese-container"]',
            option_text='Agosto'
        )
        self.wait_for_dropdown_and_select(
            '//*[@id="select2-giorno_fisso-container"]',
            option_text='8'
        )
        self.wait_for_element_and_click('(//button[@type="submit"])[3]')

        self.wait_for_element_and_click('//div[@id="tab_40"]//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.wait_for_dropdown_and_select(
            '//*[@id="select2-mese-container"]',
            option_text='Aprile'
        )
        self.wait_for_dropdown_and_select(
            '//*[@id="select2-giorno_fisso-container"]',
            option_text='8'
        )
        self.wait_for_element_and_click('(//button[@type="submit"])[3]')

        self.wait_for_element_and_click('//div[@id="tab_40"]//tbody//tr//td[2]')
        self.wait_for_element_and_click('//button[@class="btn btn-danger "]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.expandSidebar("Contabilità")
        self.navigateTo("Scadenzario")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Anagrafica"]/input')))
        self.send_keys_and_wait(search_input, 'Cliente', False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        element = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_concordata0"]')))
        element.send_keys('13/08/2025')

        self.wait_for_element_and_click('//button[@id="save"]')
        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="alert alert-warning"]')))

        element = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_concordata0"]')))
        element.clear()
        element.send_keys('20/01/2025')

        self.wait_for_element_and_click('//button[@id="save"]')
        self.wait_driver.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="alert alert-warning"]')))

        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')
        self.expandSidebar("Vendite")

    def registrazioni(self):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Tipo"]/input')))
        self.send_keys_and_wait(search_input, "Fattura immediata di vendita", False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//a[@id="link-tab_42"]')
        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_42"]//tr[5]//td')))

        self.navigateTo("Fatture di vendita")
        self.wait_loader()
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

    def controlla_allegati(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.search_entity("Cliente")
        self.click_first_result()

        self.wait_for_element_and_click('//a[@id="link-tab_30"]')
        self.wait_for_element_and_click('//div[@id="tab_30"]//a[@class="btn btn-info btn-lg"]')
        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_30"]//a[@class="btn btn-xs btn-primary"]')))

        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')
        self.expandSidebar("Vendite")

    def duplica_selezionati(self):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="copy_bulk"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')
        self.wait_for_element_and_click('//tbody//tr//td')

    def cambia_sezionale(self):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_segment"]')

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_segment-container"]',
            option_text='Autofatture'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')
        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_segment_-container"]',
            option_text='Autofatture'
        )

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_segment"]')

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_segment-container"]',
            option_text='Standard vendite'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')
        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_segment_-container"]',
            option_text='Standard vendite'
        )

    def emetti_fatture(self):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_status"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        stato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[11]'))).text
        self.assertEqual(stato, "Emessa")
        self.wait_for_element_and_click('//tbody//tr//td')

    def statistiche_vendita(self):
        self.expandSidebar("Magazzino")
        self.navigateTo("Articoli")
        self.wait_loader()

        self.wait_for_element_and_click('//a[@id="link-tab_44"]')
        self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_44"]//tbody//tr//td')))
        self.expandSidebar("Vendite")

    def controlla_fatture_elettroniche(self):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="check_bulk"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait_for_element_and_click('//div[@class="toast toast-success"]')
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def registrazione_contabile(self):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input')))
        self.send_keys_and_wait(search_input, "0001", False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="registrazione_contabile"]')

        totale = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="totale_dare"]'))).text
        self.assertEqual(totale, "305,98 €")

        self.wait_for_element_and_click('//button[@type="submit"]')

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

    def genera_fatture_elettroniche(self):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="generate_xml"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.driver.switch_to.window(self.driver.window_handles[1])

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//button[@class="btn btn-xs btn-info"]')
        self.wait_for_element_and_click('//button[@class="close"]')

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.navigateTo("Fatture di vendita")
        self.wait_loader()
        self.wait_for_element_and_click('//tbody//tr//td')

    def elimina_selezionati(self):
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="delete_bulk"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        test = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[2]'))).text
        self.assertEqual(test, "0002/2025")
