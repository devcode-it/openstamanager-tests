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
        self.navigateToAndWait('Attività')

        modal = self.open_and_fill_modal({'Cliente': f'text:{cliente}'})
        self.input(modal, 'Tipo').setByIndex(tipo)
        description_field = self.find(By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]')
        description_field.click()
        self.send_keys_and_wait(description_field, 'Test', wait_modal=False)
        self.wait_for_element_and_click('//div[@class="col-md-12 text-right"]//button[@type="button"]')

        row_manager = RowManager(self)
        self.valori = row_manager.compile(file_importi)

    def _duplica_attività(self):
        self.navigateToAndWait('Attività')
        self.click_first_result()

        self.wait_for_element_and_click('//button[@onclick="duplicaIntervento()"]')
        self.wait_for_dropdown_and_select(
            '(//span[@id="select2-id_stato-container"])[2]',
            option_xpath='//span[@class="select2-results"]//li[2]'
        )
        self.wait_for_element_and_click('//div[@class="modal-content"]//button[@type="submit"]')

    def _modifica_attività(self, modifica: str):
        self.navigateToAndWait('Attività')
        self.search_by_th_and_click_first("th_Numero", '1')

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_stato-container"]',
            option_text=modifica
        )

        self.click_save_button()
        self.navigateToAndWait('Attività')
        self.clear_filters()

    def _elimina_attività(self):
        self.navigateToAndWait('Attività')
        self.search_by_th_and_click_first("th_Numero", '2')
        self.delete_current_and_clear()

        self.navigateToAndWait('Attività')
        self.clear_filters()

    def _controllo_righe(self):
        self.navigateToAndWait('Attività')
        self.search_by_th_and_click_first("th_Numero", '1')

        imponibile = self.get_row_cell_text('righe', 2, 1, 2)
        sconto = self.get_row_cell_text('righe', 2, 2, 2)
        totale = self.get_row_cell_text('righe', 2, 3, 2)

        self.assertEqual(imponibile, (self.valori['Imponibile'] + ' €'))
        self.assertEqual(sconto, (self.valori['Sconto/maggiorazione'] + ' €'))
        self.assertEqual(totale, (self.valori['Totale imponibile'] + ' €'))

        imponibilefinale = self.get_row_cell_text('costi', 2, 1, 2)
        scontofinale = self.get_row_cell_text('costi', 2, 2, 2)
        totaleimpfinale = self.get_row_cell_text('costi', 2, 3, 2)
        iva = self.get_row_cell_text('costi', 2, 4, 2)
        totalefinale = self.get_row_cell_text('costi', 2, 5, 2)

        self.assertEqual(imponibilefinale, imponibile)
        self.assertEqual(scontofinale, sconto)
        self.assertEqual(totaleimpfinale, totale)
        #self.assertEqual(iva, (self.valori['IVA'] + ' €'))
        #self.assertEqual(totalefinale, (self.valori['Totale documento'] + ' €'))

        self.navigateToAndWait('Attività')
        self.clear_filters()

    def _verifica_attività(self):
        self.navigateToAndWait('Attività')
        self.search_by_th("th_Numero", '1')
        modificato = self.get_table_text(1, 7)
        self.assertEqual('Completato', modificato)
        self.clear_filters()

        self.verify_deleted_by_th("th_Numero", '2')