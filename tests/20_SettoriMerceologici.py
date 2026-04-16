from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common.Test import Test


class SettoriMerceologici(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Anagrafiche")
        self.wait_loader()

    def test_creazione_settori_merceologici(self):
        self._creazione_settori_merceologici("Settore Merceologico di Prova da Modificare")
        self._modifica_settori_merceologici("Settore Merceologico di Prova")
        self._creazione_settori_merceologici("Settore Merceologico di Prova da Eliminare")
        self._elimina_settore_merceologico()
        self._verifica_settore_merceologico()

    def _creazione_settori_merceologici(self, descrizione):
        self.navigateTo("Settori merceologici")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'Descrizione').setValue(descrizione)
        self.wait_for_element_and_click('//button[@class="btn btn-primary"][@type="submit"]')

    def _modifica_settori_merceologici(self, modifica):
        self.navigateTo("Settori merceologici")
        self.wait_loader()

        search_input = self.find(By.XPATH, '//th[@id="th_descrizione"]/input')
        self.send_keys_and_wait(search_input, 'Settore Merceologico di Prova da Modificare', wait_modal=False)

        self.click_first_result()

        self.driver.execute_script('window.scrollTo(0,0)')
        self.input(None, 'Descrizione').setValue(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.navigateTo("Settori merceologici")
        self.wait_loader()
        self.clear_filters()

    def _elimina_settore_merceologico(self):
        self.navigateTo("Settori merceologici")
        self.wait_loader()
        search_input = self.find(By.XPATH, '//th[@id="th_descrizione"]/input')
        self.send_keys_and_wait(search_input, 'Settore Merceologico di Prova da Eliminare', wait_modal=False)
        elemento = self.find(By.XPATH, '//tbody//tr//td[2]')
        elemento.click()

        self.driver.execute_script('window.scrollTo(0,0)')
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.clear_filters()

    def _verifica_settore_merceologico(self):
        search_input = self.find(By.XPATH, '//th[@id="th_descrizione"]/input')
        self.send_keys_and_wait(search_input, "Settore Merceologico di Prova", wait_modal=False)
        modificato = self.find(By.XPATH, '//tbody//tr[1]//td[3]').text
        self.assertEqual("Settore Merceologico di Prova", modificato)
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

        search_input = self.wait_for_element_and_click('//th[@id="th_descrizione"]/input')
        self.send_keys_and_wait(search_input, "Settore Merceologico di Prova da Eliminare", wait_modal=False)
        eliminato = self.find(By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)