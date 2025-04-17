from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoAlertPresentException,
    UnexpectedAlertPresentException,
    TimeoutException,
    NoSuchElementException,
    StaleElementReferenceException
)
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options as ChromeOptions

from .functions import get_config
from .Input import Input

import collections.abc
import unittest
import re
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('test_execution.log')
    ]
)

class Test(unittest.TestCase):
    def __init__(self, methodName):
        super().__init__(methodName)
        config = get_config()
        self.config = self.__flatten(config)
        self.logger = logging.getLogger(self.__class__.__name__)

    def connect(self):
        self.logger.info(f"Initializing {self.getConfig('browser')} browser")

        try:
            driver = None
            browser_type = self.getConfig('browser').lower()
            headless = self.getConfig('headless')

            if browser_type == 'firefox':
                options = Options()
                if headless:
                    options.add_argument('--headless')
                driver = webdriver.Firefox(options=options)
            elif browser_type == 'chrome':
                options = ChromeOptions()
                if headless:
                    options.add_argument('--headless')
                driver = webdriver.Chrome(options=options)
            else:
                self.logger.error(f"Unsupported browser type: {browser_type}")
                raise ValueError(f"Unsupported browser type: {browser_type}")

            self.driver = driver
            self.driver.get(self.getConfig('server'))
            self.driver.maximize_window()

            self.logger.info(f"Connected to {self.getConfig('server')}")
            self.addCleanup(self.close)
        except Exception as e:
            self.logger.error(f"Failed to initialize browser: {str(e)}")
            raise

    def login(self, username, password):
        self.logger.info(f"Logging in as {username}")

        try:
            username_input = self.find(By.NAME, 'username')
            username_input.clear()
            username_input.send_keys(username)

            password_input = self.find(By.NAME, 'password')
            password_input.clear()
            password_input.send_keys(password)

            self.find(By.XPATH, '//button[@type="submit"]').click()

            self.wait_loader()
            self.logger.info("Login successful")
        except Exception as e:
            self.logger.error(f"Login failed: {str(e)}")
            raise

    def close(self):
        if hasattr(self, 'driver'):
            self.logger.info("Closing browser")
            self.driver.quit()

    def setUp(self, login=True):
        super().setUp()
        self.logger.info("Setting up test environment")

        self.connect()

        if login:
            self.login(
                self.getConfig('login.username'),
                self.getConfig('login.password')
            )

    def __flatten(self, d, parent_key='', sep='.'):
        items = []
        for k, v in d.items():
            new_key = parent_key + sep + k if parent_key else k
            if isinstance(v, collections.abc.MutableMapping):
                items.extend(self.__flatten(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    def navigateTo(self, name):
        self.logger.info(f"Navigating to module: {name}")

        try:
            condition = EC.visibility_of_element_located((By.CLASS_NAME, 'sidebar'))
            self.wait(condition)

            xpath = f'//a[contains(., "{name}")]'
            element = self.find(By.XPATH, xpath)

            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            element.click()

            self.wait_loader()
            self.logger.info(f"Successfully navigated to {name}")
        except Exception as e:
            self.logger.error(f"Failed to navigate to {name}: {str(e)}")
            raise

    def expandSidebar(self, name: str):
        self.logger.info(f"Expanding sidebar section: {name}")

        try:
            xpath = f'//a[contains(., "{name}")]//i[contains(@class, "fa-angle-left")]'
            expand_icon = self.find(By.XPATH, xpath)

            expand_icon.click()

            # Wait for the menu to expand by checking for the class change
            self.wait(EC.presence_of_element_located((By.XPATH, f'//a[contains(., "{name}")]/parent::li[contains(@class, "menu-open")]')), 2)
            self.logger.info(f"Expanded sidebar section: {name}")
        except NoSuchElementException:
            self.logger.warning(f"Sidebar section '{name}' not found or already expanded")
        except Exception as e:
            self.logger.error(f"Failed to expand sidebar section '{name}': {str(e)}")
            raise

    def find(self, by=By.ID, value=None):
        try:
            return self.driver.find_element(by, value)
        except NoSuchElementException:
            self.logger.error(f"Element not found: {by}={value}")
            raise

    def find_elements(self, by=By.ID, value=None):
        return self.driver.find_elements(by, value)

    def wait_loader(self):
        self.logger.debug("Waiting for page to load")
        try:
            self.wait(EC.all_of(
                EC.invisibility_of_element_located((By.ID, 'main_loading')),
                EC.invisibility_of_element_located((By.ID, 'mini-loader')),
                EC.invisibility_of_element_located((By.ID, 'tiny-loader')),
            ))
            self.logger.debug("Page loaded successfully")
        except TimeoutException:
            self.logger.warning("Timeout waiting for page to load")

    def wait_modal(self):
        self.logger.debug("Waiting for modal dialog")
        try:
            self.wait(EC.visibility_of_element_located(
                (By.CLASS_NAME, 'modal-dialog')))

            modal = self.find_elements(By.CSS_SELECTOR, '.modal')[-1]
            self.logger.debug("Modal dialog appeared")
            return modal
        except TimeoutException:
            self.logger.error("Timeout waiting for modal dialog")
            raise
        except IndexError:
            self.logger.error("No modal found after waiting")
            raise NoSuchElementException("No modal found after waiting")

    def wait(self, condition, timeout=20):
        try:
            WebDriverWait(self.driver, timeout).until(condition)
        except TimeoutException:
            self.logger.warning(f"Timeout after {timeout}s waiting for condition")
            raise

    def getConfig(self, name):
        try:
            return self.config[name]
        except KeyError:
            self.logger.error(f"Configuration setting not found: {name}")
            raise KeyError(f"Configuration setting not found: {name}")

    def input(self, element=None, name=None, css_id=None):
        try:
            if not element:
                element = self.find(By.XPATH, '//body')

            return Input.find(self.driver, element, name, css_id)
        except Exception as e:
            self.logger.warning(f"Failed to find input {name or css_id}: {str(e)}")
            return None


def get_html(element: WebElement):
    return element.get_attribute('innerHTML')


def get_text(element: WebElement):
    return re.sub('<[^<]+?>', '', get_html(element)).strip()


if __name__ == '__main__':
    unittest.main()
