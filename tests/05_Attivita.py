from common.Test import Test
from common.RowManager import RowManager
from selenium.webdriver.common.by import By

class Attivita(Test):
    def setUp(self):
        super().setUp()

    def test_attivita(self):
        importi = RowManager.list()
        self._attivita('Cliente', '1', '2', importi[0])
        self._duplica_attività()
        self._modifica_attività('Completato')
        self._elimina_attività()
        self._controllo_righe()
        self._verifica_attività()

    def _attivita(self, cliente: str, tipo: str, stato: str, file_importi: str):
        self.navigateTo('Attività')
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()
        self.input(modal, 'Cliente').setByText(cliente)
        self.input(modal, 'Tipo').setByIndex(tipo)
        description_field = self.find(By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]')
        description_field.click()
        self.send_keys_and_wait(description_field, 'Test', wait_modal=False)
        self.wait_for_element_and_click('//div[@class="col-md-12 text-right"]//button[@type="button"]')

        row_manager = RowManager(self)
        self.valori = row_manager.compile(file_importi)

    def _duplica_attività(self):
        self.navigateTo('Attività')
        self.click_first_result()
        self.wait_for_element_and_click('//div[@id="pulsanti"]//button[1]')
        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_stato-container"]',
            option_xpath='//span[@class="select2-results"]//li[2]'
        )
        self.wait_for_element_and_click('//div[@class="modal-content"]//button[@type="submit"]')

    def _modifica_attività(self, modifica: str):
        self.navigateTo('Attività')
        search_input = self.find(By.XPATH, '//th[@id="th_Numero"]/input')
        self.send_keys_and_wait(search_input, '1', wait_modal=False)
        self.click_first_result()

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-idstatointervento-container"]',
            option_text=modifica
        )

        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')
        self.navigateTo('Attività')
        self.clear_filters()

    def _elimina_attività(self):
        self.navigateTo('Attività')
        search_input = self.find(By.XPATH, '//th[@id="th_Numero"]/input')
        self.send_keys_and_wait(search_input, '2', wait_modal=False)
        self.click_first_result()
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.navigateTo('Attività')
        self.clear_filters()

    def _controllo_righe(self):
        self.navigateTo('Attività')
        search_input = self.find(By.XPATH, '//th[@id="th_Numero"]/input')
        self.send_keys_and_wait(search_input, '1', wait_modal=False)
        self.click_first_result()

        imponibile = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[1]//td[2]').text
        sconto = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[2]//td[2]').text
        totale = self.find(By.XPATH, '//div[@id="righe"]//tbody[2]//tr[3]//td[2]').text

        self.assertEqual(imponibile, (self.valori['Imponibile'] + ' €'))
        self.assertEqual(sconto, (self.valori['Sconto/maggiorazione'] + ' €'))
        self.assertEqual(totale, (self.valori['Totale imponibile'] + ' €'))

        imponibilefinale = self.find(By.XPATH, '//div[@id="costi"]//tbody[2]//tr[1]//td[2]').text
        scontofinale = self.find(By.XPATH, '//div[@id="costi"]//tbody[2]//tr[2]//td[2]').text
        totaleimpfinale = self.find(By.XPATH, '//div[@id="costi"]//tbody[2]//tr[3]//td[2]').text
        IVA = self.find(By.XPATH, '//div[@id="costi"]//tbody[2]//tr[4]//td[2]').text
        totalefinale = self.find(By.XPATH, '//div[@id="costi"]//tbody[2]//tr[5]//td[2]').text

        self.assertEqual(imponibilefinale, imponibile)
        self.assertEqual(scontofinale, sconto)
        self.assertEqual(totaleimpfinale, totale)
        self.assertEqual(IVA, (self.valori['IVA'] + ' €'))
        self.assertEqual(totalefinale, (self.valori['Totale documento'] + ' €'))

        self.navigateTo('Attività')
        self.clear_filters()

    def _verifica_attività(self):
        self.navigateTo('Attività')
        search_input = self.find(By.XPATH, '//th[@id="th_Numero"]/input')
        self.send_keys_and_wait(search_input, '1', wait_modal=False)
        modificato = self.find(By.XPATH, '//tbody//tr[1]//td[7]').text
        self.assertEqual('Completato', modificato)
        self.clear_filters()

        search_input = self.find(By.XPATH, '//th[@id="th_Numero"]/input')
        self.send_keys_and_wait(search_input, '2', wait_modal=False)
        eliminato = self.find(By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual('Nessun dato presente nella tabella', eliminato)
        self.clear_filters()