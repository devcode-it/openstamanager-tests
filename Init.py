from selenium.webdriver.support import expected_conditions

from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Init(Test):
    def setUp(self):
        # Inizializza l'ambiente di test
        super().setUp()

        self.connect()

    def test_config(self):
        # Pulsante "Successivo"
        self.find(By.XPATH, '// *[ @ id = "smartwizard"] / div[2] / div / button[2]').click()

        # Accettazione della licenza
        self.find(By.XPATH, '// *[ @ id = "agree"]').click()

        # Pulsante "Successivo"
        self.find(By.XPATH, '// *[ @ id = "smartwizard"] / div[2] / div / button[2]').click()

        # Completamento dei campi per il nuovo elemento
        self.input(None, 'Host').setValue("localhost")
        self.input(None, "Username dell'utente MySQL").setValue("root")
        self.input(None, "Password dell'utente MySQL").setValue("")
        self.input(None, "Nome del database").setValue("osm")

        # Salvataggio della configurazione
        self.find(By.XPATH, '// *[ @ id = "install"]').click()
        self.wait_loader();

        # Avvio installazione database
        self.find(By.XPATH, '// *[ @ id = "contine_button"]').click()
        self.find(By.XPATH, '/ html / body / div[2] / div / div[10] / button[1]').click()

        self.wait(expected_conditions.visibility_of_element_located(
            (By.ID, 'result')))
        self.find(By.XPATH, '//*[@id="result"]/a').click()
        self.wait_loader()

        # Inizializzazione di base
        self.input(None, 'Username').setValue(self.getConfig('login.username'))
        self.input(None, 'Password').setValue(self.getConfig('login.password'))
        self.input(None, 'Email').setValue(self.getConfig('login.username') + '@test.com')
        self.input(None, 'Denominazione').setValue("Azienda")
        self.input(None, 'Regime Fiscale').setValue("Ordinario")
        self.input(None, 'Conto predefinito fatture di vendita').setValue("000010 - Ricavi merci c/to vendite")
        self.input(None, 'Conto predefinito fatture di acquisto').setValue("000010 - Costi merci c/acquisto di rivendita")
        self.input(None, 'Valuta').setValue("Euro - €")

        self.find(By.XPATH, '//*[@id="config"]').click()
        self.wait_loader()



