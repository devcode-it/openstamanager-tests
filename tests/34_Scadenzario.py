from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Scadenzario(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Contabilità")

    def search_scadenza(self, nome: str):
        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione-scadenza"]/input')))
        search_input.clear()
        self.send_keys_and_wait(search_input, nome, wait_modal=False)
        self.wait_for_search_results()

    def test_creazione_scadenzario(self):
        self.creazione_scadenzario("Cliente", "Scadenze generiche", "10", "Scadenza di Prova")
        self.creazione_scadenzario("Cliente", "Scadenze generiche", "10", "Scadenza di Prova da Eliminare")
        self.modifica_scadenza("Scadenza di Prova")
        self.elimina_scadenza()
        self.verifica_scadenza()
        self.registrazione_contabile()
        self.info_distinta()
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')

    def creazione_scadenzario(self, nome: str, tipo: str, importo: str, descrizione: str):
        self.navigateTo("Scadenzario")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'Tipo').setByText(tipo)
        self.input(modal, 'Anagrafica').setByText(nome)
        self.input(modal, 'Importo').setValue(importo)

        self.wait_for_element_and_click('(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]')
        iframe_element = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]')))
        iframe_element.send_keys(descrizione)

        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)
        self.wait_loader()

    def modifica_scadenza(self, modifica: str):
        self.navigateTo("Scadenzario")
        self.wait_loader()

        self.search_scadenza('Scadenza di Prova')
        self.click_first_result()

        iframe_element = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[2]')))
        iframe_element.send_keys(modifica)

        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.navigateTo("Scadenzario")
        self.wait_loader()

    def elimina_scadenza(self):
        self.navigateTo("Scadenzario")
        self.wait_loader()

        self.clear_filters()
        self.search_scadenza('Scadenza di Prova da Eliminare')
        self.click_first_result()

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.wait_loader()

        self.clear_filters()

    def verifica_scadenza(self):
        self.navigateTo("Scadenzario")
        self.wait_loader()

        self.search_scadenza("Scadenza di Prova")
        modificato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[2]'))).text
        self.assertEqual("Scadenza di Prova", modificato)
        self.clear_filters()

        self.search_scadenza("Scadenza da Eliminare")
        eliminato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]'))).text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)
        self.clear_filters()

    def registrazione_contabile(self):
        self.navigateTo("Scadenzario")
        self.wait_loader()

        self.search_scadenza("Fattura immediata di acquisto numero 01")
        self.wait_for_element_and_click('//tbody//tr//td') 
        self.wait_for_dropdown_and_select('//button[@data-toggle="dropdown"]', option_xpath='//a[@data-op="registrazione-contabile"]')
        modal = self.wait_modal()

        self.wait_for_dropdown_and_select(
            '//span[@id="select2-conto_add_1-container"]',
            option_text="700.000010"
        )
        self.wait_for_element_and_click('//div[@class="modal-body"]//button[@type="submit"]')
        self.wait_loader()

        self.wait_driver.until(EC.invisibility_of_element_located(modal))

        self.navigateTo("Scadenzario")
        self.wait_loader()

        self.clear_filters()

        
    def info_distinta(self):
        self.navigateTo("Scadenzario")
        self.wait_loader()

        self.search_scadenza("Fattura immediata di acquisto numero 02")
        self.wait_for_element_and_click('//tbody//tr//td') 
        self.wait_for_dropdown_and_select('//button[@data-toggle="dropdown"]', option_xpath='//a[@data-op="change_distinta"]')

        distinta_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="distinta"]')))
        distinta_input.send_keys("Prova")
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-warning"]')
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_loader()

        self.navigateTo("Scadenzario")
        self.wait_loader()
        self.clear_filters()