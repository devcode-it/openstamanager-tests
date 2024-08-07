from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class StampeContabili(Test):
    def setUp(self):
        super().setUp()

 
    def test_stampecontabili(self):
        self.navigateTo("Contabilità")
        self.navigateTo("Stampe contabili")

    # TODO: test stampe contabili