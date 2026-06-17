from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Anagrafiche(Test):
    def setUp(self):
        super().setUp()
        self.navigateToAndWait("Anagrafiche")

    def test_creazione_anagrafica(self):
        self._add_anagrafica('Cliente', 'Cliente')
        self._add_anagrafica('Tecnico', 'Tecnico')
        self._add_anagrafica('Fornitore', 'Fornitore')
        self._add_anagrafica('Vettore', 'Vettore')
        self._add_anagrafica('Agente', 'Agente')
        self._add_anagrafica('Anagrafica di Prova da Eliminare', 'Cliente')
        self._modifica_anagrafica('Privato')
        self._elimina_anagrafica()
        self._verifica_anagrafica()
        
        self._crea_attivita()
        self._crea_preventivo()
        self._crea_contratto()
        self._crea_ordine_cliente()
        self._crea_DDT_uscita()
        self._crea_fattura_vendita()

    def _add_anagrafica(self, nome: str, tipo: str):
        modal = self.open_and_fill_modal({'Denominazione': nome})
        self.input(modal, 'Tipo di anagrafica').setByText(tipo)
        self.submit_modal(modal)

    def _modifica_anagrafica(self, tipologia: str):
        self.navigateToAndWait("Anagrafiche")
        self.search_entity_and_click_first("Cliente")

        self.wait_for_element_and_click('//*[@id="select2-tipo-container"]')

        self.wait_for_dropdown_and_select(
            '//input[@class="select2-search__field"]',
            option_text=tipologia
        )

        self.input(None, 'Partita IVA').setValue("05024030287")
        self.input(None, 'Codice fiscale').setValue("05024030287")
        self.input(None, 'Città').setValue("Este")
        self.input(None, 'C.A.P.').setValue("35042")

        address_field = self.find(By.XPATH, '//input[@id="indirizzo"]')
        address_field.clear()
        self.send_keys_and_wait(address_field, "Via controllo caratteri speciali: &\"<>èéàòùì?'`", wait_modal=False)

        self.click_save_button()
        self.navigateToAndWait("Anagrafiche")
        self.clear_filters()

    def _elimina_anagrafica(self):
        self.navigateToAndWait("Anagrafiche")
        self.search_entity_and_click_first('Anagrafica di Prova da Eliminare')
        self.wait_loader()
        self.delete_current_and_clear()

    def _verifica_anagrafica(self):
        self.navigateToAndWait("Anagrafiche")
        self.clear_filters()

        self.search_by_th("th_Tipologia", "Privato")
        self.wait_for_search_results()

        entity_name = self.get_table_text(1, 2)
        self.assertEqual("Cliente", entity_name)

        self.navigateToAndWait("Anagrafiche")
        self.clear_filters()

        self.verify_deleted_by_th("th_Ragione-sociale", "Anagrafica di Prova da Eliminare")

    def _crea_attivita(self):
        self.navigateToAndWait("Anagrafiche")
        self.search_entity_and_click_first("Cliente")

        self.wait_for_element_and_click('//button[@class="btn btn-info dropdown-toggle"]')
        self.wait_for_element_and_click('(//a[@class="btn dropdown-item bound clickable"])[1]')

        self.wait_for_dropdown_and_select(
            '(//form[@id="add-form"]//span[@class="select2-selection select2-selection--single"])[6]',
            '//li[@class="select2-results__option select2-results__option--selectable select2-results__option--highlighted"]'
        )

        description_field = self.find(By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[2]')
        description_field.click()
        self.send_keys_and_wait(description_field, "Test", wait_modal=False)

        self.wait_for_element_and_click('//div[@class="col-md-12 text-right"]//button[@type="button"]')

        self.navigateToAndWait("Anagrafiche")
        self.search_entity_and_click_first("Cliente")

        self.wait_for_element_and_click('//a[@id="link-tab_28"]')
        activity_number = self.find(By.XPATH, '//div[@id="tab_28"]//tbody//tr//td[2]').text
        self.assertEqual("1", activity_number)

        self.click_first_table_row()
        self.close_tour()
        self.delete_current_and_clear()

        self.navigateToAndWait("Anagrafiche")
        self.clear_filters()

    def _crea_preventivo(self):
        self.navigateToAndWait("Anagrafiche")
        self.search_entity_and_click_first("Cliente")

        self.wait_for_element_and_click('//button[@class="btn btn-info dropdown-toggle"]')
        self.wait_for_element_and_click('(//a[@class="btn dropdown-item bound clickable"])[2]')
        modal = self.wait_modal()

        self.wait_for_dropdown_and_select(
            '(//form[@id="add-form"]//span[@class="select2-selection select2-selection--single"])[2]',
            '//li[@class="select2-results__option select2-results__option--selectable select2-results__option--highlighted"]'
        )

        self.input(modal, 'Nome').setValue("Preventivo di prova anagrafica")
        self.wait_for_element_and_click('(//div[@id="form_13-"]//button[@class="btn btn-primary"])')

        self.navigateToAndWait("Anagrafiche")
        self.search_entity("Cliente")
        self.click_first_result()

        self.wait_for_element_and_click('//button[@class="btn btn-tool"]')
        quote_text = self.find(By.XPATH, '//div[@id="documenti-collegati-body"]//li').text
        self.assertEqual("Preventivo 1", quote_text[0:12])

        self.wait_for_element_and_click('(//div[@class="card-body"]//li//a)[5]')
        self.wait(lambda driver: len(driver.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])

        self.delete_current_and_clear()

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.navigateToAndWait("Anagrafiche")
        self.clear_filters()

    def _crea_contratto(self):
        self.navigateToAndWait("Anagrafiche")
        self.search_entity_and_click_first("Cliente")

        self.wait_for_element_and_click('//button[@class="btn btn-info dropdown-toggle"]')
        self.wait_for_element_and_click('(//a[@class="btn dropdown-item bound clickable"])[3]')
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue("Contratto di prova anagrafica")
        self.wait_for_element_and_click('(//div[@id="form_31-"]//button[@class="btn btn-primary"])')

        self.close_tour()
        
        self.delete_current_and_clear()

        self.navigateToAndWait("Anagrafiche")
        self.clear_filters()

    def _crea_ordine_cliente(self):
        self.navigateToAndWait("Anagrafiche")
        self.search_entity_and_click_first("Cliente")

        self.wait_for_element_and_click('//button[@class="btn btn-info dropdown-toggle"]')
        self.wait_for_element_and_click('(//a[@class="btn dropdown-item bound clickable"])[4]')
        self.wait_modal()

        self.wait_for_element_and_click('(//div[@id="form_24-"]//button[@class="btn btn-primary"])')

        self.navigateToAndWait("Anagrafiche")
        self.search_entity_and_click_first("Cliente")

        self.wait_for_element_and_click('//button[@class="btn btn-tool"]')
        order_text = self.find(By.XPATH, '//div[@id="documenti-collegati-body"]//li').text
        self.assertEqual("Ordine cliente 01", order_text[0:17])

        self.wait_for_element_and_click('(//div[@class="card-body"]//li//a)[5]')
        self.wait(lambda driver: len(driver.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])

        self.close_tour()
        self.delete_current_and_clear()

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.navigateToAndWait("Anagrafiche")
        self.clear_filters()

    def _crea_DDT_uscita(self):
        self.navigateToAndWait("Anagrafiche")
        self.search_entity_and_click_first("Cliente")

        self.wait_for_element_and_click('//button[@class="btn btn-info dropdown-toggle"]')
        self.wait_for_element_and_click('(//a[@class="btn dropdown-item bound clickable"])[5]')
        modal = self.wait_modal()

        self.wait_for_dropdown_and_select(
            '//form[@id="add-form"]//span[@class="select2-selection select2-selection--single"]',
            '//li[@class="select2-results__option select2-results__option--selectable select2-results__option--highlighted"]'
        )

        self.wait_for_element_and_click('(//div[@id="form_26-"]//button[@class="btn btn-primary"])')

        self.navigateToAndWait("Anagrafiche")
        self.search_entity_and_click_first("Cliente")

        self.wait_for_element_and_click('//a[@id="link-tab_17"]')
        ddt_number = self.find(By.XPATH, '//div[@id="tab_17"]//tbody//td[2]').text
        self.assertEqual("", ddt_number)

        self.wait_for_element_and_click('//div[@id="tab_17"]//tbody//td[2]')

        self.close_tour()

        self.delete_current_and_clear()

        self.navigateToAndWait("Anagrafiche")
        self.clear_filters()

    def _crea_fattura_vendita(self):
        self.navigateToAndWait("Anagrafiche")
        self.search_entity_and_click_first("Cliente")

        self.wait_for_element_and_click('//button[@class="btn btn-info dropdown-toggle"]')
        self.wait_for_element_and_click('(//a[@class="btn dropdown-item bound clickable"])[6]')
        self.wait_for_element_and_click('(//div[@id="form_14-"]//button[@class="btn btn-primary"])')

        self.navigateToAndWait("Anagrafiche")
        self.search_entity_and_click_first("Cliente")

        self.wait_for_element_and_click('//button[@class="btn btn-tool"]')
        invoice_text = self.find(By.XPATH, '//div[@id="documenti-collegati-body"]//li').text
        self.assertEqual("Fattura immediata di vendita", invoice_text[0:28])

        self.wait_for_element_and_click('(//div[@class="card-body"]//li//a)[5]')
        self.wait(lambda driver: len(driver.window_handles) > 1)

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.close_tour()

        self.delete_current_and_clear()

        self.navigateToAndWait("Anagrafiche")
        self.clear_filters()
