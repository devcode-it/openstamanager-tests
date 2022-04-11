from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TipiAttivita(Test):
    def setUp(self):
        super().setUp()

        self.navigateTo("Attività")
        self.navigateTo("Tipi di attività")

    def test_creazione_tipiattività(self):
        self.creazione_tipiattività(codice="001", descrizione="Prova Attività", tempostandard="2,00", addebitoorario="10,00", addebitokm="5,00", addebitodirittoch="20,00", costoorario="12,00", costokm="6,00", costodirittoch="13,00" )

    def creazione_tipiattività(self, codice=str, descrizione=str, tempostandard=str, addebitoorario=str, addebitokm=str, addebitodirittoch=str, costoorario=str, costokm=str, costodirittoch=str):

        self.find(By.CSS_SELECTOR, '#tabs > li:first-child .btn-primary > .fa-plus').click()
        modal = self.wait_modal()

        self.input(modal, 'Codice').setValue(codice)
        self.input(modal, 'Descrizione').setValue(descrizione)
        self.input(modal, 'Tempo standard').setValue(tempostandard)
        self.input(modal, 'Addebito orario').setValue(addebitoorario)
        self.input(modal, 'Addebito km').setValue(addebitokm)
        self.input(modal, 'Addebito diritto ch.').setValue(addebitodirittoch)
        self.input(modal, 'Costo orario').setValue(costoorario)
        self.input(modal, 'Costo km').setValue(costokm)
        self.input(modal, 'Costo diritto ch.').setValue(costodirittoch)

        modal.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.wait_loader()
