from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import time

class Impianti(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Impianti")
        self.wait_loader()

    def test_bulk_impianti(self):
        self.add_impianto('1', 'Impianto di Prova', 'Cliente')
        self.aggiorna_cliente()
        self.esporta_selezionati()
        self.duplica()
        self.elimina_selezionati()

    def add_impianto(self, matricola: str, nome: str, cliente: str):
        self.navigate_to_and_wait("Impianti")
        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Matricola').setValue(matricola)
        self.input(modal, 'Nome').setValue(nome)
        self.wait_for_dropdown_and_select('//span[@id="select2-id_anagrafica_impianto-container"]', option_text=cliente)

        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def aggiorna_cliente(self):
        self.navigate_to_and_wait("Impianti")

        self.search_by_th("th_Matricola", "1")
        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="change_customer"]'
        )
        self.wait_for_dropdown_and_select('//span[@id="select2-id_anagrafica-container"]', option_text='Cliente')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.wait_and_click_table_row()
        cliente = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-id_anagrafica-container"]'))
        ).text
        self.assertEqual(cliente, "Cliente (Este) - 00000004")

        self.navigate_to_and_wait("Impianti")
        self.clear_filters()

    def elimina_selezionati(self):
        self.navigate_to_and_wait("Impianti")

        self.search_by_th("th_Matricola", "1")
        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//tbody//tr[2]//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="delete_bulk"]'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        risultato = self.get_empty_table_message()
        self.assertEqual(risultato, "Nessun dato presente nella tabella")

        self.clear_filters()

    def esporta_selezionati(self):
        self.navigate_to_and_wait("Impianti")

        self.search_by_th("th_Matricola", "1")
        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="export_csv"]'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        download_dir = os.path.expanduser('~/Scaricati')
        files_before = os.listdir(download_dir) if os.path.exists(download_dir) else []

        time.sleep(2)

        files_after = os.listdir(download_dir) if os.path.exists(download_dir) else []
        new_files = set(files_after) - set(files_before)

        csv_files = [f for f in new_files if f.endswith('.csv')]
        self.assertTrue(len(csv_files) > 0, "Nessun file CSV scaricato")
        self.clear_filters()

    def duplica(self):
        self.navigate_to_and_wait("Impianti")

        self.search_by_th("th_Matricola", "1")
        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="copy_bulk"]'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.clear_filters()