from selenium.webdriver.common.by import By
from common.Test import Test
from selenium.webdriver.support import expected_conditions as EC

class Zone(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Anagrafiche")
        self.wait_loader()

    def test_creazione_zone(self):
        self._creazione_zone(nome="0001", descrizione="Zona di Prova da Modificare")
        self._creazione_zone(nome="0002", descrizione="Zona di Prova da Eliminare")
        self._modifica_zone("Zona di Prova")
        self._elimina_zone()
        self._verifica_zone()

    def _creazione_zone(self, nome, descrizione):
        self.navigateTo("Zone")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        self.input(modal, 'Descrizione').setValue(descrizione)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def _modifica_zone(self, modifica):
        self.navigateTo("Zone")
        self.wait_loader()

        search_input = self.wait_for_element_and_click('//th[@id="th_Descrizione"]/input')
        self.send_keys_and_wait(search_input, 'Zona di Prova da Modificare', wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.input(None, 'Descrizione').setValue(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.navigateTo("Zone")
        self.wait_loader()
        self.clear_filters()

    def _elimina_zone(self):
        search_input = self.wait_for_element_and_click('//th[@id="th_Descrizione"]/input')
        self.send_keys_and_wait(search_input, 'Zona di Prova da Eliminare', wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.clear_filters()

    def _verifica_zone(self):
        search_input = self.wait_for_element_and_click('//th[@id="th_Descrizione"]/input')
        self.send_keys_and_wait(search_input, "Zona di Prova", wait_modal=False)
        modificato = self.find(By.XPATH, '//tbody//tr[1]//td[3]').text
        self.assertEqual("Zona di Prova", modificato)

        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

        search_input = self.wait_for_element_and_click('//th[@id="th_Descrizione"]/input')
        self.send_keys_and_wait(search_input, "Zona di Prova da Eliminare", wait_modal=False)
        eliminato = self.find(By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)
