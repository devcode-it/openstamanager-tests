from common.Test import Test
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Articoli(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Magazzino")
        self.wait_loader()

    def test_creazione_articolo(self):
        self.creazione_articolo("001", "Articolo 1", "2")
        self.creazione_articolo("002", "Articolo di Prova da Eliminare", "2")
        self.modifica_articolo("20", "1")
        self.elimina_articolo()
        self.verifica_articolo()
        self.serial()
        self.provvigioni()
        self.listino_fornitori()
        self.giacenze()
        self.statistiche()
        self.netto_clienti()
        self.aggiorna_prezzo_acquisto()
        self.aggiorna_prezzo_vendita()
        self.coefficiente_vendita()
        self.aggiorna_quantita()
        self.crea_preventivo()
        self.aggiorna_iva()
        self.aggiorna_unita_misura()
        self.conto_predefinito_acquisto()
        self.conto_predefinito_vendita()
        self.imposta_provvigione()
        self.aggiorna_prezzo_unitario()
        self.copia_listini()
        self.imposta_prezzo_da_fattura()
        self.stampa_etichette()
        self.elimina_selezionati()

    def creazione_articolo(self, codice: str, descrizione: str, qta: str):
        self.navigateTo("Articoli")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'Codice').setValue(codice)
        self.input(modal, 'Descrizione').setValue(descrizione)

        self.wait_for_element_and_click('//button[@class="btn btn-tool"]')
        self.wait(EC.visibility_of_element_located((By.XPATH, '//label[contains(text(), "Quantità iniziale")]/following-sibling::div/input')))

        self.input(modal, 'Quantità iniziale').setValue(qta)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def modifica_articolo(self, acquisto: str, coefficiente: str):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.find(By.XPATH, '//th[@id="th_Descrizione"]/input')
        self.send_keys_and_wait(search_input, 'Articolo 1', False)

        self.click_first_result()

        self.input(None, 'Prezzo di acquisto').setValue(acquisto)
        self.input(None, 'Coefficiente').setValue(coefficiente)

        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')
        self.wait_for_element_and_click('//a[@id="back"]')

        verificaqta = self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[10]//div[1][1]').text
        self.assertEqual(verificaqta, "2,00")

        self.clear_filters()

    def elimina_articolo(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.find(By.XPATH, '//th[@id="th_Descrizione"]/input')
        self.send_keys_and_wait(search_input, 'Articolo di Prova da Eliminare', False)

        self.click_first_result()

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.clear_filters()

    def verifica_articolo(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.find(By.XPATH, '//th[@id="th_Codice"]/input')
        self.send_keys_and_wait(search_input, '001', False)

        modificato = self.find(By.XPATH, '//tbody//tr[1]//td[9]').text
        self.assertEqual("20,00", modificato)
        self.clear_filters()

        search_input = self.find(By.XPATH, '//th[@id="th_Descrizione"]/input')
        self.send_keys_and_wait(search_input, 'Articolo di prova da Eliminare', False)

        eliminato = self.find(By.XPATH, '//tbody//tr[1]//td[1]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)
        self.clear_filters()

    def serial(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.find(By.XPATH, '//th[@id="th_Descrizione"]/input')
        self.send_keys_and_wait(search_input, 'Articolo 1', False)

        self.click_first_result()

        self.wait_for_element_and_click('(//i[@class="fa fa-plus"])[2]')
        self.wait_for_element_and_click('//label[@for="abilita_serial"]')
        self.wait_for_element_and_click('//button[@id="save"]')

        self.wait_for_element_and_click('//a[@id="link-tab_11"]')

        serial_start = self.find(By.XPATH, '//input[@id="serial_start"]')
        serial_start.send_keys("1")

        serial_end = self.find(By.XPATH, '//input[@id="serial_end"]')
        serial_end.send_keys(Keys.BACK_SPACE, "2")

        self.wait_for_element_and_click('//div[@id="tab_11"]//button[@type="button"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-primary"]')

        serial = self.find(By.XPATH, '//div[@id="tab_11"]//div[@class="card"]//tbody//tr[2]//td[1]').text
        self.assertEqual(serial, "1")

        self.wait_for_element_and_click('(//a[@class="btn btn-danger btn-sm ask"])[2]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.wait(EC.invisibility_of_element_located((By.XPATH, '//div[@id="tab_11"]//div[@class="card"]//tbody//tr[2]//td[1]')))

        self.navigateTo("Articoli")
        self.wait_loader()
        self.clear_filters()

    def provvigioni(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.find(By.XPATH, '//th[@id="th_Descrizione"]/input')
        self.send_keys_and_wait(search_input, 'Articolo 1', False)

        self.click_first_result()

        self.wait_for_element_and_click('//a[@id="link-tab_43"]')
        self.wait_for_element_and_click('//div[@id="tab_43"]//i[@class="fa fa-plus"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-idagente-container"]', option_text='Agente')

        provvigione_input = self.find(By.XPATH, '//input[@id="provvigione"]')
        self.send_keys_and_wait(provvigione_input, '1.00')

        self.wait_for_element_and_click('//div[@id="tab_43"]//tbody//tr//td[3]')
        self.wait_modal()

        provvigione_input = self.find(By.XPATH, '//input[@id="provvigione"]')
        self.send_keys_and_wait(provvigione_input, '2')

        provvigione = self.find(By.XPATH, '//div[@id="tab_43"]//tbody//tr//td[3]').text
        self.assertEqual(provvigione, "2.00 €")

        self.wait_for_element_and_click('//div[@id="tab_43"]//tbody//tr//td[3]')
        self.wait_for_element_and_click('(//a[@class="btn btn-danger ask"])[2]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.navigateTo("Articoli")
        self.wait_loader()
        self.clear_filters()

    def listino_fornitori(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.find(By.XPATH, '//th[@id="th_Descrizione"]/input')
        self.send_keys_and_wait(search_input, 'Articolo 1', False)

        self.click_first_result()
        self.wait_for_element_and_click('//a[@id="link-tab_32"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_fornitore_informazioni-container"]', option_text='Fornitore')

        self.wait_for_element_and_click('//button[@class="btn btn-info"]')
        modal = self.wait_modal()

        self.wait(EC.visibility_of_element_located((By.XPATH, '//input[@id="qta_minima"]')))

        qta_minima = self.find(By.XPATH, '//input[@id="qta_minima"]')
        qta_minima.send_keys("100")

        giorni_consegna = self.find(By.XPATH, '//input[@id="giorni_consegna"]')
        giorni_consegna.send_keys("15")

        self.wait_for_element_and_click('(//label[@class="btn btn-default active"])[3]')

        prezzo_unitario = self.find(By.XPATH, '//input[@id="prezzo_unitario_fisso"]')
        self.send_keys_and_wait(prezzo_unitario, '15')

        self.expandSidebar("Acquisti")
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        numero_esterno = self.find(By.XPATH, '//input[@id="numero_esterno"]')
        numero_esterno.send_keys("78")

        self.wait_for_dropdown_and_select('//span[@id="select2-idanagrafica_add-container"]', option_text='Fornitore')

        self.wait_for_element_and_click('//button[@class="btn btn-primary"]')

        self.driver.execute_script('window.scrollTo(0,0)')

        self.wait_for_dropdown_and_select('//span[@id="select2-idpagamento-container"]', option_text='Bancomat')
        self.wait_for_dropdown_and_select('//span[@id="select2-id_articolo-container"]', option_text='Articolo 1')
        self.wait_for_element_and_click('//button[@class="btn btn-primary tip tooltipstered"]')

        prezzo = self.find(By.XPATH, '//tbody[@id="righe"]//tr[1]//td[8]').text
        self.assertEqual(prezzo, "15,00 €")

        self.wait_for_element_and_click('//a[@id="elimina"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.expandSidebar("Magazzino")
        self.navigateTo("Articoli")
        self.wait_loader()

        self.click_first_result()
        self.wait_for_dropdown_and_select('//span[@id="select2-id_fornitore-container"]', option_text='Fornitore')

        self.navigateTo("Articoli")
        self.wait_loader()

        self.click_first_result()

        self.wait_for_element_and_click('//a[@id="link-tab_32"]')
        self.wait_for_element_and_click('//a[@class="btn btn-secondary btn-warning"]')
        self.wait_modal()

        element = self.find(By.XPATH, '//input[@id="codice_fornitore"]')
        element.clear()
        self.send_keys_and_wait(element, '1')

        codice = self.find(By.XPATH, '//div[@id="tab_32"]//tbody//tr//td[3]').text
        self.assertEqual(codice, "1")

        self.wait_for_element_and_click('//a[@class="btn btn-secondary btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        messaggio = self.find(By.XPATH, '(//div[@class="alert alert-info"])[4]').text
        self.assertEqual(messaggio, "Nessuna informazione disponibile...")

        self.navigateTo("Articoli")
        self.wait_loader()
        self.clear_filters()

    def giacenze(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.find(By.XPATH, '//th[@id="th_Descrizione"]/input')
        self.send_keys_and_wait(search_input, 'Articolo 1', False)

        self.click_first_result()
        self.wait_for_element_and_click('//a[@id="link-tab_22"]')

        totale = self.find(By.XPATH, '//div[@id="tab_22"]//tbody//tr//td[2]').text
        self.assertEqual(totale, "3,00")

        totale_2 = self.find(By.XPATH, '(//div[@id="tab_22"]//div[@class="col-md-12 text-center"])[2]').text
        self.assertEqual(totale_2, "3,00")

        self.navigateTo("Articoli")
        self.wait_loader()
        self.clear_filters()

    def statistiche(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.find(By.XPATH, '//th[@id="th_Descrizione"]/input')
        self.send_keys_and_wait(search_input, 'Articolo 1', False)

        self.click_first_result()
        self.wait_for_element_and_click('//a[@id="link-tab_24"]')

        numero_1 = self.find(By.XPATH, '(//div[@id="tab_24"]//td[@class="text-center"])[1]').text
        self.assertEqual(numero_1, "1")

        numero_2 = self.find(By.XPATH, '(//div[@id="tab_24"]//td[@class="text-center"])[2]').text
        self.assertEqual(numero_2, "1")

        self.navigateTo("Articoli")
        self.wait_loader()
        self.clear_filters()

    def netto_clienti(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.find(By.XPATH, '//th[@id="th_Descrizione"]/input')
        self.send_keys_and_wait(search_input, 'Articolo 1', False)

        self.click_first_result()
        self.wait_for_element_and_click('//a[@id="link-tab_27"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_cliente_informazioni-container"]', option_text='Cliente')

        self.wait_for_element_and_click('//button[@class="btn btn-info btn-block"]')
        self.wait_for_element_and_click('(//label[@class="btn btn-default"])[3]')

        prezzo_unitario = self.find(By.XPATH, '//input[@id="prezzo_unitario_fisso"]')
        self.send_keys_and_wait(prezzo_unitario, '5')

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        self.wait_modal()

        self.wait_for_dropdown_and_select('//span[@id="select2-idanagrafica_add-container"]', option_text='Cliente')

        self.wait_for_element_and_click('//button[@class="btn btn-primary"]')
        self.wait_for_element_and_click('//span[@id="select2-id_articolo-container"]')
        self.wait_for_element_and_click('//ul[@class="select2-results__options select2-results__options--nested"]//li[1]')
        self.wait_for_element_and_click('//button[@class="btn btn-primary tip tooltipstered"]')

        prezzo = self.find(By.XPATH, '//tbody[@id="righe"]//tr[1]//td[9]').text
        self.assertEqual(prezzo, "5,00 €")

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask "]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.expandSidebar("Magazzino")
        self.navigateTo("Articoli")
        self.wait_loader()

        self.click_first_result()
        self.wait_for_element_and_click('//a[@id="link-tab_27"]')

        self.navigateTo("Articoli")
        self.wait_loader()
        self.clear_filters()

    def aggiorna_prezzo_acquisto(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        self.wait_modal()

        codice_input = self.find(By.XPATH, '//input[@id="codice"]')
        codice_input.send_keys("08")

        descrizione_input = self.find(By.XPATH, '//textarea[@id="descrizione"]')
        descrizione_input.send_keys("Prova")

        self.wait_for_element_and_click('//button[@class="btn btn-primary"]')

        prezzo_acquisto = self.find(By.XPATH, '//input[@id="prezzo_acquisto"]')
        prezzo_acquisto.send_keys("1")

        prezzo_vendita = self.find(By.XPATH, '//input[@id="prezzo_vendita"]')
        prezzo_vendita.send_keys("1")

        self.wait_for_element_and_click('//button[@id="save"]')

        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.find(By.XPATH, '//th[@id="th_Codice"]/input')
        self.send_keys_and_wait(search_input, '08', False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_purchase_price"]')

        percentuale_input = self.find(By.XPATH, '//input[@id="percentuale"]')
        percentuale_input.send_keys("10")

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        prezzo = self.find(By.XPATH, '//tbody//tr//td[8]').text
        self.assertEqual(prezzo, "1,10")

        self.clear_filters()

    def aggiorna_prezzo_vendita(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.find(By.XPATH, '//th[@id="th_Codice"]/input')
        self.send_keys_and_wait(search_input, '08', False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_sale_price"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-prezzo_partenza-container"]', option_text='Prezzo di vendita')

        percentuale_input = self.find(By.XPATH, '//input[@id="percentuale"]')
        percentuale_input.send_keys("20")

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        prezzo = self.find(By.XPATH, '//tbody//tr//td[9]').text
        self.assertEqual(prezzo, "0,98")

        self.clear_filters()

    def coefficiente_vendita(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.find(By.XPATH, '//th[@id="th_Codice"]/input')
        self.send_keys_and_wait(search_input, '08', False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_coefficient"]')

        coefficiente_input = self.find(By.XPATH, '//input[@id="coefficiente"]')
        coefficiente_input.send_keys("12")

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        prezzo = self.find(By.XPATH, '//tbody//tr[1]//td[9]//div').text
        self.assertEqual(prezzo, "13,20")

        self.clear_filters()

    def aggiorna_quantita(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.find(By.XPATH, '//th[@id="th_Codice"]/input')
        self.send_keys_and_wait(search_input, '08', False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_quantity"]')

        qta_input = self.find(By.XPATH, '//input[@id="qta"]')
        qta_input.send_keys("3")

        descrizione_input = self.find(By.XPATH, '//input[@id="descrizione"]')
        descrizione_input.send_keys("test")

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        quantita = self.find(By.XPATH, '//tbody//tr//td[10]').text
        self.assertEqual(quantita, "3,00")

        self.clear_filters()

    def crea_preventivo(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.find(By.XPATH, '//th[@id="th_Codice"]/input')
        self.send_keys_and_wait(search_input, '08', False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="create_estimate"]')

        nome_input = self.find(By.XPATH, '//input[@id="nome"]')
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

    def aggiorna_iva(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.find(By.XPATH, '//th[@id="th_Codice"]/input')
        self.send_keys_and_wait(search_input, '08', False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_vat"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_iva-container"]', option_text='Iva 10%')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        iva = self.find(By.XPATH, '//span[@id="select2-idiva_vendita-container"]').text
        self.assertEqual(iva[2:20], "10 - Aliq. Iva 10%")

        self.navigateTo("Articoli")
        self.wait_loader()
        self.clear_filters()

    def aggiorna_unita_misura(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.find(By.XPATH, '//th[@id="th_Codice"]/input')
        self.send_keys_and_wait(search_input, '08', False)

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

    def conto_predefinito_acquisto(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.find(By.XPATH, '//th[@id="th_Codice"]/input')
        self.send_keys_and_wait(search_input, '08', False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_purchase_account"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-conto_acquisto-container"]', option_text='Fabbricati')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.click_first_result()

        conto = self.find(By.XPATH, '//span[@id="select2-idconto_acquisto-container"]').text
        self.assertEqual(conto[2:24], "220.000010 Fabbricati")

        self.navigateTo("Articoli")
        self.wait_loader()
        self.clear_filters()

    def conto_predefinito_vendita(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.find(By.XPATH, '//th[@id="th_Codice"]/input')
        self.send_keys_and_wait(search_input, '08', False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_sale_account"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-conto_vendita-container"]', option_text='Automezzi')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.click_first_result()

        conto = self.find(By.XPATH, '//span[@id="select2-idconto_vendita-container"]').text
        self.assertEqual(conto[2:24], "220.000030 Automezzi")

        self.navigateTo("Articoli")
        self.wait_loader()
        self.clear_filters()

    def imposta_provvigione(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.find(By.XPATH, '//th[@id="th_Codice"]/input')
        self.send_keys_and_wait(search_input, '08', False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="set_commission"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-idagente-container"]', option_text='Agente')

        provvigione_input = self.find(By.XPATH, '//input[@id="provvigione"]')
        provvigione_input.send_keys("10")

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.click_first_result()
        self.wait_for_element_and_click('//a[@id="link-tab_43"]')

        provvigione = self.find(By.XPATH, '(//div[@id="tab_43" ]//tr[1]//td[3]//div)[2]').text
        self.assertEqual(provvigione, "10.00 %")

        self.navigateTo("Articoli")
        self.wait_loader()
        self.clear_filters()

    def aggiorna_prezzo_unitario(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.find(By.XPATH, '//th[@id="th_Codice"]/input')
        self.send_keys_and_wait(search_input, '08', False)

        self.click_first_result()
        self.wait_for_element_and_click('//a[@id="link-tab_32"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_fornitore_informazioni-container"]', option_text='Fornitore')

        self.wait_for_element_and_click('//button[@class="btn btn-info"]')
        modal = self.wait_modal()

        qta_minima = self.find(By.XPATH, '//input[@id="qta_minima"]')
        qta_minima.send_keys("100")

        giorni_consegna = self.find(By.XPATH, '//input[@id="giorni_consegna"]')
        giorni_consegna.send_keys("15")

        self.wait_for_element_and_click('//div[@class="modal-content"]//div[@class="btn-group checkbox-buttons"]')

        prezzo_unitario = self.find(By.XPATH, '//input[@id="prezzo_unitario_fisso"]')
        self.send_keys_and_wait(prezzo_unitario, '15')

        self.navigateTo("Listini")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_prezzo"]')

        percentuale_input = self.find(By.XPATH, '//input[@id="percentuale"]')
        percentuale_input.send_keys("20")

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        prezzo = self.find(By.XPATH, '//tbody//tr[2]//td[8]').text
        self.assertEqual(prezzo, "15,00")

        self.navigateTo("Listini")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td')

        self.navigateTo("Articoli")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.clear_filters()

    def copia_listini(self):
        self.navigateTo("Listini")
        self.wait_loader()

        self.wait_for_dropdown_and_select('//span[@id="select2-id_segment_-container"]', option_text='Fornitori')
        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="copy_listino"]')

        self.wait_for_dropdown_and_select('//span[@class="select2-selection select2-selection--multiple"]', option_text='Estero')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.wait_for_element_and_click('//tbody//tr//td')

        search_input = self.find(By.XPATH, '//th[@id="th_Ragione-sociale"]/input')
        self.send_keys_and_wait(search_input, 'Fornitore Estero', False)

        articolo = self.find(By.XPATH, '//tbody//tr//td[2]').text
        self.assertEqual(articolo, "08 - Prova")

        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.find(By.XPATH, '//th[@id="th_Codice"]/input')
        self.send_keys_and_wait(search_input, '08', False)

        self.click_first_result()
        self.wait_for_element_and_click('//a[@id="link-tab_32"]')
        self.wait_for_element_and_click('//a[@class="btn btn-secondary btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.wait_for_element_and_click('//button[@class="btn btn-warning"]')
        self.wait_for_element_and_click('(//label[@class="btn btn-default active"])[4]')
        self.wait_for_element_and_click('//button[@class="btn btn-primary pull-right"]')

        self.navigateTo("Articoli")
        self.wait_loader()
        self.clear_filters()

    def imposta_prezzo_da_fattura(self):
        self.expandSidebar("Acquisti")
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        numero_esterno = self.find(By.XPATH, '//input[@id="numero_esterno"]')
        numero_esterno.send_keys("04")

        self.wait_for_dropdown_and_select('//span[@id="select2-idanagrafica_add-container"]', option_text='Fornitore')

        self.wait_for_element_and_click('//button[@class="btn btn-primary"]')

        self.driver.execute_script('window.scrollTo(0,0)')

        self.wait_for_dropdown_and_select('//span[@id="select2-idpagamento-container"]', option_text='Assegno')
        self.wait_for_dropdown_and_select('//span[@id="select2-id_articolo-container"]', option_text='Articolo 1')

        self.wait_for_element_and_click('//button[@class="btn btn-primary tip tooltipstered"]')
        self.wait_for_element_and_click('//a[@class="btn btn-xs btn-warning"]')

        prezzo_unitario = self.find(By.XPATH, '//input[@id="prezzo_unitario"]')
        prezzo_unitario.send_keys("10")

        self.wait_for_element_and_click('//button[@class="btn btn-primary pull-right"]')
        self.wait_for_element_and_click('//button[@id="save"]')

        self.expandSidebar("Magazzino")
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.find(By.XPATH, '//th[@id="th_Codice"]/input')
        self.send_keys_and_wait(search_input, '001', False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="set_purchase_price_if_zero"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        prezzo = self.find(By.XPATH, '//tbody//tr//td[8]').text
        self.assertEqual(prezzo, "20,00")

        self.clear_filters()

        self.expandSidebar("Acquisti")
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()

        self.click_first_result()
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask "]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.expandSidebar("Magazzino")

    def stampa_etichette(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.find(By.XPATH, '//th[@id="th_Codice"]/input')
        self.send_keys_and_wait(search_input, '08', False)

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

    def elimina_selezionati(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.find(By.XPATH, '//th[@id="th_Codice"]/input')
        self.send_keys_and_wait(search_input, '08', False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="delete_bulk"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        risultato = self.find(By.XPATH, '//tbody//tr//td').text
        self.assertEqual(risultato, "La ricerca non ha portato alcun risultato.")

        self.clear_filters()
