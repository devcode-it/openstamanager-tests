from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GiacenzeSedi(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Magazzino")
        
    def test_giacenze_sedi(self):
        # Aggiunta sede
        self.aggiunta_sede()

        # Creazione ddt in uscita
        importi = RowManager.list()
        self.creazione_ddt_uscita("Admin spa", "2", importi[0])

        # Trasporto sedi
        self.trasporto()

        # Verifica movimenti sede  
        self.verifica_movimenti()


    def aggiunta_sede(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Anagrafiche")
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Admin spa", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()    
        sleep(1) 

        #Aggiunta sede
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@id="link-tab_4"]'))).click()
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_4"]//i[@class="fa fa-plus"]').click()
        sleep(1)

        self.input(None, 'Nome sede').setValue("Sede di Roma")
        self.find(By.XPATH, '(//input[@id="cap"])[2]').send_keys("35042")
        self.find(By.XPATH, '(//input[@id="citta"])[2]').click()
        self.find(By.XPATH, '(//input[@id="citta"])[2]').send_keys("Roma")

        self.find(By.XPATH, '(//span[@id="select2-id_nazione-container"])[2]').click()
        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="form_2-4"]//i[@class="fa fa-plus"])[3]'))).click()
        sleep(2)


    def creazione_ddt_uscita(self, cliente: str, causale: str, file_importi: str):  
        self.expandSidebar("Magazzino")
        self.navigateTo("Ddt in uscita")
        sleep(1)

        # Crea un nuovo ddt al cliente indicato. 
        # Apre la schermata di nuovo elemento
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        select = self.input(modal, 'Destinatario')
        select.setByText(cliente)

        select = self.input(modal, 'Causale trasporto')
        select.setByIndex(causale)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

        row_manager = RowManager(self)
        self.valori=row_manager.compile(file_importi)

        self.find(By.XPATH, '//span[@id="select2-idsede_destinazione-container"]').click()
        self.find(By.XPATH, '//input[@class="select2-search__field"]').send_keys("Roma")
        sleep(1)

        self.find(By.XPATH, '//input[@class="select2-search__field"]').send_keys(Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idstatoddt-container"]').click()
        self.find(By.XPATH, '//input[@class="select2-search__field"]').send_keys("Evaso", Keys.ENTER)    
        self.find(By.XPATH, '//a[@id="save"]').click()    
        sleep(1) 

    def trasporto(self):  
        self.navigateTo("Ddt in uscita")
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()    
        sleep(1) 

        self.find(By.XPATH, '//button[@onclick="completaTrasporto()"]').click()
        self.find(By.XPATH, '//span[@id="select2-id_segment-container"]').click()
        self.find(By.XPATH, '//input[@class="select2-search__field"]').send_keys("Standard ddt in entrata")
        sleep(1)

        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-success"]').click()  
        sleep(2)

    def verifica_movimenti(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Articoli")
        self.wait_loader()

        #verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("001", Keys.ENTER)
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]'))).click()
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="control-sidebar-button"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@id="link-tab_10"]'))).click()

        scarico = wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_10"]//tbody//td[5])[1]'))).text
        carico = wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="tab_10"]//tbody//td[5])[2]'))).text

        self.assertEqual(scarico, "Sede di Roma")
        self.assertEqual(carico, "Sede legale")