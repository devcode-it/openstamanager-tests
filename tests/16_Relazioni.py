from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from common.Test import Test, get_html

class Relazioni(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Anagrafiche")
        self.navigateTo("Relazioni")
        self.wait_loader()

    def test_creazione_relazioni(self):
        self.creazione_relazioni("Relazione di Prova da Modificare","#9d2929")
        self.creazione_relazioni("Relazione di Prova da Eliminare","#3737db")
        self.modifica_relazioni("Relazione di Prova")
        self.elimina_relazioni()
        self.verifica_relazione()

    def creazione_relazioni(self, descrizione=str, colore=str):
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'Colore').setValue(colore)
        self.input(modal, 'Descrizione').setValue(descrizione)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    def modifica_relazioni(self, modifica=str):
        self.navigateTo("Relazioni")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))), 'Relazione di Prova da Modificare', False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        colore = self.find(By.XPATH, '//input[@id="colore"]')
        colore.clear()
        colore.send_keys("#436935")

        self.input(None,'Descrizione').setValue(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.navigateTo("Relazioni")
        self.wait_loader()
        self.wait_for_element_and_click('//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]')

    def elimina_relazioni(self):
        self.navigateTo("Relazioni")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))), 'Relazione di Prova da Eliminare', False)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        self.wait_for_element_and_click('//div[@id="tab_0"]//a[@class="btn btn-danger ask"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-danger"]')

        self.wait_for_element_and_click('//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]')

    def verifica_relazione(self):
        self.navigateTo("Relazioni")
        self.wait_loader()

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))), "Relazione di Prova", False)

        modificato = self.find(By.XPATH, '//tbody//tr[1]//td[2]').text
        self.assertEqual("Relazione di Prova", modificato)
        self.wait_for_element_and_click('//i[@class="deleteicon fa fa-times"]')

        self.send_keys_and_wait(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))), "Relazione di Prova da Eliminare", False)

        eliminato = self.find(By.XPATH, '//tbody//tr[1]//td[1]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)
