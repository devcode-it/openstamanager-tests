from common.Test import Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from typing import Optional


class Attivita_Dashboard(Test):
    def setUp(self):
        super().setUp()

    def test_attivita_dashboard(self):
        self._create_activity('Cliente', '1')

        self.navigateTo("Dashboard")
        self.wait_loader()
        self._drag_activity_and_update_technician()

        self.navigateTo("Dashboard")
        self.wait_loader()
        self._verify_activity()

    def _create_activity(self, cliente: str, tipo: str):
        self.navigateTo('Attività')
        self.wait_for_element_and_click('//i[@class="fa fa-plus"]')
        modal = self.wait_modal()

        self.input(modal, 'Cliente').setByText(cliente)
        self.input(modal, 'Tipo').setByIndex(tipo)

        iframe = self.wait_for_element_and_click('(//iframe[@class="cke_wysiwyg_frame cke_reset"])[1]')
        iframe.send_keys('Test')
        self.wait_for_element_and_click('//div[@class="col-md-12 text-right"]//button[@type="button"]')

    def _drag_activity_and_update_technician(self):
        attivita = self.wait_for_element_and_click('//div[@class="fc-event fc-event-primary"]')
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(attivita, -1000, 0).perform()
        modal = self.wait_modal()

        self.wait_for_element_and_click('//a[@id="tecnici-sessioni-tab"]')
        self.wait_for_dropdown_and_select(
            '//span[@id="select2-idtecnico-container"]',
            option_text='Stefano Bianchi'
        )

        self.wait_for_element_and_click('//div[@class="modal-content"]//button[@onclick="salva(this)"]')

    def _verify_activity(self):
        self.wait_for_element_and_click('//button[@class="btn btn-block counter_object btn-danger"]')
        self.wait_for_element_and_click('//input[@class="dashboard_tecnico"]')

        trova_element = self.find(By.XPATH, '//div[@class="fc-event-main"]')
        trova = trova_element.text
        self.assertEqual(trova, "Int. 2 Cliente\nTecnico: Stefano Bianchi")