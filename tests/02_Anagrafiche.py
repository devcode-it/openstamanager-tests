from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.Test import Test


class Anagrafiche(Test):
    def setUp(self):
        super().setUp()
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

    def add_anagrafica(self, nome: str, tipo: str):
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()
        self.input(modal, 'Denominazione').setValue(nome)
        self.input(modal, 'Tipo di anagrafica').setByText(tipo)
        modal.find_element(By.XPATH, './/div[@class="modal-footer"]//button[@type="submit"]').click()
        self.wait_loader()

    def modifica_anagrafica(self, tipologia: str):
        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.search_entity("Cliente")
        self.click_first_result()

        self.wait_for_element_and_click('//*[@id="select2-tipo-container"]')

        self.wait_for_dropdown_and_select(
            '(//input[@class="select2-search__field"])[2]',
            option_text=tipologia
        )

        self.input(None, 'Partita IVA').setValue("05024030287")
        self.input(None, 'Codice fiscale').setValue("05024030287")

        address_field = self.wait_driver.until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="indirizzo"]'))
        )
        address_field.clear()
        self.send_keys_and_wait(address_field, "Via controllo caratteri speciali: &\"<>èéàòùì?'`", wait_modal=False)

        self.input(None, 'C.A.P.').setValue("35042")
        self.input(None, 'Città').setValue("Este")

        self.wait_for_element_and_click('//button[@id="save"]')
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
        self.clear_filters()

    def verifica_anagrafica(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.clear_filters()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Tipologia"]/input'))
        )
        search_input.clear()
        self.send_keys_and_wait(search_input, "Privato", wait_modal=False)
        self.wait_for_search_results()

        entity_name = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[2]'))
        ).text
        self.assertEqual("Cliente", entity_name)

        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.clear_filters()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))
        )
        search_input.clear()
        self.send_keys_and_wait(search_input, "Anagrafica di Prova da Eliminare", wait_modal=False)
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
        self.send_keys_and_wait(description_field, "Test", wait_modal=False)

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
        self.wait(lambda driver: len(driver.window_handles) > 1)
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

        self.navigateTo("Anagrafiche")
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
        self.wait(lambda driver: len(driver.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.clear_filters()

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
        self.wait(lambda driver: len(driver.window_handles) > 1)

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask "]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.navigateTo("Anagrafiche")
        self.wait_loader()
        self.clear_filters()
