from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Listini(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Magazzino")

    def test_creazione_listino_cliente(self):
        self.navigate_to_and_wait("Listini cliente")

        self.creazione_listino_cliente("Listino cliente di Prova da Modificare","01/12/2026", "01/01/2026")
        self.creazione_listino_cliente("Listino cliente di Prova da Eliminare", "01/12/2026", "01/01/2026")
        self.modifica_listino_cliente("Listino cliente di Prova")
        self.elimina_listino_cliente()
        self.verifica_listino_cliente()
        self.aggiorna_listino_cliente()
        self.aggiungi_a_listino_cliente()

    def creazione_listino_cliente(self, nome:str, dataatt: str, datascad: str):
        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Data attivazione').setValue(dataatt)
        self.input(modal, 'Data scadenza default').setValue(datascad)
        self.input(modal, 'Nome').setValue(nome)
        self.wait_for_element_and_click('//div[@class="modal-footer"]//button[@type="submit"]')

    def modifica_listino_cliente(self, modifica:str):
        self.navigate_to_and_wait("Listini cliente")

        self.search_by_th_and_click_first("th_Nome", 'Listino cliente di Prova da Modificare')

        self.wait_for_dropdown_and_select('//span[@class="select2-selection select2-selection--single"]', option_text='001')

        self.wait_for_element_and_click('//button[@class="btn btn-success btn-block"]')

        prezzo_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario_fisso"]')))
        prezzo_input.send_keys("10,00")
        sconto_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="sconto_percentuale"]')))
        sconto_input.send_keys("10")
        self.wait_for_element_and_click('(//button[@class="btn btn-success"])[2]')

        self.input(None,'Nome').setValue(modifica)
        self.wait_for_element_and_click('//button[@id="save"]')
        self.click_back_button()
        self.clear_filters()

    def elimina_listino_cliente(self):
        self.navigate_to_and_wait("Listini cliente")

        self.search_by_th_and_click_first("th_Nome", 'Listino cliente di Prova da Eliminare')

        self.delete_current_and_clear()

    def verifica_listino_cliente(self):
        self.navigate_to_and_wait("Listini cliente")

        self.search_by_th("th_Nome", "Listino cliente di Prova")
        modificato = self.get_table_text(1, 2)
        self.assertEqual("Listino cliente di Prova", modificato)
        self.clear_filters()

        self.verify_deleted_by_th("th_Nome", "Listino cliente di Prova da Eliminare")
        self.clear_filters()

    def aggiorna_listino_cliente(self):
        self.navigate_to_and_wait("Anagrafiche")

        self.search_by_th("th_Ragione-sociale", "Cliente")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="update_price_list"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_listino-container"]', option_text='Listino cliente di Prova')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.click_first_table_row()
        self.wait_loader()

        self.wait_for_element_and_click('(//button[@class="select2-selection__clear"])[4]')
        self.wait_for_element_and_click('//button[@id="save"]')
        self.wait_loader()

        self.navigate_to_and_wait("Anagrafiche")
        self.wait_for_element_and_click('//th[@id="th_Ragione-sociale"]/i[@class="deleteicon fa fa-times"]')
        self.expandSidebar("Magazzino")

    def aggiungi_a_listino_cliente(self):
        self.navigate_to_and_wait("Articoli")

        self.search_by_th("th_Codice", "001")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="add_price_list"]')

        self.wait_for_element_and_click('//span[@id="select2-id_listino-container"]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--selectable select2-results__option--highlighted"]')

        sconto_input = self.find(By.XPATH, '//input[@id="sconto_percentuale"]')
        sconto_input.send_keys("10")
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.navigate_to_and_wait("Listini cliente")

        self.click_first_table_row()
        self.wait_loader()

        self.find(By.XPATH, '//tr[1]//td[8]')
