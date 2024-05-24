from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Checklists(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")


    def test_checklists(self):
        # Creazione Checklist
        self.checklists("Checklist di Prova da Modificare", "Attività", "Interventi svolti")
        self.checklists("Checklist di Prova da Eliminare", "Attività", "Interventi svolti")

        # Modifica Checklist
        self.modifica_checklist("Checklist di Prova")
        
        # Cancellazione Checklist
        self.elimina_checklist()
        
        # Verifica Checklist
        self.verifica_checklist()

    def checklists(self, nome=str, modulo= str, plugin=str):
        self.navigateTo("Checklists")
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        self.input(modal, 'Nome').setValue(nome)
        select = self.input(modal, 'Modulo del template')
        select.setByText(modulo)
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

    def modifica_checklist(self, modifica=str):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Checklists")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Checklist di Prova da Modificare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        sleep(1)

        self.driver.execute_script('window.scrollTo(0,0)')
        self.input(None,'Nome').setValue(modifica)

        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        self.wait_loader()

        self.find(By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]').click()  
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).send_keys("TestPadre")
        self.find(By.XPATH, '(//button[@type="submit"])[3]').click()
        sleep(1)

        self.find(By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]').click()  
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).send_keys("TestFiglio")
        self.find(By.XPATH, '(//span[@class="select2-selection select2-selection--single"])[3]').click()
        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()
        self.find(By.XPATH, '(//button[@type="submit"])[3]').click()
        sleep(1)

        self.navigateTo("Checklists")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()

    def elimina_checklist(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Checklists")
        self.wait_loader()    

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys('Checklist di Prova da Eliminare', Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        sleep(1)

        self.driver.execute_script('window.scrollTo(0,0)')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()      

        self.find(By.XPATH, '//th[@id="th_Nome"]/i[@class="deleteicon fa fa-times"]').click()

    def verifica_checklist(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Checklists")
        self.wait_loader()    

        #verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Checklist di Prova", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[2]').text
        self.assertEqual("Checklist di Prova",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()

        #verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))).send_keys("Checklist di Prova da Eliminare", Keys.ENTER)
        sleep(2)

        self.navigateTo("Attività")
        self.wait_loader()   

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//tr[2]//td[2]').click()
        self.wait_loader()

        self.find(By.XPATH, '//a[@href="#tab_checks"]').click()
        self.wait_loader()

        self.find(By.XPATH, '(//a[@data-title="Aggiungi check"])[2]').click()
        sleep(2)

        self.find(By.XPATH, '//div[@class="modal-content"]//span[@class="select2-selection__placeholder"]').click()
        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()
        self.find(By.XPATH, '//button[@id="check-add"]').click()
        sleep(2)

        TestPadre = self.find(By.XPATH, '(//div[@id="tab_checks"]//tbody//td[2]//span)[1]').text
        TestFiglio = self.find(By.XPATH, '(//div[@id="tab_checks"]//tbody//td[2]//span)[2]').text
        self.assertEqual("TestPadre", TestPadre)
        self.assertEqual("TestFiglio", TestFiglio)

        self.find(By.XPATH, '(//input[@class="checkbox unblockable"])[2]').click()

        test1 = self.find(By.XPATH, '(//input[@class="checkbox unblockable"])[1]').is_selected()
        test2 = self.find(By.XPATH, '(//input[@class="checkbox unblockable"])[2]').is_selected()
        self.assertEqual(test1, False)
        self.assertEqual(test2, True)                