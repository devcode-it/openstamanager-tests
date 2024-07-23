from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Impostazioni(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")

    def test_impostazioni(self):
        self.cifre_decimali_importi()
        self.valuta()
        self.periodo_calendario()
        self.lingua()

    def cifre_decimali_importi(self):
        wait = WebDriverWait(self.driver, 20)
        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting47-container"]').click()    #seleziono 4 cifre decimali per gli importi
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('4', Keys.ENTER)
        sleep(1)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '//button[@class="btn btn-primary bound clickable"]').click()   #click su +
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-idanagrafica_add-container"]').click() #seleziono Cliente come anagrafica
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("Cliente", Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click() #click su aggiungi
        self.wait_loader()

        self.find(By.XPATH, '//span[@id="select2-id_articolo-container"]').click()  #aggiungo un articolo
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Articolo 1')
        sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="btn btn-primary tip tooltipstered"]').click() #click su aggiungi
        sleep(1)

        importo=self.find(By.XPATH, '//tbody//tr[1]//td[9]').text   #controllo se l'importo corrisponde a 20 euro con 4 cifre decimali
        self.assertEqual(importo, "20,0000 €")

        self.find(By.XPATH, '//a[@id="elimina"]').click() #elimina fattura
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting47-container"]').click()    #seleziono 2 cifre decimali per gli importi
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('2', Keys.ENTER)
        sleep(1)

    def valuta(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting83-container"]').click() #cambio valuta in sterline
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Sterlina', Keys.ENTER)
        sleep(1)

        self.expandSidebar("Vendite")
        self.navigateTo("Fatture di vendita")
        self.wait_loader()

        self.find(By.XPATH, '(//tr[1]//td[2])[2]').click() #apro prima fattura
        self.wait_loader()

        nuova_valuta=self.find(By.XPATH, '//tbody//tr[1]//td[5]//div//span').text   #controllo se è cambiata la valuta
        self.assertEqual(nuova_valuta, "£")
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting83-container"]').click() #cambio valuta in euro
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Euro', Keys.ENTER)
        sleep(1)

    def periodo_calendario(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//input[@id="setting135"]').click()
        data_inizio=self.find(By.XPATH, '//input[@id="setting135"]') #cambio inizio periodo
        data_inizio.clear()
        data_inizio.send_keys("01/01/2024", Keys.ENTER)
        self.find(By.XPATH, '//input[@id="setting135"]').click()
        data_fine=self.find(By.XPATH, '//input[@id="setting136"]') #cambio fine periodo
        data_fine.clear()
        data_fine.send_keys("30/06/2024", Keys.ENTER)
        sleep(2)

        self.find(By.XPATH, '//a[@class="nav-link bg-danger"]').click() #logout
        self.wait_loader()
        sleep(2)

        #login
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys('admin')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys('') #password da mettere prima del test
        self.find(By.XPATH, '//button[@class="btn btn-danger btn-block btn-flat"]').click() 
        sleep(2)
        self.wait_loader()

        data=self.find(By.XPATH, '//a[@class="nav-link text-danger"]').text #controllo se la data è cambiata
        self.assertEqual(data, "01/01/2024 - 30/06/2024")
        #torno alle impostazioni di prima
        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        data_inizio=self.find(By.XPATH, '//input[@id="setting135"]') #cambio inizio periodo
        data_inizio.clear()
        data_inizio.send_keys("01/01/2024", Keys.ENTER)
        data_fine=self.find(By.XPATH, '//input[@id="setting136"]') #cambio fine periodo
        data_fine.clear()
        data_fine.send_keys("31/12/2024", Keys.ENTER)
        self.find(By.XPATH, '//a[@class="nav-link bg-danger"]').click() #logout
        self.wait_loader()

        #login
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="form-control"]'))).send_keys('admin')
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))).send_keys('') #password da mettere prima del test
        self.find(By.XPATH, '//button[@class="btn btn-danger btn-block btn-flat"]').click() 
        sleep(2)
        self.wait_loader()

    def lingua(self):
        wait = WebDriverWait(self.driver, 20)  
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting199-container"]').click()   #metto la lingua in inglese
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('English')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.navigateTo("Anagrafiche")
        self.wait_loader() 

        scritta=self.find(By.XPATH, '(//li[@id="2"]//p)[1]').text   #controllo se ha cambiato lingua
        self.assertEqual(scritta, "Entities")
        #torno alle impostazioni di prima
        self.expandSidebar("Tools")
        self.navigateTo("Settings")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-11"]').click() #apro Generali
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-setting199-container"]').click()   #metto la lingua in italiano
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys('Italiano')
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.navigateTo("Settings")
        self.wait_loader()
        sleep(2)



        

