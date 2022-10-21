from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class GestioneEmail(Test):
    def setUp(self):
        super().setUp()

        
    def test_gestione_email(self):
        self.expandSidebar("Gestione email")

