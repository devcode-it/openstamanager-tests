from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import time

class Articoli(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Magazzino")
        self.wait_loader()

    def test_bulk_articolo(self):
        self.aggiorna_iva()
        self.aggiorna_categoria()
        self.coefficiente_vendita()
        self.conto_predefinito_acquisto()
        self.conto_predefinito_vendita()
        self.aggiorna_prezzo_acquisto()
        self.aggiorna_prezzo_vendita()
        self.aggiorna_quantita()
        self.aggiorna_unita_misura()
        self.aggiungi_a_listino_cliente()
        self.attiva_disattiva_articoli()
        self.crea_preventivo()
        self.elimina_selezionati()
        self.esporta_selezionati()
        self.genera_barcode()
        self.imposta_prezzo_da_fattura()
        self.imposta_provvigione()
        self.stampa_etichette()
        self.duplica()
        self.unisci()

    def aggiorna_iva(self):
        self.navigate_to_and_wait("Articoli")

        self.search_by_th("th_Codice", "001")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="change_vat"]'
        )
        self.wait_for_dropdown_and_select('//span[@id="select2-id_iva-container"]', option_text='Iva 10%')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.click_first_table_row()
        iva = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_iva_vendita-container"]'))
        ).text
        self.assertEqual(iva[0:20], "10 - Aliq. Iva 10%")

        self.navigate_to_and_wait("Articoli")
        self.clear_filters()

    def aggiorna_categoria(self):
        self.navigate_to_and_wait("Articoli")

        self.search_by_th("th_Codice", "001")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="change_category"]'
        )

        self.wait_for_dropdown_and_select('//span[@id="select2-id_categoria-container"]', option_text='Componenti')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.click_first_result()
        self.wait_for_element_and_click('//button[@class="btn btn-tool"]')

        categoria = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-categoria_edit-container"]'))
        ).text
        self.assertEqual(categoria, "Componenti")

        self.navigate_to_and_wait("Articoli")
        self.clear_filters()

    def coefficiente_vendita(self):
        self.navigate_to_and_wait("Articoli")

        self.search_by_th("th_Codice", "001")
        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="change_coefficient"]'
        )

        coefficiente_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="coefficiente"]'))
        )
        coefficiente_input.send_keys("12")

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        prezzo = self.get_table_text(1, 9)
        self.assertEqual(prezzo, "240,00")

        self.clear_filters()

    def conto_predefinito_acquisto(self):
        self.navigate_to_and_wait("Articoli")

        self.search_by_th("th_Codice", "001")
        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="change_purchase_account"]'
        )

        self.wait_for_dropdown_and_select('//span[@id="select2-conto_acquisto-container"]', option_text='Fabbricati')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.click_first_result()

        conto = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_conto_acquisto-container"]'))
        ).text
        self.assertEqual(conto[0:24], "220.000010 Fabbricati")

        self.navigate_to_and_wait("Articoli")
        self.clear_filters()

    def conto_predefinito_vendita(self):
        self.navigate_to_and_wait("Articoli")

        self.search_by_th("th_Codice", "001")
        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="change_sale_account"]'
        )

        self.wait_for_dropdown_and_select('//span[@id="select2-conto_vendita-container"]', option_text='Automezzi')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.click_first_result()

        conto = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_conto_vendita-container"]'))
        ).text
        self.assertEqual(conto[0:24], "220.000030 Automezzi")

        self.navigate_to_and_wait("Articoli")
        self.clear_filters()

    def aggiorna_prezzo_acquisto(self):
        self.navigate_to_and_wait("Articoli")
        self.search_by_th("th_Codice", "001")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="change_purchase_price"]'
        )

        percentuale_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="percentuale"]'))
        )
        percentuale_input.send_keys("10")

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        prezzo = self.get_table_text(1, 8)
        self.assertEqual(prezzo, "18,00")

        self.clear_filters()

    def aggiorna_prezzo_vendita(self):
        self.navigate_to_and_wait("Articoli")

        self.click_add_button()
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

        self.navigate_to_and_wait("Articoli")

        self.search_by_th("th_Codice", "08")
        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="change_sale_price"]'
        )

        self.wait_for_dropdown_and_select('//span[@id="select2-prezzo_partenza-container"]', option_text='Prezzo di vendita')

        percentuale_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="percentuale"]'))
        )
        percentuale_input.send_keys("20")

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        prezzo = self.get_table_text(1, 9)
        self.assertEqual(prezzo, "0,98")

        self.clear_filters()

    def aggiorna_quantita(self):
        self.navigate_to_and_wait("Articoli")

        self.search_by_th("th_Codice", "001")
        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="change_quantity"]'
        )

        qta_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="qta"]'))
        )
        qta_input.send_keys("3")

        descrizione_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="descrizione"]'))
        )
        descrizione_input.send_keys("test")

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        quantita = self.get_table_text(1, 10)
        self.assertEqual(quantita, "3,00")

        self.clear_filters()

    def aggiorna_unita_misura(self):
        self.navigate_to_and_wait("Articoli")

        self.search_by_th("th_Codice", "001")
        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="change_unit"]'
        )

        self.wait_for_dropdown_and_select('//span[@id="select2-um-container"]', option_text='ore')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.click_first_table_row()

        self.wait_for_element_and_click('(//i[@class="fa fa-plus"])[2]')

        unita_misura = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-um-container"]'))).text
        self.assertEqual(unita_misura[0:5], "ore")

        self.navigate_to_and_wait("Articoli")
        self.clear_filters()

    def aggiungi_a_listino_cliente(self):
        self.navigate_to_and_wait("Articoli")

        self.search_by_th("th_Codice", "08")
        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="add_price_list"]'
        )

        self.wait_for_dropdown_and_select('//span[@id="select2-id_listino-container"]', option_text='Test')

        coefficiente_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="sconto_percentuale"]'))
        )
        coefficiente_input.send_keys("20")
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.navigate_to_and_wait("Articoli")
        self.clear_filters()

    def attiva_disattiva_articoli(self):
        self.navigate_to_and_wait("Articoli")

        self.search_by_th("th_Codice", "001")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="change_active"]'
        )

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.wait_and_click_table_row()
        stato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@class="badge badge-danger"]'))
        ).text
        self.assertEqual(stato, "Disattivato")

        self.navigate_to_and_wait("Articoli")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="change_active"]'
        )

        self.wait_for_element_and_click('//label[@class="btn btn-default active"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.navigate_to_and_wait("Articoli")
        self.clear_filters()

    def crea_preventivo(self):
        self.navigate_to_and_wait("Articoli")

        self.search_by_th("th_Codice", "001")
        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="create_estimate"]'
        )

        nome_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))
        )
        nome_input.send_keys("Prova")

        self.wait_for_dropdown_and_select('//span[@id="select2-id_cliente-container"]', option_text='Cliente')
        self.wait_for_dropdown_and_select('//span[@id="select2-id_segment-container"]', option_text='Standard preventivi')
        self.wait_for_dropdown_and_select('//span[@id="select2-id_tipo-container"]', option_text='Generico')

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.delete_current_and_clear()

        self.expandSidebar("Magazzino")
        self.navigate_to_and_wait("Articoli")
        self.clear_filters()

    def elimina_selezionati(self):
        self.navigate_to_and_wait("Articoli")

        self.search_by_th("th_Codice", "08")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="delete_bulk"]'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        risultato = self.get_empty_table_message()
        self.assertEqual(risultato, "Nessun dato presente nella tabella")

        self.clear_filters()

    def esporta_selezionati(self):
        self.navigate_to_and_wait("Articoli")

        self.search_by_th("th_Codice", "001")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="export_csv"]'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        download_dir = os.path.expanduser('~/Scaricati')
        files_before = os.listdir(download_dir) if os.path.exists(download_dir) else []

        time.sleep(2)

        files_after = os.listdir(download_dir) if os.path.exists(download_dir) else []
        new_files = set(files_after) - set(files_before)

        csv_files = [f for f in new_files if f.endswith('.csv')]
        self.assertTrue(len(csv_files) > 0, "Nessun file CSV scaricato")

        self.navigate_to_and_wait("Articoli")
        self.clear_filters()

    def genera_barcode(self):
        self.navigate_to_and_wait("Articoli")

        self.search_by_th("th_Codice", "001")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="generate_barcode_bulk"]'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.click_first_result()
        self.wait_for_element_and_click('//a[@id="link-tab_22"]')

        barcode = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_22"]//tbody//tr[1]//td[2]'))
        ).text
        self.assertTrue(len(barcode) > 0)

        self.navigate_to_and_wait("Articoli")
        self.clear_filters()

    def imposta_prezzo_da_fattura(self):
        self.expandSidebar("Acquisti")
        self.navigate_to_and_wait("Fatture di acquisto")

        self.click_add_button()
        modal = self.wait_modal()

        numero_esterno = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="numero_esterno"]'))
        )
        numero_esterno.send_keys("04")

        self.wait_for_dropdown_and_select('//span[@id="select2-id_anagrafica_add-container"]', option_text='Fornitore')

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
        self.navigate_to_and_wait("Articoli")

        self.search_by_th("th_Codice", "001")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="set_purchase_price_if_zero"]'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        prezzo = self.get_table_text(1, 8)
        self.assertEqual(prezzo, "18,00")

        self.clear_filters()

        self.expandSidebar("Acquisti")
        self.navigate_to_and_wait("Fatture di acquisto")
        self.search_by_th("th_Numero", "04")

        self.click_first_result()
        self.delete_current_and_clear()

        self.expandSidebar("Magazzino")

    def imposta_provvigione(self):
        self.navigate_to_and_wait("Articoli")

        self.search_by_th("th_Codice", "001")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="set_commission"]'
        )

        self.wait_for_dropdown_and_select('//span[@id="select2-id_agente-container"]', option_text='Agente')

        provvigione_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="provvigione"]'))
        )
        provvigione_input.send_keys("10")

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.click_first_result()
        self.wait_for_element_and_click('//a[@id="link-tab_43"]')

        provvigione = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_43" ]//tr[1]//td[3]//div)[2]'))
        ).text
        self.assertEqual(provvigione, "10.00 %")

        self.navigate_to_and_wait("Articoli")
        self.clear_filters()

    def stampa_etichette(self):
        self.navigate_to_and_wait("Articoli")

        self.search_by_th("th_Codice", "001")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="print_labels"]'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.driver.switch_to.window(self.driver.window_handles[1])

        prezzo = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="viewer"]//span)[3]'))).text
        self.assertEqual(prezzo, "216,00 €")

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.wait_and_click_table_row()
        self.clear_filters()

    def duplica(self):
        self.navigate_to_and_wait("Articoli")

        self.search_by_th("th_Codice", "001")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="copy_bulk"]'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.clear_filters()

        codice = self.get_table_text(2, 3)
        self.assertEqual(codice, "4")

    def unisci(self):
        self.navigate_to_and_wait("Articoli")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//tbody//tr[2]//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="merge_products"]'
        )

        self.wait_for_dropdown_and_select('//span[@id="select2-id_articolo_principale-container"]', option_text='001')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.search_by_th("th_Codice", "4")

        risultato = self.get_empty_table_message()
        self.assertEqual(risultato, "Nessun dato presente nella tabella")

        self.clear_filters()