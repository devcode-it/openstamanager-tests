from common.Test import Test
from common.RowManager import RowManager
from selenium.webdriver.common.by import By

class DdtEntrata(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Magazzino")

    def test_creazione_ddt_entrata(self):
        importi = RowManager.list()
        self._creazione_ddt_entrata("Fornitore", "1", importi[0])
        self._duplica_ddt_entrata()
        self._modifica_ddt("Evaso")
        self._elimina_ddt()
        self._verifica_ddt()

    def _creazione_ddt_entrata(self, fornitore: str, causale: str, file_importi: str):
        self.navigate_to_and_wait("Ddt in entrata")
        self.click_add_button()
        modal = self.wait_modal()

        select = self.input(modal, 'Mittente')
        select.setByText(fornitore)
        select = self.input(modal, 'Causale trasporto')
        select.setByIndex(causale)
        self.wait_for_element_and_click('//button[@type="submit"]')
        self.close_tour()

        row_manager = RowManager(self)
        self.valori = row_manager.compile(file_importi)

    def _duplica_ddt_entrata(self):
        self.navigate_to_and_wait("Ddt in entrata")
        self.click_first_result()

        self.driver.execute_script('window.scrollTo(0,0)')
        self.wait_for_element_and_click('//button[@class="btn btn-primary ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

    def _modifica_ddt(self, modifica):
        self.navigate_to_and_wait("Ddt in entrata")
        self.search_by_th_and_click_first("th_Numero", '1')

        self.select_state('Evaso')

        sconto = self.get_row_cell_text('righe', 2, 2, 2)
        totale_imponibile = self.get_row_cell_text('righe', 2, 3, 2)
        iva = self.get_row_cell_text('righe', 2, 4, 2)
        totale = self.get_row_cell_text('righe', 2, 5, 2)

        self.assertEqual(sconto, (self.valori["Sconto/maggiorazione"] + ' €'))
        self.assertEqual(totale_imponibile, (self.valori["Totale imponibile"] + ' €'))
        self.assertEqual(iva, (self.valori["IVA"] + ' €'))
        self.assertEqual(totale, (self.valori["Totale documento"] + ' €'))

        self.click_save_button()
        self.navigate_to_and_wait("Ddt in entrata")
        self.clear_filters()

    def _elimina_ddt(self):
        self.navigate_to_and_wait("Ddt in entrata")
        self.click_first_result()

        self.delete_current_and_clear()

    def _verifica_ddt(self):
        self.navigate_to_and_wait("Ddt in entrata")
        self.search_by_th("th_Numero", "1")
        modificato = self.get_table_text(1, 11)
        self.assertEqual("Evaso", modificato)
        self.clear_filters()

        self.verify_deleted_by_th("th_Numero", "2")
