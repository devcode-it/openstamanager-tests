from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from common.Test import Test, get_html


class AccountEmail(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Gestione email")


    def test_creazione_accountemail(self):
        # Creazione account email   *Required* 
        self.creazione_account_email("Account di Prova da Modificare", self.getConfig('tests.email_user'), self.getConfig('tests.email_user'))
        self.creazione_account_email("Account di Prova da Eliminare", self.getConfig('tests.email_user'), self.getConfig('tests.email_user'))

        # Modifica account email
        self.modifica_account_email("Account Email", "smtps.aruba.it", "465")

        # Cancellazione account email
        self.elimina_account_email()

        # Verifica account email
        self.verifica_account_email()

        # Invia mail (Azioni di gruppo) da Attività
        self.invia_mail()

    def creazione_account_email(self, nomeaccount=str, nomevisualizzato=str, emailmittente=str):
        self.navigateTo("Account email")

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        self.input(modal, 'Nome account').setValue(nomeaccount)
        self.input(modal, 'Nome visualizzato').setValue(nomevisualizzato)
        self.input(modal, 'Email mittente').setValue(emailmittente)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

    def modifica_account_email(self, modifica:str, server:str, porta:str):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Account email")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome-account"]/input'))).send_keys('Account di Prova da Modificare', Keys.ENTER)        
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        self.wait_loader()
        
        self.input(None,'Nome account').setValue(modifica)
        self.input(None, 'Server SMTP').setValue(server)
        self.input(None, 'Porta SMTP').setValue(porta)

        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Account email")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Nome-account"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

    def elimina_account_email(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Account email")
        self.wait_loader()    

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome-account"]/input'))).send_keys('Account di Prova da Eliminare', Keys.ENTER)        
        sleep(1)

        self.find(By.XPATH, '//tbody//tr//td[2]').click()
        sleep(1)
        
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Nome-account"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2)
        
    def verifica_account_email(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Account email")
        self.wait_loader()    

        #verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome-account"]/input'))).send_keys("Account Email", Keys.ENTER)
        sleep(1)

        modificato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[3]').text
        self.assertEqual("Account Email",modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

        #verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome-account"]/input'))).send_keys("Account di Prova da Eliminare", Keys.ENTER)
        sleep(1)
        
        eliminato=self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.",eliminato)

        self.find(By.XPATH, '//th[@id="th_Nome-account"]/i[@class="deleteicon fa fa-times"]').click()
        sleep(2)

    def invia_mail(self):
        wait = WebDriverWait(self.driver, 20)
        self.navigateTo("Account email")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome-account"]/input'))).send_keys("Account email", Keys.ENTER)  #cerco account mail numero 1
        sleep(1)

        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()
        self.wait_loader()

        #sicurezza smpt
        self.find(By.XPATH, '//span[@id="select2-encryption-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("SSL", Keys.ENTER)

        #password smpt
        self.input(None, 'Password SMTP').setValue(self.getConfig('tests.email_password'))

        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Anagrafiche")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//tbody//td[2]//div[1]').click()   #aggiungo email a "Cliente"
        sleep(1)

        self.input(None, 'Email').setValue(self.getConfig('tests.email_user'))
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Attività")
        self.wait_loader()

        self.find(By.XPATH, '//tbody//tr//td').click() #seleziono attività 
        self.find(By.XPATH, '//button[@class="btn btn-primary btn-lg dropdown-toggle dropdown-toggle-split"]').click() #apro azioni di gruppo
        sleep(1)

        self.find(By.XPATH, '//a[@data-op="send-mail"]').click()
        sleep(1)

        self.find(By.XPATH, '//span[@id="select2-id_template-container"]').click()  #scelgo il template
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("rapportino")
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  #invio email
        self.wait_loader()

        scritta=self.find(By.XPATH, '(//tr[1]//td[14]//div)[2]').text   #controllo se l'email è stata inviata
        self.assertEqual(scritta, "Inviata via email")


        
