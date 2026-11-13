from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MarcheImpianti(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")

    def test_creazione_marche(self):
        self.navigate_to_and_wait("Marche")
        self.creazione_marche(nome= "Marca di Prova da Modificare")
        self.creazione_marche(nome= "Marca di Prova da Eliminare")
        self.modifica_marche("Marca di Prova")
        self.elimina_marche()
        self.verifica_marche()
        
    def creazione_marche(self, nome = str):
        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        self.wait_for_element_and_click('//div[@class="modal-footer"]//button[@type="submit"]')

    def modifica_marche(self, modifica = str):
        self.navigate_to_and_wait("Marche")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Marca di Prova da Modificare', wait_modal=False)
        self.click_first_result()

        self.input(None,'Nome').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Marche")
        self.clear_filters()

    def elimina_marche(self):
        self.navigate_to_and_wait("Marche")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Marca di Prova da Eliminare', wait_modal=False)
        self.click_first_result()

        self.delete_current_and_clear()

    def verifica_marche(self):
        self.navigate_to_and_wait("Marche")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Marca di Prova", wait_modal=False)
        modificato = self.get_table_text(1, 2)
        self.assertEqual("Marca di Prova", modificato)
        self.clear_filters()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Marca di Prova da Eliminare", wait_modal=False)
        eliminato = self.get_empty_table_message()
        self.assertEqual("Nessun dato presente nella tabella", eliminato)