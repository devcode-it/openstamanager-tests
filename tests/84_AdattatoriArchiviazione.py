from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Adattatori(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")

    def test_creazione_adattatore(self):
        self.navigate_to_and_wait("Adattatori di archiviazione")

        self.creazione_adattatore("Adattatore di Prova da Modificare", "Archiviazione FTP")
        self.creazione_adattatore("Adattatore di Prova da Eliminare", "Archiviazione FTP")
        self.modifica_adattatore("Adattatore di Prova")
        self.elimina_adattatore()
        self.verifica_adattatore()
        
    def creazione_adattatore(self, nome: str, tipo: str):
        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        self.wait_for_dropdown_and_select('//span[@id="select2-class_add-container"]', option_text=tipo)
        self.wait_for_element_and_click('//div[@class="modal-footer"]//button[@type="submit"]')

    def modifica_adattatore(self, modifica = str):
        self.navigate_to_and_wait("Adattatori di archiviazione")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Adattatore di Prova da Modificare', wait_modal=False)
        self.click_first_result()

        self.input(None,'Nome').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Adattatori di archiviazione")
        self.clear_filters()

    def elimina_adattatore(self):
        self.navigate_to_and_wait("Adattatori di archiviazione")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Adattatore di Prova da Eliminare', wait_modal=False)
        self.click_first_result()

        self.delete_current_and_clear()

    def verifica_adattatore(self):
        self.navigate_to_and_wait("Adattatori di archiviazione")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Adattatore di Prova", wait_modal=False)
        modificato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[2]'))).text
        self.assertEqual("Adattatore di Prova", modificato)
        self.clear_filters()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Adattatore di Prova da Eliminare", wait_modal=False)
        eliminato = self.get_empty_table_message()
        self.assertEqual("Nessun dato presente nella tabella", eliminato)