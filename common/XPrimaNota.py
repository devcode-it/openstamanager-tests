from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class PrimaNota(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Contabilità")
        self.navigateTo("Prima nota")

    def test_creazione_prima_nota(self):
        # Crea un nuovo movimento di prima nota. 
        self.creazione_prima_nota("Pag. 1", "Cassa")

    def creazione_prima_nota(self, causale: str, conto: str):
        # Crea un nuovo movimento di prima nota. 
        # Apre la schermata di nuovo elemento
        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Causale').setValue(causale)

        self.driver.execute_script(
            '$("#conto_0").select2("open");')

        # Attesa del caricamento
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//ul[@class="select2-results__options"]/li[contains(., "100.000010 Cassa") and not (contains(@class, "loading-results"))][1]')))

        item = self.driver.find_element(By.XPATH, '//ul[@class="select2-results__options"]/li[contains(., "100.000010 Cassa") and not (contains(@class, "loading-results"))][1]')
        item.click()

        time.sleep(4)
        # Submit
        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

        
        
        #toast = self.driver.find_elements(By.CLASS_NAME, 'toast-message')
        #self.assertIn('Aggiunto movimento', toast)
    
        
        