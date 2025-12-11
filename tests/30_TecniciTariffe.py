from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.Test import Test


class TecniciTariffe(Test):
    def setUp(self):
        super().setUp()
        self.expandSidebar("Attività")
        self.wait_loader()

    def test_tecnici_tariffe(self):
        self.modifica_tariffe("28.00")
        self.verifica_tariffe()

    def search_tecnico(self, nome: str):
        self.navigateTo("Tecnici e tariffe")
        self.wait_loader()
        search_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Nome"]/input'))
        )
        search_input.clear()
        self.send_keys_and_wait(search_input, nome, wait_modal=False)

    def modifica_tariffe(self, modifica: str):
        self.search_tecnico('Tecnico')
        self.click_first_result()

        costo_input = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="input-group"]/input[@id="costo_ore1"]'))
        )
        costo_input.clear()
        costo_input.send_keys(modifica)
        self.wait_for_element_and_click('//div[@id="tab_0"]//button[@id="save"]')

        self.navigateTo("Tecnici e tariffe")
        self.wait_loader()
        self.clear_filters()

    def verifica_tariffe(self):
        self.search_tecnico("Tecnico")
        self.click_first_result()

        costo_value = self.wait_driver.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="input-group"]/input[@id="costo_ore1"]'))
        ).get_attribute('value')
        self.assertEqual("28,00", costo_value)
        self.clear_filters()

