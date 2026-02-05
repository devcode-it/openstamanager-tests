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
        #TODO: barcode
        #self.barcode()
        self.provvigioni()
        #TODO: varianti articolo
        #self.varianti_articolo()
        #TODO: piani di sconto/maggiorazione
        #self.piani_sconto_maggiorazione()
        self.listino_fornitori()
        self.netto_clienti()
        self.statistiche()
        self.giacenze()
        self.serial()
        #TODO: movimenti
        #self.movimenti()
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')
        
    def provvigioni(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))
        )
        self.send_keys_and_wait(search_input, 'Articolo 1', wait_modal=False)

        self.click_first_result()

        self.wait_for_element_and_click('//a[@id="link-tab_43"]')
        self.wait_for_element_and_click('//div[@id="tab_43"]//i[@class="fa fa-plus"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-idagente-container"]', option_text='Agente')

        provvigione_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="provvigione"]'))
        )
        self.send_keys_and_wait(provvigione_input, '1.00')

        self.wait_for_element_and_click('//div[@id="tab_43"]//tbody//tr//td[3]')
        self.wait_modal()

        provvigione_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="provvigione"]'))
        )
        self.send_keys_and_wait(provvigione_input, '2')

        provvigione = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_43"]//tbody//tr//td[3]'))
        ).text
        self.assertEqual(provvigione, "2.00 €")

        self.wait_for_element_and_click('//div[@id="tab_43"]//tbody//tr//td[3]')
        self.wait_for_element_and_click('(//a[@class="btn btn-danger ask"])[2]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.navigateTo("Articoli")
        self.wait_loader()
        self.clear_filters()
    def listino_fornitori(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))
        )
        self.send_keys_and_wait(search_input, 'Articolo 1', wait_modal=False)

        self.click_first_result()
        self.wait_for_element_and_click('//a[@id="link-tab_32"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_fornitore_informazioni-container"]', option_text='Fornitore')

        self.wait_for_element_and_click('//button[@class="btn btn-info"]')
        modal = self.wait_modal()

        self.wait(EC.visibility_of_element_located((By.XPATH, '//input[@id="qta_minima"]')))

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
        self.navigateTo("Fatture di acquisto")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        numero_esterno = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="numero_esterno"]'))
        )
        numero_esterno.send_keys("78")

        self.wait_for_dropdown_and_select('//span[@id="select2-idanagrafica_add-container"]', option_text='Fornitore')

        self.wait_for_element_and_click('//div[@class="modal-footer"]//button[@class="btn btn-primary"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_articolo-container"]', option_text='Articolo 1')
        self.wait_for_element_and_click('//button[@class="btn btn-primary tip tooltipstered"]')

        prezzo = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe"]//tr[1]//td[8]'))
        ).text
        self.assertEqual(prezzo, "15,00 €")

        self.wait_for_element_and_click('//a[@id="elimina"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.expandSidebar("Magazzino")
        self.navigateTo("Articoli")
        self.wait_loader()

        self.click_first_result()
        self.wait_for_dropdown_and_select('//span[@id="select2-id_fornitore-container"]', option_text='Fornitore')

        self.navigateTo("Articoli")
        self.wait_loader()

        self.click_first_result()

        self.wait_for_element_and_click('//a[@id="link-tab_32"]')
        self.wait_for_element_and_click('//a[@class="btn btn-secondary btn-warning"]')
        self.wait_modal()

        element = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="codice_fornitore"]'))
        )
        element.clear()
        self.send_keys_and_wait(element, '1')

        codice = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_32"]//tbody//tr//td[3]'))
        ).text
        self.assertEqual(codice, "1")

        self.wait_for_element_and_click('//a[@class="btn btn-secondary btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        messaggio = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_32"]//div[@class="alert alert-info"]'))
        ).text
        self.assertEqual(messaggio, "Nessuna informazione disponibile...")

        self.navigateTo("Articoli")
        self.wait_loader()
        self.clear_filters()
    def netto_clienti(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))
        )
        self.send_keys_and_wait(search_input, 'Articolo 1', wait_modal=False)

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
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        self.wait_modal()

        self.wait_for_dropdown_and_select('//span[@id="select2-idanagrafica_add-container"]', option_text='Cliente')

        self.wait_for_element_and_click('//div[@class="modal-footer"]//button[@class="btn btn-primary"]')
        self.wait_for_element_and_click('//span[@id="select2-id_articolo-container"]')
        self.wait_for_element_and_click('//ul[@class="select2-results__options select2-results__options--nested"]//li[1]')
        self.wait_for_element_and_click('//button[@class="btn btn-primary tip tooltipstered"]')

        prezzo = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody[@id="righe"]//tr[1]//td[9]'))
        ).text
        self.assertEqual(prezzo, "5,00 €")

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask "]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.expandSidebar("Magazzino")
        self.navigateTo("Articoli")
        self.wait_loader()

        self.click_first_result()
        self.wait_for_element_and_click('//a[@id="link-tab_27"]')

        self.navigateTo("Articoli")
        self.wait_loader()
        self.clear_filters()
    def statistiche(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))
        )
        self.send_keys_and_wait(search_input, 'Articolo 1', wait_modal=False)

        self.click_first_result()
        self.wait_for_element_and_click('//a[@id="link-tab_24"]')

        numero_1 = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_24"]//td[@class="text-center"])[1]'))
        ).text
        self.assertEqual(numero_1, "1")

        numero_2 = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_24"]//td[@class="text-center"])[2]'))
        ).text
        self.assertEqual(numero_2, "1")

        self.navigateTo("Articoli")
        self.wait_loader()
        self.clear_filters()
    def giacenze(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))
        )
        self.send_keys_and_wait(search_input, 'Articolo 1', wait_modal=False)

        self.click_first_result()
        self.wait_for_element_and_click('//a[@id="link-tab_22"]')

        totale = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_22"]//tbody//tr//td[2]'))
        ).text
        self.assertEqual(totale, "12,00")

        totale_2 = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_22"]//div[@class="col-md-12 text-center"])[2]'))
        ).text
        self.assertEqual(totale_2, "12,00")

        self.navigateTo("Articoli")
        self.wait_loader()
        self.clear_filters()
        
    def serial(self):
        self.navigateTo("Articoli")
        self.wait_loader()

        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))
        )
        self.send_keys_and_wait(search_input, 'Articolo 1', wait_modal=False)

        self.click_first_result()

        self.wait_for_element_and_click('(//i[@class="fa fa-plus"])[2]')
        self.wait_for_element_and_click('//label[@for="abilita_serial"]')
        self.wait_for_element_and_click('//button[@id="save"]')

        self.wait_for_element_and_click('//a[@id="link-tab_11"]')

        serial_start = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="serial_start"]'))
        )
        serial_start.send_keys("1")

        serial_end = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="serial_end"]'))
        )
        serial_end.send_keys(Keys.BACK_SPACE, "2")

        self.wait_for_element_and_click('//div[@id="tab_11"]//button[@type="button"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-primary"]')

        self.wait_for_element_and_click('(//div[@id="tab_11"]//a[@class="btn btn-danger btn-sm ask"])[2]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.wait(EC.invisibility_of_element_located((By.XPATH, '//div[@id="tab_11"]//div[@class="card"]//tbody//tr[2]//td[1]')))

        self.navigateTo("Articoli")
        self.wait_loader()
        self.clear_filters()
   