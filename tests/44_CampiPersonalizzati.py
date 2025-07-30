from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Campi_personalizzati(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")
        
    def test_campi_personalizzati(self):
        # Creazione campi personalizzati *Required*
        self.creazione_campi_personalizzati(nome="Campo personalizzato di Prova da Modificare", contenuto="Prova")
        self.creazione_campi_personalizzati(nome="Campo personalizzato di Prova da Eliminare", contenuto="Prova")
        
        # Modifica campi personalizzati
        self.modifica_campi_personalizzati(modifica="Campo personalizzato di Prova")

        # Cancellazione campi personalizzati
        self.elimina_campi_personalizzati()

        # Verifica campi personalizzati
        self.verifica_campi_personalizzati()

    def creazione_campi_personalizzati(self, nome:str, contenuto:str):
                self.navigateTo("Campi personalizzati")
        self.wait_loader()  

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@id="select2-module_id-container"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-search select2-search--dropdown"]//input[@type="search"]'))).send_keys("Attività")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))).click()

        self.input(modal, 'Nome').setValue(nome)
        self.input(modal, 'Codice').setValue(contenuto)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

    def modifica_campi_personalizzati(self, modifica:str):
                self.navigateTo("Campi personalizzati")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Campo personalizzato di Prova da Modificare', Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        
        self.input(None,'Nome').setValue(modifica)
        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Campi personalizzati")
        self.wait_loader()  

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()

    def elimina_campi_personalizzati(self):
                self.navigateTo("Campi personalizzati")
        self.wait_loader()  

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Campo personalizzato di Prova da Eliminare', Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()
        
    def verifica_campi_personalizzati(self):
                self.navigateTo("Campi personalizzati")
        self.wait_loader()    

        # Verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Campo personalizzato di Prova", Keys.ENTER)

        modificato = self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[4]').text
        self.assertEqual("Campo personalizzato di Prova", modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()

        # Verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Campo personalizzato di Prova da Eliminare", Keys.ENTER)

        eliminato = self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)

