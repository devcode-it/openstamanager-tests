from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TipiScadenze(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")

    def test_creazione_categorie_contratti(self):
        self.creazione_categorie_contratti("Categoria di Contratto di Prova da Modificare")
        self.creazione_categorie_contratti("Categoria di Contratto di Prova da Eliminare")
        self.modifica_categorie_contratti("Categoria di Contratto di Prova")
        self.elimina_categorie_contratti()
        self.verifica_categorie_contratti()
        
    def creazione_categorie_contratti(self, descrizione= str):
        self.navigate_to_and_wait("Categorie contratti")
        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(descrizione)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def modifica_categorie_contratti(self, modifica = str):
        self.navigate_to_and_wait("Categorie contratti")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))) 
        self.send_keys_and_wait(search_input, 'Categoria di Contratto di Prova da Modificare', wait_modal=False)
        self.click_first_table_row()

        self.input(None,'Nome').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Categorie contratti")
        self.clear_filters()

    def elimina_categorie_contratti(self):  
        self.navigate_to_and_wait("Categorie contratti")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))) 
        self.send_keys_and_wait(search_input, 'Categoria di Contratto di Prova da Eliminare', wait_modal=False)
        self.click_first_table_row()

        self.delete_current_and_clear()

    def verifica_categorie_contratti(self):
        self.navigate_to_and_wait("Categorie contratti")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))) 
        self.send_keys_and_wait(search_input, 'Categoria di Contratto di Prova', wait_modal=False)
        self.click_first_table_row()       