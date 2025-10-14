from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from common.Test import Test

class AnagraficheBis(Test):
    def setUp(self):
        super().setUp()
        self.wait_driver = self.wait_driver
        self.navigateTo("Anagrafiche")

    def test_funzionalita_aggiuntive_anagrafica(self):
        self.aggiunta_referente()
        self.aggiunta_sede()
        self.plugin_statistiche()
        self.dichiarazione_di_intento()
        self.assicurazione_crediti()
        #self.ricerca_coordinate()
        self.elimina_selezionati()
        self.cambia_relazione()

    def aggiunta_referente(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.search_entity("Cliente")
        self.click_first_result()

        self.wait_for_element_and_click('//a[@id="link-tab_3"]')

        self.wait_for_element_and_click('//h4//i[@class="fa fa-plus"]')
        modal = self.wait_modal()
        self.input(modal,'Nominativo').setValue("Referente di prova")

        self.wait_for_element_and_click('//div[@class="modal-dialog modal-lg"]//i[@class="fa fa-plus"]')
        modal = self.wait_modal()
        job_title_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="modal-content"]//div[@id="form_82-"]//input[@id="nome"]'))
        )
        self.send_keys_and_click(job_title_input, "Segretario", '//form[@id="add-form"]//button[@class="btn btn-primary"]')

        self.wait_for_element_and_click('//span[@id="select2-idmansione-container"]')
        self.wait_for_element_and_click('//div[@class="modal-body"]//button[@class="btn btn-primary"]')

        self.wait_for_element_and_click('//div[@id="tab_3"]//tbody//tr//td[2]')
        self.wait_modal()
        name_input = self.find(By.XPATH, '(//input[@id="nome"])[2]')
        name_input.clear()
        self.send_keys_and_click(name_input, "Prova", '//div[@class="modal-footer"]//button[@type="submit"]')

        contact_name = self.find(By.XPATH, '//div[@id="tab_3"]//tbody//tr//td[2]').text
        self.assertEqual(contact_name, "Prova")

        self.wait_for_element_and_click('//div[@id="tab_3"]//tbody//tr//td[2]')
        self.wait_for_element_and_click('(//a[@class="btn btn-danger ask"])[2]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        empty_message = self.find(By.XPATH, '//div[@id="tab_3"]//tbody//tr').text
        self.assertEqual(empty_message, "Nessun dato presente nella tabella")

        self.wait_for_element_and_click('//h4//i[@class="fa fa-plus"]')
        modal = self.wait_modal()
        contact_name_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//input[@id="nome"])[2]'))
        )
        self.send_keys_and_wait(contact_name_input, "Referente di prova", wait_modal = False)

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-idmansione-container"]',
            '//ul[@id="select2-idmansione-results"]//li[1]'
        )
        self.wait_for_element_and_click('(//button[@type="submit"])[3]')

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Mansione"]/input'))
        )
        self.send_keys_and_wait(search_input, "Segretario", wait_modal = False)
        self.wait_for_search_results()

        job_title = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_3"]//tbody//tr//td[3]'))
        ).text
        self.assertEqual("Segretario", job_title)

        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.clear_filters()

    def aggiunta_sede(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.search_entity("Cliente")
        self.click_first_result()

        self.wait_for_element_and_click('//a[@id="link-tab_4"]')

        self.wait_for_element_and_click('//div[@id="tab_4"]//i[@class="fa fa-plus"]')
        modal = self.wait_modal()
        self.input(None, 'Nome sede').setValue("Filiale XY")

        postal_code_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//input[@id="cap"])[2]'))
        )
        self.send_keys_and_wait(postal_code_input, "35042", wait_modal = False)

        city_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//input[@id="citta"])[2]'))
        )
        city_input.click()
        self.send_keys_and_wait(city_input, "Padova", wait_modal = False)

        self.wait_for_dropdown_and_select(
            '(//span[@id="select2-id_nazione-container"])[2]',
            '//li[@class="select2-results__option select2-results__option--highlighted"]'
        )
        self.wait_for_element_and_click('(//button[@type="submit"])[3]')

        self.wait_for_element_and_click('//div[@id="tab_4"]//tbody/tr//td[2]')
        name_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="nomesede"]'))
        )
        name_input.clear()
        self.send_keys_and_click(name_input, "Prova", '//div[@class="modal-footer"]//button[@type="submit"]')

        name_input = self.find(By.XPATH, '//div[@id="tab_4"]//tbody/tr//td[2]').text
        self.assertEqual(name_input, "Prova")

        self.wait_for_element_and_click('//div[@id="tab_4"]//tbody/tr//td[2]')
        self.wait_for_element_and_click('//button[@class="btn btn-danger "]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        empty_message = self.find(By.XPATH, '//div[@id="tab_4"]//tbody//tr').text
        self.assertEqual(empty_message, "Nessun dato presente nella tabella")

        self.wait_for_element_and_click('//div[@id="tab_4"]//i[@class="fa fa-plus"]')
        modal = self.wait_modal()
        self.input(None, 'Nome sede').setValue("Filiale XY")

        postal_code_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//input[@id="cap"])[2]'))
        )
        self.send_keys_and_wait(postal_code_input, "35042", wait_modal = False)

        city_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//input[@id="citta"])[2]'))
        )
        city_input.click()
        self.send_keys_and_wait(city_input, "Padova", wait_modal = False)

        self.wait_for_dropdown_and_select(
            '(//span[@id="select2-id_nazione-container"])[2]',
            '//li[@class="select2-results__option select2-results__option--highlighted"]'
        )
        self.wait_for_element_and_click('(//button[@type="submit"])[3]')

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//th[@id="th_Nome"]/input)[2]'))
        )
        self.send_keys_and_wait(search_input, "Filiale XY", wait_modal = False)

        location_name = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_4"]//tbody//td[2]'))
        ).text
        self.assertEqual("Filiale XY", location_name)

        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.clear_filters()

    def plugin_statistiche(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.search_entity("Cliente")
        self.click_first_result()

        self.wait_for_element_and_click('//a[@id="link-tab_7"]')

        stats_labels = [
            ("Preventivi", '//span[@class="info-box-text pull-left"]'),
            ("Contratti", '(//span[@class="info-box-text pull-left"])[2]'),
            ("Ordini cliente", '(//span[@class="info-box-text pull-left"])[3]'),
            ("Attività", '(//span[@class="info-box-text pull-left"])[4]'),
            ("Ddt in uscita", '(//span[@class="info-box-text pull-left"])[5]'),
            ("Fatture", '(//span[@class="info-box-text pull-left"])[6]'),
            ("Ore lavorate", '(//span[@class="info-box-text pull-left"])[7]')
        ]

        for expected_label, xpath in stats_labels:
            actual_label = self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            ).text
            self.assertEqual(actual_label, expected_label)

        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.clear_filters()

    def dichiarazione_di_intento(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.search_entity("Cliente")
        self.click_first_result()

        self.wait_for_element_and_click('//a[@id="link-tab_25"]')

        self.wait_for_element_and_click('//div[@id="tab_25"]//i[@class="fa fa-plus"]')

        form_fields = [
            ('//input[@id="numero_protocollo"]', "012345678901234567890123"),
            ('//input[@id="data_protocollo"]', "01/01/2025"),
            ('//input[@id="numero_progressivo"]', "001"),
            ('//input[@id="data_inizio"]', "01/01/2025"),
            ('//input[@id="data_fine"]', "31/12/2028"),
            ('//input[@id="massimale"]', "50000"),
            ('//input[@id="data_emissione"]', "13/01/2025")
        ]

        for xpath, value in form_fields:
            field = self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            self.send_keys_and_wait(field, value, wait_modal = False)

        data_emissione = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="data_emissione"]'))
        )
        self.send_keys_and_wait(data_emissione, "", wait_modal = False)

        self.wait_for_element_and_click('//div[@class="modal-footer"]//button[@class="btn btn-primary"]')
        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_25"]//tbody//tr//td[1]'))
        )

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        self.wait_modal()

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-idanagrafica_add-container"]',
            option_text="Cliente (Este)"
        )
        self.wait_for_element_and_click('//div[@class="modal-footer"]//button[@class="btn btn-primary"]')

        declaration_message = self.find(By.XPATH, '(//div[@class="alert alert-info"])[1]').text
        self.assertEqual("La fattura è collegata ad una dichiarazione d'intento", declaration_message[0:53])

        self.wait_for_element_and_click('//a[@class="btn btn-primary"]')

        description_field = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))
        )
        self.send_keys_and_wait(description_field, "prova per dichiarazione", wait_modal = False)

        quantity_field = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="qta"]'))
        )
        self.send_keys_and_wait(quantity_field, "100", wait_modal = False)

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-um-container"]',
            option_text="pz"
        )

        price_field = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))
        )
        self.send_keys_and_wait(price_field, "1", wait_modal = False)

        self.wait_for_element_and_click('//button[@class="btn btn-primary pull-right"]')
        self.wait_for_element_and_click('//button[@id="save"]')

        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.search_entity("Cliente")
        self.click_first_result()

        self.wait_for_element_and_click('//a[@id="link-tab_25"]')

        total_amount = self.find(By.XPATH, '//div[@id="tab_25"]//tbody//tr//td[5]').text
        self.assertEqual(total_amount, "102.00")

        self.wait_for_element_and_click('//div[@id="tab_25"]//tbody//tr//td[5]')
        modal = self.wait_modal()
        self.input(modal, 'Progressivo int.').setValue("01")
        self.wait_for_element_and_click('//div[@id="modals"]//button[@type="submit"]')
        
        progressive = self.find(By.XPATH, '//div[@id="tab_25"]//tbody//td[3]').text
        self.assertEqual(progressive, "01")

        self.wait_for_element_and_click('//div[@id="tab_25"]//tbody//td[3]')
        self.wait_for_element_and_click('//a[@class="btn btn-danger ask "]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        empty_message = self.find(By.XPATH, '//div[@id="tab_25"]//td[@class="dataTables_empty"]').text
        self.assertEqual(empty_message, "Nessun dato presente nella tabella")

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//a[@id="elimina"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.navigateTo("Anagrafiche")
        self.clear_filters()

    def assicurazione_crediti(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.search_entity("Cliente")
        self.click_first_result()

        self.wait_for_element_and_click('//a[@id="link-tab_45"]')

        self.wait_for_element_and_click('//div[@id="tab_45"]//i[@class="fa fa-plus"]')

        start_date_field = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="data_inizio"]'))
        )
        self.send_keys_and_wait(start_date_field, "01/01/2025", wait_modal = False)

        end_date_field = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="data_fine"]'))
        )
        end_date_field.clear()
        self.send_keys_and_wait(end_date_field, "31/12/2025", wait_modal = False)

        credit_limit_field = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="fido_assicurato"]'))
        )
        self.send_keys_and_wait(credit_limit_field, "50000")

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        date_field = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="data"]'))
        )
        self.send_keys_and_wait(date_field, "01/01/2025", wait_modal = False)

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-idanagrafica_add-container"]',
            option_text="Cliente"
        )
        self.wait_for_element_and_click('//div[@class="modal-footer"]//button[@class="btn btn-primary"]')

        self.wait_for_element_and_click('//a[@class="btn btn-primary"]')

        description_field = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))
        )
        self.send_keys_and_wait(description_field, "prova", wait_modal = False)

        price_field = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))
        )
        self.send_keys_and_wait(price_field, "51000", wait_modal = False)

        self.wait_for_element_and_click('//button[@class="btn btn-primary pull-right"]')
        self.wait_for_element_and_click('//button[@id="save"]')

        warning_message = self.find(By.XPATH, '//div[@class="alert alert-warning text-center"]').text
        self.assertEqual("Attenzione!", warning_message[0:11])

        self.wait_for_element_and_click('//a[@id="elimina"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.search_entity("Cliente")
        self.click_first_result()

        self.wait_for_element_and_click('//a[@id="link-tab_45"]')

        self.wait_for_element_and_click('//div[@id="tab_45"]//tbody//tr//td[2]')
        credit_limit_field = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="fido_assicurato"]'))
        )
        credit_limit_field.send_keys(Keys.BACK_SPACE, "49000")
        self.wait_for_element_and_click('//button[@class="btn btn-primary pull-right"]')

        modified_limit = self.find(By.XPATH, '//div[@id="tab_45"]//tbody//tr//td[2]').text
        self.assertEqual(modified_limit, "49000.00")

        self.wait_for_element_and_click('//div[@id="tab_45"]//tbody//tr//td[2]')
        self.wait_for_element_and_click('//div[@id="modals"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.navigateTo("Anagrafiche")
        self.clear_filters()

    def ricerca_coordinate(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))
        )
        self.send_keys_and_wait(search_input, "Admin spa", wait_modal = False)
        self.wait_for_search_results()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="search_coordinates"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//a[@onclick="modificaPosizione()"]')
        self.wait_for_element_and_click('//ul//li[2]//div')

        latitude = self.find(By.XPATH, '//input[@id="lat"]').text
        self.assertNotEqual(latitude, "0")
        longitude = self.find(By.XPATH, '//input[@id="lng"]').text
        self.assertNotEqual(longitude, "0")

        self.wait_for_element_and_click('//button[@class="close"]')

        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.clear_filters()

    def elimina_selezionati(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))
        )
        self.send_keys_and_wait(search_input, "Vettore", wait_modal = False)
        self.wait_for_search_results()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="delete_bulk"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        no_results_message = self.find(By.XPATH, '//tbody//tr[1]').text
        self.assertEqual(no_results_message, "La ricerca non ha portato alcun risultato.")

        self.clear_filters()

    def cambia_relazione(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.search_entity("Cliente")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_relation"]')

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-idrelazione-container"]',
            option_text="Attivo"
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')

        relation = self.find(By.XPATH, '//tbody//tr//td[7]').text
        self.assertEqual(relation, "Attivo")

        self.wait_for_element_and_click('//tbody//tr//td[7]')
        self.wait_for_element_and_click('//span[@id="select2-idrelazione-container"]//span[@class="select2-selection__clear"]')

        search_field = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))
        )
        self.send_keys_and_wait(search_field, "Da contattare", wait_modal = False)
        self.wait_for_element_and_click('//button[@id="save"]')

        self.navigateTo("Anagrafiche")
        self.wait_loader()

        new_relation = self.find(By.XPATH, '//tbody//tr//td[7]').text
        self.assertNotEqual(new_relation, "Attivo")

        self.clear_filters()
