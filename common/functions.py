from argparse import ArgumentParser
from pathlib import Path
import os
import glob
import string
import random
import json
import time
from typing import Dict, List, Optional, Callable, Union

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver, WebElement


class TestHelperMixin:
    """Mixin class that provides helper methods for Selenium tests.

    This mixin wraps the helper functions to avoid passing driver and wait_driver
    parameters repeatedly. It assumes the class has self.driver and self.wait_driver attributes.
    """

    def search_entity(self, name: str) -> None:
        """Search for an entity by name."""
        search_entity(self.driver, self.wait_driver, name)

    def click_first_result(self) -> None:
        """Click on the first result in the search results."""
        click_first_result(self.driver, self.wait_driver)

    def wait_for_filter_cleared(self) -> None:
        """Wait for filters to be cleared."""
        wait_for_filter_cleared(self.driver, self.wait_driver)

    def clear_filters(self) -> None:
        """Clear all filters."""
        clear_filters(self.driver, self.wait_driver)

    def wait_for_search_results(self) -> None:
        """Wait for search results to load."""
        wait_for_search_results(self.driver, self.wait_driver)

    def wait_for_element_and_click(self, selector: str, by: By = By.XPATH) -> WebElement:
        """Wait for an element to be clickable and click it."""
        return wait_for_element_and_click(self.driver, self.wait_driver, selector, by)

    def wait_for_dropdown_and_select(self, dropdown_xpath: str, option_xpath: str = None, option_text: str = None, by: By = By.XPATH) -> None:
        """Wait for a dropdown to be clickable, click it, and select an option."""
        wait_for_dropdown_and_select(self.driver, self.wait_driver, dropdown_xpath, option_xpath, option_text)

    def wait_loader(self) -> None:
        """Wait for all loaders to disappear."""
        wait_loader(self.driver, self.wait_driver)

    def send_keys_and_wait(self, element, text, wait_modal=True) -> None:
        """Send keys to an element and wait for the page to load after pressing Enter."""
        # Use the global function for consistency
        return send_keys_and_wait(self.driver, self.wait_driver, element, text, wait_modal)

    def send_keys_and_click(self, element, text, click_selector: str, by: By = By.XPATH) -> None:
        """Send keys to an element and click on a specified element instead of pressing Enter."""
        return send_keys_and_click(self.driver, self.wait_driver, element, text, click_selector, by)

    def wait_for_expanded_element(self, selector: str, by: By = By.XPATH) -> WebElement:
        """Wait for an element to be fully expanded and visible after an animation."""
        return wait_for_expanded_element(self.driver, self.wait_driver, selector, by)


def random_string(size: int = 32, chars: str = string.ascii_letters + string.digits) -> str:
    return ''.join(random.choice(chars) for _ in range(size))

def get_cache_directory() -> Path:
    current_dir = Path(__file__).parent
    cache_dir = current_dir.parent / 'cache'
    cache_dir.mkdir(exist_ok=True)
    return cache_dir

def get_config() -> Dict:
    config_file = get_cache_directory().parent / 'config.json'

    try:
        if config_file.exists():
            with config_file.open('r', encoding='utf-8') as f:
                return json.load(f)
    except json.JSONDecodeError:
        print(f"Errore nel parsing del file {config_file}")
    except Exception as e:
        print(f"Errore nella lettura del file {config_file}: {e}")

    return {}

def update_config(config: Dict) -> None:
    config_file = get_cache_directory().parent / 'config.json'

    try:
        with config_file.open('w+', encoding='utf-8') as f:
            json.dump(config, f, indent=4, sort_keys=True, ensure_ascii=False)
    except Exception as e:
        print(f"Errore nell'aggiornamento del file {config_file}: {e}")

def get_args() -> ArgumentParser:
    parser = ArgumentParser(description='Script di gestione test')
    parser.add_argument(
        "-a",
        "--action",
        dest="action",
        help="Imposta l'azione da eseguire",
        metavar="ACTION"
    )
    return parser.parse_args()

def list_files(path: str, include_hidden: bool = True) -> List[str]:
    path = Path(path)
    if not path.exists():
        return []

    files = glob.glob(str(path / '**' / '*'), recursive=True)

    if include_hidden:
        hidden_files = glob.glob(str(path / '**' / '.*'), recursive=True)
        files.extend(hidden_files)

    return sorted(files)

def safe_path_join(*paths: str) -> str:
    return os.path.normpath(os.path.join(*paths))

def ensure_directory(path: str) -> None:
    Path(path).mkdir(parents=True, exist_ok=True)


def search_entity(driver: WebDriver, wait_driver: WebDriverWait, name: str) -> None:
    try:
        clear_buttons = driver.find_elements(By.XPATH, '//i[@class="deleteicon fa fa-times"]')
        for button in clear_buttons:
            try:
                button.click()
                wait_driver.until(
                    EC.invisibility_of_element_located((By.XPATH, '//div[@class="select2-search select2-search--dropdown"]'))
                )
            except:
                pass
    except:
        pass

    search_input = wait_driver.until(
        EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Ragione-sociale"]/input'))
    )
    search_input.clear()
    search_input.send_keys(name, Keys.ENTER)

    time.sleep(1)


def click_first_result(driver: WebDriver, wait_driver: WebDriverWait) -> None:
    wait_loader(driver, wait_driver)

    try:
        wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[2]'))
        ).click()
        wait_loader(driver, wait_driver)
    except Exception as e:
        wait_loader(driver, wait_driver)
        wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[2]'))
        ).click()
        wait_loader(driver, wait_driver)


def wait_for_filter_cleared(driver: WebDriver, wait_driver: WebDriverWait) -> None:
    wait_driver.until(
        EC.invisibility_of_element_located((By.XPATH, '//div[@class="select2-search select2-search--dropdown"]'))
    )


def clear_filters(driver: WebDriver, wait_driver: WebDriverWait) -> None:
    try:
        wait_loader(driver, wait_driver)

        clear_buttons = driver.find_elements(By.XPATH, '//i[@class="deleteicon fa fa-times"]')

        if not clear_buttons:
            search_inputs = driver.find_elements(By.XPATH, '//th//input[not(@type="checkbox")]')
            for input_field in search_inputs:
                if input_field.get_attribute('value'):
                    input_field.clear()
                    input_field.send_keys(Keys.ENTER)
                    wait_loader(driver, wait_driver)
        else:
            for button in clear_buttons:
                try:
                    button.click()
                    wait_for_filter_cleared(driver, wait_driver)
                    wait_loader(driver, wait_driver)
                except:
                    pass

        wait_loader(driver, wait_driver)
    except Exception as e:
        print(f"Warning: Could not clear filters: {str(e)}")


class AnyOf:
    def __init__(self, *conditions):
        self.conditions = conditions

    def __call__(self, driver):
        for condition in self.conditions:
            try:
                if condition(driver):
                    return True
            except:
                pass
        return False

def wait_for_search_results(driver: WebDriver, wait_driver: WebDriverWait) -> None:
    wait_loader(driver, wait_driver)

    wait_driver.until(
        AnyOf(
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[2]')),
            EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[@class="dataTables_empty"]'))
        )
    )

    time.sleep(1)


def wait_for_element_and_click(driver: WebDriver, wait_driver: WebDriverWait, selector: str, by: By = By.XPATH) -> WebElement:
    wait_loader(driver, wait_driver)

    max_retries = 3
    for attempt in range(max_retries):
        try:
            wait_driver.until(EC.visibility_of_element_located((by, selector)))
            element = wait_driver.until(EC.element_to_be_clickable((by, selector)))
            try:
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
                time.sleep(0.5)
            except:
                pass
            element.click()
            wait_loader(driver, wait_driver)
            return element
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            wait_loader(driver, wait_driver)
            time.sleep(1)


def wait_for_dropdown_and_select(driver: WebDriver, wait_driver: WebDriverWait, dropdown_xpath: str, option_xpath: str = None, option_text: str = None) -> None:
    # Check if the desired option is already selected
    if option_text:
        try:
            dropdown_element = wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, dropdown_xpath))
            )
            current_text = dropdown_element.text.strip()
            if option_text in current_text:
                return
        except:
            pass

    wait_for_element_and_click(driver, wait_driver, dropdown_xpath, By.XPATH)
    time.sleep(1)

    if option_xpath:
        wait_for_element_and_click(driver, wait_driver, option_xpath, By.XPATH)
    elif option_text:
        option = wait_driver.until(
            EC.any_of(
                EC.visibility_of_element_located((By.XPATH, f'//li[contains(text(), "{option_text}")]')),
                EC.visibility_of_element_located((By.XPATH, f'//a[contains(text(), "{option_text}")]'))
            )
        )
        option.click()

    wait_driver.until(
        EC.invisibility_of_element_located((By.XPATH, '//div[@class="select2-search select2-search--dropdown"]'))
    )
    wait_loader(driver, wait_driver)


class AllOf:
    def __init__(self, *conditions):
        self.conditions = conditions

    def __call__(self, driver):
        results = []
        for condition in self.conditions:
            try:
                result = condition(driver)
                results.append(result)
            except:
                return False
        return all(results)

def wait_loader(driver: WebDriver, wait_driver: WebDriverWait) -> None:
    try:
        wait_driver.until(AllOf(
            EC.invisibility_of_element_located((By.ID, 'main_loading')),
            EC.invisibility_of_element_located((By.ID, 'mini-loader')),
            EC.invisibility_of_element_located((By.ID, 'tiny-loader')),
        ))
    except:
        pass


def send_keys_and_wait(driver: WebDriver, wait_driver: WebDriverWait, element: WebElement, text: str, wait_for_modal: bool = True) -> Optional[WebElement]:
    """Send keys to an element and wait for the page to load after pressing Enter.

    Args:
        driver: The WebDriver instance
        wait_driver: The WebDriverWait instance
        element: The element to send keys to
        text: The text to send
        wait_for_modal: Whether to wait for a modal to appear after sending keys

    Returns:
        The modal element if wait_for_modal is True and a modal appears, None otherwise
    """
    # Store the current page state to detect changes
    old_html = driver.find_element(By.TAG_NAME, 'body').get_attribute('innerHTML')

    # Send keys and press Enter
    element.send_keys(text, Keys.ENTER)

    # Wait for loaders to disappear
    wait_loader(driver, wait_driver)

    # Wait for page content to change (indicating the search results have loaded)
    # Use a shorter timeout for this check
    try:
        WebDriverWait(driver, 1).until(lambda d: d.find_element(By.TAG_NAME, 'body').get_attribute('innerHTML') != old_html)
    except:
        pass

    # Wait for search results to appear with a shorter timeout
    try:
        WebDriverWait(driver, 1).until(
            AnyOf(
                EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[2]')),
                EC.visibility_of_element_located((By.XPATH, '//tbody//tr//td[@class="dataTables_empty"]'))
            )
        )
    except:
        pass

    # Wait for loaders again to ensure everything is fully loaded
    wait_loader(driver, wait_driver)

    # If we need to wait for a modal
    if wait_for_modal:
        try:
            wait_driver.until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-dialog')))
            modal = driver.find_elements(By.CSS_SELECTOR, '.modal')[-1]
            return modal
        except:
            return None

    return None


def send_keys_and_click(driver: WebDriver, wait_driver: WebDriverWait, element: WebElement, text: str, click_selector: str, by: By = By.XPATH) -> None:
    """Send keys to an element and click on a specified element instead of pressing Enter.

    Args:
        driver: The WebDriver instance
        wait_driver: The WebDriverWait instance
        element: The element to send keys to
        text: The text to send
        click_selector: The selector for the element to click
        by: The locator strategy for the click element (default: By.XPATH)
    """
    # Send keys without pressing Enter
    element.send_keys(text)

    # Wait for loaders to disappear
    wait_loader(driver, wait_driver)

    # Click on the specified element
    wait_for_element_and_click(driver, wait_driver, click_selector, by)

    # Wait for loaders again to ensure everything is fully loaded
    wait_loader(driver, wait_driver)


def wait_for_expanded_element(driver: WebDriver, wait_driver: WebDriverWait, selector: str, by: By = By.XPATH) -> WebElement:
    """Wait for an element to be fully expanded and visible after an animation.

    This function waits for an element to be:
    1. Displayed (visible in the DOM)
    2. Have a height greater than 0 (fully expanded after CSS animation)

    Args:
        driver: The WebDriver instance
        wait_driver: The WebDriverWait instance
        selector: The selector for the element to wait for
        by: The locator strategy (default: By.XPATH)

    Returns:
        The fully expanded and visible element
    """
    return wait_driver.until(
        lambda d: d.find_element(by, selector)
        if d.find_element(by, selector).is_displayed()
        and d.find_element(by, selector).size['height'] > 0
        else False
    )