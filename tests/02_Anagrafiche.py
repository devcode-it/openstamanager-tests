from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from common.Test import Test
from common.functions import (
    search_entity, click_first_result, wait_for_filter_cleared,
    clear_filters, wait_for_search_results, wait_for_element_and_click,
    wait_for_dropdown_and_select, wait_loader
)


class Anagrafiche(Test):
    def setUp(self):
        super().setUp()
        self.wait_driver = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")

    def test_creazione_anagrafica(self):
        try:
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
        except Exception as e:
            self.driver.save_screenshot(f"error_test_creazione_anagrafica.png")
            raise e

    def add_anagrafica(self, nome=str, tipo=str):
        try:
            wait_for_element_and_click(self.driver, self.wait_driver, '//i[@class="fa fa-plus"]')

            modal = self.wait_modal()
            self.input(modal, 'Denominazione').setValue(nome)
            select = self.input(modal, 'Tipo di anagrafica')
            select.setByText(tipo)

            modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
            wait_loader(self.driver, self.wait_driver)
        except Exception as e:
            self.driver.save_screenshot(f"error_add_anagrafica_{nome}.png")
            raise Exception(f"Failed to add entity {nome}: {str(e)}")

    def modifica_anagrafica(self, tipologia:str):
        try:
            self.navigateTo("Anagrafiche")
            wait_loader(self.driver, self.wait_driver)
            search_entity(self.driver, self.wait_driver, "Cliente")
            click_first_result(self.driver, self.wait_driver)

            self.wait_driver.until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="select2-tipo-container"]'))
            ).click()

            self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, '(//input[@class="select2-search__field"])[2]'))
            ).send_keys(tipologia, Keys.ENTER)
            wait_loader(self.driver, self.wait_driver)

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
            wait_loader(self.driver, self.wait_driver)

            self.navigateTo("Anagrafiche")
            wait_loader(self.driver, self.wait_driver)

            clear_filters(self.driver, self.wait_driver)
        except Exception as e:
            self.driver.save_screenshot("error_modifica_anagrafica.png")
            raise Exception(f"Failed to modify entity: {str(e)}")

    def elimina_anagrafica(self):
        try:
            self.navigateTo("Anagrafiche")
            wait_loader(self.driver, self.wait_driver)
            search_entity(self.driver, self.wait_driver, 'Anagrafica di Prova da Eliminare')
            click_first_result(self.driver, self.wait_driver)

            wait_for_element_and_click(self.driver, self.wait_driver, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')

            wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="swal2-confirm btn btn-lg btn-danger"]')
            wait_loader(self.driver, self.wait_driver)

            clear_filters(self.driver, self.wait_driver)
        except Exception as e:
            self.driver.save_screenshot("error_elimina_anagrafica.png")
            raise Exception(f"Failed to delete entity: {str(e)}")

    def verifica_anagrafica(self):
        try:
            self.navigateTo("Anagrafiche")
            wait_loader(self.driver, self.wait_driver)

            search_input = self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Tipologia"]/input'))
            )
            search_input.clear()
            search_input.send_keys("Privato", Keys.ENTER)
            wait_for_search_results(self.driver, self.wait_driver)

            entity_name = self.driver.find_element(By.XPATH,'//tbody//tr//td[2]').text
            self.assertEqual("Cliente", entity_name)

            clear_filters(self.driver, self.wait_driver)

            search_input = self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))
            )
            search_input.clear()
            search_input.send_keys("Anagrafica di Prova da Eliminare", Keys.ENTER)
            wait_for_search_results(self.driver, self.wait_driver)

            no_results_message = self.driver.find_element(By.XPATH,'//tbody//tr//td[1]').text
            self.assertEqual("La ricerca non ha portato alcun risultato.", no_results_message)

            clear_filters(self.driver, self.wait_driver)
        except Exception as e:
            self.driver.save_screenshot("error_verifica_anagrafica.png")
            raise Exception(f"Failed to verify entity: {str(e)}")

    def crea_attivita(self):
        try:
            self.navigateTo("Anagrafiche")
            wait_loader(self.driver, self.wait_driver)

            search_entity(self.driver, self.wait_driver, "Cliente")
            click_first_result(self.driver, self.wait_driver)

            wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="btn btn-info dropdown-toggle"]')
            wait_for_element_and_click(self.driver, self.wait_driver, '(//a[@class="btn dropdown-item bound clickable"])[1]')

            wait_for_dropdown_and_select(
                self.driver, self.wait_driver,
                '(//form[@id="add-form"]//span[@class="select2-selection select2-selection--single"])[8]',
                '(//li[@class="select2-results__option"])'
            )

            description_field = self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[2]'))
            )
            description_field.click()
            description_field.send_keys("Test")

            wait_for_element_and_click(self.driver, self.wait_driver, '//div[@class="col-md-12 text-right"]//button[@type="button"]')

            self.navigateTo("Anagrafiche")
            wait_loader(self.driver, self.wait_driver)
            search_entity(self.driver, self.wait_driver, "Cliente")
            click_first_result(self.driver, self.wait_driver)

            wait_for_element_and_click(self.driver, self.wait_driver, '//a[@id="link-tab_28"]')
            activity_number = self.driver.find_element(By.XPATH,'//div[@id="tab_28"]//tbody//tr//td[2]').text
            self.assertEqual("1", activity_number)

            wait_for_element_and_click(self.driver, self.wait_driver, '//div[@id="tab_28"]//tbody//td[2]')

            wait_for_element_and_click(self.driver, self.wait_driver, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
            wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="swal2-confirm btn btn-lg btn-danger"]')
            wait_loader(self.driver, self.wait_driver)

            self.navigateTo("Anagrafiche")
            clear_filters(self.driver, self.wait_driver)
        except Exception as e:
            self.driver.save_screenshot("error_crea_attivita.png")
            raise Exception(f"Failed to create activity: {str(e)}")

    def crea_preventivo(self):
        try:
            self.navigateTo("Anagrafiche")
            wait_loader(self.driver, self.wait_driver)

            search_entity(self.driver, self.wait_driver, "Cliente")
            click_first_result(self.driver, self.wait_driver)

            wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="btn btn-info dropdown-toggle"]')
            wait_for_element_and_click(self.driver, self.wait_driver, '(//a[@class="btn dropdown-item bound clickable"])[2]')
            modal = self.wait_modal()

            wait_for_dropdown_and_select(
                self.driver, self.wait_driver,
                '(//form[@id="add-form"]//span[@class="select2-selection select2-selection--single"])[4]',
                '(//li[@class="select2-results__option"])'
            )

            wait_for_dropdown_and_select(
                self.driver, self.wait_driver,
                '(//form[@id="add-form"]//span[@class="select2-selection select2-selection--single"])[5]',
                '(//li[@class="select2-results__option"])'
            )

            self.input(modal, 'Nome').setValue("Preventivo di prova anagrafica")

            wait_for_element_and_click(self.driver, self.wait_driver, '(//div[@id="form_13-"]//button[@class="btn btn-primary"])')

            self.navigateTo("Anagrafiche")
            wait_loader(self.driver, self.wait_driver)
            search_entity(self.driver, self.wait_driver, "Cliente")
            click_first_result(self.driver, self.wait_driver)

            wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="btn btn-tool"]')

            quote_text = self.driver.find_element(By.XPATH,'(//div[@class="card-body"]//li)[7]').text
            self.assertEqual("Preventivo 1", quote_text[0:12])

            wait_for_element_and_click(self.driver, self.wait_driver, '(//div[@class="card-body"]//li//a)[5]')

            self.wait_driver.until(lambda driver: len(driver.window_handles) > 1)
            self.driver.switch_to.window(self.driver.window_handles[1])

            wait_for_element_and_click(self.driver, self.wait_driver, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
            wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="swal2-confirm btn btn-lg btn-danger"]')
            wait_loader(self.driver, self.wait_driver)

            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

            self.navigateTo("Anagrafiche")
            clear_filters(self.driver, self.wait_driver)
        except Exception as e:
            self.driver.save_screenshot("error_crea_preventivo.png")
            raise Exception(f"Failed to create quote: {str(e)}")

    def crea_contratto(self):
        try:
            self.navigateTo("Anagrafiche")
            wait_loader(self.driver, self.wait_driver)

            search_entity(self.driver, self.wait_driver, "Cliente")
            click_first_result(self.driver, self.wait_driver)

            wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="btn btn-info dropdown-toggle"]')
            wait_for_element_and_click(self.driver, self.wait_driver, '(//a[@class="btn dropdown-item bound clickable"])[3]')
            modal = self.wait_modal()

            self.input(modal, 'Nome').setValue("Contratto di prova anagrafica")

            wait_for_dropdown_and_select(
                self.driver, self.wait_driver,
                '(//form[@id="add-form"]//span[@class="select2-selection select2-selection--single"])[2]',
                '(//li[@class="select2-results__option"])'
            )

            wait_for_element_and_click(self.driver, self.wait_driver, '(//div[@id="form_31-"]//button[@class="btn btn-primary"])')

            wait_for_element_and_click(self.driver, self.wait_driver, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
            wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="swal2-confirm btn btn-lg btn-danger"]')
            wait_loader(self.driver, self.wait_driver)

            self.navigateTo("Anagrafiche")
            wait_loader(self.driver, self.wait_driver)
            clear_filters(self.driver, self.wait_driver)
        except Exception as e:
            self.driver.save_screenshot("error_crea_contratto.png")
            raise Exception(f"Failed to create contract: {str(e)}")

    def crea_ordine_cliente(self):
        try:
            self.navigateTo("Anagrafiche")
            wait_loader(self.driver, self.wait_driver)

            search_entity(self.driver, self.wait_driver, "Cliente")
            click_first_result(self.driver, self.wait_driver)

            wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="btn btn-info dropdown-toggle"]')
            wait_for_element_and_click(self.driver, self.wait_driver, '(//a[@class="btn dropdown-item bound clickable"])[4]')
            self.wait_modal()

            wait_for_element_and_click(self.driver, self.wait_driver, '(//div[@id="form_24-"]//button[@class="btn btn-primary"])')
            wait_loader(self.driver, self.wait_driver)

            self.navigateTo("Anagrafiche")
            wait_loader(self.driver, self.wait_driver)
            search_entity(self.driver, self.wait_driver, "Cliente")
            click_first_result(self.driver, self.wait_driver)

            wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="btn btn-tool"]')

            order_text = self.driver.find_element(By.XPATH,'(//div[@class="card-body"]//li)[7]').text
            self.assertEqual("Ordine cliente 01", order_text[0:17])

            wait_for_element_and_click(self.driver, self.wait_driver, '(//div[@class="card-body"]//li//a)[5]')

            self.wait_driver.until(lambda driver: len(driver.window_handles) > 1)
            self.driver.switch_to.window(self.driver.window_handles[1])

            wait_for_element_and_click(self.driver, self.wait_driver, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
            wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="swal2-confirm btn btn-lg btn-danger"]')
            wait_loader(self.driver, self.wait_driver)

            self.navigateTo("Anagrafiche")
            clear_filters(self.driver, self.wait_driver)

            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
        except Exception as e:
            self.driver.save_screenshot("error_crea_ordine_cliente.png")
            raise Exception(f"Failed to create customer order: {str(e)}")

    def crea_DDT_uscita(self):
        try:
            self.navigateTo("Anagrafiche")
            wait_loader(self.driver, self.wait_driver)

            search_entity(self.driver, self.wait_driver, "Cliente")
            click_first_result(self.driver, self.wait_driver)

            wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="btn btn-info dropdown-toggle"]')
            wait_for_element_and_click(self.driver, self.wait_driver, '(//a[@class="btn dropdown-item bound clickable"])[5]')
            modal = self.wait_modal()

            wait_for_dropdown_and_select(
                self.driver, self.wait_driver,
                '(//form[@id="add-form"]//span[@class="select2-selection select2-selection--single"])[3]',
                '(//li[@class="select2-results__option"])'
            )

            wait_for_element_and_click(self.driver, self.wait_driver, '(//div[@id="form_26-"]//button[@class="btn btn-primary"])')

            self.navigateTo("Anagrafiche")
            wait_loader(self.driver, self.wait_driver)
            search_entity(self.driver, self.wait_driver, "Cliente")
            click_first_result(self.driver, self.wait_driver)

            wait_for_element_and_click(self.driver, self.wait_driver, '//a[@id="link-tab_17"]')

            ddt_number = self.driver.find_element(By.XPATH,'//div[@id="tab_17"]//tbody//td[2]').text
            self.assertEqual("01", ddt_number)

            wait_for_element_and_click(self.driver, self.wait_driver, '//div[@id="tab_17"]//tbody//td[2]')

            wait_for_element_and_click(self.driver, self.wait_driver, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
            wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="swal2-confirm btn btn-lg btn-danger"]')
            wait_loader(self.driver, self.wait_driver)

            self.navigateTo("Anagrafiche")
            clear_filters(self.driver, self.wait_driver)
        except Exception as e:
            self.driver.save_screenshot("error_crea_DDT_uscita.png")
            raise Exception(f"Failed to create delivery note: {str(e)}")

    def crea_fattura_vendita(self):
        try:
            self.navigateTo("Anagrafiche")
            wait_loader(self.driver, self.wait_driver)

            search_entity(self.driver, self.wait_driver, "Cliente")
            click_first_result(self.driver, self.wait_driver)

            wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="btn btn-info dropdown-toggle"]')
            wait_for_element_and_click(self.driver, self.wait_driver, '(//a[@class="btn dropdown-item bound clickable"])[6]')

            wait_for_element_and_click(self.driver, self.wait_driver, '(//div[@id="form_14-"]//button[@class="btn btn-primary"])')

            self.navigateTo("Anagrafiche")
            wait_loader(self.driver, self.wait_driver)
            search_entity(self.driver, self.wait_driver, "Cliente")
            click_first_result(self.driver, self.wait_driver)

            wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="btn btn-tool"]')

            invoice_text = self.driver.find_element(By.XPATH,'(//div[@class="card-body"]//li)[7]').text
            self.assertEqual("Fattura immediata di vendita", invoice_text[0:28])

            wait_for_element_and_click(self.driver, self.wait_driver, '(//div[@class="card-body"]//li//a)[5]')

            self.wait_driver.until(lambda driver: len(driver.window_handles) > 1)

            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

            wait_for_element_and_click(self.driver, self.wait_driver, '//div[@id="tab_0"]//a[@class="btn btn-danger ask "]')
            wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="swal2-confirm btn btn-lg btn-danger"]')
            wait_loader(self.driver, self.wait_driver)

            self.navigateTo("Anagrafiche")
            wait_loader(self.driver, self.wait_driver)
            clear_filters(self.driver, self.wait_driver)
        except Exception as e:
            self.driver.save_screenshot("error_crea_fattura_vendita.png")
            raise Exception(f"Failed to create sales invoice: {str(e)}")

    def aggiunta_referente(self):
        try:
            self.navigateTo("Anagrafiche")
            wait_loader(self.driver, self.wait_driver)

            search_entity(self.driver, self.wait_driver, "Cliente")
            click_first_result(self.driver, self.wait_driver)

            wait_for_element_and_click(self.driver, self.wait_driver, '//a[@id="link-tab_3"]')

            wait_for_element_and_click(self.driver, self.wait_driver, '//h4//i[@class="fa fa-plus"]')
            modal = self.wait_modal()

            self.input(modal,'Nominativo').setValue("Referente di prova")

            wait_for_element_and_click(self.driver, self.wait_driver, '//div[@class="modal-dialog modal-lg"]//i[@class="fa fa-plus"]')
            modal = self.wait_modal()

            job_title_input = self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, '//div[@class="modal-content"]//div[@id="form_82-"]//input[@id="nome"]'))
            )
            job_title_input.send_keys("Segretario")

            wait_for_element_and_click(self.driver, self.wait_driver, '(//button[@type="submit"])[4]')

            wait_for_element_and_click(self.driver, self.wait_driver, '(//button[@type="submit"])[3]')
            wait_loader(self.driver, self.wait_driver)

            wait_for_element_and_click(self.driver, self.wait_driver, '//div[@id="tab_3"]//tbody//tr//td[2]')

            name_input = self.find(By.XPATH, '(//input[@id="nome"])[2]')
            name_input.clear()
            name_input.send_keys("Prova")

            wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="btn btn-success pull-right"]')
            wait_loader(self.driver, self.wait_driver)

            contact_name = self.find(By.XPATH, '//div[@id="tab_3"]//tbody//tr//td[2]').text
            self.assertEqual(contact_name, "Prova")

            wait_for_element_and_click(self.driver, self.wait_driver, '//div[@id="tab_3"]//tbody//tr//td[2]')
            wait_for_element_and_click(self.driver, self.wait_driver, '(//a[@class="btn btn-danger ask"])[2]')
            wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="swal2-confirm btn btn-lg btn-danger"]')
            wait_loader(self.driver, self.wait_driver)

            empty_message = self.find(By.XPATH, '//div[@id="tab_3"]//tbody//tr').text
            self.assertEqual(empty_message, "Nessun dato presente nella tabella")

            wait_for_element_and_click(self.driver, self.wait_driver, '//h4//i[@class="fa fa-plus"]')
            modal = self.wait_modal()

            contact_name_input = self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, '(//input[@id="nome"])[2]'))
            )
            contact_name_input.send_keys("Referente di prova")

            wait_for_dropdown_and_select(
                self.driver, self.wait_driver,
                '//span[@id="select2-idmansione-container"]',
                '//ul[@id="select2-idmansione-results"]//li[1]'
            )

            wait_for_element_and_click(self.driver, self.wait_driver, '(//button[@type="submit"])[3]')
            wait_loader(self.driver, self.wait_driver)

            search_input = self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Mansione"]/input'))
            )
            search_input.send_keys("Segretario", Keys.ENTER)
            wait_for_search_results(self.driver, self.wait_driver)

            job_title = self.driver.find_element(By.XPATH,'//div[@id="tab_3"]//tbody//tr//td[3]').text
            self.assertEqual("Segretario", job_title)

            self.navigateTo("Anagrafiche")
            wait_loader(self.driver, self.wait_driver)
            clear_filters(self.driver, self.wait_driver)
        except Exception as e:
            self.driver.save_screenshot("error_aggiunta_referente.png")
            raise Exception(f"Failed to add contact: {str(e)}")

    def aggiunta_sede(self):
        try:
            self.navigateTo("Anagrafiche")
            wait_loader(self.driver, self.wait_driver)

            search_entity(self.driver, self.wait_driver, "Cliente")
            click_first_result(self.driver, self.wait_driver)

            wait_for_element_and_click(self.driver, self.wait_driver, '//a[@id="link-tab_4"]')

            wait_for_element_and_click(self.driver, self.wait_driver, '//div[@id="tab_4"]//i[@class="fa fa-plus"]')

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

            wait_for_dropdown_and_select(
                self.driver, self.wait_driver,
                '(//span[@id="select2-id_nazione-container"])[2]',
                '//li[@class="select2-results__option select2-results__option--highlighted"]'
            )

            wait_for_element_and_click(self.driver, self.wait_driver, '(//button[@type="submit"])[3]')

            wait_for_element_and_click(self.driver, self.wait_driver, '//div[@id="tab_4"]//tbody/tr//td[2]')

            location_name_input = self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, '//input[@id="nomesede"]'))
            )
            location_name_input.clear()
            location_name_input.send_keys("Prova")

            wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="btn btn-primary pull-right"]')
            wait_loader(self.driver, self.wait_driver)

            location_name = self.find(By.XPATH, '//div[@id="tab_4"]//tbody/tr//td[2]').text
            self.assertEqual(location_name, "Prova")

            wait_for_element_and_click(self.driver, self.wait_driver, '//div[@id="tab_4"]//tbody/tr//td[2]')
            wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="btn btn-danger "]')
            wait_for_element_and_click(self.driver, self.wait_driver, '//button[@class="swal2-confirm btn btn-lg btn-danger"]')
            wait_loader(self.driver, self.wait_driver)

            empty_message = self.find(By.XPATH, '//div[@id="tab_4"]//tbody//tr').text
            self.assertEqual(empty_message, "Nessun dato presente nella tabella")

            wait_for_element_and_click(self.driver, self.wait_driver, '//div[@id="tab_4"]//i[@class="fa fa-plus"]')

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

            wait_for_dropdown_and_select(
                self.driver, self.wait_driver,
                '(//span[@id="select2-id_nazione-container"])[2]',
                '//li[@class="select2-results__option select2-results__option--highlighted"]'
            )

            wait_for_element_and_click(self.driver, self.wait_driver, '(//button[@type="submit"])[3]')

            search_input = self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, '(//th[@id="th_Nome"]/input)[2]'))
            )
            search_input.send_keys("Filiale XY", Keys.ENTER)
            wait_for_search_results(self.driver, self.wait_driver)

            location_name = self.driver.find_element(By.XPATH,'//div[@id="tab_4"]//tbody//td[2]').text
            self.assertEqual("Filiale XY", location_name)

            self.navigateTo("Anagrafiche")
            wait_loader(self.driver, self.wait_driver)
            clear_filters(self.driver, self.wait_driver)
        except Exception as e:
            self.driver.save_screenshot("error_aggiunta_sede.png")
            raise Exception(f"Failed to add location: {str(e)}")

    def plugin_statistiche(self):
        try:
            self.navigateTo("Anagrafiche")
            wait_loader(self.driver, self.wait_driver)

            search_entity(self.driver, self.wait_driver, "Cliente")
            click_first_result(self.driver, self.wait_driver)

            wait_for_element_and_click(self.driver, self.wait_driver, '//a[@id="link-tab_7"]')

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
            wait_loader(self.driver, self.wait_driver)
            clear_filters(self.driver, self.wait_driver)
        except Exception as e:
            self.driver.save_screenshot("error_plugin_statistiche.png")
            raise Exception(f"Failed to verify statistics plugin: {str(e)}")

    def dichiarazione_di_intento(self):
        try:
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
        except Exception as e:
            self.driver.save_screenshot("error_dichiarazione_di_intento.png")
            raise Exception(f"Failed to manage declaration of intent: {str(e)}")

    def assicurazione_crediti(self):
        try:
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
        except Exception as e:
            self.driver.save_screenshot("error_assicurazione_crediti.png")
            raise Exception(f"Failed to manage credit insurance: {str(e)}")

    def ricerca_coordinate(self):
        try:
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
        except Exception as e:
            self.driver.save_screenshot("error_ricerca_coordinate.png")
            raise Exception(f"Failed to search coordinates: {str(e)}")

    def elimina_selezionati(self):
        try:
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
        except Exception as e:
            self.driver.save_screenshot("error_elimina_selezionati.png")
            raise Exception(f"Failed to delete selected entities: {str(e)}")

    def cambia_relazione(self):
        try:
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
        except Exception as e:
            self.driver.save_screenshot("error_cambia_relazione.png")
            raise Exception(f"Failed to change relation: {str(e)}")
