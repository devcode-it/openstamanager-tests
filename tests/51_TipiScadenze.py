from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TipiScadenze(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")

    def test_creazione_tipi_scadenze(self):
        self.creazione_tipi_scadenze(nome= "Tipo di Scadenza di Prova da Modificare")
        self.creazione_tipi_scadenze(nome= "Tipo di Scadenza di Prova da Eliminare")
        self.modifica_tipi_scadenze("Tipo di Scadenza di Prova")
        self.elimina_tipi_scadenze()
        self.verifica_tipi_scadenze()
        
    def creazione_tipi_scadenze(self, nome = str):
        self.navigate_to_and_wait("Tipi scadenze")

        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def modifica_tipi_scadenze(self, modifica = str):
        self.navigate_to_and_wait("Tipi scadenze")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Tipo di Scadenza di Prova da Modificare', wait_modal=False)
        self.click_first_table_row()

        self.input(None,'Nome').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Tipi scadenze")
        self.clear_filters()

    def elimina_tipi_scadenze(self):
        self.navigate_to_and_wait("Tipi scadenze")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Tipo di Scadenza di Prova da Eliminare', wait_modal=False)
        self.click_first_table_row()

        self.delete_current_and_clear()

    def verifica_tipi_scadenze(self):
        self.navigate_to_and_wait("Tipi scadenze")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Tipo di Scadenza di Prova", wait_modal=False)
        modificato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[2]'))).text
        self.assertEqual("Tipo di Scadenza di Prova", modificato)
        self.clear_filters()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Tipo di Scadenza di Prova da Eliminare", wait_modal=False)
        eliminato = self.get_empty_table_message()
        self.assertEqual("Nessun dato presente nella tabella", eliminato)