from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class RitenutePrevidenziali(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")

    def test_creazione_ritenute_previdenziali(self):
        self.creazione_ritenute_previdenziali(descrizione= "Ritenuta Previdenziale di Prova da Modificare", percentuale="80,00", percentualeimp="60,00")
        self.creazione_ritenute_previdenziali(descrizione= "Ritenuta Previdenziale di Prova da Eliminare", percentuale="20,00", percentualeimp="40,00")
        self.modifica_ritenute_previdenziali("Ritenuta Previdenziale di Prova")
        self.elimina_ritenute_previdenziali()
        self.verifica_ritenuta_previdenziale()

    def creazione_ritenute_previdenziali(self, descrizione = str, percentuale = str, percentualeimp = str):
        self.navigateTo("Ritenute previdenziali")
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'Descrizione').setValue(descrizione)
        self.input(modal, 'Percentuale').setValue(percentuale)
        self.input(modal, 'Causale ritenuta').setValue("A")
        self.input(modal, 'Tipo ritenuta').setValue("RT01")
        self.input(modal, 'Percentuale imponibile').setValue(percentualeimp)
        self.wait_for_element_and_click('button[type="submit"]', By.CSS_SELECTOR)

    def modifica_ritenute_previdenziali(self, modifica = str):
        self.navigateTo("Ritenute previdenziali")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Ritenuta Previdenziale di Prova da Modificare', wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.input(None,'Descrizione').setValue(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.navigateTo("Ritenute previdenziali")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]')

    def elimina_ritenute_previdenziali(self):
        self.navigateTo("Ritenute previdenziali")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, 'Ritenuta Previdenziale di Prova da Eliminare', wait_modal=False)
        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')
        self.wait_for_element_and_click('//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]')

    def verifica_ritenuta_previdenziale(self):
        self.navigateTo("Ritenute previdenziali")
        self.wait_loader()

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, "Ritenuta Previdenziale di Prova", wait_modal=False)
        modificato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[3]'))).text
        self.assertEqual("Ritenuta Previdenziale di Prova", modificato)
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

        search_input = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input')))
        self.send_keys_and_wait(search_input, "Ritenuta Previdenziale di Prova da Eliminare", wait_modal=False)
        eliminato = self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]'))).text
        self.assertEqual("Nessun dato presente nella tabella", eliminato)