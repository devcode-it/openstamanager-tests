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
        self.navigate_to_and_wait("Categorie")
        self.creazione_categorie(nome="Categoria di Prova da Modificare", colore="#30db67")
        self.creazione_categorie(nome="Categoria di Prova da Eliminare", colore="#ea2c2c")
        self.modifica_categorie("Categoria di Prova")
        self.elimina_categorie()
        self.verifica_categorie()
        
    def creazione_categorie(self, nome: str, colore: str):
        self.click_add_button()
        modal = self.wait_modal()

        colore_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@name="colore_add"]')))
        colore_input.send_keys(colore)

        nome_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@name="nome_add"]')))
        nome_input.send_keys(nome)

        self.wait_for_element_and_click('//div[@class="modal-footer"]//button[@type="submit"]')
        self.wait_loader()

    def modifica_categorie(self, modifica: str):
        self.navigate_to_and_wait("Categorie")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Categoria di Prova da Modificare', wait_modal=False)
        self.click_first_table_row()

        self.driver.execute_script('window.scrollTo(0,0)')
        self.input(None, 'Nome').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Categorie")
        self.clear_filters()

    def elimina_categorie(self):
        self.navigate_to_and_wait("Categorie")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Categoria di Prova da Eliminare", wait_modal=False)
        self.click_first_result()
        self.wait_loader()

        self.driver.execute_script('window.scrollTo(0,0)')
        self.delete_current_and_clear()

    def verifica_categorie(self):
        self.navigate_to_and_wait("Categorie")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Categoria di Prova", wait_modal=False)
        self.click_first_result()
        self.wait_loader()

        self.driver.execute_script('window.scrollTo(0,0)')
        modificato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@name="nome"]'))
        ).get_attribute('value')
        self.assertEqual('Categoria di Prova', modificato)

        self.navigate_to_and_wait("Categorie")
        self.clear_filters()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Categoria di Prova da Eliminare', wait_modal=False)
        eliminato = self.get_empty_table_message()
        self.assertEqual('Nessun dato presente nella tabella', eliminato)
