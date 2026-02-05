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
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')
        
    def creazione_utenti_permessi(self, nome):
        self.navigateTo('Utenti e permessi')
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        self.wait_for_element_and_click('//div[@id="form_38-"]//button[@type="button"]')
        self.wait_loader()

    def modifica_utenti_permessi(self, user: str, anag: str, passw: str, modifica: str):
        self.navigateTo('Utenti e permessi')
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Gruppo"]/input'))
        )
        self.send_keys_and_wait(search_input, 'Tipo Utente di Prova', wait_modal=False)
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td[2]')
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

        self.navigateTo('Utenti e permessi')
        self.wait_loader()
        self.clear_filters()

    def elimina_utenti_permessi(self):
        self.navigateTo('Utenti e permessi')
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Gruppo"]/input'))
        )
        self.send_keys_and_wait(search_input, 'Tipo Utente di Prova', wait_modal=False)
        self.wait_for_search_results()

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask "]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.wait_loader()
        self.clear_filters()

    def verifica_utenti_permessi(self):
        self.navigateTo('Utenti e permessi')
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Gruppo"]/input'))
        )
        self.send_keys_and_wait(search_input, 'Tipo Utente di Prova', wait_modal=False)
        self.wait_for_search_results()

        eliminato = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]'))
        ).text
        self.assertEqual('Nessun dato presente nella tabella', eliminato)