#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_firefox_browser(url='https://google.com', headless=False, timeout=10):
    try:
        options = Options()
        if headless:
            options.add_argument('--headless')

        driver = webdriver.Firefox(options=options)
        driver.set_window_size(1366, 768)
        wait = WebDriverWait(driver, timeout)

        print(f"Opening {url}...")
        driver.get(url)

        # Wait for page to be fully loaded
        wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')

        # Wait for at least one element to be present to ensure page is rendered
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        print(f"Page title: {driver.title}")

        driver.save_screenshot('firefox_test.png')
        print("Screenshot saved as 'firefox_test.png'")

        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        return False
    finally:
        if 'driver' in locals():
            driver.quit()
            print("Browser closed.")

if __name__ == "__main__":
    test_firefox_browser()
