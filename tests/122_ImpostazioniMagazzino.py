from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Impostazioni(Test):
    def setUp(self):
        super().setUp()

    def test_impostazioni_magazzino(self):
        return True
        ## TODO: Movimenta il magazzino durante l'inserimento o eliminazione dei lotti/serial number

        # Serial number abilitato di default 
        #self.serial_abilitato_default()

        ## TODO: Magazzino cespiti

    def serial_abilitato_default(self):
                self.expandSidebar("Magazzino")
        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click() #click su +

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione"]'))).send_keys("test") #descrizione
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su aggiungi
        self.wait_loader()

        serial = self.find(By.XPATH, '(//label[@class="btn btn-default active"]//span)[2]').text
        self.assertEqual(serial, "Disattivato")
        #elimino articolo
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()

        self.navigateTo("Impianti") #aggiunto perchè non riesce ad entrare in impostazioni dato che non è visibile quando il sidebar magazzino è aperto
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-12"]').click() #apro Magazzino

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[2]').click()   #attiva impostazione

        self.expandSidebar("Magazzino")
        self.navigateTo("Articoli")
        self.wait_loader()

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click() #click su +

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id="descrizione"]'))).send_keys("test") #descrizione
        self.find(By.XPATH, '//button[@class="btn btn-primary"]').click()   #click su aggiungi
        self.wait_loader()

        serial = self.find(By.XPATH, '(//label[@class="btn btn-default active"]//span)[1]').text
        self.assertEqual(serial, "Attivato")
        #elimino articolo
        self.find(By.XPATH, '//a[@class="btn btn-danger ask"]').click()

        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()
        #torno alle impostazioni di prima
        self.navigateTo("Impianti") #aggiunto perchè non riesce ad entrare in impostazioni dato che non è visibile quando il sidebar magazzino è aperto
        self.wait_loader()

        self.expandSidebar("Strumenti")
        self.navigateTo("Impostazioni")
        self.wait_loader()

        self.find(By.XPATH, '//div[@id="impostazioni-12"]').click() #apro Magazzino

        self.find(By.XPATH, '(//label[@class="btn btn-default active"])[2]').click()   #disattiva impostazione
