from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Import_(Test):
    def setUp(self):
        super().setUp()

     
    def test_import(self):
        self.expandSidebar("Strumenti")
        self.navigateTo("Import")
