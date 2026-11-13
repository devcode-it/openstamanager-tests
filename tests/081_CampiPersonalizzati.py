from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.Test import Test
from common.functions import TestHelperMixin


class Campi_personalizzati(Test, TestHelperMixin):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")

    def test_campi_personalizzati(self):
        self.navigate_to_and_wait("Campi personalizzati")

        self.creazione_campi_personalizzati(nome="Campo personalizzato di Prova da Modificare", contenuto="Prova")
        self.creazione_campi_personalizzati(nome="Campo personalizzato di Prova da Eliminare", contenuto="Prova")
        self.modifica_campi_personalizzati(modifica="Campo personalizzato di Prova")
        self.elimina_campi_personalizzati()
        self.verifica_campi_personalizzati()
        
    def creazione_campi_personalizzati(self, nome: str, contenuto: str):
        self.click_add_button()
        modal = self.wait_modal()

        self.wait_for_dropdown_and_select('//span[@id="select2-module_id_add-container"]', option_text='Attività')

        self.input(modal, 'Nome').setValue(nome)
        self.input(modal, 'Codice').setValue(contenuto)

        self.wait_for_element_and_click('//div[@class="modal-body"]//button[@type="submit"]')
        self.wait_loader()

    def modifica_campi_personalizzati(self, modifica: str):
        self.navigate_to_and_wait("Campi personalizzati")
        
        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))
        )
        self.send_keys_and_wait(search_input, 'Campo personalizzato di Prova da Modificare', wait_modal=False)
        self.wait_for_search_results()

        self.click_first_result()
        self.input(None, 'Nome').setValue(modifica)
        self.click_save_button()
        self.wait_loader()

        self.navigate_to_and_wait("Campi personalizzati")
        self.clear_filters()

    def elimina_campi_personalizzati(self):
        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))
        )
        self.send_keys_and_wait(search_input, 'Campo personalizzato di Prova da Eliminare', wait_modal=False)
        self.wait_for_search_results()

        self.click_first_result()
        self.delete_current_and_clear()

        self.navigate_to_and_wait("Campi personalizzati")
        self.clear_filters()

    def verifica_campi_personalizzati(self):
        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))
        )
        self.send_keys_and_wait(search_input, "Campo personalizzato di Prova", wait_modal=False)
        self.wait_for_search_results()

        modificato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[4]'))
        ).text
        self.assertEqual("Campo personalizzato di Prova", modificato)
        self.clear_filters()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))
        )
        self.send_keys_and_wait(search_input, "Campo personalizzato di Prova da Eliminare", wait_modal=False)
        self.wait_for_search_results()

        eliminato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]'))
        ).text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)

