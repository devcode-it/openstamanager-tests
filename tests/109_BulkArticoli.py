from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Articoli(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Magazzino")
        self.wait_loader()

    def test_bulk_articolo(self):
        self.aggiorna_iva()
        #TODO: Aggiorna categoria e sottocategoria
        #self.aggiorna_categoria()
        self.coefficiente_vendita()
        self.conto_predefinito_acquisto()
        self.conto_predefinito_vendita()
        self.aggiorna_prezzo_acquisto()
        self.aggiorna_prezzo_vendita()
        self.aggiorna_quantita()
        self.aggiorna_unita_misura()
        #TODO: Aggiungi a listino cliente
        #self.aggiungi_a_listino_cliente()
        #TODO: Attiva/Disattiva articoli
        #self.attiva_disattiva_articoli()
        self.elimina_selezionati()
        #TODO: Esporta
        #self.esporta_selezionati()
        self.crea_preventivo()
        #TODO: Genera barcode
        #self.genera_barcode()
        self.imposta_prezzo_da_fattura()
        self.imposta_provvigione()
        self.stampa_etichette()
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')

    def aggiorna_iva(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))
        )
        self.send_keys_and_wait(search_input, '08', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_vat"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_iva-container"]', option_text='Iva 10%')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        iva = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idiva_vendita-container"]'))
        ).text
        self.assertEqual(iva[2:20], "10 - Aliq. Iva 10%")

        self.navigateTo("Articoli")
        self.wait_loader()
        self.clear_filters()
    def coefficiente_vendita(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))
        )
        self.send_keys_and_wait(search_input, '08', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_coefficient"]')

        coefficiente_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="coefficiente"]'))
        )
        coefficiente_input.send_keys("12")

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        prezzo = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[9]//div'))
        ).text
        self.assertEqual(prezzo, "13,20")

        self.clear_filters()
    def conto_predefinito_acquisto(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))
        )
        self.send_keys_and_wait(search_input, '08', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_purchase_account"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-conto_acquisto-container"]', option_text='Fabbricati')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.click_first_result()

        conto = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idconto_acquisto-container"]'))
        ).text
        self.assertEqual(conto[2:24], "220.000010 Fabbricati")

        self.navigateTo("Articoli")
        self.wait_loader()
        self.clear_filters()
    def conto_predefinito_vendita(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))
        )
        self.send_keys_and_wait(search_input, '08', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_sale_account"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-conto_vendita-container"]', option_text='Automezzi')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.click_first_result()

        conto = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-idconto_vendita-container"]'))
        ).text
        self.assertEqual(conto[2:24], "220.000030 Automezzi")

        self.navigateTo("Articoli")
        self.wait_loader()
        self.clear_filters()
    def aggiorna_prezzo_acquisto(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        self.wait_modal()

        codice_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="codice"]'))
        )
        codice_input.send_keys("08")

        descrizione_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione"]'))
        )
        descrizione_input.send_keys("Prova")

        self.wait_for_element_and_click('//button[@class="btn btn-primary"]')

        prezzo_acquisto = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_acquisto"]'))
        )
        prezzo_acquisto.send_keys("1")

        prezzo_vendita = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_vendita"]'))
        )
        prezzo_vendita.send_keys("1")

        self.wait_for_element_and_click('//button[@id="save"]')

        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))
        )
        self.send_keys_and_wait(search_input, '08', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_purchase_price"]')

        percentuale_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="percentuale"]'))
        )
        percentuale_input.send_keys("10")

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        prezzo = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[8]'))
        ).text
        self.assertEqual(prezzo, "1,10")

        self.clear_filters()
    def aggiorna_prezzo_vendita(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))
        )
        self.send_keys_and_wait(search_input, '08', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_sale_price"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-prezzo_partenza-container"]', option_text='Prezzo di vendita')

        percentuale_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="percentuale"]'))
        )
        percentuale_input.send_keys("20")

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        prezzo = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[9]'))
        ).text
        self.assertEqual(prezzo, "0,98")

        self.clear_filters()
    def aggiorna_quantita(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))
        )
        self.send_keys_and_wait(search_input, '08', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_quantity"]')

        qta_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="qta"]'))
        )
        qta_input.send_keys("3")

        descrizione_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="descrizione"]'))
        )
        descrizione_input.send_keys("test")

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        quantita = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[10]'))
        ).text
        self.assertEqual(quantita, "3,00")

        self.clear_filters()
    def aggiorna_unita_misura(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))
        )
        self.send_keys_and_wait(search_input, '08', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_unit"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-um-container"]', option_text='ore')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.wait_for_element_and_click('(//i[@class="fa fa-plus"])[2]')

        unita_misura = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-um-container"]'))).text
        self.assertEqual(unita_misura[2:5], "ore")

        self.navigateTo("Articoli")
        self.wait_loader()
        self.clear_filters()
    def elimina_selezionati(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))
        )
        self.send_keys_and_wait(search_input, '08', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="delete_bulk"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        risultato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td'))
        ).text
        self.assertEqual(risultato, "Nessun dato presente nella tabella")

        self.clear_filters()
    def crea_preventivo(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))
        )
        self.send_keys_and_wait(search_input, '08', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="create_estimate"]')

        nome_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))
        )
        nome_input.send_keys("Prova")

        self.wait_for_dropdown_and_select('//span[@id="select2-id_cliente-container"]', option_text='Cliente')
        self.wait_for_dropdown_and_select('//span[@id="select2-id_segment-container"]', option_text='Standard preventivi')
        self.wait_for_dropdown_and_select('//span[@id="select2-id_tipo-container"]', option_text='Generico')

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.wait_for_element_and_click('//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.expandSidebar("Magazzino")
        self.navigateTo("Articoli")
        self.wait_loader()
        self.clear_filters()
    def imposta_prezzo_da_fattura(self):
        self.expandSidebar("Acquisti")
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        numero_esterno = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="numero_esterno"]'))
        )
        numero_esterno.send_keys("04")

        self.wait_for_dropdown_and_select('//span[@id="select2-idanagrafica_add-container"]', option_text='Fornitore')

        self.wait_for_element_and_click('//div[@class="modal-footer"]//button[@class="btn btn-primary"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_articolo-container"]', option_text='Articolo 1')

        self.wait_for_element_and_click('//button[@class="btn btn-primary tip tooltipstered"]')
        self.wait_for_element_and_click('//a[@class="btn btn-xs btn-warning"]')

        prezzo_unitario = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))
        )
        prezzo_unitario.send_keys("10")

        self.wait_for_element_and_click('//button[@class="btn btn-primary pull-right"]')
        self.wait_for_element_and_click('//button[@id="save"]')

        self.expandSidebar("Magazzino")
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))
        )
        self.send_keys_and_wait(search_input, '001', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="set_purchase_price_if_zero"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        prezzo = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[8]'))
        ).text
        self.assertEqual(prezzo, "20,00")

        self.clear_filters()

        self.expandSidebar("Acquisti")
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()

        self.click_first_result()
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask "]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.expandSidebar("Magazzino")
    def imposta_provvigione(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))
        )
        self.send_keys_and_wait(search_input, '08', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="set_commission"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-idagente-container"]', option_text='Agente')

        provvigione_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="provvigione"]'))
        )
        provvigione_input.send_keys("10")

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.click_first_result()
        self.wait_for_element_and_click('//a[@id="link-tab_43"]')

        provvigione = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_43" ]//tr[1]//td[3]//div)[2]'))
        ).text
        self.assertEqual(provvigione, "10.00 %")

        self.navigateTo("Articoli")
        self.wait_loader()
        self.clear_filters()
    def stampa_etichette(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))
        )
        self.send_keys_and_wait(search_input, '08', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="print_labels"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.driver.switch_to.window(self.driver.window_handles[1])

        prezzo = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="viewer"]//span)[3]'))).text
        self.assertEqual(prezzo, "13,20 €")

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.wait_for_element_and_click('//tbody//tr//td')
        self.clear_filters()












