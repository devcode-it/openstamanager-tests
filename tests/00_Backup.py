from common.Test import Test

class Backup(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")

    def test_creazione_backup(self):
        self.navigateTo("Backup")
        self.wait_loader()

        self.wait_for_element_and_click('//a[@onclick="creaBackup(this)"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')
        self.wait_for_element_and_click('//i[@class="fa fa-power-off nav-icon"]')
