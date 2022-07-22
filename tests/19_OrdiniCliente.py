from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class OrdiniCliente(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Vendite")


    def test_creazione_ordine_cliente(self):
        # Crea una nuovo ordine cliente per il cliente "Cliente". *Required*
        importi = RowManager.list()
        self.creazione_ordine_cliente("Cliente", importi[0])
        self.creazione_ordine_cliente("Cliente", importi[0])

        # Modifica ordine cliente
        self.modifica_ordine_cliente()

        # Cancellazione ordine cliente
        self.elimina_ordine_cliente()

        # Verifica ordine cliente
        self.verifica_ordine_cliente()


    def creazione_ordine_cliente(self, cliente: str, file_importi: str):
        self.navigateTo("Ordini cliente")
        self.wait_loader() 

        # Crea un nuovo ordine cliente per il cliente indicato. 
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        select = self.input(modal, 'Cliente')
        select.setByText(cliente)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

        #toast = self.driver.find_elements(By.CLASS_NAME, 'toast-message')
        #self.assertIn('Aggiunto ordine cliente', toast)

        row_manager = RowManager(self)
        row_manager.compile(file_importi)

    def modifica_ordine_cliente(self):
        self.navigateTo("Ordini cliente")
        self.wait_loader()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Numero"]/input')
        element.send_keys('1')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        
        self.find(By.XPATH,'//span[@id="select2-idstatoordine-container"]').click()
        self.wait_loader()

        element=self.find(By.XPATH,'//input[@type="search"]')
        element.send_keys("Accettato")

        self.find(By.XPATH,'//li[@class="select2-results__option select2-results__option--highlighted"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        self.wait_loader()
        
        self.navigateTo("Ordini cliente")
        self.wait_loader()  

        self.find(By.XPATH, '//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def elimina_ordine_cliente(self):
        self.navigateTo("Ordini cliente")
        self.wait_loader()  

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Numero"]/input')
        element.send_keys('2')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys(Keys.ENTER)

        sleep(2)
        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]').click()
        self.wait_loader()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Numero"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

    def verifica_ordine_cliente(self):
        self.navigateTo("Ordini cliente")
        self.wait_loader()  

        #verifica elemento modificato
        element=self.driver.find_element(By.XPATH,'//th[@id="th_icon_title_Stato"]/input')
        element.send_keys("Accettato")
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_icon_title_Stato"]/input'))).send_keys(Keys.ENTER)
        sleep(1)
        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[7]').text
        self.assertEqual("Accettato",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times fa-2x"]').click()
        sleep(1)

        #verifica elemento eliminato
        element=self.driver.find_element(By.XPATH,'//th[@id="th_Numero"]/input')
        element.send_keys("2")
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Numero"]/input'))).send_keys(Keys.ENTER)
        sleep(1)
        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)