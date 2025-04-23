from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from common.Test import Test

class Anagrafiche(Test):
    def setUp(self):
        super().setUp()
        self.wait_driver = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")

    def test_creazione_anagrafica(self):
        self.add_anagrafica('Cliente', 'Cliente')
        self.add_anagrafica('Tecnico', 'Tecnico')
        self.add_anagrafica('Fornitore', 'Fornitore')
        self.add_anagrafica('Vettore', 'Vettore')
        self.add_anagrafica('Agente', 'Agente')
        self.add_anagrafica('Anagrafica di Prova da Eliminare', 'Cliente')
        self.modifica_anagrafica('Privato')
        self.elimina_anagrafica()
        self.verifica_anagrafica()
        self.crea_attivita()
        self.crea_preventivo()
        self.crea_contratto()
        self.crea_ordine_cliente()
        self.crea_DDT_uscita()
        self.crea_fattura_vendita()
        self.aggiunta_referente()
        self.aggiunta_sede()
        self.plugin_statistiche()
        self.dichiarazione_di_intento()
        self.assicurazione_crediti()
        self.ricerca_coordinate()
        self.elimina_selezionati()
        self.cambia_relazione()
        self.logger.info("Test di creazione anagrafica completato con successo")

    def add_anagrafica(self, nome=str, tipo=str):
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')

        modal = self.wait_modal()
        self.input(modal, 'Denominazione').setValue(nome)
        select = self.input(modal, 'Tipo di anagrafica')
        select.setByText(tipo)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
    def modifica_anagrafica(self, tipologia:str):
        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.search_entity("Cliente")
        self.click_first_result()

        self.wait_driver.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="select2-tipo-container"]'))
        ).click()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))
        ).send_keys(tipologia, Keys.ENTER)
        self.wait_loader()

        self.input(None, 'Partita IVA').setValue("05024030287")
        self.input(None, 'Codice fiscale').setValue("05024030287")

        address_field = self.wait_driver.until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="indirizzo"]'))
        )
        address_field.clear()
        address_field.send_keys("Via controllo caratteri speciali: &\"<>èéàòùì?'`")

        self.input(None, 'C.A.P.').setValue("35042")
        self.input(None, 'Città').setValue("Este")

        self.wait_driver.until(
            EC.element_to_be_clickable((By.XPATH, '//button[@id="save"]'))
        ).click()
        self.wait_loader()

        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.clear_filters()

    def elimina_anagrafica(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.search_entity('Anagrafica di Prova da Eliminare')
        self.click_first_result()
        self.wait_loader()

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.wait_loader()

        self.clear_filters()

    def verifica_anagrafica(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.clear_filters()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Tipologia"]/input'))
        )

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Tipologia"]/input'))
        )
        search_input.clear()
        search_input.send_keys("Privato", Keys.ENTER)
        self.wait_for_search_results()

        entity_name = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[2]'))
        ).text
        self.assertEqual("Cliente", entity_name)

        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.clear_filters()

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))
        )

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))
        )
        search_input.clear()
        search_input.send_keys("Anagrafica di Prova da Eliminare", Keys.ENTER)
        self.wait_for_search_results()

        no_results_message = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[1]'))
        ).text
        self.assertEqual("La ricerca non ha portato alcun risultato.", no_results_message)

        self.clear_filters()

    def crea_attivita(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.search_entity("Cliente")
        self.click_first_result()

        self.wait_for_element_and_click('//button[@class="btn btn-info dropdown-toggle"]')
        self.wait_for_element_and_click('(//a[@class="btn dropdown-item bound clickable"])[1]')

        self.wait_for_dropdown_and_select(
            '(//form[@id="add-form"]//span[@class="select2-selection select2-selection--single"])[8]',
            '(//li[@class="select2-results__option"])'
        )

        description_field = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[2]'))
        )
        description_field.click()
        description_field.send_keys("Test")

        self.wait_for_element_and_click('//div[@class="col-md-12 text-right"]//button[@type="button"]')

        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.search_entity("Cliente")
        self.click_first_result()

        self.wait_for_element_and_click('//a[@id="link-tab_28"]')
        activity_number = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_28"]//tbody//tr//td[2]'))
        ).text
        self.assertEqual("1", activity_number)

        self.wait_for_element_and_click('//div[@id="tab_28"]//tbody//td[2]')

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.wait_loader()

        self.navigateTo("Anagrafiche")
        self.clear_filters()

    def crea_preventivo(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.search_entity("Cliente")
        self.click_first_result()

        self.wait_for_element_and_click('//button[@class="btn btn-info dropdown-toggle"]')
        self.wait_for_element_and_click('(//a[@class="btn dropdown-item bound clickable"])[2]')
        modal = self.wait_modal()

        self.wait_for_dropdown_and_select(
            '(//form[@id="add-form"]//span[@class="select2-selection select2-selection--single"])[4]',
            '(//li[@class="select2-results__option"])'
        )

        self.wait_for_dropdown_and_select(
            '(//form[@id="add-form"]//span[@class="select2-selection select2-selection--single"])[5]',
            '(//li[@class="select2-results__option"])'
        )

        self.input(modal, 'Nome').setValue("Preventivo di prova anagrafica")

        self.wait_for_element_and_click('(//div[@id="form_13-"]//button[@class="btn btn-primary"])')

        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.search_entity("Cliente")
        self.click_first_result()

        self.wait_for_element_and_click('//button[@class="btn btn-tool"]')

        quote_text = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//div[@class="card-body"]//li)[7]'))
        ).text
        self.assertEqual("Preventivo 1", quote_text[0:12])

        self.wait_for_element_and_click('(//div[@class="card-body"]//li//a)[5]')

        self.wait_driver.until(lambda driver: len(driver.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.wait_loader()

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.navigateTo("Anagrafiche")
        self.clear_filters()

    def crea_contratto(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.search_entity("Cliente")
        self.click_first_result()

        self.wait_for_element_and_click('//button[@class="btn btn-info dropdown-toggle"]')
        self.wait_for_element_and_click('(//a[@class="btn dropdown-item bound clickable"])[3]')
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue("Contratto di prova anagrafica")

        self.wait_for_dropdown_and_select(
            '(//form[@id="add-form"]//span[@class="select2-selection select2-selection--single"])[2]',
            '(//li[@class="select2-results__option"])'
        )

        self.wait_for_element_and_click('(//div[@id="form_31-"]//button[@class="btn btn-primary"])')

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.wait_loader()

        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.clear_filters()

    def crea_ordine_cliente(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.search_entity("Cliente")
        self.click_first_result()

        self.wait_for_element_and_click('//button[@class="btn btn-info dropdown-toggle"]')
        self.wait_for_element_and_click('(//a[@class="btn dropdown-item bound clickable"])[4]')
        self.wait_modal()

        self.wait_for_element_and_click('(//div[@id="form_24-"]//button[@class="btn btn-primary"])')
        self.wait_loader()

        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.search_entity("Cliente")
        self.click_first_result()

        self.wait_for_element_and_click('//button[@class="btn btn-tool"]')

        order_text = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//div[@class="card-body"]//li)[7]'))
        ).text
        self.assertEqual("Ordine cliente 01", order_text[0:17])

        self.wait_for_element_and_click('(//div[@class="card-body"]//li//a)[5]')

        self.wait_driver.until(lambda driver: len(driver.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.wait_loader()

        self.navigateTo("Anagrafiche")
        self.clear_filters()

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def crea_DDT_uscita(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.search_entity("Cliente")
        self.click_first_result()

        self.wait_for_element_and_click('//button[@class="btn btn-info dropdown-toggle"]')
        self.wait_for_element_and_click('(//a[@class="btn dropdown-item bound clickable"])[5]')
        modal = self.wait_modal()

        self.wait_for_dropdown_and_select(
            '(//form[@id="add-form"]//span[@class="select2-selection select2-selection--single"])[3]',
            '(//li[@class="select2-results__option"])'
        )

        self.wait_for_element_and_click('(//div[@id="form_26-"]//button[@class="btn btn-primary"])')

        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.search_entity("Cliente")
        self.click_first_result()

        self.wait_for_element_and_click('//a[@id="link-tab_17"]')

        ddt_number = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_17"]//tbody//td[2]'))
        ).text
        self.assertEqual("01", ddt_number)

        self.wait_for_element_and_click('//div[@id="tab_17"]//tbody//td[2]')

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.wait_loader()

        self.navigateTo("Anagrafiche")
        self.clear_filters()

    def crea_fattura_vendita(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.search_entity("Cliente")
        self.click_first_result()

        self.wait_for_element_and_click('//button[@class="btn btn-info dropdown-toggle"]')
        self.wait_for_element_and_click('(//a[@class="btn dropdown-item bound clickable"])[6]')

        self.wait_for_element_and_click('(//div[@id="form_14-"]//button[@class="btn btn-primary"])')

        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.search_entity("Cliente")
        self.click_first_result()

        self.wait_for_element_and_click('//button[@class="btn btn-tool"]')

        invoice_text = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//div[@class="card-body"]//li)[7]'))
        ).text
        self.assertEqual("Fattura immediata di vendita", invoice_text[0:28])

        self.wait_for_element_and_click('(//div[@class="card-body"]//li//a)[5]')

        self.wait_driver.until(lambda driver: len(driver.window_handles) > 1)

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask "]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.wait_loader()

        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.clear_filters()

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
        job_title_input.send_keys("Segretario", Keys.ENTER)

        self.wait_for_element_and_click('(//button[@type="submit"])[3]')
        self.wait_loader()

        self.wait_for_element_and_click('//div[@id="tab_3"]//tbody//tr//td[2]')

        name_input = self.find(By.XPATH, '(//input[@id="nome"])[2]')
        name_input.clear()
        name_input.send_keys("Prova")

        self.wait_for_element_and_click('//button[@class="btn btn-success pull-right"]')
        self.wait_loader()

        contact_name = self.find(By.XPATH, '//div[@id="tab_3"]//tbody//tr//td[2]').text
        self.assertEqual(contact_name, "Prova")

        self.wait_for_element_and_click('//div[@id="tab_3"]//tbody//tr//td[2]')
        self.wait_for_element_and_click('(//a[@class="btn btn-danger ask"])[2]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.wait_loader()

        empty_message = self.find(By.XPATH, '//div[@id="tab_3"]//tbody//tr').text
        self.assertEqual(empty_message, "Nessun dato presente nella tabella")

        self.wait_for_element_and_click('//h4//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        contact_name_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//input[@id="nome"])[2]'))
        )
        contact_name_input.send_keys("Referente di prova")

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-idmansione-container"]',
            '//ul[@id="select2-idmansione-results"]//li[1]'
        )

        self.wait_for_element_and_click('(//button[@type="submit"])[3]')
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Mansione"]/input'))
        )
        search_input.send_keys("Segretario", Keys.ENTER)
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

        self.input(None, 'Nome sede').setValue("Filiale XY")

        postal_code_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//input[@id="cap"])[2]'))
        )
        postal_code_input.send_keys("35042")

        city_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//input[@id="citta"])[2]'))
        )
        city_input.click()
        city_input.send_keys("Padova")

        self.wait_for_dropdown_and_select(
            '(//span[@id="select2-id_nazione-container"])[2]',
            '//li[@class="select2-results__option select2-results__option--highlighted"]'
        )

        self.wait_for_element_and_click('(//button[@type="submit"])[3]')

        self.wait_for_element_and_click('//div[@id="tab_4"]//tbody/tr//td[2]')

        location_name_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="nomesede"]'))
        )
        location_name_input.clear()
        location_name_input.send_keys("Prova")

        self.wait_for_element_and_click('//button[@class="btn btn-primary pull-right"]')
        self.wait_loader()

        location_name = self.find(By.XPATH, '//div[@id="tab_4"]//tbody/tr//td[2]').text
        self.assertEqual(location_name, "Prova")

        self.wait_for_element_and_click('//div[@id="tab_4"]//tbody/tr//td[2]')
        self.wait_for_element_and_click('//button[@class="btn btn-danger "]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.wait_loader()

        empty_message = self.find(By.XPATH, '//div[@id="tab_4"]//tbody//tr').text
        self.assertEqual(empty_message, "Nessun dato presente nella tabella")

        self.wait_for_element_and_click('//div[@id="tab_4"]//i[@class="fa fa-plus"]')

        self.input(None, 'Nome sede').setValue("Filiale XY")

        postal_code_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//input[@id="cap"])[2]'))
        )
        postal_code_input.send_keys("35042")

        city_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//input[@id="citta"])[2]'))
        )
        city_input.click()
        city_input.send_keys("Padova")

        self.wait_for_dropdown_and_select(
            '(//span[@id="select2-id_nazione-container"])[2]',
            '//li[@class="select2-results__option select2-results__option--highlighted"]'
        )

        self.wait_for_element_and_click('(//button[@type="submit"])[3]')

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//th[@id="th_Nome"]/input)[2]'))
        )
        search_input.send_keys("Filiale XY", Keys.ENTER)
        self.wait_for_search_results()

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
            field.send_keys(value)

        self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="data_emissione"]'))
        ).send_keys(Keys.ENTER)

        self.wait_for_element_and_click('(//button[@class="btn btn-primary"])[2]')
        self.wait_loader()

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
            option_text="Cliente"
        )

        self.wait_for_element_and_click('//button[@class="btn btn-primary"]')
        self.wait_loader()

        declaration_message = self.find(By.XPATH, '(//div[@class="alert alert-info"])[1]').text
        self.assertEqual("La fattura è collegata ad una dichiarazione d'intento", declaration_message[0:53])

        self.wait_for_element_and_click('//a[@class="btn btn-primary"]')

        description_field = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))
        )
        description_field.send_keys("prova per dichiarazione")

        quantity_field = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="qta"]'))
        )
        quantity_field.send_keys("100")

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-um-container"]',
            option_text="pz"
        )

        price_field = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))
        )
        price_field.send_keys("1")

        self.wait_for_element_and_click('//button[@class="btn btn-primary pull-right"]')

        self.wait_for_element_and_click('//button[@id="save"]')
        self.wait_loader()

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
        self.wait_loader()

        progressive = self.find(By.XPATH, '//div[@id="tab_25"]//tbody//td[3]').text
        self.assertEqual(progressive, "01")

        self.wait_for_element_and_click('//div[@id="tab_25"]//tbody//td[3]')
        self.wait_for_element_and_click('//a[@class="btn btn-danger ask "]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.wait_loader()

        empty_message = self.find(By.XPATH, '//div[@id="tab_25"]//td[@class="dataTables_empty"]').text
        self.assertEqual(empty_message, "Nessun dato presente nella tabella")

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_loader()

        self.wait_for_element_and_click('//a[@id="elimina"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.wait_loader()

        self.navigateTo("Anagrafiche")
        self.clear_filters()

    def assicurazione_crediti(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.search_entity("Cliente")
        self.click_first_result()

        self.wait_for_element_and_click('//a[@id="link-tab_45"]')

        self.wait_for_element_and_click('//div[@id="tab_45"]//i[@class="fa fa-plus"]')
        self.wait_loader()

        start_date_field = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="data_inizio"]'))
        )
        start_date_field.send_keys("01/01/2025")

        end_date_field = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="data_fine"]'))
        )
        end_date_field.clear()
        end_date_field.send_keys("31/12/2025")

        credit_limit_field = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="fido_assicurato"]'))
        )
        credit_limit_field.send_keys("50000", Keys.ENTER)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        date_field = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="data"]'))
        )
        date_field.send_keys("01/01/2025")

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-idanagrafica_add-container"]',
            option_text="Cliente"
        )

        self.wait_for_element_and_click('//button[@class="btn btn-primary"]')
        self.wait_loader()

        self.wait_for_element_and_click('//a[@class="btn btn-primary"]')

        description_field = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione_riga"]'))
        )
        description_field.send_keys("prova")

        price_field = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario"]'))
        )
        price_field.send_keys("51000")

        self.wait_for_element_and_click('//button[@class="btn btn-primary pull-right"]')

        self.wait_for_element_and_click('//button[@id="save"]')
        self.wait_loader()

        warning_message = self.find(By.XPATH, '//div[@class="alert alert-warning text-center"]').text
        self.assertEqual("Attenzione!", warning_message[0:11])

        self.wait_for_element_and_click('//a[@id="elimina"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.wait_loader()

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
        self.wait_loader()

        self.navigateTo("Anagrafiche")
        self.clear_filters()

    def ricerca_coordinate(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))
        )
        search_input.send_keys("Admin spa", Keys.ENTER)
        self.wait_for_search_results()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')

        self.wait_for_element_and_click('//a[@data-op="ricerca-coordinate"]')

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_loader()

        self.wait_for_element_and_click('//a[@onclick="modificaPosizione()"]')

        self.wait_for_element_and_click('//ul//li[2]//div')

        latitude = self.find(By.XPATH, '//input[@id="lat"]').text
        self.assertNotEqual(latitude, "0")

        longitude = self.find(By.XPATH, '//input[@id="lng"]').text
        self.assertNotEqual(longitude, "0")

        self.wait_for_element_and_click('//button[@class="close"]')
        self.wait_loader()

        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.clear_filters()

    def elimina_selezionati(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))
        )
        search_input.send_keys("Vettore", Keys.ENTER)
        self.wait_for_search_results()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')

        self.wait_for_element_and_click('//a[@data-op="delete-bulk"]')

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.wait_loader()

        no_results_message = self.find(By.XPATH, '//tbody//tr[1]').text
        self.assertEqual(no_results_message, "La ricerca non ha portato alcun risultato.")

        self.clear_filters()

    def cambia_relazione(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        self.search_entity("Cliente")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')

        self.wait_for_element_and_click('//a[@data-op="cambia-relazione"]')

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-idrelazione-container"]',
            option_text="Attivo"
        )

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')
        self.wait_loader()

        relation = self.find(By.XPATH, '//tbody//tr//td[7]').text
        self.assertEqual(relation, "Attivo")

        self.wait_for_element_and_click('//tbody//tr//td[7]')
        self.wait_loader()

        self.wait_for_element_and_click('//span[@id="select2-idrelazione-container"]//span[@class="select2-selection__clear"]')

        search_field = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))
        )
        search_field.send_keys("Da contattare", Keys.ENTER)

        self.wait_for_element_and_click('//button[@id="save"]')
        self.wait_loader()

        self.navigateTo("Anagrafiche")
        self.wait_loader()

        new_relation = self.find(By.XPATH, '//tbody//tr//td[7]').text
        self.assertNotEqual(new_relation, "Attivo")

        self.clear_filters()
