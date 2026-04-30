from selenium.webdriver.common.by import By
from common.Test import Test


class FasceOrarie(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Attività")
        self.wait_loader()

    def test_creazione_fasce_orarie(self):
        self._creazione_fasce_orarie("Fascia Oraria di Prova da Modificare", "8:00", "10:00")
        self._creazione_fasce_orarie("Fascia Oraria di Prova da Eliminare", "8:00", "10:00")
        self._modifica_fasce_orarie("Fascia Oraria di Prova")
        self._elimina_fasce_orarie()
        self._verifica_fasce_orarie()

    def _creazione_fasce_orarie(self, nome: str, inizio: str, fine: str):
        self.navigateTo("Fasce orarie")
        self.wait_loader()
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(None, 'Ora inizio').setValue(inizio)
        self.input(None, 'Ora fine').setValue(fine)
        self.input(modal, 'Nome').setValue(nome)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def _search_fascia_oraria(self, nome: str):
        self.navigateTo("Fasce orarie")
        self.wait_loader()
        search_input = self.find(By.XPATH, '//th[@id="th_Nome"]/input')
        search_input.clear()
        self.send_keys_and_wait(search_input, nome, wait_modal=False)

    def _modifica_fasce_orarie(self, modifica: str):
        self._search_fascia_oraria('Fascia Oraria di Prova da Modificare')
        self.click_first_result()
        self.input(None, 'Nome').setValue(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.navigateTo("Fasce orarie")
        self.wait_loader()
        self.clear_filters()

    def _elimina_fasce_orarie(self):
        self._search_fascia_oraria('Fascia Oraria di Prova da Eliminare')
        self.click_first_result()
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask "]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.clear_filters()

    def _verifica_fasce_orarie(self):
        self._search_fascia_oraria("Fascia Oraria di Prova")
        modificato = self.find(By.XPATH, '//tbody//tr[1]//td[2]').text
        self.assertEqual("Fascia Oraria di Prova", modificato)
        self.clear_filters()

        self._search_fascia_oraria("Fascia Oraria di Prova da Eliminare")
        eliminato = self.find(By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)
        self.clear_filters()