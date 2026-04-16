from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.Test import Test


class TipiAnagrafiche(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Anagrafiche")
        self.wait_loader()

    def test_creazione_tipo_anagrafiche(self):
        self.navigateTo("Tipi di anagrafiche")
        self.wait_loader()

        self._creazione_tipo_anagrafiche("Tipo di anagrafica di Prova da Modificare")
        self._creazione_tipo_anagrafiche("Tipo di anagrafica di Prova da Eliminare")
        self._modifica_tipo_anagrafiche("Tipo di anagrafica di Prova")
        self._elimina_tipo_anagrafiche()
        self._verifica_tipo_anagrafiche()

    def _creazione_tipo_anagrafiche(self, descrizione):
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()
        self.input(modal, 'Descrizione').setValue(descrizione)
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

    def _modifica_tipo_anagrafiche(self, modifica):
        self.navigateTo("Tipi di anagrafiche")
        self.wait_loader()

        search_input = self.find(By.XPATH, '//th[@id="th_Descrizione"]/input')
        self.send_keys_and_wait(search_input, 'Tipo di anagrafica di Prova da Modificare', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.input(None, 'Descrizione').setValue(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.navigateTo("Tipi di anagrafiche")
        self.wait_loader()
        self.clear_filters()

    def _elimina_tipo_anagrafiche(self):
        self.navigateTo("Tipi di anagrafiche")
        self.wait_loader()

        search_input = self.find(By.XPATH, '//th[@id="th_Descrizione"]/input')
        self.send_keys_and_wait(search_input, 'Tipo di anagrafica di Prova da Eliminare', wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.wait_for_element_and_click('//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]')

    def _verifica_tipo_anagrafiche(self):
        self.navigateTo("Tipi di anagrafiche")
        self.wait_loader()

        search_input = self.find(By.XPATH, '//th[@id="th_Descrizione"]/input')
        self.send_keys_and_wait(search_input, "Tipo di anagrafica di Prova", wait_modal=False)
        modificato = self.find(By.XPATH, '//tbody//tr[1]//td[2]').text
        self.assertEqual("Tipo di anagrafica di Prova", modificato)
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

        search_input = self.find(By.XPATH, '//th[@id="th_Descrizione"]/input')
        self.send_keys_and_wait(search_input, "Tipo di anagrafica di Prova da Eliminare", wait_modal=False)
        eliminato = self.find(By.XPATH, '//tbody//tr[1]//td[1]').text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)
