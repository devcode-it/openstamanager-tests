from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class GestioneTask (Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")

    def test_creazione_task(self):
        self.modifica_task("Backup")
        self.verifica_task()
        
    def modifica_task(self, modifica = str):
        self.navigate_to_and_wait("Gestione task")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Backup automatico', wait_modal=False)
        self.click_first_result()

        self.input(None,'Nome').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Gestione task")
        self.clear_filters()

    def verifica_task(self):
        self.navigate_to_and_wait("Gestione task")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Backup", wait_modal=False)
        modificato = self.get_table_text(1, 2)
        self.assertEqual("Backup", modificato)
        self.clear_filters()
