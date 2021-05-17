from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from common.Test import Test


class Init(Test):
    def setUp(self):
        # Inizializza l'ambiente di test
        super().setUp()

        self.connect()

    def test_config(self):
        # Pulsante "Successivo"
        self.wait(expected_conditions.visibility_of_element_located(
            (By.XPATH, '// *[ @ id = "smartwizard"] / div[2] / div / button[2]')))
        self.find(By.XPATH, '// *[ @ id = "smartwizard"] / div[2] / div / button[2]').click()

        # Accettazione della licenza
        self.find(By.XPATH, '// *[ @ id = "agree"]').click()

        # Pulsante "Successivo"
        self.find(By.XPATH, '// *[ @ id = "smartwizard"] / div[2] / div / button[2]').click()

        # Completamento dei campi per il nuovo elemento
        self.input(None, "Host del database").setValue(self.getConfig('database.host'))
        self.input(None, "Username dell'utente MySQL").setValue(self.getConfig('database.user'))
        self.input(None, "Password dell'utente MySQL").setValue(self.getConfig('database.pass'))
        self.input(None, "Nome del database").setValue(self.getConfig('database.name'))

        # Salvataggio della configurazione
        self.find(By.XPATH, '// *[ @ id = "install"]').click()
        self.wait(expected_conditions.visibility_of_element_located(
            (By.ID, 'contine_button')))

        # Avvio installazione database
        self.find(By.XPATH, '// *[ @ id = "contine_button"]').click()
        self.find(By.XPATH, '/ html / body / div[2] / div / div[10] / button[1]').click()

        # Attesa del pulsante "Continua"  (fine installazione)
        self.wait(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[@id="result"]/a')), 300)
        self.find(By.XPATH, '//*[@id="result"]/a').click()

        # Inizializzazione di base
        self.input(None, 'Username').setValue(self.getConfig('login.username'))
        self.input(None, 'Password').setValue(self.getConfig('login.password'))
        self.input(None, 'Email').setValue(self.getConfig('login.username') + '@test.com')
        self.input(None, 'Denominazione').setValue("Azienda")
        self.input(None, 'Regime Fiscale').setByText("Ordinario")
        self.input(None, 'Conto predefinito fatture di vendita').setByText("000010 - Ricavi merci c/to vendite")
        self.input(None, 'Conto predefinito fatture di acquisto').setByText("000010 - Costi merci c/acquisto di rivendita")
        self.input(None, 'Valuta').setByText("Euro - €")

        self.find(By.XPATH, '//*[@id="config"]').click()
