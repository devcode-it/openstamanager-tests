from common.Test import Test
from common.RowManager import RowManager
from selenium.webdriver.common.by import By

class Preventivi(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Vendite")

    def test_creazione_preventivo(self):
        importi = RowManager.list()
        self._creazione_preventivo("Preventivo di Prova","Cliente", "1", importi[0])
        self._duplica_preventivo()
        self._modifica_preventivo("Accettato")
        self._elimina_preventivo()

        self._creazione_contratto()
        self._creazione_ordine_cliente()
        self._creazione_ordine_fornitore()
        self._creazione_attività()
        self._creazione_ddt_uscita()
        self._creazione_fattura()
        self._verifica_preventivi()

    def _creazione_preventivo(self, nome:str, cliente:str, idtipo: str, file_importi: str):
        self.navigate_to_and_wait("Preventivi")

        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        select = self.input(modal, 'Cliente')
        select.setByText(cliente)
        select = self.input(modal, 'Tipo di Attività')
        select.setByIndex(idtipo)
        self.submit_modal(modal)
        self.close_tour()

        row_manager = RowManager(self)
        self.valori = row_manager.compile(file_importi)

    def _duplica_preventivo(self):
        self.navigate_to_and_wait("Preventivi")

        self.click_first_table_row()
        self.wait_for_element_and_click('//div[@id="pulsanti"]//button[@class="btn ask btn-primary"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.driver.execute_script('window.scrollTo(0,0)')
        nome_field = self.find(By.XPATH, '//input[@id="nome"]')
        nome_field.send_keys(" da Eliminare")

        self.wait_for_element_and_click('//button[@class="btn btn-success"]')

    def _modifica_preventivo(self, stato:str):
        self.navigate_to_and_wait("Preventivi")

        self.search_by_th("th_Nome", '=Preventivo di Prova')

        self.click_first_table_row()

        select = self.input(None, 'Stato')
        select.setByText(stato)
        self.click_save_button()

        sconto = self.get_row_cell_text('righe', 2, 2, 2)
        totale_imponibile = self.get_row_cell_text('righe', 2, 3, 2)
        iva = self.get_row_cell_text('righe', 2, 4, 2)
        totale = self.get_row_cell_text('righe', 2, 5, 2)

        self.assertEqual(sconto, (self.valori["Sconto/maggiorazione"] + ' €'))
        self.assertEqual(totale_imponibile, (self.valori["Totale imponibile"] + ' €'))
        self.assertEqual(iva, (self.valori["IVA"] + ' €'))
        self.assertEqual(totale, (self.valori["Totale documento"] + ' €'))

        self.navigate_to_and_wait("Preventivi")
        self.clear_filters()

    def _elimina_preventivo(self):
        self.navigate_to_and_wait("Preventivi")

        self.search_by_th_and_click_first("th_Nome", '=Preventivo di Prova da Eliminare')
        self.delete_current_and_clear()

        self.navigate_to_and_wait("Preventivi")

    def _creazione_contratto(self):
        self.navigate_to_and_wait("Preventivi")

        self.search_by_th_and_click_first("th_Nome", 'Preventivo di Prova')
        totalepreventivo = self.get_row_cell_text('righe', 2, 3, 2)

        self.wait_for_element_and_click('//div[@id="pulsanti"]//button[@class="btn btn-info dropdown-toggle "]')
        self.wait_for_element_and_click('//a[@class="btn dropdown-item bound clickable"][@data-title="Crea contratto"]')
        self.wait_for_element_and_click('//span[@id="select2-id_segment-container"]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--selectable select2-results__option--highlighted"]')
        self.wait_for_element_and_click('//button[@id="submit_btn"]')

        totalecontratto = self.get_row_cell_text('righe', 2, 3, 2)
        self.assertEqual(totalecontratto, totalepreventivo)

        self.delete_current_and_clear()

        self.navigate_to_and_wait("Preventivi")
        self.clear_filters()

    def _creazione_ordine_cliente(self):
        self.navigate_to_and_wait("Preventivi")

        self.search_by_th_and_click_first("th_Nome", 'Preventivo di Prova')
        totalepreventivo = self.get_row_cell_text('righe', 2, 3, 2)

        self.wait_for_element_and_click('//button[@class="btn btn-info dropdown-toggle "]')
        self.wait_for_element_and_click('//a[@class="btn dropdown-item bound clickable"][@data-title="Crea ordine cliente"]')
        self.wait_for_element_and_click('//span[@id="select2-id_segment-container"]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--selectable select2-results__option--highlighted"]')
        self.wait_for_element_and_click('//button[@id="submit_btn"]')

        totaleordinecliente = self.get_row_cell_text('righe', 2, 3, 2)
        self.assertEqual(totaleordinecliente, totalepreventivo)

        self.delete_current_and_clear()

        self.navigate_to_and_wait("Preventivi")
        self.clear_filters()

    def _creazione_ordine_fornitore(self):
        self.navigate_to_and_wait("Preventivi")

        self.search_by_th_and_click_first("th_Nome", 'Preventivo di Prova')

        self.wait_for_element_and_click('//button[@class="btn btn-info dropdown-toggle "]')
        self.wait_for_element_and_click('//a[@class="btn dropdown-item bound clickable"][@data-title="Crea ordine fornitore"]')
        self.wait_for_element_and_click('(//span [@id="select2-id_anagrafica-container"])[2]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--selectable select2-results__option--highlighted"]')
        self.wait_for_element_and_click('//span[@id="select2-id_segment-container"]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--selectable select2-results__option--highlighted"]')
        self.wait_for_element_and_click('//button[@id="submit_btn"]')

        totaleordinefornitore = self.get_row_cell_text('righe', 2, 3, 2)
        self.assertEqual(totaleordinefornitore, '7,20 €')

        self.delete_current_and_clear()

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Preventivi")
        self.clear_filters()

    def _creazione_attività(self):
        self.navigate_to_and_wait("Preventivi")

        self.search_by_th_and_click_first("th_Nome", 'Preventivo di Prova')
        totalepreventivo = self.get_row_cell_text('righe', 2, 3, 2)

        self.wait_for_element_and_click('//button[@class="btn btn-info dropdown-toggle "]')
        self.wait_for_element_and_click('//a[@class="btn dropdown-item bound clickable"][@data-title="Crea attività"]')
        self.wait_for_element_and_click('(//span[@id="select2-id_tipo_intervento-container"])[2]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--selectable select2-results__option--highlighted"]')
        self.wait_for_element_and_click('(//span[@id="select2-id_stato-container"])[2]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--selectable select2-results__option--highlighted"]')
        self.wait_for_element_and_click('//span[@id="select2-id_segment-container"]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--selectable select2-results__option--highlighted"]')
        self.wait_for_element_and_click('//button[@id="submit_btn"]')

        totaleattività = self.get_row_cell_text('righe', 2, 3, 2)
        self.assertEqual(totaleattività, totalepreventivo)

        self.delete_current_and_clear()

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Preventivi")
        self.clear_filters()

    def _creazione_ddt_uscita(self):
        self.navigate_to_and_wait("Preventivi")

        self.search_by_th_and_click_first("th_Nome", 'Preventivo di Prova')
        totalepreventivo = self.get_row_cell_text('righe', 2, 3, 2)

        self.wait_for_element_and_click('//button[@class="btn btn-info dropdown-toggle "]')
        self.wait_for_element_and_click('//a[@class="btn dropdown-item bound clickable"][@data-title="Crea DDT in uscita"]')
        self.wait_for_element_and_click('//span[@id="select2-id_causale_trasporto-container"]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--selectable select2-results__option--highlighted"]')
        self.wait_for_element_and_click('//span[@id="select2-id_segment-container"]')
        self.wait_for_element_and_click('//li[@class="select2-results__option select2-results__option--selectable select2-results__option--highlighted"]')
        self.wait_for_element_and_click('//button[@id="submit_btn"]')

        totaleddtuscita = self.get_row_cell_text('righe', 2, 3, 2)
        self.assertEqual(totaleddtuscita, totalepreventivo)

        self.delete_current_and_clear()

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Preventivi")
        self.clear_filters()

    def _creazione_fattura(self):
        self.navigate_to_and_wait("Preventivi")

        self.search_by_th_and_click_first("th_Nome", 'Preventivo di Prova')
        totalepreventivo = self.get_row_cell_text('righe', 2, 3, 2)

        self.wait_for_element_and_click('//button[@class="btn btn-info dropdown-toggle "]')
        self.wait_for_element_and_click('//a[@class="btn dropdown-item bound clickable"][@data-title="Crea fattura"]')
        self.wait_for_element_and_click('//button[@id="submit_btn"]')

        totalefattura = self.get_row_cell_text('righe', 2, 3, 2)
        self.assertEqual(totalefattura, totalepreventivo)

        self.delete_current_and_clear()

        self.navigate_to_and_wait("Preventivi")
        self.clear_filters()

    def _verifica_preventivi(self):
        self.navigate_to_and_wait("Preventivi")

        self.search_by_th("th_Nome", "Preventivo di Prova")

        modificato = self.get_table_text(1, 3)
        self.assertEqual("Preventivo di Prova", modificato)
        self.clear_filters()

        self.search_by_th("th_Nome", "Preventivo di Prova da Eliminare")

        eliminato = self.get_empty_table_message()
        self.assertEqual("Nessun dato presente nella tabella", eliminato)
        self.clear_filters()

        self.verify_deleted_by_th("th_Nome", "Preventivo di Prova da Eliminare")
        self.clear_filters()