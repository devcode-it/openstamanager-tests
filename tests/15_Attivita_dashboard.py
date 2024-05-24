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


class Attivita_Dashboard(Test):
    def setUp(self):
        super().setUp()

       
    def test_attivita_dashboard(self):
        # Crea un nuovo intervento. *Required*
        importi = RowManager.list()
        self.attivita("Cliente", "1", "2", importi[0])


        self.navigateTo("Dashboard")
        self.wait_loader()
        wait = WebDriverWait(self.driver, 20)

        actions = webdriver.common.action_chains.ActionChains(self.driver)
        attivita = self.find(By.XPATH, '//div[@class="fc-event fc-event-primary"]')
        actions.drag_and_drop_by_offset(attivita, -1000, 0).perform()
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="box box-info collapsable "]//input[@class="select2-search__field"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))).click()
        self.find(By.XPATH, '//div[@class="modal-content"]//button[@onclick="salva(this)"]').click()
        sleep(2)

        self.navigateTo("Dashboard")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-block counter_object btn-danger"]').click()
        sleep(1)
        self.find(By.XPATH, '//input[@class="dashboard_tecnico"]').click()
        sleep(1)
        att="Int. 2 Cliente\nTecnici: Stefano Bianchi"
        trova=self.find(By.XPATH, '//div[@class="fc-event-main"]').text
        self.assertEqual(trova, att)

    def attivita(self, cliente: str, tipo: str, stato: str, file_importi: str):
        self.navigateTo("Attività")
        wait = WebDriverWait(self.driver, 20)
        # Crea un nuovo intervento. 
        # Apre la schermata di nuovo elemento
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        self.input(modal, 'Cliente').setByText(cliente)
        self.input(modal, 'Tipo').setByIndex(tipo)
        
        self.find(By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]').click()  
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]'))).send_keys("Test")
        self.find(By.XPATH, '//div[@class="col-md-12 text-right"]//button[@type="button"]').click()
        self.wait_loader()

        row_manager = RowManager(self)
        self.valori=row_manager.compile(file_importi)