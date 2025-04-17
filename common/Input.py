from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select as WebSelect
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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
        element_id = element.get_attribute("id")

        prefix = ''
        if element_id:
            prefix = '//*[@id="' + element_id + '"]'

        if name:
            prefix += '//label[contains(., "' + name + '")]/parent::div/parent::div//'
        elif css_selector:
            prefix += '//' + css_selector

        return prefix

    @staticmethod
    def find(driver, element, name=None, css_selector=None):
        prefix = Input.xpath(element, name, css_selector)

        element_types = [
            {'xpath': prefix + 'select', 'class': Select},
            {'xpath': prefix + 'input[@type="checkbox"]', 'class': Checkbox},
            {'xpath': prefix + 'input', 'class': Input},
            {'xpath': prefix + 'textarea', 'class': Input}
        ]

        for elem_type in element_types:
            try:
                found_element = element.find_element(By.XPATH, elem_type['xpath'])
                return elem_type['class'](driver, found_element)
            except NoSuchElementException:
                continue

        return None


class Select(Input):
    def __init__(self, driver, element):
        super().__init__(driver, element)
        self.select_element = WebSelect(element)

    def setValue(self, value: str):
        try:
            self.driver.execute_script(
                '$("#' + self.element_id + '").select2("destroy");')
            self.select_element.select_by_value(value)
        except Exception as e:
            raise Exception(f"Failed to set value '{value}' on select element: {str(e)}")

    def setByText(self, value: str):
        try:
            self.driver.execute_script(
                '$("#' + self.element_id + '").select2("open");')

            xpath = f'//ul[@class="select2-results__options"]/li[contains(., "{value}") and not (contains(@class, "loading-results"))][1]'
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))

            item = self.driver.find_element(By.XPATH, xpath)
            item.click()
        except TimeoutException:
            raise Exception(f"Timeout waiting for select option with text '{value}'")
        except Exception as e:
            raise Exception(f"Failed to select option with text '{value}': {str(e)}")

    def setByIndex(self, index: int):
        try:
            index_str = str(index)

            self.driver.execute_script(
                '$("#' + self.element_id + '").select2("open");')

            base_xpath = '//ul[@class="select2-results__options"]/li[not (contains(@class, "loading-results"))]'
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, f'{base_xpath}[1]')))

            item = self.driver.find_element(By.XPATH, f'{base_xpath}[{index_str}]')
            item.click()
        except TimeoutException:
            raise Exception(f"Timeout waiting for select options to load")
        except Exception as e:
            raise Exception(f"Failed to select option at index {index}: {str(e)}")

class Checkbox(Input):
    def __init__(self, driver, element):
        super().__init__(driver, element)
        self.checkbox_element = element

    def setValue(self, value: bool):
        current_state = self.checkbox_element.is_selected()
        if current_state != value:
            self.clickFlag()

    def clickFlag(self):
        try:
            self.checkbox_element.find_element(By.XPATH, './/following-sibling::div/label[contains(@class, "active")]').click()
        except NoSuchElementException:
            self.checkbox_element.click()
        except Exception as e:
            raise Exception(f"Failed to click checkbox: {str(e)}")