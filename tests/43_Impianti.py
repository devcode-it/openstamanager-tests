from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Impianti(Test):
    def setUp(self):
        super().setUp()

    def test_creazione_impianto(self):
        self.add_impianto('01', 'Impianto di Prova da Modificare', 'Cliente')
        self.add_impianto('02', 'Impianto di Prova da Eliminare', 'Cliente')
        self.modifica_impianto("Impianto di Prova")
        self.elimina_impianto()
        self.verifica_impianto()
        self.apri_impianti()
        self.plugin_impianti()
        self.plugin_interventi_svolti()
        self.componenti()
        self.elimina_selezionati()
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')

    def add_impianto(self, matricola: str, nome: str, cliente: str):
        self.navigateTo("Impianti")
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'Matricola').setValue(matricola)
        self.input(modal, 'Nome').setValue(nome)
        self.wait_for_dropdown_and_select('//span[@id="select2-idanagrafica_impianto-container"]', option_text=cliente)

        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def modifica_impianto(self, modifica=str):
        self.navigateTo("Impianti")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Impianto di Prova da Modificare', wait_modal=False)
        self.wait_for_search_results()

        self.click_first_result()
        self.input(None, 'Nome').setValue(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.navigateTo("Impianti")
        self.wait_loader()
        self.clear_filters()

    def elimina_impianto(self):
        self.navigateTo("Impianti")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, 'Impianto di Prova da Eliminare', wait_modal=False)
        self.wait_for_search_results()

        self.click_first_result()
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask "]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.clear_filters()

    def verifica_impianto(self):
        self.navigateTo("Impianti")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Impianto di Prova", wait_modal=False)
        self.wait_for_search_results()

        modificato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[3]'))).text
        self.assertEqual("Impianto di Prova", modificato)
        self.clear_filters()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Impianto di Prova da Eliminare", wait_modal=False)
        eliminato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]'))).text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)

        self.navigateTo("Impianti")
        self.clear_filters()

    def apri_impianti(self):
        self.navigateTo("Anagrafiche")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input')))
        self.send_keys_and_wait(search_input, "Cliente", wait_modal=False)

        self.click_first_result()
        self.wait_for_element_and_click('//a[@id="link-tab_1"]')

        impianto = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="text-right"]'))).text
        self.assertEqual(impianto, "01")

        self.navigateTo("Anagrafiche")
        self.clear_filters()

    def plugin_impianti(self):
        self.navigateTo("Attività")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.wait_for_dropdown_and_select('//span[@id="select2-idanagrafica-container"]', option_text="Cliente")
        self.wait_for_dropdown_and_select('//span[@id="select2-idtipointervento-container"]', option_text="Generico")
        iframe = self.wait_for_element_and_click('(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]')
        iframe.send_keys('Test')
        self.wait_for_element_and_click('//div[@class="col-md-12 text-right"]//button[@type="button"]')

        self.wait_for_element_and_click('//a[@id="link-tab_2"]')
        self.wait_loader()

        self.wait_for_dropdown_and_select('//span[@id="select2-id_impianto_add-container"]', '//li[@class="select2-results__option select2-results__option--highlighted"]')
        self.wait_for_element_and_click('(//button[@class="btn btn-primary tip tooltipstered"])[2]')

        matricola = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_2"]//tbody//tr//td[2]'))).text
        self.assertEqual(matricola, "01")

        self.wait_for_element_and_click('//button[@class="btn btn-sm btn-outline-danger "]')

        self.wait_for_dropdown_and_select('//span[@id="select2-id_impianto_add-container"]', '//li[@class="select2-results__option select2-results__option--highlighted"]')
        self.wait_for_element_and_click('(//button[@class="btn btn-primary tip tooltipstered"])[2]')

        self.navigateTo("Attività")
        self.clear_filters()

    def plugin_interventi_svolti(self):
        self.navigateTo("Impianti")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Impianto di Prova", wait_modal=False)

        self.click_first_result()
        self.wait_for_element_and_click('//a[@id="link-tab_8"]')
        self.wait_loader()

        totale = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[3]//td[2]'))).text
        self.assertEqual(totale, "0,00 €")

        self.navigateTo("Impianti")
        self.wait_loader()
        self.clear_filters()

    def componenti(self):
        self.navigateTo("Impianti")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input')))
        self.send_keys_and_wait(search_input, "Impianto di Prova", wait_modal=False)

        self.click_first_result()
        self.wait_for_element_and_click('//a[@id="link-tab_31"]')
        self.wait_loader()

        self.wait_for_element_and_click('(//button[@class="btn btn-primary bound clickable"])[2]')
        self.wait_for_dropdown_and_select('//span[@id="select2-id_articolo-container"]', option_text="Articolo 1")
        self.wait_for_element_and_click('(//form//button[@class="btn btn-primary"])[2]')

        self.wait_for_element_and_click('//div[@id="tab_31"]//button[@class="btn btn-tool"]')
        data_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="data_installazione_1"]')))
        self.send_keys_and_wait(data_input, "01/01/2026", wait_modal=False)
        self.wait_for_element_and_click('//button[@class="btn btn-success pull-right"]')

        data_installazione = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_31"]//tr[1]//td[3]'))).text
        self.assertEqual(data_installazione, "01/01/2026")

        self.wait_for_element_and_click('//div[@id="tab_31"]//button[@class="btn btn-tool"]')
        self.wait_for_element_and_click('//button[@class="btn btn-warning pull-right"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-primary"]')

        sostituito = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_31"]//tr[1]//td[1])[1]'))).text
        self.assertEqual(sostituito, "#2")

        self.navigateTo("Impianti")
        self.wait_loader()
        self.clear_filters()

    def elimina_selezionati(self):
        self.navigateTo("Impianti")
        self.wait_loader()

        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        matricola_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="matricola"]')))
        self.send_keys_and_wait(matricola_input, "02", wait_modal=False)

        nome_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]')))
        self.send_keys_and_wait(nome_input, "Prova", wait_modal=False)

        self.wait_for_dropdown_and_select('//span[@id="select2-idanagrafica_impianto-container"]', option_text="Cliente")
        self.wait_for_element_and_click('//button[@class="btn btn-primary"]')

        self.navigateTo("Impianti")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Matricola"]/input')))
        self.send_keys_and_wait(search_input, "02", wait_modal=False)

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select('//button[@data-toggle="dropdown"]', '//a[@data-op="delete_bulk"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        scritta = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr'))).text
        self.assertEqual(scritta, "Nessun dato presente nella tabella")
        self.clear_filters()
