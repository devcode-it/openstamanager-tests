from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Banche(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")

    def test_creazione_banca(self):
        self.creazione_banca("Cliente", "Banca di Prova da Modificare", "IT11C1234512345678912345679", "12345678")
        self.creazione_banca("Cliente", "Banca di Prova da Eliminare", "IT11C1234512345678912345679", "12345678")
        self.modifica_banca("Banca di Prova")
        self.elimina_banca()
        self.verifica_banca()
        self.aggiorna_banca_fatture_acquisto()
        self.aggiorna_banca_scadenzario()
        self.aggiorna_banca_fatture_vendita()
        
    def creazione_banca(self, anagrafica: str, nome: str, iban: str, bic: str):
        self.navigate_to_and_wait("Banche")
        self.click_add_button()
        modal = self.wait_modal()

        select = self.input(modal, 'Anagrafica')
        select.setByText(anagrafica)
        self.input(modal, 'Nome').setValue(nome)
        self.input(modal, 'IBAN').setValue(iban)
        self.input(modal, 'BIC').setValue(bic)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def modifica_banca(self, modifica = str):
        self.navigate_to_and_wait("Banche")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Banca di Prova da Modificare', wait_modal=False)
        self.click_first_table_row()

        self.input(None,'Nome').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Banche")
        self.clear_filters()

    def elimina_banca(self):
        self.navigate_to_and_wait("Banche")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Banca di Prova da Eliminare', wait_modal=False)
        self.click_first_table_row()

        self.delete_current_and_clear()

    def verifica_banca(self):
        self.navigate_to_and_wait("Banche")

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Banca di Prova", wait_modal=False)
        modificato = self.get_table_text(1, 2)
        self.assertEqual("Banca di Prova", modificato)
        self.clear_filters()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Banca di Prova da Eliminare", wait_modal=False)
        eliminato = self.get_empty_table_message()
        self.assertEqual("Nessun dato presente nella tabella", eliminato)

    def aggiorna_banca_fatture_acquisto(self):
        self.navigate_to_and_wait("Banche")

        self.click_add_button()

        self.wait_for_dropdown_and_select('//span[@id="select2-id_anagrafica-container"]', option_text='Admin spa')

        nome_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]')))
        nome_input.send_keys("Banca Admin spa")
        iban_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="iban"]')))
        iban_input.send_keys("IT11C1234512345678912345679")
        bic_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="bic"]')))
        bic_input.send_keys("123456789")

        self.wait_for_element_and_click('//button[@class="btn btn-primary"]')
        self.wait_loader()

        self.expandSidebar("Acquisti")
        self.navigate_to_and_wait("Fatture di acquisto")

        numero_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]//input')))
        self.send_keys_and_wait(numero_input, "2", wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_bank"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_banca-container"]', option_text='Banca Admin spa')

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        banca = self.get_table_text(1, 9)
        self.assertEqual(banca, "Banca Admin spa - IT11C1234512345678912345679")

    def aggiorna_banca_scadenzario(self):
        self.expandSidebar("Contabilità")
        self.navigate_to_and_wait("Scadenzario")

        self.wait_for_dropdown_and_select('//span[@id="select2-id_segment_-container"]', option_text='Scadenzario clienti')

        tipo_pagamento_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Tipo-di-pagamento"]//input')))
        self.send_keys_and_wait(tipo_pagamento_input, "Assegno", wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_bank"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_banca-container"]', option_text='Banca Admin spa')

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        widget = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="toast toast-success"]//div[3]'))).text
        self.assertEqual(widget, "Banca aggiornata per le Fatture 0001 !")

    def aggiorna_banca_fatture_vendita(self):
        self.expandSidebar("Vendite")
        self.navigate_to_and_wait("Fatture di vendita")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_element_and_click('//button[@data-toggle="dropdown"]')
        self.wait_for_element_and_click('//a[@data-op="change_bank"]')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_banca-container"]', option_text='Banca Admin spa')

        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        banca = self.get_table_text(1, 7)
        self.assertEqual(banca, "Banca Admin spa - IT11C1234512345678912345679")
        self.click_first_table_row()
        self.wait_loader()

        self.wait_for_element_and_click('//a[@id="elimina"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

