from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.Test import Test


class UtentiPermessi(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar('Strumenti')
        self.expandSidebar('Gestione accessi')
        self.wait_loader()

    def test_creazione_utenti_permessi(self):
        self.creazione_utenti_permessi(nome='Tipo Utente di Prova')
        self.modifica_utenti_permessi('Test', 'Admin spa', '1qa2ws3ed!', 'Lettura e scrittura')
        self.elimina_utenti_permessi()
        self.verifica_utenti_permessi()
        
    def creazione_utenti_permessi(self, nome):
        self.navigate_to_and_wait('Utenti e permessi')

        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        self.wait_for_element_and_click('//div[@id="form_38-"]//button[@type="button"]')
        self.wait_loader()

    def modifica_utenti_permessi(self, user: str, anag: str, passw: str, modifica: str):
        self.navigate_to_and_wait('Utenti e permessi')

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Gruppo"]/input'))
        )
        self.send_keys_and_wait(search_input, 'Tipo Utente di Prova', wait_modal=False)
        self.wait_loader()

        self.click_first_table_row()
        self.wait_for_element_and_click('//a[@class="btn btn-sm btn-primary bound clickable"]')
        modal = self.wait_modal()

        self.input(None, 'Username').setValue(user)
        self.wait_for_dropdown_and_select('//span[@id="select2-idanag-container"]', option_text=anag)

        self.input(None, 'Password').setValue(passw)
        self.wait_for_element_and_click('//button[@id="submit-button"]')
        self.wait_loader()

        self.wait_for_dropdown_and_select('//span[@id="select2-permesso_1-container"]', option_text=modifica)
        self.wait_for_dropdown_and_select('//span[@id="select2-permesso_2-container"]', option_text=modifica)
        self.wait_for_dropdown_and_select('//span[@id="select2-permesso_8-container"]', option_text=modifica)
        self.wait_for_dropdown_and_select('//span[@id="select2-permesso_38-container"]', option_text=modifica)

        self.navigate_to_and_wait('Utenti e permessi')
        self.clear_filters()

    def elimina_utenti_permessi(self):
        self.navigate_to_and_wait('Utenti e permessi')

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Gruppo"]/input'))
        )
        self.send_keys_and_wait(search_input, 'Tipo Utente di Prova', wait_modal=False)
        self.wait_for_search_results()

        self.click_first_table_row()
        self.delete_current_and_clear()


    def verifica_utenti_permessi(self):
        self.navigate_to_and_wait('Utenti e permessi')

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Gruppo"]/input'))
        )
        self.send_keys_and_wait(search_input, 'Tipo Utente di Prova', wait_modal=False)
        self.wait_for_search_results()

        eliminato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]'))
        ).text
        self.assertEqual('Nessun dato presente nella tabella', eliminato)