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

        
    def test_giacenze_sedi(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Statistiche")
        self.wait_loader()

        periodi = self.find(By.XPATH, '(//h4[@class="card-title"])[1]').text
        self.assertEqual(periodi, "Vendite e acquisti")

        vendite = self.find(By.XPATH, '(//h4[@class="card-title"])[2]').text
        self.assertEqual(vendite, "Periodi temporali")

        clienti = self.find(By.XPATH, '(//h4[@class="card-title"])[3]').text
        articoli = self.find(By.XPATH, '(//h4[@class="card-title"])[4]').text
        periodo = "01/01/2024 - 31/12/2024"

        self.assertEqual(clienti, "I 20 clienti TOP per il periodo: "+periodo)
        self.assertEqual(articoli, "I 20 articoli più venduti per il periodo: "+periodo)

        numero_interventi = self.find(By.XPATH, '(//h4[@class="card-title"])[5]').text
        self.assertEqual(numero_interventi, "Numero interventi per tipologia")

        ore_interventi = self.find(By.XPATH, '(//h4[@class="card-title"])[6]').text
        self.assertEqual(ore_interventi, "Ore interventi per tipologia")

        ore_tecnico = self.find(By.XPATH, '(//h4[@class="card-title"])[7]').text
        self.assertEqual(ore_tecnico, "Ore di lavoro per tecnico")

        anagrafiche = self.find(By.XPATH, '(//h4[@class="card-title"])[8]').text
        self.assertEqual(anagrafiche, "Nuove anagrafiche")