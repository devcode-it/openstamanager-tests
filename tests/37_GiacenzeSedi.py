from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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
        self.creazione_ddt_uscita("Admin spa", "Vendita", importi[0])

        # Trasporto sedi
        self.trasporto()

        # Verifica movimenti sede  
        self.verifica_movimenti()

    def aggiunta_sede(self):
                self.navigateTo("Anagrafiche")
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Admin spa", Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td[2]') 

        #Aggiunta sede
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@id="link-tab_4"]'))).click()

        self.find(By.XPATH, '//div[@id="tab_4"]//i[@class="fa fa-plus"]').click()

        self.input(None, 'Nome sede').setValue("Sede di Roma")
        self.find(By.XPATH, '(//input[@id="cap"])[2]').send_keys("35042")
        self.find(By.XPATH, '(//input[@id="citta"])[2]').click()
        self.find(By.XPATH, '(//input[@id="citta"])[2]').send_keys("Roma")

        self.find(By.XPATH, '(//span[@id="select2-id_nazione-container"])[2]').click()
        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="form_2-4"]//i[@class="fa fa-plus"])[4]'))).click()

    def creazione_ddt_uscita(self, cliente: str, causale: str, file_importi: str):  
        self.expandSidebar("Magazzino")
        self.navigateTo("Ddt in uscita")

        # Crea un nuovo ddt al cliente indicato. 
        # Apre la schermata di nuovo elemento
        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        select = self.input(modal, 'Destinatario')
        select.setByText(cliente)
        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()

        select = self.input(modal, 'Causale trasporto')
        select.setByText(causale)

        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        row_manager = RowManager(self)
        self.valori = row_manager.compile(file_importi)

        self.find(By.XPATH, '//span[@id="select2-idsede_destinazione-container"]').click()
        self.find(By.XPATH, '//input[@class="select2-search__field"]').send_keys("Roma")

        self.find(By.XPATH, '//input[@class="select2-search__field"]').send_keys(Keys.ENTER)

        self.find(By.XPATH, '//span[@id="select2-idstatoddt-container"]').click()
        self.find(By.XPATH, '//input[@class="select2-search__field"]').send_keys("Evaso", Keys.ENTER)    
        self.find(By.XPATH, '//button[@id="save"]').click() 

    def trasporto(self):  
        self.navigateTo("Ddt in uscita")

        self.wait_for_element_and_click('//tbody//tr//td[2]') 

        self.find(By.XPATH, '//button[@onclick="completaTrasporto()"]').click()
        self.find(By.XPATH, '//span[@id="select2-id_segment-container"]').click()
        self.find(By.XPATH, '//input[@class="select2-search__field"]').send_keys("Standard ddt in entrata")

        self.find(By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-success"]').click()

    def verifica_movimenti(self):
                self.navigateTo("Articoli")
        self.wait_loader()

        # Verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Codice"]/input'))).send_keys("001", Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@id="link-tab_10"]'))).click()

        scarico = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_10"]//tbody//tr//td[6]'))).text
        carico = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_10"]//tbody//tr[3]//td[6]'))).text

        self.assertEqual(scarico, "Sede di Roma")
        self.assertEqual(carico, "Sede legale")