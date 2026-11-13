from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Categorie(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")
        self.wait_loader()

    def test_creazione_categorie(self):
        self.navigate_to_and_wait("Categorie file")
        self.creazione_categorie(descrizione="Categoria di Prova da Modificare")
        self.creazione_categorie(descrizione="Categoria di Prova da Eliminare")
        self.modifica_categorie("Categoria di Prova")
        self.elimina_categorie()
        self.verifica_categorie()
        
    def creazione_categorie(self, descrizione: str):
        self.click_add_button()
        modal = self.wait_modal()

        descrizione_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@name="name_add"]')))
        descrizione_input.send_keys(descrizione)

        self.wait_for_element_and_click('//div[@class="modal-footer"]//button[@type="submit"]')
        self.wait_loader()

    def modifica_categorie(self, modifica: str):
        self.navigate_to_and_wait("Categorie file")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Categoria di Prova da Modificare', wait_modal=False)
        self.click_first_table_row()

        self.input(None, 'Descrizione').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Categorie file")
        self.clear_filters()

    def elimina_categorie(self):
        self.navigate_to_and_wait("Categorie file")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, "Categoria di Prova da Eliminare", wait_modal=False)
        self.click_first_result()
        self.wait_loader()

        self.delete_current_and_clear()

    def verifica_categorie(self):
        self.navigate_to_and_wait("Categorie file")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, "Categoria di Prova", wait_modal=False)
        self.click_first_result()
        self.wait_loader()

        modificato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@name="name"]'))
        ).get_attribute('value')
        self.assertEqual('Categoria di Prova', modificato)

        self.navigate_to_and_wait("Categorie file")
        self.clear_filters()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Categoria di Prova da Eliminare', wait_modal=False)
        eliminato = self.get_empty_table_message()
        self.assertEqual('Nessun dato presente nella tabella', eliminato)
