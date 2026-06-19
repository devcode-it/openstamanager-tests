from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class StatiPreventivi(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")

    def test_creazione_stati_preventivi(self):
        self.creazione_stati_preventivi("Stato Preventivi di Prova da Modificare", "fa fa-check text-success")
        self.creazione_stati_preventivi("Stato Preventivi di Prova da Eliminare", "fa fa-thumbs-down text-danger")
        self.modifica_stati_preventivi("Stato Preventivi di Prova")
        self.elimina_stati_preventivi()
        self.verifica_stati_preventivi()
        
    def creazione_stati_preventivi(self, descrizione = str, icona = str):
        self.navigate_to_and_wait("Stati dei preventivi")
        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Colore').setValue("#000545")
        self.input(modal, 'Descrizione').setValue(descrizione)
        self.input(modal, 'Icona').setValue(icona)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def modifica_stati_preventivi(self, modifica = str):
        self.navigate_to_and_wait("Stati dei preventivi")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Stato Preventivi di Prova da Modificare', wait_modal=False)
        self.click_first_table_row()

        self.input(None,'Descrizione').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Stati dei preventivi")
        self.wait_for_element_and_click('//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]')

    def elimina_stati_preventivi(self):
        self.navigate_to_and_wait("Stati dei preventivi")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Stato Preventivi di Prova da Eliminare', wait_modal=False)
        self.click_first_table_row()

        self.delete_current_and_clear()

    def verifica_stati_preventivi(self):
        self.navigate_to_and_wait("Stati dei preventivi")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, "Stato Preventivi di Prova", wait_modal=False)
        modificato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[2]'))).text
        self.assertEqual("Stato Preventivi di Prova", modificato)
        self.clear_filters()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, "Stato Preventivi di Prova da Eliminare", wait_modal=False)
        eliminato = self.get_empty_table_message()
        self.assertEqual("Nessun dato presente nella tabella", eliminato)