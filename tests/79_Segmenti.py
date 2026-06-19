from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Segmenti(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")

    def test_creazione_segmenti(self):
        self.navigate_to_and_wait("Segmenti")

        self.creazione_segmenti("Segmento di Prova da Modificare", "1234/2026", "Articoli")
        self.creazione_segmenti("Segmento di Prova da Eliminare", "1234/2026", "Articoli")
        self.modifica_segmento("Segmento di Prova")
        self.elimina_segmento()
        self.verifica_segmento()
        
    def creazione_segmenti(self, nome = str, maschera = str, modulo = str):
        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        self.input(modal, 'Maschera').setValue(maschera)
        self.wait_for_dropdown_and_select('//span[@id="select2-module_add-container"]', option_text=modulo)
        self.wait_for_element_and_click('//div[@class="modal-footer"]//button[@type="submit"]')
        self.wait_loader()

    def modifica_segmento(self, modifica = str):
        self.navigate_to_and_wait("Segmenti")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Segmento di Prova da Modificare', wait_modal=False)
        self.click_first_table_row()

        self.input(None,'Nome').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Segmenti")
        self.clear_filters()

    def elimina_segmento(self):
        self.navigate_to_and_wait("Segmenti")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Segmento di Prova da Eliminare', wait_modal=False)
        self.click_first_table_row()

        self.delete_current_and_clear()

    def verifica_segmento(self):
        self.navigate_to_and_wait("Segmenti")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Segmento di Prova", wait_modal=False)
        modificato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[2]'))).text
        self.assertEqual("Segmento di Prova", modificato)
        self.clear_filters()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Segmento di Prova da Eliminare", wait_modal=False)
        eliminato = self.get_empty_table_message()
        self.assertEqual("Nessun dato presente nella tabella", eliminato)