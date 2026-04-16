from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common.Test import Test


class Newsletter(Test):
    def setUp(self):
        super().setUp()

    def test_creazione_newsletter(self):
        self.expandSidebar("Gestione email")
        self._add_newsletter('Newsletter di Prova da Modificare', "Contratto")
        self._add_newsletter('Newsletter di Prova da Eliminare', "Ddt")
        self._modifica_newsletter("Newsletter di Prova")
        self._elimina_newsletter()
        self._verifica_newsletter()

    def _add_newsletter(self, nome: str, modulo: str):
        self.navigateTo("Newsletter")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        select = self.input(modal, 'Template email')
        select.setByText(modulo)
        self.input(modal, 'Nome').setValue(nome)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def _modifica_newsletter(self, modifica: str):
        self.navigateTo("Newsletter")
        self.wait_loader()

        search_input = self.find(By.XPATH, '//th[@id="th_Nome"]/input')
        self.send_keys_and_wait(search_input, 'Newsletter di Prova da Modificare', wait_modal=False)
        self.click_first_result()

        self.input(None, 'Nome').setValue(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.navigateTo("Newsletter")
        self.wait_loader()
        self.clear_filters()

    def _elimina_newsletter(self):
        search_input = self.find(By.XPATH, '//th[@id="th_Nome"]/input')
        self.send_keys_and_wait(search_input, 'Newsletter di Prova da Eliminare', wait_modal=False)
        self.click_first_result()

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.clear_filters()

    def _verifica_newsletter(self):
        search_input = self.find(By.XPATH, '//th[@id="th_Nome"]/input')
        self.send_keys_and_wait(search_input, "Newsletter di Prova", wait_modal=False)
        modificato = self.find(By.XPATH, '//tbody//tr[1]//td[2]').text
        self.assertEqual("Newsletter di Prova", modificato)
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

        search_input = self.find(By.XPATH, '//th[@id="th_Nome"]/input')
        self.send_keys_and_wait(search_input, "Newsletter di Prova da Eliminare", wait_modal=False)
        eliminato = self.find(By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)