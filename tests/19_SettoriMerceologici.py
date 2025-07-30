from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class SettoriMerceologici(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Anagrafiche")
        self.navigateTo("Settori merceologici")

    def test_creazione_settori_merceologici(self):
        # Creazione settore merceologico      *Required*
        self.creazione_settori_merceologici("Settore Merceologico di Prova da Modificare")

        # Modifica settore merceologico
        self.modifica_settori_merceologici("Settore Merceologico di Prova")

        self.creazione_settori_merceologici("Settore Merceologico di Prova da Eliminare")
        # Cancellazione settore merceologico
        self.elimina_settore_merceologico()

        # Verifica settore merceologico
        self.verifica_settore_merceologico()

    def creazione_settori_merceologici(self, descrizione=str):
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'Descrizione').setValue(descrizione)
        self.wait_for_element_and_click('//button[@class="btn btn-primary"][@type="submit"]')

    def modifica_settori_merceologici(self, modifica=str):
        self.navigateTo("Settori merceologici")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_descrizione"]/input'))), 'Settore Merceologico di Prova da Modificare', False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.driver.execute_script('window.scrollTo(0,0)')
        self.input(None,'Descrizione').setValue(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.navigateTo("Settori merceologici")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_descrizione"]/i[@class="deleteicon fa fa-times"]')

    def elimina_settore_merceologico(self):
        self.navigateTo("Settori merceologici")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_descrizione"]/input'))), 'Settore merceologico di Prova da Eliminare', False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.driver.execute_script('window.scrollTo(0,0)')
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.wait_for_element_and_click('//th[@id="th_descrizione"]/i[@class="deleteicon fa fa-times"]')

    def verifica_settore_merceologico(self):
        self.navigateTo("Settori merceologici")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_descrizione"]/input'))), "Settore Merceologico di Prova", False)

        modificato = self.driver.find_element(By.XPATH, '//tbody//tr[1]//td[3]').text
        self.assertEqual("Settore Merceologico di Prova", modificato)
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_descrizione"]/input'))), "Settore Merceologico di Prova da Eliminare", False)

        eliminato = self.driver.find_element(By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)