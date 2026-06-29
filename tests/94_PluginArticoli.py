from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
class Articoli(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Magazzino")
        self.wait_loader()

    def test_plugin_articolo(self):
        self.movimenti()
        self.serial()
        self.giacenze()
        self.statistiche()
        self.netto_clienti()
        self.listino_fornitori()
        self.piani_sconto_maggiorazione()
        self.provvigioni()
        self.barcode()
        
    def movimenti(self):
        self.navigate_to_and_wait("Articoli")

        self.click_first_result()

        self.wait_for_element_and_click('//a[@id="link-tab_10"]')

        base_xpath = '//div[@id="tab_10"]//div[@class="card"]//div[@class="card-body"]//tbody'
        carico = self.find(By.XPATH, f'{base_xpath}//tr[2]//td[2]').text

        self.assertEqual(carico, "10,00")

    def serial(self):
        self.navigate_to_and_wait("Articoli")

        self.search_by_th("th_Descrizione", 'Articolo 1', wait_modal=False)

        self.click_first_result()

        self.wait_for_element_and_click('(//i[@class="fa fa-plus"])[2]')
        self.wait_for_element_and_click('//label[@for="abilita_serial"]')
        self.wait_for_element_and_click('//button[@id="save"]')

        self.wait_for_element_and_click('//a[@id="link-tab_11"]')

        serial_start = self.driver.find_element(By.XPATH, '//input[@id="serial_start"]')
        self.send_keys_and_wait(serial_start, '2')

        serial_end = self.driver.find_element(By.XPATH, '//input[@id="serial_end"]')
        serial_end.send_keys(Keys.BACK_SPACE, "2")

        self.wait_for_element_and_click('//div[@id="tab_11"]//button[@type="button"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.wait_for_element_and_click('//div[@id="tab_11"]//a[@class="btn btn-danger btn-sm ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.navigate_to_and_wait("Articoli")
        self.clear_filters()
   
    def giacenze(self):
        self.navigate_to_and_wait("Articoli")

        self.search_by_th("th_Descrizione", 'Articolo 1', wait_modal=False)

        self.click_first_result()
        self.wait_for_element_and_click('//a[@id="link-tab_22"]')

        totale = self.driver.find_element(By.XPATH, '//div[@id="tab_22"]//tbody//tr//td[2]').text
        self.assertEqual(totale, "12,00")

        totale_2 = self.driver.find_element(By.XPATH, '//input[@id="giacenza_0"]').get_attribute('value')
        self.assertEqual(totale_2, "12,00")

        self.navigate_to_and_wait("Articoli")
        self.clear_filters()
        
    def statistiche(self):
        self.navigate_to_and_wait("Articoli")

        self.search_by_th("th_Descrizione", 'Articolo 1', wait_modal=False)

        self.click_first_result()
        self.wait_for_element_and_click('//a[@id="link-tab_24"]')

        numero_1 = self.driver.find_element(By.XPATH, '(//div[@id="tab_24"]//td[@class="text-center"])[1]').text
        self.assertEqual(numero_1, "1")

        numero_2 = self.driver.find_element(By.XPATH, '(//div[@id="tab_24"]//td[@class="text-center"])[2]').text
        self.assertEqual(numero_2, "1")

        self.navigate_to_and_wait("Articoli")
        self.clear_filters()

    def netto_clienti(self):
        self.navigate_to_and_wait("Articoli")

        self.search_by_th("th_Descrizione", 'Articolo 1', wait_modal=False)

        self.click_first_result()
        self.wait_for_element_and_click('//a[@id="link-tab_27"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_cliente_informazioni-container"]', option_text='Cliente')

        self.wait_for_element_and_click('//button[@class="btn btn-info btn-block"]')
        self.wait_for_element_and_click('(//label[@class="btn btn-default"])[4]')

        prezzo_unitario = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario_fisso"]'))
        )
        self.send_keys_and_wait(prezzo_unitario, '5')

        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")

        self.click_add_button()
        self.wait_modal()

        self.wait_for_dropdown_and_select('//span[@id="select2-id_anagrafica_add-container"]', option_text='Cliente')

        self.wait_for_element_and_click('//div[@class="modal-footer"]//button[@class="btn btn-primary"]')
        self.wait_for_element_and_click('//span[@id="select2-id_articolo-container"]')
        self.wait_for_element_and_click('//ul[@class="select2-results__options select2-results__options--nested"]//li[1]')
        self.wait_for_element_and_click('//button[@class="btn btn-primary tip tooltipstered"]')

        prezzo = self.driver.find_element(By.XPATH, '//tbody[@id="righe"]//tr[1]//td[9]').text
        self.assertEqual(prezzo, "5,00 €")

        self.delete_current_and_clear()

        self.expandSidebar("Magazzino")
        self.navigate_to_and_wait("Articoli")

        self.click_first_result()
        self.wait_for_element_and_click('//a[@id="link-tab_27"]')

        self.navigate_to_and_wait("Articoli")
        self.clear_filters()
    
    def listino_fornitori(self):
        self.navigate_to_and_wait("Articoli")

        self.search_by_th("th_Descrizione", 'Articolo 1', wait_modal=False)

        self.click_first_result()
        self.wait_for_element_and_click('//a[@id="link-tab_32"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_fornitore_informazioni-container"]', option_text='Fornitore')

        self.wait_for_element_and_click('//button[@class="btn btn-info"]')
        modal = self.wait_modal()

        qta_minima = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="qta_minima"]'))
        )
        qta_minima.send_keys("100")

        giorni_consegna = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="giorni_consegna"]'))
        )
        giorni_consegna.send_keys("15")

        self.wait_for_element_and_click('(//label[@class="btn btn-default active"])[4]')

        prezzo_unitario = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="prezzo_unitario_fisso"]'))
        )
        self.send_keys_and_wait(prezzo_unitario, '15')

        self.expandSidebar("Acquisti")
        self.navigate_to_and_wait("Fatture di acquisto")

        self.click_add_button()
        modal = self.wait_modal()

        numero_esterno = self.driver.find_element(By.XPATH, '//input[@id="numero_esterno"]')
        self.send_keys_and_wait(numero_esterno, '2')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_anagrafica_add-container"]', option_text='Fornitore')

        self.wait_for_element_and_click('//div[@class="modal-footer"]//button[@class="btn btn-primary"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_articolo-container"]', option_text='Articolo 1')
        self.wait_for_element_and_click('//button[@class="btn btn-primary tip tooltipstered"]')

        prezzo = self.driver.find_element(By.XPATH, '//tbody[@id="righe"]//tr[1]//td[8]').text
        self.assertEqual(prezzo, "15,00 €")

        self.wait_for_element_and_click('//a[@id="elimina"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.expandSidebar("Magazzino")
        self.navigate_to_and_wait("Articoli")

        self.click_first_result()
        self.wait_for_dropdown_and_select('//span[@id="select2-id_fornitore-container"]', option_text='Fornitore')

        self.navigate_to_and_wait("Articoli")

        self.click_first_result()

        self.wait_for_element_and_click('//a[@id="link-tab_32"]')
        self.wait_for_element_and_click('//a[@class="btn btn-secondary btn-warning"]')
        self.wait_modal()

        element = self.driver.find_element(By.XPATH, '//input[@id="codice_fornitore"]')
        element.clear()
        self.send_keys_and_wait(element, '1')

        codice = self.driver.find_element(By.XPATH, '//div[@id="tab_32"]//tbody//tr//td[3]').text
        self.assertEqual(codice, "1")

        self.wait_for_element_and_click('//a[@class="btn btn-secondary btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        messaggio = self.driver.find_element(By.XPATH, '//div[@id="tab_32"]//div[@class="alert alert-info"]').text
        self.assertEqual(messaggio, "Nessuna informazione disponibile...")

        self.navigate_to_and_wait("Articoli")
        self.clear_filters()
    
    def piani_sconto_maggiorazione(self):
        self.navigate_to_and_wait("Articoli")  
    
        self.click_first_result()
        self.wait_for_element_and_click('//a[@id="link-tab_33"]')

        self.wait_for_element_and_click('//div[@id="tab_33"]//i[@class="fa fa-external-link"]')

        self.driver.switch_to.window(self.driver.window_handles[1])
        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue('Test')
        self.input(modal, 'Sconto/magg. combinato').setValue('10')
        self.submit_modal(modal)

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.navigate_to_and_wait("Articoli")  
        self.click_first_result()
        self.wait_for_element_and_click('//a[@id="link-tab_33"]')

        sconto = self.driver.find_element(By.XPATH, '(//div[@class="card card-primary"]//tbody//tr[3]//td[2])[3]').text
        self.assertEqual(sconto, "18,00 €")

        self.navigate_to_and_wait("Articoli")
        self.clear_filters()
    
    def provvigioni(self):
        self.navigate_to_and_wait("Articoli")

        self.search_by_th("th_Descrizione", 'Articolo 1', wait_modal=False)

        self.click_first_result()

        self.wait_for_element_and_click('//a[@id="link-tab_43"]')
        self.wait_for_element_and_click('//div[@id="tab_43"]//i[@class="fa fa-plus"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_agente-container"]', option_text='Agente')

        self.send_keys_and_wait(self.driver.find_element(By.XPATH, '//input[@id="provvigione"]'), '1.00')

        self.wait_for_element_and_click('//div[@id="tab_43"]//tbody//tr//td[3]')
        self.wait_modal()

        self.send_keys_and_wait(self.driver.find_element(By.XPATH, '//input[@id="provvigione"]'), '2')

        provvigione = self.driver.find_element(By.XPATH, '//div[@id="tab_43"]//tbody//tr//td[3]').text
        self.assertEqual(provvigione, "2.00 €")

        self.wait_for_element_and_click('//div[@id="tab_43"]//tbody//tr//td[3]')
        self.wait_for_element_and_click('(//a[@class="btn btn-danger ask"])[2]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        self.navigate_to_and_wait("Articoli")
        self.clear_filters()

    def barcode(self):
        self.navigate_to_and_wait("Articoli")

        self.click_first_result()

        self.wait_for_element_and_click('//a[@id="link-tab_49"]')
        self.wait_for_element_and_click('//div[@id="tab_49"]//i[@class="fa fa-plus"]')

        self.send_keys_and_wait(self.driver.find_element(By.XPATH, '//input[@id="barcode"]'), '2000000000022')

        barcode = self.driver.find_element(By.XPATH, '(//div[@id="tab_49"]//tbody//tr//td[2])[8]').text
        self.assertEqual(barcode, "2000000000022")

        self.navigate_to_and_wait("Articoli")
        self.clear_filters()