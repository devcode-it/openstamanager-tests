from common.Test import Test
from common.RowManager import RowManager
from selenium.webdriver.common.by import By

class DdtUscita(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Magazzino")

    def test_creazione_ddt_uscita(self):
        importi = RowManager.list()
        self._creazione_ddt_uscita("Cliente", "2", importi[0])
        self._duplica_ddt_uscita()
        self._modifica_ddt("Evaso")
        self._elimina_ddt()
        self._verifica_ddt()
        self._ddt_del_cliente()


    def _creazione_ddt_uscita(self, cliente: str, causale: str, file_importi: str):
        self.navigate_to_and_wait("Ddt in uscita")
        self.wait_for_element_and_click( '//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        select = self.input(modal, 'Destinatario')
        select.setByText(cliente)
        select = self.input(modal, 'Causale trasporto')
        select.setByIndex(causale)
        self.wait_for_element_and_click('//button[@type="submit"]')
        self.close_tour()

        row_manager = RowManager(self)
        self.valori = row_manager.compile(file_importi)

    def _duplica_ddt_uscita(self):
        self.navigate_to_and_wait("Ddt in uscita")
        self.click_first_result()

        self.wait_for_element_and_click( '//button[@class="btn btn-primary ask"]')
        self.wait_for_element_and_click( '//button[@class="swal2-confirm btn btn-lg btn-success"]')

    def _modifica_ddt(self, modifica):
        self.navigate_to_and_wait("Ddt in uscita")
        self.click_first_result()

        self.driver.execute_script('window.scrollTo(0,0)')
        self.select_state('Evaso')
        self.wait_for_element_and_click( '//div[@id="tab_0"]//button[@id="save"]')

        sconto = self.get_row_cell_text('righe', 2, 2, 2)
        totale_imponibile = self.get_row_cell_text('righe', 2, 3, 2)
        iva = self.get_row_cell_text('righe', 2, 4, 2)
        totale = self.get_row_cell_text('righe', 2, 5, 2)

        self.assertEqual(sconto, (self.valori["Sconto/maggiorazione"] + ' €'))
        self.assertEqual(totale_imponibile, (self.valori["Totale imponibile"] + ' €'))
        self.assertEqual(iva, (self.valori["IVA"] + ' €'))
        self.assertEqual(totale, (self.valori["Totale documento"] + ' €'))

        self.navigate_to_and_wait("Ddt in uscita")
        self.clear_filters()

    def _elimina_ddt(self):
        self.navigate_to_and_wait("Ddt in uscita")
        self.search_by_th_and_click_first("th_Numero", '!=01')

        self.delete_current_and_clear()

    def _verifica_ddt(self):
        self.navigate_to_and_wait("Ddt in uscita")
        self.search_by_th("th_Numero", "01")

        modificato = self.get_table_text(1, 11)
        self.assertEqual("Evaso", modificato)
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

        self.verify_deleted_by_th("th_Numero", "!=01")
        self.clear_filters()

    def _ddt_del_cliente(self):
        self.navigate_to_and_wait("Anagrafiche")
        self.search_entity_and_click_first("Cliente")

        self.wait_for_element_and_click( '//a[@id="link-tab_17"]')
        self.wait_for_element_and_click( '//tbody//tr[5]//td[2]')
