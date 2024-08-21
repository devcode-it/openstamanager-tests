from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class CategorieImpianti(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Impianti")

    def test_creazione_categorie_impianti(self):
        # Creazione categorie impianto *Required*
        self.creazione_categorie_impianti(nome= "Categoria Impianti di Prova da Modificare", colore="#30db67")
        self.creazione_categorie_impianti(nome= "Categoria Impianti di Prova da Eliminare", colore="#ea2c2c")

        # Modifica Categoria impianto
        self.modifica_categorie_impianti("Categoria Impianti di Prova")
        
        # Cancellazione Categoria impianto
        self.elimina_categorie_impianti()
        
        # Verifica categoria impianto
        self.verifica_categorie_impianti()

    def creazione_categorie_impianti(self, nome=str, colore=str):
        self.navigateTo("Categorie impianti")
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        self.input(modal, 'Colore').setValue(colore)
        self.input(modal, 'Nome').setValue(nome)
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

    def modifica_categorie_impianti(self, modifica=str):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Categorie impianti")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Categoria Impianti di Prova da Modificare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        sleep(1)          

        self.driver.execute_script('window.scrollTo(0,0)')
        self.input(None,'Nome').setValue(modifica)
        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Categorie impianti")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

    def elimina_categorie_impianti(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Categorie impianti")
        self.wait_loader()    

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Categoria Impianti di Prova da Eliminare', Keys.ENTER)
        sleep(1)
        
        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        sleep(1)          

        self.driver.execute_script('window.scrollTo(0,0)')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(1)
        
    def verifica_categorie_impianti(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Categorie impianti")
        self.wait_loader()    

        # Verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Categoria Impianti di Prova", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[2]').text
        self.assertEqual("Categoria Impianti di Prova",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(1)

        # Verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Categoria Impianti di Prova da Eliminare", Keys.ENTER)
        sleep(1)
        
        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)