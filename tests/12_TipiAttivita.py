from common.Test import Test, get_html
from selenium.webdriver.common.keys import Keys
from common.RowManager import RowManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TipiAttivita(Test):
    def setUp(self):
        super().setUp()

        self.expandSidebar("Attività")
        
    def test_creazione_tipiattività(self, modifica= "Tipo di Attività di Prova"):
        self.creazione_tipiattività(codice="001", descrizione="Tipo di Prova da Modificare", tempostandard="2,00", addebitoorario="10,00", addebitokm="5,00", addebitodirittoch="20,00", costoorario="12,00", costokm="6,00", costodirittoch="13,00" )
        self.creazione_tipiattività(codice="002", descrizione="Tipo di Prova da Eliminare", tempostandard="2,00", addebitoorario="10,00", addebitokm="5,00", addebitodirittoch="20,00", costoorario="12,00", costokm="6,00", costodirittoch="13,00")
        

        # Modifica tipi di attività
        self.navigateTo("Tipi di attività")
        self.wait_loader()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Descrizione"]/input')
        element.send_keys('Tipo di Prova da Modificare')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys(Keys.ENTER)
        sleep(1)

        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        
        self.input(None,'Descrizione').setValue(modifica)

        self.find(By.XPATH, '//div[@id="tab_0"]//a[@id="save"]').click()
        self.wait_loader()


        # Cancellazione tipi di attività
        self.navigateTo("Tipi di attività")
        self.wait_loader()  

        self.find(By.XPATH, '//th[@id="th_Descrizione"]/i[@class="deleteicon fa fa-times fa-2x"]').click()

        element=self.driver.find_element(By.XPATH,'//th[@id="th_Descrizione"]/input')
        element.send_keys('Tipo di Prova da Eliminare')
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//th[@id="th_Descrizione"]/input'))).send_keys(Keys.ENTER)

        sleep(2)
        self.find(By.XPATH, '//div[@id="tab_0"]//tbody//td[2]//div[1]').click()
        self.wait_loader()
        self.find(By.XPATH, '//div[@id="tab_0"]//a[@class="btn btn-danger ask"]').click()
        self.wait_loader()
        self.find(By.XPATH, '//button[@class="swal2-confirm btn btn-lg btn-danger"]').click()
        self.wait_loader()



    def creazione_tipiattività(self, codice=str, descrizione=str, tempostandard=str, addebitoorario=str, addebitokm=str, addebitodirittoch=str, costoorario=str, costokm=str, costodirittoch=str):
        self.navigateTo("Tipi di attività")
        self.wait_loader()  

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
