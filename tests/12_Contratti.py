from common.Test import Test
from common.RowManager import RowManager
from selenium.webdriver.common.by import By

class Contratti(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Vendite")

    def test_creazione_contratto(self):
        importi = RowManager.list()
        self._creazione_contratto("Contratto di Prova da Modificare", "Cliente", importi[0])
        self._duplica_contratto()
        self._modifica_contratto("Contratto di Prova")
        self._elimina_contratto()
        self._verifica_contratto()
        self._contratti_del_cliente()


    def _creazione_contratto(self, nome:str, cliente: str, file_importi: str):
        self.navigate_to_and_wait("Contratti")

        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        select = self.input(modal, 'Cliente')
        select.setByText(cliente)
        self.submit_modal(modal)
        self.close_tour()

        row_manager = RowManager(self)
        self.valori = row_manager.compile(file_importi)

    def _duplica_contratto(self):
        self.navigate_to_and_wait("Contratti")

        self.click_first_table_row()
        self.click_duplicate_button()
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        element = self.find(By.XPATH, '//input[@id="nome"]')
        element.clear()
        element.send_keys("Contratto di Prova da Eliminare")
        self.wait_for_element_and_click('//button[@id="save"]')

    def _modifica_contratto(self, modifica=str):
        self.navigate_to_and_wait("Contratti")

        self.send_keys_and_wait(self.find(By.XPATH, '//th[@id="th_Nome"]/input'), '=Contratto di Prova da Modificare', wait_modal=False)

        self.click_first_table_row()

        element = self.find(By.XPATH, '//input[@id="nome"]')
        element.clear()
        element.send_keys(modifica)
        self.click_save_button()

        sconto = self.get_row_cell_text('righe', 2, 2, 2)
        totale_imponibile = self.get_row_cell_text('righe', 2, 3, 2)
        iva = self.get_row_cell_text('righe', 2, 4, 2)
        totale = self.get_row_cell_text('righe', 2, 5, 2)

        self.assertEqual(sconto, (self.valori["Sconto/maggiorazione"] + ' €'))
        self.assertEqual(totale_imponibile, (self.valori["Totale imponibile"] + ' €'))
        self.assertEqual(iva, (self.valori["IVA"] + ' €'))
        self.assertEqual(totale, (self.valori["Totale documento"] + ' €'))

        self.navigate_to_and_wait("Contratti")
        self.clear_filters()

    def _elimina_contratto(self):
        self.navigate_to_and_wait("Contratti")

        self.send_keys_and_wait(self.find(By.XPATH, '//th[@id="th_Nome"]/input'), 'Contratto di Prova da Eliminare', wait_modal=False)

        self.click_first_table_row()
        self.delete_current_and_clear()

    def _verifica_contratto(self):
        self.navigate_to_and_wait("Contratti")

        self.send_keys_and_wait(self.find(By.XPATH, '//th[@id="th_Nome"]/input'), "Contratto di Prova", wait_modal=False)

        modificato = self.get_table_text(1, 3)
        self.assertEqual("Contratto di Prova", modificato)
        self.clear_filters()

        self.send_keys_and_wait(self.find(By.XPATH, '//th[@id="th_Nome"]/input'), "Contratto di Prova da Eliminare", wait_modal=False)

        eliminato = self.get_empty_table_message()
        self.assertEqual("Nessun dato presente nella tabella", eliminato)
        self.clear_filters()

    def _contratti_del_cliente(self):
        self.navigate_to_and_wait("Anagrafiche")

        self.send_keys_and_wait(self.find(By.XPATH, '//th[@id="th_Ragione-sociale"]/input'), "Cliente", wait_modal=False)

        self.click_first_table_row()
        self.wait_for_element_and_click('//a[@id="link-tab_35"]')

        self.find(By.XPATH, '//div[@id="tab_35"]//tbody//tr/td[2]')
