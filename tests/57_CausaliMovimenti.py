from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CausaliMovimenti(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")

    def test_creazione_causali_movimenti(self):
        self.creazione_causali_movimenti("Causale Movimento di Prova da Modificare", "Descrizione Causale", "Carico")
        self.creazione_causali_movimenti("Causale Movimento di Prova da Eliminare", "Descrizione Causale", "Scarico")
        self.modifica_causale_movimento("Causale Movimento di Prova")
        self.elimina_causale_movimento()
        self.verifica_causale_movimento()
        
    def creazione_causali_movimenti(self, nome = str, descrizione = str, tipo = str):
        self.navigate_to_and_wait("Causali movimenti")
        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        select = self.input(modal, 'Tipo movimento')
        select.setByText(tipo)
        self.input(modal, 'Descrizione').setValue(descrizione)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def modifica_causale_movimento(self, modifica):
        self.navigate_to_and_wait("Causali movimenti")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Causale Movimento di Prova da Modificare', wait_modal=False)
        self.click_first_table_row()

        self.input(None,'Nome').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Causali movimenti")
        self.clear_filters()

    def elimina_causale_movimento(self):
        self.navigate_to_and_wait("Causali movimenti")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Causale Movimento di Prova da Eliminare', wait_modal=False)
        self.click_first_table_row()

        self.delete_current_and_clear()

    def verifica_causale_movimento(self):
        self.navigate_to_and_wait("Causali movimenti")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Causale Movimento di Prova", wait_modal=False)
        modificato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[2]'))).text
        self.assertEqual("Causale Movimento di Prova", modificato)
        self.clear_filters()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Causale Movimento di Prova da Eliminare", wait_modal=False)
        eliminato = self.get_empty_table_message()
        self.assertEqual("Nessun dato presente nella tabella", eliminato)