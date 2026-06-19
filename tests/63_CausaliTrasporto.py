from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Causali(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")

    def test_creazione_causali(self):
        self.navigate_to_and_wait("Causali trasporto")

        self.creazione_causali("Causale di Prova da Modificare")
        self.creazione_causali("Causale di Prova da Eliminare")
        self.modifica_causale("Causale di Prova")
        self.elimina_causale()
        self.verifica_causale()
        
    def creazione_causali(self, descrizione= str):
        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Descrizione').setValue(descrizione)
        self.wait_for_element_and_click('//div[@class="modal-footer"]//button[@type="submit"]')

    def modifica_causale(self, modifica = str):
        self.navigate_to_and_wait("Causali trasporto")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Causale di Prova da Modificare', wait_modal=False)
        self.click_first_table_row()

        self.input(None,'Descrizione').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Causali trasporto")
        self.wait_for_element_and_click('//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]')

    def elimina_causale(self):
        self.navigate_to_and_wait("Causali trasporto")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Causale di Prova da Eliminare', wait_modal=False)
        self.click_first_table_row()

        self.delete_current_and_clear()

    def verifica_causale(self):
        self.navigate_to_and_wait("Causali trasporto")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, "Causale di Prova", wait_modal=False)
        modificato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[2]'))).text
        self.assertEqual("Causale di Prova", modificato)
        self.clear_filters()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, "Causale di Prova da Eliminare", wait_modal=False)
        eliminato = self.get_empty_table_message()
        self.assertEqual("Nessun dato presente nella tabella", eliminato)