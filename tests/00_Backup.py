from common.Test import Test


class Backup(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Strumenti")

    def test_creazione_backup(self):
        self._navigate_to_backup()
        self._create_backup()

    def _navigate_to_backup(self):
        self.navigateTo("Backup")
        self.wait_loader()

    def _create_backup(self):
        self.wait_for_element_and_click('//a[@onclick="creaBackup(this)"]')
        self.wait_for_element_and_click('//button[@class="swal2-confirm btn btn-lg btn-success"]')