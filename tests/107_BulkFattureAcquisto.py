from common.Test import Test
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os

class FattureAcquisto(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Acquisti")

    def test_bulk_fattura_acquisto(self):
        self.aggiorna_banca()
        self.cambia_sezionale()
        self.duplica_selezionati()
        self.elimina_selezionati()
        self.esporta_selezionati()
        self.esporta_stampe_fe()
        #self.esporta_ricevute()
        #self.esporta_xml()
        self.invia_fatture()
        self.registrazione_contabile()

    def aggiorna_banca(self):
        self.navigate_to_and_wait("Fatture di acquisto")
        self.search_by_th("th_Ragione-sociale", "Fornitore estero")
        self.wait_for_search_results()

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="change_bank"]'
        )

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_banca-container"]',
            option_text="Test"
        )

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

    def cambia_sezionale(self):
        self.navigate_to_and_wait("Fatture di acquisto")
        self.click_first_result()

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_stato-container"]',
            option_text='Bozza')
        self.wait_for_element_and_click('//button[@id="save"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.navigate_to_and_wait("Fatture di acquisto")
        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="change_segment"]'
        )

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_segment-container"]',
            option_text='Autofatture'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_segment_-container"]',
            option_text='Autofatture'
        )

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="change_segment"]'
        )
        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_segment-container"]',
            option_text='Acquisti'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')
        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_segment_-container"]',
            option_text='Acquisti'
        )
    
    def duplica_selezionati(self):
        self.navigate_to_and_wait("Fatture di acquisto")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="copy_bulk"]'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')
        self.wait_for_element_and_click('//tbody//tr//td')

    def elimina_selezionati(self):
        self.navigate_to_and_wait("Fatture di acquisto")
        self.search_by_th("th_Numero", "2")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="delete_bulk"]'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        eliminato = self.get_empty_table_message()
        self.assertEqual("Nessun dato presente nella tabella", eliminato)
        self.clear_filters()

    def esporta_selezionati(self):
        self.navigate_to_and_wait("Fatture di acquisto")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="export_csv"]'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        download_dir = os.path.expanduser('~/Scaricati')
        files_before = os.listdir(download_dir) if os.path.exists(download_dir) else []
        
        import time
        time.sleep(2)
        
        files_after = os.listdir(download_dir) if os.path.exists(download_dir) else []
        new_files = set(files_after) - set(files_before)
        
        csv_files = [f for f in new_files if f.endswith('.csv')]
        self.assertTrue(len(csv_files) > 0, "Nessun file CSV scaricato")

    def esporta_stampe_fe(self):
        self.navigate_to_and_wait("Fatture di acquisto")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="export_fe_bulk"]'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        download_dir = os.path.expanduser('~/Scaricati')
        files_before = os.listdir(download_dir) if os.path.exists(download_dir) else []
        
        import time
        time.sleep(2)
        
        files_after = os.listdir(download_dir) if os.path.exists(download_dir) else []
        new_files = set(files_after) - set(files_before)
        
        csv_files = [f for f in new_files if f.endswith('.zip')]
        self.assertTrue(len(csv_files) > 0, "Nessun file ZIP scaricato")

    def esporta_ricevute(self):
        self.navigate_to_and_wait("Fatture di acquisto")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="export_receipts_bulk"]'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        download_dir = os.path.expanduser('~/Scaricati')
        files_before = os.listdir(download_dir) if os.path.exists(download_dir) else []
        
        import time
        time.sleep(2)
        
        files_after = os.listdir(download_dir) if os.path.exists(download_dir) else []
        new_files = set(files_after) - set(files_before)
        
        csv_files = [f for f in new_files if f.endswith('.zip')]
        self.assertTrue(len(csv_files) > 0, "Nessun file ZIP scaricato")

    def esporta_xml(self):
        self.navigate_to_and_wait("Fatture di acquisto")
        self.search_by_th("th_Numero", "01")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="export_xml_bulk"]'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        download_dir = os.path.expanduser('~/Scaricati')
        files_before = os.listdir(download_dir) if os.path.exists(download_dir) else []
        
        import time
        time.sleep(2)
        
        files_after = os.listdir(download_dir) if os.path.exists(download_dir) else []
        new_files = set(files_after) - set(files_before)
        
        csv_files = [f for f in new_files if f.endswith('.zip')]
        self.assertTrue(len(csv_files) > 0, "Nessun file ZIP scaricato")

        self.clear_filters()

    def invia_fatture(self):
        self.navigate_to_and_wait("Fatture di acquisto")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="send-invoices"]'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')
        self.clear_filters()

    def registrazione_contabile(self):
        self.navigate_to_and_wait("Fatture di acquisto")
        self.search_by_th("th_Numero", "01")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="registrazione_contabile"]'
        )
        modal = self.wait_modal()
        totale = self.find(By.XPATH, '//th[@id="totale_dare_add"]').text
        self.assertEqual(totale, "264,80")

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-conto_add_1-container"]',
            option_text='Banca C/C'
        )

        self.wait_for_element_and_click('//button[@type="submit"]')

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")
        self.clear_filters()

