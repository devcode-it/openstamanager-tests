from selenium.webdriver.common.by import By
from common.Test import Test


class StatiAttivita(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Attività")
        self.wait_loader()

    def test_creazione_stati_attivita(self):
        self._creazione_stati_attivita("0001", "Stato di Prova da Modificare", "#9d2929")
        self._creazione_stati_attivita("0002", "Stato di Prova da Eliminare", "#38468f")
        self._modifica_stato_attivita("Stato di Attività di Prova")
        self._elimina_stato_attivita()
        self._verifica_stato_attivita()

    def _creazione_stati_attivita(self, codice: str, descrizione: str, colore: str):
        self.navigateTo("Stati di attività")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'Colore').setValue(colore)
        self.input(modal, 'Codice').setValue(codice)
        self.input(modal, 'Descrizione').setValue(descrizione)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def _search_stato_attivita(self, nome: str):
        self.navigateTo("Stati di attività")
        self.wait_loader()
        
        search_input = self.find(By.XPATH, '//th[@id="th_Descrizione"]/input')
        search_input.clear()
        self.send_keys_and_wait(search_input, nome, wait_modal=False)

    def _modifica_stato_attivita(self, modifica: str):
        self._search_stato_attivita('Stato di Prova da Modificare')
        self.click_first_result()
        self.input(None, 'Descrizione').setValue(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.navigateTo("Stati di attività")
        self.wait_loader()
        self.clear_filters()

    def _elimina_stato_attivita(self):
        self._search_stato_attivita('Stato di Prova da Eliminare')
        self.click_first_result()
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.clear_filters()

    def _verifica_stato_attivita(self):
        self._search_stato_attivita("Stato di Attività di Prova")
        modificato = self.find(By.XPATH, '//tbody//tr[1]//td[3]').text
        self.assertEqual("Stato di Attività di Prova", modificato)
        self.clear_filters()

        self._search_stato_attivita("Stato di Attività di Prova da Eliminare")
        eliminato = self.find(By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)
        self.clear_filters()