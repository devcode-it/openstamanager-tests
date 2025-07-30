from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from common.Test import Test, get_html

class AccountEmail(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Gestione email")

    def test_creazione_accountemail(self):
        # Creazione account email   *Required* 
        self.creazione_account_email("Account di Prova da Eliminare", self.getConfig('tests.email_user'), self.getConfig('tests.email_user'))

        # Modifica account email
        self.modifica_account_email(self.getConfig('tests.email_user'), "smtps.aruba.it", "465")

        # Cancellazione account email
        self.elimina_account_email()

        # Verifica account email
        self.verifica_account_email()

        # Invia mail (Azioni di gruppo) da Attività
        self.invia_mail()

    def creazione_account_email(self, nomeaccount = str, nomevisualizzato = str, emailmittente = str):
        self.navigateTo("Account email")

        self.find(By.XPATH,'//i[@class="fa fa-plus"]').click()
        modal = self.wait_modal()

        self.input(modal, 'Nome account').setValue(nomeaccount)
        self.input(modal, 'Nome visualizzato').setValue(nomevisualizzato)
        self.input(modal, 'Email mittente').setValue(emailmittente)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()

    def modifica_account_email(self, emailmittente:str, server:str, porta:str):
                self.navigateTo("Account email")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome-account"]/input'))).send_keys('Account Email da Impostazioni', Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.input(None, 'Email mittente').setValue(emailmittente)
        self.input(None, 'Server SMTP').setValue(server)
        self.input(None, 'Porta SMTP').setValue(porta)

        self.find(By.XPATH, '//div[@id="tab_0"]//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Account email")
        self.wait_loader()    

        self.find(By.XPATH, '//th[@id="th_Nome-account"]/i[@class="deleteicon fa fa-times"]').click()

    def elimina_account_email(self):
                self.navigateTo("Account email")
        self.wait_loader()    

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome-account"]/input'))).send_keys('Account di Prova da Eliminare', Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td[2]')
        
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]'))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]'))).click()
        self.wait_loader()

        self.find(By.XPATH, '//th[@id="th_Nome-account"]/i[@class="deleteicon fa fa-times"]').click()

        
    def verifica_account_email(self):
                self.navigateTo("Account email")
        self.wait_loader()    

        # Verifica elemento modificato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome-account"]/input'))).send_keys("Account email da Impostazioni", Keys.ENTER)

        modificato = self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[3]').text
        self.assertEqual("Account email da Impostazioni", modificato)
        self.find(By.XPATH, '//i[@class="deleteicon fa fa-times"]').click()

        # Verifica elemento eliminato
        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome-account"]/input'))).send_keys("Account di Prova da Eliminare", Keys.ENTER)
        
        eliminato = self.driver.find_element(By.XPATH,'//tbody//tr[1]//td[@class="dataTables_empty"]').text
        self.assertEqual("La ricerca non ha portato alcun risultato.", eliminato)

        self.find(By.XPATH, '//th[@id="th_Nome-account"]/i[@class="deleteicon fa fa-times"]').click()

    def invia_mail(self):
                self.navigateTo("Account email")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome-account"]/input'))).send_keys("Account email", Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.find(By.XPATH, '//span[@id="select2-encryption-container"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("SSL", Keys.ENTER)

        self.input(None, 'Password SMTP').setValue(self.getConfig('tests.email_password'))

        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Anagrafiche")
        self.wait_loader()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))).send_keys("Cliente", Keys.ENTER)

        self.wait_for_element_and_click('//tbody//tr//td[2]')

        self.input(None, 'Email').setValue(self.getConfig('tests.email_user'))
        self.find(By.XPATH, '//button[@id="save"]').click()
        self.wait_loader()

        self.navigateTo("Attività")
        self.wait_loader()

        self.wait_for_element_and_click('//tbody//tr//td') 
        self.find(By.XPATH, '//button[@data-toggle="dropdown"]').click()

        self.find(By.XPATH, '//a[@data-op="send-mail"]').click()

        self.find(By.XPATH, '//span[@id="select2-id_template-container"]').click() 
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys("rapportino")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="select2-search__field"]'))).send_keys(Keys.ENTER)
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-warning"]').click()  
        self.wait_loader()

        scritta = self.find(By.XPATH, '//tbody//tr//td[14]').text 
        self.assertEqual(scritta, "Inviata via email")

        
