from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Impianti(Test):
    def setUp(self):
        super().setUp()

    def test_creazione_impianto(self):
        self.add_impianto('01', 'Impianto di Prova da Modificare', 'Cliente')
        self.close_tour()
        
        self.add_impianto('02', 'Impianto di Prova da Eliminare', 'Cliente')
        self.modifica_impianto("Impianto di Prova")
        self.elimina_impianto()
        self.verifica_impianto()
        self.apri_impianti()
        self.plugin_impianti()
        self.plugin_interventi_svolti()
        self.componenti()
        self.elimina_selezionati()

    def add_impianto(self, matricola: str, nome: str, cliente: str):
        self.navigate_to_and_wait("Impianti")
        self.click_add_button()
        modal = self.wait_modal()

        self.input(modal, 'Matricola').setValue(matricola)
        self.input(modal, 'Nome').setValue(nome)
        self.wait_for_dropdown_and_select('//span[@id="select2-id_anagrafica_impianto-container"]', option_text=cliente)

        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def modifica_impianto(self, modifica=str):
        self.navigate_to_and_wait("Impianti")

        self.search_by_th_and_click_first("th_Nome", 'Impianto di Prova da Modificare')
        self.input(None, 'Nome').setValue(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Impianti")
        self.clear_filters()

    def elimina_impianto(self):
        self.navigate_to_and_wait("Impianti")

        self.search_by_th_and_click_first("th_Nome", 'Impianto di Prova da Eliminare')
        self.delete_current_and_clear()

    def verifica_impianto(self):
        self.navigate_to_and_wait("Impianti")

        self.search_by_th("th_Nome", "Impianto di Prova")

        modificato = self.get_table_text(1, 3)
        self.assertEqual("Impianto di Prova", modificato)
        self.clear_filters()

        self.verify_deleted_by_th("th_Nome", "Impianto di Prova da Eliminare")

    def apri_impianti(self):
        self.navigate_to_and_wait("Anagrafiche")

        self.search_by_th_and_click_first("th_Ragione-sociale", "Cliente")
        self.wait_for_element_and_click('//a[@id="link-tab_1"]')

        impianto = self.find(By.XPATH, '//div[@class="text-right"]').text
        self.assertEqual(impianto, "01")

        self.navigate_to_and_wait("Anagrafiche")
        self.clear_filters()

    def plugin_impianti(self):
        self.navigate_to_and_wait("Attività")

        self.click_add_button()
        modal = self.wait_modal()

        self.wait_for_dropdown_and_select('//span[@id="select2-id_anagrafica-container"]', option_text="Cliente")
        self.wait_for_dropdown_and_select('//span[@id="select2-id_tipo_intervento-container"]', option_text="Generico")
        iframe = self.wait_for_element_and_click('(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]')
        iframe.send_keys('Test')
        self.wait_for_element_and_click('//div[@class="col-md-12 text-right"]//button[@type="button"]')

        self.wait_for_element_and_click('//a[@id="link-tab_2"]')
        self.wait_loader()

        self.wait_for_dropdown_and_select('//span[@id="select2-id_impianto_add-container"]', '//li[@class="select2-results__option select2-results__option--selectable select2-results__option--highlighted"]')
        self.wait_for_element_and_click('(//button[@class="btn btn-primary tip tooltipstered"])[2]')

        matricola = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_2"]//tbody//tr//td[2]'))).text
        self.assertEqual(matricola, "01")

        self.wait_for_element_and_click('//button[@class="btn btn-sm btn-outline-danger "]')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_impianto_add-container"]', '//li[@class="select2-results__option select2-results__option--selectable select2-results__option--highlighted"]')
        self.wait_for_element_and_click('(//button[@class="btn btn-primary tip tooltipstered"])[2]')

        self.navigate_to_and_wait("Attività")
        self.clear_filters()

    def plugin_interventi_svolti(self):
        self.navigate_to_and_wait("Impianti")

        self.search_by_th_and_click_first("th_Nome", "Impianto di Prova")
        self.wait_for_element_and_click('//a[@id="link-tab_8"]')
        self.wait_loader()

        totale = self.get_table_text(3, 2)
        self.assertEqual(totale, "0,00 €")

        self.navigate_to_and_wait("Impianti")
        self.clear_filters()

    def componenti(self):
        self.navigate_to_and_wait("Impianti")

        self.search_by_th_and_click_first("th_Nome", "Impianto di Prova")
        self.wait_for_element_and_click('//a[@id="link-tab_31"]')
        self.wait_loader()

        self.wait_for_element_and_click('(//button[@class="btn btn-primary bound clickable"])[2]')
        self.wait_for_dropdown_and_select('//span[@id="select2-id_articolo_componente-container"]', option_text="Articolo 1")
        self.wait_for_element_and_click('(//button[@type="submit"])[3]')

        self.wait_for_element_and_click('//div[@id="tab_31"]//button[@class="btn btn-sm btn-default"]')
        data_input = self.find(By.XPATH, '//input[@id="data_installazione_1"]')
        self.send_keys_and_wait(data_input, "01/01/2026", wait_modal=False)
        self.wait_for_element_and_click('(//button[@class="btn btn-success"])[2]')

        data_installazione = self.find(By.XPATH, '//div[@id="tab_31"]//tr[1]//td[3]').text
        self.assertEqual(data_installazione, "01/01/2026")

        self.wait_for_element_and_click('//div[@id="tab_31"]//button[@class="btn btn-sm btn-warning"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        sostituito = self.find(By.XPATH, '(//div[@id="tab_31"]//tr[1]//td[1])[1]').text
        self.assertEqual(sostituito, "#2")

        self.navigate_to_and_wait("Impianti")
        self.clear_filters()

    def elimina_selezionati(self):
        self.navigate_to_and_wait("Impianti")

        self.click_add_button()
        modal = self.wait_modal()

        matricola_input = self.find(By.XPATH, '//input[@id="matricola"]')
        self.send_keys_and_wait(matricola_input, "02", wait_modal=False)

        nome_input = self.find(By.XPATH, '//input[@id="nome"]')
        self.send_keys_and_wait(nome_input, "Prova", wait_modal=False)

        self.wait_for_dropdown_and_select('//span[@id="select2-id_anagrafica_impianto-container"]', option_text="Cliente")
        self.wait_for_element_and_click('//button[@class="btn btn-primary"]')

        self.navigate_to_and_wait("Impianti")

        self.search_by_th("th_Matricola", "02")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select('//button[@data-toggle="dropdown"]', '//a[@data-op="delete_bulk"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')

        scritta = self.find(By.XPATH, '//tbody//tr').text
        self.assertEqual(scritta, "Nessun dato presente nella tabella")
        self.clear_filters()
