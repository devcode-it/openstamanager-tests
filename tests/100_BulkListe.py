from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.Test import Test

class Liste(Test):
    def setUp(self):
        super().setUp()
        self.wait_driver = self.wait_driver
        self.expandSidebar("Gestione email")

    def test_bulk_liste(self):
        self.aggiorna_liste()

    def aggiorna_liste(self):
        self.navigate_to_and_wait("Liste")

        self.wait_for_element_and_click('//tbody//tr//td')
        self.wait_for_dropdown_and_select(
            '//button[@data-toggle="dropdown"]',
            option_xpath='//a[@data-op="update_lists"]'
        )
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')