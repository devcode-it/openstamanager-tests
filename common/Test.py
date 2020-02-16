from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoAlertPresentException, UnexpectedAlertPresentException
from .functions import get_config
import collections
import unittest
import re


class Test(unittest.TestCase):
    def __init__(self, methodName):
        super().__init__(methodName)

        config = get_config()
        self.config = self.__flatten(config)

    def connect(self):
        ''' Inizializza il browser indicato nella configurazione.'''
        driver = None
        if (self.getConfig('browser') == 'firefox'):
            driver = webdriver.Firefox()
        elif (self.getConfig('browser') == 'chrome'):
            driver = webdriver.Chrome()

        self.driver = driver
        self.driver.get(self.getConfig('server'))

        self.addCleanup(self.close)

        self.assertIn('OpenSTAManager', self.driver.title)

    def login(self, username, password):
        ''' Effetta il login con le credenziali indicate nella configurazione.'''
        username_input = self.find(By.NAME, 'username')
        username_input.send_keys(username)

        password_input = self.find(By.NAME, 'password')
        password_input.send_keys(password)

        self.find(By.ID, 'login').click()
        self.wait_loader()

    def close(self):
        ''' Chiude il test.'''
        self.driver.quit()
        None

    def setUp(self):
        ''' Inizializza l'ambiente di test.'''
        super().setUp()

        self.connect()
        self.login(self.getConfig('login.username'),
                   self.getConfig('login.password'))

    # Source: https://stackoverflow.com/a/6027615
    def __flatten(self, d, parent_key='', sep='.'):
        items = []
        for k, v in d.items():
            new_key = parent_key + sep + k if parent_key else k
            if isinstance(v, collections.MutableMapping):
                items.extend(self.__flatten(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    def navigateTo(self, name):
        ''' Naviga attraverso la sidebar principale per accedere al modulo di cui viene indicato il nome.'''
        condition = expected_conditions.element_to_be_clickable(
            (By.CLASS_NAME, 'sidebar'))
        self.wait(condition)

        # URL pagina corrente
        current_url = self.driver.current_url

        xpath = ''.join(['//a[contains(., "', name, '")]'])
        link = self.find(By.XPATH, xpath)

        try:
            link.click()

            self.driver.switch_to.alert.accept()  # Gestione eventuali alert
        except (NoAlertPresentException, UnexpectedAlertPresentException):
            None

        self.wait_loader()
        self.driver.implicitly_wait(15)

    def expandSidebar(self, name: str):
        xpath = ''.join(
            ['//a[contains(., "', name, '")]//span[contains(@class, "pull-right-container")]'])

        self.find(By.XPATH, xpath).click()

    def find(self, by=By.ID, value=None):
        ''' Ricerca una componente HTML nella pagina.'''
        return self.driver.find_element(by, value)

    def find_elements(self, by=By.ID, value=None):
        ''' Ricerca una serie di componenti HTML nella pagina.'''
        return self.driver.find_elements(by, value)

    def input(self, name: str):
        ''' Ricerca un input HTML nella pagina.'''
        return get_input(self.driver, name)

    def wait_loader(self):
        ''' Attende il completamento del caricamento della pagina, visibile attraverso il loader principale.'''
        self.wait(expected_conditions.invisibility_of_element_located(
            (By.ID, 'main_loading')))

    def wait_modal(self):
        ''' Attende il caricamento del modal e ne restituisce un riferimento.'''
        self.wait(expected_conditions.visibility_of_element_located(
            (By.CLASS_NAME, 'modal')))

        return self.find_elements(By.CSS_SELECTOR, '.modal')[-1]

    def wait(self, condition):
        ''' Attende un evento specifico con timeout di 60 secondi.'''
        WebDriverWait(self.driver, 60).until(condition)

    def getConfig(self, name):
        ''' Restituisce il contenuto dell'impostazione richiesta.'''
        return self.config[name]

    def setValue(self, element: WebElement, value: str):
        ''' Imposta il valore del campo indicato.'''
        self.driver.execute_script(
            '$(".inputmask-decimal").inputmask("remove");')

        element.clear()
        element.send_keys(value)


def get_html(element: WebElement):
    ''' Restituisce il contenuto HTML di un WebElement.'''
    return element.get_attribute('innerHTML')


def get_text(element: WebElement):
    ''' Restituisce il testo di un WebElement.'''
    return re.sub('<[^<]+?>', '', get_html(element)).strip()


def get_input(element, name: str):
    element_id = element.get_attribute("id")

    if element_id:
        xpath = ['//*[@id="', element_id, '"]//label[contains(., "', name, '")]/parent::div/parent::div//input | //*[@id="',
                 element_id, '"]//label[contains(., "', name, '")]/parent::div/parent::div//textarea']
    else:
        xpath = ['//label[contains(., "', name, '")]/parent::div/parent::div//input | //label[contains(., "',
                 name, '")]/parent::div/parent::div//textarea']

    return element.find_element(By.XPATH, ''.join(xpath))


if __name__ == '__main__':
    unittest.main()
