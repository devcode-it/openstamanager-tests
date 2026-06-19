from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ModelliPrimaNota(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")

    def test_creazione_modelli_prima_nota(self):
        self.creazione_modelli_prima_nota(nome="Modello Prima Nota di Prova da Modificare", causale="Prova anticipo fattura num. {numero} del {data}")
        self.creazione_modelli_prima_nota(nome="Modello Prima Nota di Prova da Eliminare", causale="Prova anticipo fattura num. {numero} del {data}")
        self.modifica_modello_prima_nota("Modello Prima Nota di Prova")
        self.elimina_modello_prima_nota()
        self.verifica_modello_prima_nota()
        
    def creazione_modelli_prima_nota(self, nome = str, causale = str):
        self.navigate_to_and_wait("Modelli prima nota")

        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        self.input(modal, 'Causale').setValue(causale)

        self.wait_for_element_and_click('//span[@id="select2-conto0-container"]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--selectable select2-results__option--highlighted"]')

        self.wait_for_element_and_click('//span[@id="select2-conto1-container"]')
        self.wait_for_element_and_click('//input[@class="select2-search__field"]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--selectable select2-results__option--highlighted"]')
        self.wait_loader()

        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def modifica_modello_prima_nota(self, modifica = str):
        self.navigate_to_and_wait("Modelli prima nota")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Modello Prima Nota di Prova da Modificare', wait_modal=False)
        self.click_first_table_row()

        self.input(None,'Nome').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Modelli prima nota")
        self.clear_filters()

    def elimina_modello_prima_nota(self):
        self.navigate_to_and_wait("Modelli prima nota")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Modello Prima Nota di Prova da Eliminare', wait_modal=False)
        self.click_first_table_row()

        self.delete_current_and_clear()

    def verifica_modello_prima_nota(self):
        self.navigate_to_and_wait("Modelli prima nota")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Modello Prima Nota di Prova", wait_modal=False)
        modificato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[2]'))).text
        self.assertEqual("Modello Prima Nota di Prova", modificato)
        self.clear_filters()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Modello Prima Nota di Prova da Eliminare", wait_modal=False)
        eliminato = self.get_empty_table_message()
        self.assertEqual("Nessun dato presente nella tabella", eliminato)