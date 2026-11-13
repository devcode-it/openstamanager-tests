from common.Test import Test, get_html
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Banche(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")
        self.expandSidebar("Tabelle")

    def test_plugin_banche(self):
        self.mandati_sepa()

    def mandati_sepa(self):
        self.navigate_to_and_wait("Banche")

        self.click_first_table_row()
        self.wait_for_element_and_click('//a[@id="link-tab_47"]')

        self.input(None,'ID Mandato').setValue("123456")
        self.wait_for_element_and_click('//div[@id="tab_47"]//button[@type="submit"]')