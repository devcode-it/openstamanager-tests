from common.Test import Test
from selenium.webdriver.common.by import By


class AttributiCombinazioni(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Magazzino")

    def test_creazione_attributi(self):
        self.creazione_attributi("Attributo di Prova da Modificare")
        self.creazione_attributi("Attributo di Prova da Eliminare")
        self.modifica_attributi("Taglie")
        self.elimina_attributi()
        self.verifica_attributi()

    def creazione_attributi(self, titolo=str):
        self.navigate_to_and_wait("Attributi Combinazioni")

        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Titolo').setValue(titolo)
        self.wait_for_element_and_click('//button[@type="submit"]')

        self.wait_for_element_and_click('//button[@onclick="aggiungiValore(this)"]')
        modal = self.wait_modal()
        nome_input = self.find(By.XPATH, '//input[@id="nome"]')
        self.send_keys_and_wait(nome_input, 'S')

        self.wait_for_element_and_click('//button[@onclick="aggiungiValore(this)"]')
        self.wait_modal()
        nome_input = self.find(By.XPATH, '//input[@id="nome"]')
        self.send_keys_and_wait(nome_input, 'M')

        self.wait_for_element_and_click('//button[@onclick="aggiungiValore(this)"]')
        self.wait_modal()
        nome_input = self.find(By.XPATH, '//input[@id="nome"]')
        self.send_keys_and_wait(nome_input, 'L')

    def modifica_attributi(self, modifica=str):
        self.navigate_to_and_wait("Attributi Combinazioni")

        search_input = self.find(By.XPATH, '//th[@id="th_Nome"]/input')
        search_input.clear()
        self.send_keys_and_wait(search_input, 'Attributo di Prova da Modificare', wait_modal=False)
        self.click_first_result()

        self.input(None, 'Titolo').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Attributi Combinazioni")
        self.clear_filters()

    def elimina_attributi(self):
        self.navigate_to_and_wait("Attributi Combinazioni")

        search_input = self.find(By.XPATH, '//th[@id="th_Nome"]/input')
        search_input.clear()
        self.send_keys_and_wait(search_input, 'Attributo di Prova da Eliminare', wait_modal=False)
        self.click_first_result()
        self.delete_current_and_clear()

    def verifica_attributi(self):
        self.navigate_to_and_wait("Attributi Combinazioni")

        search_input = self.find(By.XPATH, '//th[@id="th_Nome"]/input')
        search_input.clear()
        self.send_keys_and_wait(search_input, "Taglie", wait_modal=False)
        self.wait_for_search_results()
        modificato = self.get_table_text(1, 2)
        self.assertEqual("Taglie", modificato)

        self.clear_filters()

        search_input = self.find(By.XPATH, '//th[@id="th_Nome"]/input')
        search_input.clear()
        self.send_keys_and_wait(search_input, "Attributo di Prova da Eliminare", wait_modal=False)
        self.wait_for_search_results()
        eliminato = self.get_empty_table_message()
        self.assertEqual("Nessun dato presente nella tabella", eliminato)
