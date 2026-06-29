from common.Test import Test
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os

class FattureVendita(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Vendite")

    def test_bulk_fattura_vendita(self):
        self.aggiorna_banca()
        self.cambia_sezionale()
        self.controlla_fatture_elettroniche()
        self.duplica_selezionati()
        self.elimina_selezionati()
        self.emetti_fatture()
        self.esporta_selezionati()
        self.esporta_stampe()
        self.esporta_stampe_fe()
        #self.esporta_ricevute()
        self.esporta_xml()
        self.genera_fatture_elettroniche()
        self.invia_fatture()
        self.registrazione_contabile()

    def aggiorna_banca(self):
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")
        self.navigate_to_and_wait("Banche")

        self.click_add_button()
        modal = self.wait_modal()
        
        self.wait_for_dropdown_and_select('//span[@id="select2-id_anagrafica-container"]', option_text='Admin spa')
        self.input(modal, 'Nome').setValue('Test')
        self.input(modal, 'IBAN').setValue('IT60X0542811101000000123456')
        self.input(modal, 'BIC').setValue('BNPAITMM')
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")
        self.search_by_th("th_Ragione-sociale", "Cliente")
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
        self.navigate_to_and_wait("Fatture di vendita")

        self.wait_for_element_and_click('//tbody//tr[3]//td')
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
            option_text='Vendite'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')
        self.wait_for_dropdown_and_select(
            '//span[@id="select2-id_segment_-container"]',
            option_text='Vendite'
        )
    
    def controlla_fatture_elettroniche(self):
        self.navigate_to_and_wait("Fatture di vendita")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="check_bulk"]'
        )

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait_for_element_and_click('//div[@class="toast toast-success"]')
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def duplica_selezionati(self):
        self.navigate_to_and_wait("Fatture di vendita")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="copy_bulk"]'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')
        self.wait_for_element_and_click('//tbody//tr//td')

    def elimina_selezionati(self):
        self.navigate_to_and_wait("Fatture di vendita")
        self.search_by_th("th_Numero", "0002/2026")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="delete_bulk"]'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        eliminato = self.get_empty_table_message()
        self.assertEqual("Nessun dato presente nella tabella", eliminato)
        self.clear_filters()

    def emetti_fatture(self):
        self.navigate_to_and_wait("Fatture di vendita")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="change_status"]'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        stato = self.get_table_text(1, 11)
        self.assertEqual(stato, "Emessa")
        self.wait_for_element_and_click('//tbody//tr//td')

    def esporta_selezionati(self):
        self.navigate_to_and_wait("Fatture di vendita")

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

    def esporta_stampe(self):
        self.navigate_to_and_wait("Fatture di vendita")

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

    def esporta_stampe_fe(self):
        self.navigate_to_and_wait("Fatture di vendita")

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
        self.navigate_to_and_wait("Fatture di vendita")

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
        self.navigate_to_and_wait("Fatture di vendita")

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

    def genera_fatture_elettroniche(self):
        self.navigate_to_and_wait("Fatture di vendita")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="generate_xml"]'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.driver.switch_to.window(self.driver.window_handles[1])

        self.click_first_table_row()
        self.wait_for_element_and_click('//button[@class="btn btn-xs btn-info"]')
        self.wait_for_element_and_click('//button[@class="close"]')

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.navigate_to_and_wait("Fatture di vendita")
        self.wait_for_element_and_click('//tbody//tr//td')

    def invia_fatture(self):
        self.navigate_to_and_wait("Fatture di vendita")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="send-invoices"]'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')
        self.clear_filters()

    def registrazione_contabile(self):
        self.navigate_to_and_wait("Fatture di vendita")
        self.search_by_th("th_Numero", "0001")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="registrazione_contabile"]'
        )
        modal = self.wait_modal()
        totale = self.find(By.XPATH, '//th[@id="totale_dare_add"]').text
        self.assertEqual(totale, "323,06")

        self.wait_for_element_and_click('//button[@type="submit"]')

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")
        self.clear_filters()

