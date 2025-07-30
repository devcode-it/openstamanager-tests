from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from common.Test import Test, get_html

class TipiAnagrafiche(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Anagrafiche")
        self.navigateTo("Tipi di anagrafiche")

    def test_creazione_tipo_anagrafiche(self):
        # Creazione tipo di anagrafica *Required*
        self.creazione_tipo_anagrafiche("Tipo di anagrafica di Prova da Modificare")
        self.creazione_tipo_anagrafiche("Tipo di anagrafica di Prova da Eliminare")

        # Modifica tipo di anagrafica
        self.modifica_tipo_anagrafiche("Tipo di anagrafica di Prova")

        # Cancellazione tipo di anagrafica
        self.elimina_tipo_anagrafiche()

        # Verifica tipo di anagrafica
        self.verifica_tipo_anagrafiche()

    def creazione_tipo_anagrafiche(self, descrizione = str, colore = str):
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        self.input(modal, 'Descrizione').setValue(descrizione)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

    def modifica_tipo_anagrafiche(self, modifica = str):
                self.navigateTo("Tipi di anagrafiche")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Tipo di anagrafica di Prova da Modificare', Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        
        self.input(None,'Descrizione').setValue(modifica)
        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Tipi di anagrafiche")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()

    def elimina_tipo_anagrafiche(self):
                self.navigateTo("Tipi di anagrafiche")
        self.wait_loader()    

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Tipo di anagrafica di Prova da Eliminare', Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
        
    def verifica_tipo_anagrafiche(self):
                self.navigateTo("Tipi di anagrafiche")
        self.wait_loader()    

        # Verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys("Tipo di anagrafica di Prova", Keys.ENTER)

        modificato = self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[2]').text
        self.assertEqual("Tipo di anagrafica di Prova", modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()

        # Verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys("Tipo di anagrafica di Prova da Eliminare", Keys.ENTER)

        eliminato = self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[1]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)
