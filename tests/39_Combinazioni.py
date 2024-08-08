from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Combinazioni(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Magazzino")


    def test_creazione_combinazioni(self):
        # Creazione combinazioni *Required*
        self.creazione_combinazioni(codice="0001", nome="Combinazione di Prova da Modificare", attributi="Attributo modificato")
        self.creazione_combinazioni(codice="0002", nome="Combinazione di Prova da Eliminare", attributi="Attributo modificato")

        # Modifica Combinazioni
        self.modifica_combinazioni("Combinazione di Prova")

        # Cancellazione Combinazioni
        self.elimina_combinazioni()
        
        # Verifica Combinazioni
        self.verifica_combinazioni()

        # Plugin varianti articoli da Articoli
        self.varianti_articoli()

    def creazione_combinazioni(self, codice: str, nome: str, attributi: str):
        self.navigateTo("Combinazioni")
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        self.input(modal, 'Codice').setValue(codice)
        self.input(modal, 'Nome').setValue(nome)
        select = self.input(modal, 'Attributi')
        select.setByText(attributi)
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
       
    def modifica_combinazioni(self, modifica):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Combinazioni")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Combinazione di Prova da Modificare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()
        
        self.input(None,'Nome').setValue(modifica)
        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Combinazioni")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def elimina_combinazioni(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Combinazioni")
        self.wait_loader()    

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Combinazione di Prova da Eliminare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        sleep(1)
        
        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)
        
    def verifica_combinazioni(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Combinazioni")
        self.wait_loader()    

        #verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Combinazione di Prova", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[3]').text
        self.assertEqual("Combinazione di Prova",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

        #verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Attributo di Prova da Eliminare", Keys.ENTER)
        sleep(1)

        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)

    def varianti_articoli(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Attributi Combinazioni")
        self.wait_loader()

        # Creazione Attributi
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        self.wait_modal()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="titolo"]'))).send_keys('Taglie', Keys.ENTER)
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@onclick="aggiungiValore(this)"]'))).click()
        self.wait_modal()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys('S', Keys.ENTER)
        sleep(2)

        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()
        self.wait_modal()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys('M', Keys.ENTER)
        sleep(2)

        self.find(By.XPATH, '//button[@class="btn btn-primary pull-right"]').click()
        self.wait_modal()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys('L', Keys.ENTER)
        sleep(2)

        self.navigateTo("Combinazioni")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        # Creazione combinazioni
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="codice"]'))).send_keys('001')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="nome"]'))).send_keys('Vestito')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="select2-selection select2-selection--multiple"]'))).send_keys('Taglie', Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-warning "]').click()
        self.wait_loader()

        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        # Verifica combinazioni
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys('Vestito', Keys.ENTER)
        sleep(2)

        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        self.find(By.XPATH, '//a[@id="link-tab_34"]').click() 
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_34"]//tr[3]')))

        # Modifica combinazioni
        self.navigateTo("Attributi Combinazioni")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr[2]//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '(//button[@class="btn btn-warning btn-xs"])[1]').click()
        sleep(1)

        element = self.find(By.XPATH, '//input[@id="nome"]')
        element.clear()
        element.send_keys("XS",Keys.ENTER)
        self.wait_loader()

        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        self.find(By.XPATH, '//a[@id="link-tab_34"]').click() 
        self.wait_loader()

        taglia=self.find(By.XPATH, '//div[@id="tab_34"]//tr[1]//td[2]').text
        self.assertEqual(taglia, "Taglie: XS")

        # Elimina attributi
        self.navigateTo("Attributi Combinazioni")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        sleep(1)

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        wait.until(EC.invisibility_of_element_located((By.XPATH, '//tbody//tr[2]')))

        # Elimina combinazioni
        self.navigateTo("Combinazioni")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@class="form-control"])[1]'))).send_keys("001", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr[2]//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)
