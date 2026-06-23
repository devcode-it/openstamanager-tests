from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.Test import Test

class Anagrafiche(Test):
    def setUp(self):
        super().setUp()
        self.wait_driver = self.wait_driver
        self.navigate_to_and_wait("Anagrafiche")

    def test_bulk_anagrafica(self):
        self.cambia_relazione()
        self.elimina_selezionati()
        self.esporta_selezionati()
        self.aggiorna_agente()
        self.imposta_listino()
        self.ricerca_coordinate()
        self.esporta_email_newsletter()
        self.crea_lista()
        
    def cambia_relazione(self):
        self.navigate_to_and_wait("Anagrafiche")
        self.search_entity("Cliente")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_relation"]')

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_relazione-container"]',
            option_text="Attivo"
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        relation = self.get_table_text(1, 7)
        self.assertEqual(relation, "Attivo")

        self.click_first_result()

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_relazione-container"]',
            option_text='Da contattare'
        )
        self.wait_for_element_and_click('//button[@id="save"]')

        self.navigate_to_and_wait("Anagrafiche")

        new_relation = self.get_table_text(1, 7)
        self.assertNotEqual(new_relation, "Attivo")

        self.clear_filters()

    def elimina_selezionati(self):
        self.navigate_to_and_wait("Anagrafiche")

        search_input = self.driver.find_element(By.XPATH, '//th[@id="th_Ragione-sociale"]/input')
        self.send_keys_and_wait(search_input, "Vettore", wait_modal=False)
        self.wait_for_search_results()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="delete_bulk"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        no_results_message = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]'))
        ).text
        self.assertEqual(no_results_message, "Nessun dato presente nella tabella")

        self.clear_filters()
    
    def esporta_selezionati(self):
        self.navigate_to_and_wait("Anagrafiche")
    
        search_input = self.driver.find_element(By.XPATH, '//th[@id="th_Ragione-sociale"]/input')
        self.send_keys_and_wait(search_input, "Cliente", wait_modal=False)
        self.wait_for_search_results()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="export_csv"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

    def aggiorna_agente(self):
        self.navigate_to_and_wait("Anagrafiche")

        search_input = self.driver.find_element(By.XPATH, '//th[@id="th_Ragione-sociale"]/input')
        self.send_keys_and_wait(search_input, "Cliente", wait_modal=False)
        self.wait_for_search_results()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="update_agenti"]')

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_agente-container"]',
            option_text="Agente"
        )

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')
        self.click_first_result()

        agente = self.driver.find_element(By.XPATH, '//span[@id="select2-id_agente-container"]').text
        self.assertEqual(agente, "Agente")

    def imposta_listino(self):
        self.expandSidebar("Magazzino")
        self.navigate_to_and_wait("Listini cliente")

        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Data attivazione').setValue('01/01/2026')
        self.input(modal, 'Data scadenza default').setValue('31/12/2026')
        self.input(modal, 'Nome').setValue('Test')
        self.wait_for_element_and_click('//div[@class="modal-footer"]//button[@type="submit"]')

        self.navigate_to_and_wait("Anagrafiche")

        search_input = self.driver.find_element(By.XPATH, '//th[@id="th_Ragione-sociale"]/input')
        self.send_keys_and_wait(search_input, "Cliente", wait_modal=False)
        self.wait_for_search_results()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="update_price_list"]')

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_listino-container"]',
            option_text="Test"
        )

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')
        self.click_first_result()

        agente = self.driver.find_element(By.XPATH, '//span[@id="select2-id_listino-container"]').text
        self.assertEqual(agente, "Test")

    def ricerca_coordinate(self):
        self.navigate_to_and_wait("Anagrafiche")

        self.search_by_th("th_Ragione-sociale", "Admin spa", wait_modal=False)
        self.wait_for_search_results()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="search_coordinates"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.click_first_table_row()
        self.wait_for_element_and_click('//a[@onclick="modificaPosizione()"]')
        self.wait_for_element_and_click('//ul//li[2]//div')

        latitude = self.driver.find_element(By.XPATH, '//input[@id="lat"]').text
        self.assertNotEqual(latitude, "0")
        longitude = self.driver.find_element(By.XPATH, '//input[@id="lng"]').text
        self.assertNotEqual(longitude, "0")

        self.wait_for_element_and_click('//button[@class="close"]')

        self.navigate_to_and_wait("Anagrafiche")
        self.clear_filters()

    def esporta_email_newsletter(self):
        self.navigate_to_and_wait("Anagrafiche")

        search_input = self.driver.find_element(By.XPATH, '//th[@id="th_Ragione-sociale"]/input')
        self.send_keys_and_wait(search_input, "Cliente", wait_modal=False)
        self.wait_for_search_results()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="export_newsletter_csv"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

    def crea_lista(self):
        self.navigate_to_and_wait("Anagrafiche")

        search_input = self.driver.find_element(By.XPATH, '//th[@id="th_Ragione-sociale"]/input')
        self.send_keys_and_wait(search_input, "Cliente", wait_modal=False)
        self.wait_for_search_results()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="crea-lista"]')

        self.input(name='Nome lista').setValue('Lista test')
        
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')