from selenium.webdriver.common.by import By
from common.Test import Test


class TecniciTariffe(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Attività")
        self.wait_loader()

    def test_tecnici_tariffe(self):
        self._modifica_tariffe("28.00")
        self._verifica_tariffe()

    def _search_tecnico(self, nome: str):
        self.navigate_to_and_wait("Tecnici e tariffe")
        search_input = self.find(By.XPATH, '//th[@id="th_Nome"]/input')
        search_input.clear()
        self.send_keys_and_wait(search_input, nome, wait_modal=False)

    def _modifica_tariffe(self, modifica: str):
        self._search_tecnico('Tecnico')
        self.click_first_result()

        costo_input = self.find(By.XPATH, '//div[@class="input-group"]/input[@id="costo_ore1"]')
        costo_input.clear()
        costo_input.send_keys(modifica)
        self.click_save_button()

        self.navigate_to_and_wait("Tecnici e tariffe")
        self.clear_filters()

    def _verifica_tariffe(self):
        self._search_tecnico("Tecnico")
        self.click_first_result()

        costo_value = self.find(By.XPATH, '//div[@class="input-group"]/input[@id="costo_ore1"]').get_attribute('value')
        self.assertEqual("28,00", costo_value)
        self.clear_filters()

