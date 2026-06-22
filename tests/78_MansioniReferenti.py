from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MansioniReferenti(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")
        self.navigate_to_and_wait("Mansioni referenti")

    def test_creazione_mansioni_referenti(self):
        self.creazione_mansioni_referenti("Mansione Referente di Prova da Modificare")
        self.creazione_mansioni_referenti("Mansione Referente di Prova da Eliminare")
        self.modifica_mansione_referente("Mansione Referente di Prova")
        self.elimina_mansione_referente()
        self.verifica_mansione_referente()
        
    def creazione_mansioni_referenti(self, mansione= str):
        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Mansione').setValue(mansione)
        self.wait_for_element_and_click('//div[@class="modal-footer"]//button[@type="submit"]')

    def modifica_mansione_referente(self, modifica = str):
        self.navigate_to_and_wait("Mansioni referenti")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Mansione Referente di Prova da Modificare', wait_modal=False)
        self.click_first_table_row()

        self.input(None,'Nome').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Mansioni referenti")
        self.clear_filters()

    def elimina_mansione_referente(self):
        self.navigate_to_and_wait("Mansioni referenti")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Mansione Referente di Prova da Eliminare', wait_modal=False)
        self.click_first_table_row()

        self.delete_current_and_clear()

    def verifica_mansione_referente(self):
        self.navigate_to_and_wait("Mansioni referenti")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Mansione Referente di Prova", wait_modal=False)
        modificato = self.get_table_text(1, 2)
        self.assertEqual("Mansione Referente di Prova", modificato)
        self.clear_filters()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Mansione Referente di Prova da Eliminare", wait_modal=False)
        eliminato = self.get_empty_table_message()
        self.assertEqual("Nessun dato presente nella tabella", eliminato)