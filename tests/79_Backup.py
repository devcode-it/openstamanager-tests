from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Backup(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Strumenti")

    def test_creazione_backup(self):
        self.creazione_backup()

    def creazione_backup(self):
        self.navigateTo("Backup")
        self.find(By.CSS_SELECTOR, 'button[onclick="creaBackup(this)"]').click()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-success"]').click()
