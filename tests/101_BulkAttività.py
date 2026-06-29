from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os

class Attivita(Test):
    def setUp(self):
        super().setUp()

    def test_bulk_attivita(self):      
        self.cambio_stato()
        self.duplica()
        self.elimina()
        self.esporta()
        self.firma()
        self.fattura()
        self.invia_mail()
        self.stampa_riepilogo()
        
    def cambio_stato(self):
        self.navigate_to_and_wait('Attività')

        self.search_by_th("th_Numero", "1")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="change_status"]'
        )

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_stato-container"]',
            option_text='Programmato'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        stato = self.get_table_text(1, 7)
        self.assertEqual(stato, 'Programmato')
        self.wait_for_element_and_click('//tbody//tr//td')
        self.clear_filters()

    def duplica(self):
        self.navigate_to_and_wait('Attività')
        self.search_by_th("th_Numero", "1")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="copy_bulk"]'
        )

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_stato-container"]',
            option_text='Da programmare'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')
        self.clear_filters()

        search_input = self.wait_for_element_and_click('//th[@id="th_Numero"]/input')
        self.send_keys_and_wait(search_input, '2', wait_modal=False)
        numero = self.get_table_text(1, 2)
        self.assertEqual(numero, '2')
        self.clear_filters()

    def elimina(self):
        self.navigate_to_and_wait('Attività')
        self.search_by_th("th_Numero", "2")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="delete_bulk"]'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        scritta = self.get_empty_table_message()
        self.assertEqual(scritta, 'Nessun dato presente nella tabella')
        self.clear_filters()

    def esporta(self):
        self.navigate_to_and_wait('Attività')
        self.search_by_th("th_Numero", "1")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="export_bulk"]'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        download_dir = os.path.expanduser('~/Scaricati')
        files_before = os.listdir(download_dir) if os.path.exists(download_dir) else []
        
        import time
        time.sleep(2)
        
        files_after = os.listdir(download_dir) if os.path.exists(download_dir) else []
        new_files = set(files_after) - set(files_before)
        
        csv_files = [f for f in new_files if f.endswith('.zip')]
        self.assertTrue(len(csv_files) > 0, "Nessun file CSV scaricato")

        self.navigate_to_and_wait("Attività")
        self.clear_filters()

    def firma(self):
        self.navigate_to_and_wait('Attività')
        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="firma-intervento"]'
        )

        self.wait_for_element_and_click('//button[@id="firma"]')
        firma_input = self.wait_for_element_and_click('//input[@id="firma_nome"]')
        self.send_keys_and_wait(firma_input, 'firma')
        self.wait_driver.until(EC.invisibility_of_element_located((By.XPATH, '//div[contains(@class, "modal") and contains(@class, "show")]')))
        
        
    def fattura(self):
        self.navigate_to_and_wait('Attività')
        self.search_by_th("th_Numero", "1")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="create_invoice"]'
        )

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-raggruppamento-container"]',
            option_text='Cliente'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        stato = self.get_table_text(1, 7)
        self.assertEqual(stato, 'Fatturato')

        self.expandSidebar('Vendite')
        self.navigate_to_and_wait('Fatture di vendita')

        self.wait_for_element_and_click('(//tbody//tr//td[2])[3]')
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask "]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.navigate_to_and_wait('Attività')
        self.clear_filters()

    def invia_mail(self):
        self.navigate_to_and_wait('Attività')
        self.search_by_th("th_Numero", "1")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="send_mail"]'
        )

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_template-container"]',
            option_text='Rapportino intervento'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')
        self.clear_filters()

    def stampa_riepilogo(self):
        self.navigate_to_and_wait('Attività')
        self.search_by_th("th_Numero", "1")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="print_summary"]'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.driver.switch_to.window(self.driver.window_handles[1])
        prezzo = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="viewer"]//span)[38]'))).text
        self.assertEqual(prezzo, '2,00 €')