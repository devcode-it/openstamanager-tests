from common.Test import Test
from common.RowManager import RowManager
from selenium.webdriver.common.by import By

class OrdiniFornitore(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Acquisti")

    def test_creazione_ordine_fornitore(self):
        importi = RowManager.list()
        self._creazione_ordine_fornitore("Fornitore", importi[0])
        self._creazione_ordine_fornitore("Fornitore", importi[0])
        self._modifica_ordine_fornitore("Modifica di Prova")
        self._elimina_ordine_fornitore()
        self._verifica_ordine_fornitore()


    def _creazione_ordine_fornitore(self, fornitore: str, file_importi: str):
        self.navigate_to_and_wait("Ordini fornitore")

        self.click_add_button()
        modal = self.wait_modal()

        select = self.input(modal, 'Fornitore')
        select.setByText(fornitore)
        self.submit_modal(modal)
        self.close_tour()

        row_manager = RowManager(self)
        self.valori = row_manager.compile(file_importi)

    def _modifica_ordine_fornitore(self, modifica):
        self.navigate_to_and_wait("Ordini fornitore")

        self.send_keys_and_wait(self.find(By.XPATH, '//th[@id="th_Numero"]/input'), '1', wait_modal=False)

        self.click_first_table_row()
        self.driver.execute_script('window.scrollTo(0,0)')

        self.wait_for_dropdown_and_select('//span[@aria-labelledby="select2-id_stato-container"]', option_text='Accettato')
        self.click_save_button()

        sconto = self.get_row_cell_text('righe', 2, 2, 2)
        totale_imponibile = self.get_row_cell_text('righe', 2, 3, 2)
        iva = self.get_row_cell_text('righe', 2, 4, 2)
        totale = self.get_row_cell_text('righe', 2, 5, 2)

        self.assertEqual(sconto, (self.valori["Sconto/maggiorazione"] + ' €'))
        self.assertEqual(totale_imponibile, (self.valori["Totale imponibile"] + ' €'))
        self.assertEqual(iva, (self.valori["IVA"] + ' €'))
        self.assertEqual(totale, (self.valori["Totale documento"] + ' €'))

        self.navigate_to_and_wait("Ordini fornitore")
        self.wait_for_element_and_click('//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]')

    def _elimina_ordine_fornitore(self):
        self.navigate_to_and_wait("Ordini fornitore")

        self.send_keys_and_wait(self.find(By.XPATH, '//th[@id="th_Numero"]/input'), '2', wait_modal=False)

        self.click_first_table_row()
        self.delete_current_and_clear()

    def _verifica_ordine_fornitore(self):
        self.navigate_to_and_wait("Ordini fornitore")

        self.send_keys_and_wait(self.find(By.XPATH, '//th[@id="th_icon_title_Stato"]/input'), "Accettato", wait_modal=False)

        modificato = self.get_table_text(1, 6)
        self.assertEqual("Accettato", modificato)
        self.clear_filters()

        self.send_keys_and_wait(self.find(By.XPATH, '//th[@id="th_Numero"]/input'), "2", wait_modal=False)

        eliminato = self.get_empty_table_message()
        self.assertEqual("Nessun dato presente nella tabella", eliminato)
        self.wait_for_element_and_click('//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times"]')
