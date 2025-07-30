from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Provenienze_clienti(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Anagrafiche")
        self.navigateTo("Provenienze clienti")
        self.wait_loader()

    def test_creazione_provenienze_clienti(self):
        self.creazione_provenienze_clienti("Provenienza Clienti di Prova da Modificare","#9d2929")
        self.creazione_provenienze_clienti("Provenienza Clienti di Prova da Eliminare","#3737db")
        self.modifica_provenienze_clienti("Provenienza Clienti di Prova")
        self.elimina_provenienze_clienti()
        self.verifica_provenienze_clienti()

    def creazione_provenienze_clienti(self, descrizione=str, colore=str):
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'Colore').setValue(colore)
        self.input(modal, 'Descrizione').setValue(descrizione)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    def modifica_provenienze_clienti(self, modifica=str):
        self.navigateTo("Provenienze clienti")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_descrizione"]/input'))), 'Provenienza Clienti di Prova da Modificare', False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.driver.execute_script('window.scrollTo(0,0)')
        self.input(None,'Descrizione').setValue(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.navigateTo("Provenienze clienti")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_descrizione"]/i[@class="deleteicon fa fa-times"]')

    def elimina_provenienze_clienti(self):
        self.navigateTo("Provenienze clienti")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_descrizione"]/input'))), 'Provenienza Clienti di Prova da Eliminare', False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.driver.execute_script('window.scrollTo(0,0)')
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.wait_for_element_and_click('//th[@id="th_descrizione"]/i[@class="deleteicon fa fa-times"]')

    def verifica_provenienze_clienti(self):
        self.navigateTo("Provenienze clienti")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_descrizione"]/input'))), "Provenienza Clienti di Prova", False)

        modificato = self.find(By.XPATH, '//tbody//tr[1]//td[3]').text
        self.assertEqual("Provenienza Clienti di Prova", modificato)
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_descrizione"]/input'))), "Provenienza Clienti di Prova da Eliminare", False)

        eliminato = self.find(By.XPATH, '//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)