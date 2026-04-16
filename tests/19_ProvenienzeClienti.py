from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common.Test import Test


class Provenienze_clienti(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Anagrafiche")
        self.wait_loader()

    def test_creazione_provenienze_clienti(self):
        self._creazione_provenienze_clienti("Provenienza Clienti di Prova da Modificare", "#9d2929")
        self._creazione_provenienze_clienti("Provenienza Clienti di Prova da Eliminare", "#3737db")
        self._modifica_provenienze_clienti("Provenienza Clienti di Prova")
        self._elimina_provenienze_clienti()
        self._verifica_provenienze_clienti()

    def _creazione_provenienze_clienti(self, descrizione, colore):
        self.navigateTo("Provenienze clienti")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'Colore').setValue(colore)
        self.input(modal, 'Descrizione').setValue(descrizione)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def _modifica_provenienze_clienti(self, modifica):
        self.navigateTo("Provenienze clienti")
        self.wait_loader()

        search_input = self.wait_for_element_and_click('//th[@id="th_descrizione"]/input')
        self.send_keys_and_wait(search_input, 'Provenienza Clienti di Prova da Modificare', wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.driver.execute_script('window.scrollTo(0,0)')
        self.input(None, 'Descrizione').setValue(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.navigateTo("Provenienze clienti")
        self.wait_loader()
        self.clear_filters()

    def _elimina_provenienze_clienti(self):
        search_input = self.wait_for_element_and_click('//th[@id="th_descrizione"]/input')
        self.send_keys_and_wait(search_input, 'Provenienza Clienti di Prova da Eliminare', wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.driver.execute_script('window.scrollTo(0,0)')
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.clear_filters()

    def _verifica_provenienze_clienti(self):
        search_input = self.wait_for_element_and_click('//th[@id="th_descrizione"]/input')
        self.send_keys_and_wait(search_input, "Provenienza Clienti di Prova", wait_modal=False)
        modificato = self.find(By.XPATH, '//tbody//tr[1]//td[3]').text
        self.assertEqual("Provenienza Clienti di Prova", modificato)
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

        search_input = self.wait_for_element_and_click('//th[@id="th_descrizione"]/input')
        self.send_keys_and_wait(search_input, "Provenienza Clienti di Prova da Eliminare", wait_modal=False)
        eliminato = self.find(By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)