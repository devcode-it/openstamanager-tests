from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class GiacenzeSedi(Test):
    def setUp(self):
        super().setUp()

    def test_giacenze_sedi(self):
        self.navigateTo("Statistiche")
        self.wait_loader()
        periodo = "01/01/2025 - 31/12/2025"

        self.assertEqual(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//h3[@class="card-title"])[1]'))).text, "Vendite e acquisti")
        self.assertEqual(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//h3[@class="card-title"])[2]'))).text, "I 20 clienti TOP")
        self.assertEqual(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//h3[@class="card-title"])[3]'))).text, "I 20 articoli più venduti")
        self.assertEqual(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//h3[@class="card-title"])[4]'))).text, "I 20 fornitori TOP")
        self.assertEqual(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//h3[@class="card-title"])[5]'))).text, "I 20 articoli più acquistati")
        self.assertEqual(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//h3[@class="card-title"])[6]'))).text, "Numero interventi per tipologia")
        self.assertEqual(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//h3[@class="card-title"])[7]'))).text, "Ore interventi per tipologia")
        self.assertEqual(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//h3[@class="card-title"])[8]'))).text, "Ore di lavoro per tecnico")
        self.assertEqual(self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, '(//h3[@class="card-title"])[9]'))).text, "Nuove anagrafiche")