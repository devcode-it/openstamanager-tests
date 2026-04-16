from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.Test import Test


class Liste(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Gestione email")

    def test_creazione_lista(self):
        self._creazione_lista(nome="Lista di Prova da Modificare")
        self._creazione_lista(nome="Lista di Prova da Eliminare")
        self._modifica_lista("Lista di Prova")
        self._elimina_lista()
        self._verifica_lista()

    def _creazione_lista(self, nome=str):
        self.navigateTo("Liste")
        self.wait_loader()
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()
        self.input(modal, 'Nome').setValue(nome)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def _modifica_lista(self, modifica: str):
        self.navigateTo("Liste")
        self.wait_loader()
        search_input = self.find(By.XPATH, '//th[@id="th_Nome"]/input')
        self.send_keys_and_wait(search_input, 'Lista di Prova da Modificare', wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.input(None, 'Nome').setValue(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')
        self.navigateTo("Liste")
        self.wait_loader()
        self.clear_filters()

    def _elimina_lista(self):
        self.navigateTo("Liste")
        self.wait_loader()
        search_input = self.find(By.XPATH, '//th[@id="th_Nome"]/input')
        self.send_keys_and_wait(search_input, 'Lista di Prova da Eliminare', wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.clear_filters()

    def _verifica_lista(self):
        self.navigateTo("Liste")
        self.wait_loader()
        search_input = self.find(By.XPATH, '//th[@id="th_Nome"]/input')
        self.send_keys_and_wait(search_input, "Lista di Prova", wait_modal=False)
        modificato = self.find(By.XPATH, '//tbody//tr[1]//td[2]').text
        self.assertEqual("Lista di Prova", modificato)
        self.clear_filters()
        search_input = self.find(By.XPATH, '//th[@id="th_Nome"]/input')
        self.send_keys_and_wait(search_input, "Lista di Prova da Eliminare", wait_modal=False)
        eliminato = self.find(By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)
        self.clear_filters()