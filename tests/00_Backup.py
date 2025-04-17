from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Backup(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")

    def test_creazione_backup(self):
        wait = WebDriverWait(self.driver, 20)
        
        self.navigateTo("Backup")
        self.wait_loader()

        backup_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@onclick="creaBackup(this)"]'))
        )
        backup_button.click()

        confirm_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-success"]'))
        )
        confirm_button.click()

        self.wait_loader()
