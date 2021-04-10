from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select as WebSelect
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Input:
    def __init__(self, driver, element):
        self.driver = driver
        self.element = element

        self.element_id = self.element.get_attribute("id")

    def setValue(self, value: str):
        self.element.clear()
        self.element.click()
        self.element.send_keys(value)

    @staticmethod
    def xpath(element, name=None, css_selector=None):
        ''' Restituisce il percorso xPath responsabile per la gestione dell'input indicato.'''
        element_id = element.get_attribute("id")

        prefix = ''
        if element_id:
            prefix = '//*[@id="' + element_id + '"]'
        
        if name:
            prefix += '//label[contains(., "' + name + '")]/parent::div/parent::div//'
        else:
            prefix += '//' + css_selector

        return prefix

    @staticmethod
    def find(driver, element, name=None, css_selector=None):
        ''' Restituisce l'oggetto responsabile per la gestione dell'input indicato.'''
        prefix = Input.xpath(element, name, css_selector)

        # Ricerca dei select (Select2)
        xpath = prefix + 'select'
        try:
            select = element.find_element(By.XPATH, xpath)

            return Select(driver, select)
        except NoSuchElementException:
            pass

        # Ricerca degli input normali
        xpath = prefix + 'input'
        try:
            normal_input = element.find_element(By.XPATH, xpath)

            return Input(driver, normal_input)
        except NoSuchElementException:
            pass

        # Ricerca degli input di tipo textarea
        xpath = prefix + 'textarea'
        try:
            textarea = element.find_element(By.XPATH, xpath)

            return Input(driver, textarea)
        except NoSuchElementException:
            pass

        return None


class Select(Input):
    def __init__(self, driver, element):
        super().__init__(driver, element)

        self.select_element = WebSelect(element)

    def setValue(self, value: str):
        self.driver.execute_script(
            '$("#' + self.element_id + '").select2("destroy");')

        self.select_element.select_by_value(value)

    def setByText(self, value: str):
        self.driver.execute_script(
            '$("#' + self.element_id + '").select2("open");')

        # Attesa del caricamento
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'select2-results__option')))

        item = self.driver.find_element(By.XPATH, '//ul[@class="select2-results__options"]/li[contains(., "' + value + '")]')
        item.click()

    def setByIndex(self, value: str):
        self.driver.execute_script(
            '$("#' + self.element_id + '").select2("open");')

        # Attesa del caricamento
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'select2-results__option')))

        item = self.driver.find_element(By.XPATH, '//ul([@class="select2-results__options"]/li[' + (value + 1) + '')
        item.click()
