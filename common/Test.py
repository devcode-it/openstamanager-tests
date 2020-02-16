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
        browser = None
        if (self.getConfig('browser') == 'firefox'):
            browser = webdriver.Firefox()
        elif (self.getConfig('browser') == 'chrome'):
            browser = webdriver.Chrome()

        self.browser = browser
        self.browser.get(self.getConfig('server'))

        self.addCleanup(self.close)
        
        self.assertIn('OpenSTAManager', self.browser.title)

    def login(self, username, password):
        ''' Effetta il login con le credenziali indicate nella configurazione.'''
        username_input = webfind(self.browser, {'name': 'username'})
        password_input = webfind(self.browser, {'name': 'password'})

        username_input.send_keys(username)
        password_input.send_keys(password)

        button = webfind(self.browser, {'id': 'login'})
        button.click()

    def close(self):
        self.browser.quit()

    def setUp(self):
        self.connect()
        self.login(self.getConfig('login.username'), self.getConfig('login.password'))

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
        try:
            condition = expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'sidebar'))
            self.wait(condition)

            elements = webfind(self.browser, {'css': '.treeview>a'})
            for e in elements:
                text = get_text(e)
                if (text == name):
                    e.click()
        except NoAlertPresentException:
            None
        except UnexpectedAlertPresentException:
            None

    def wait(self, condition):
        ''' Attende un evento specifico con timeout di 60 secondi.'''
        WebDriverWait(self.browser, 60).until(condition)

    def getConfig(self, name):
        ''' Restituisce il contenuto dell'impostazione richiesta.'''
        return self.config[name]

def get_html(element: WebElement):
    ''' Restituisce il contenuto HTML di un WebElement.'''
    return element.get_attribute('innerHTML')

def get_text(element: WebElement):
    ''' Restituisce il testo di un WebElement.'''
    return re.sub('<[^<]+?>', '', get_html(element)).strip()

def webfind(element, data: dict):
    ''' Ricerca un WebElement nell'elemento indicato secondo i dati forniti.'''
    result = None

    if ('id' in data):
        result = element.find_element_by_id(data['id'])
    elif ('name' in data):
        result = element.find_element_by_name(data['name'])
    elif ('css' in data):
        result = element.find_elements_by_css_selector(data['css'])
    elif ('tag' in data):
        result = element.find_elements_by_tag_name(data['tag'])
    elif ('link' in data):
        result = element.find_elements_by_link_text(data['link'])
    elif ('xpath' in data):
        result = element.find_elements_by_xpath(data['xpath'])

    return result

if __name__ == '__main__':
    unittest.main()