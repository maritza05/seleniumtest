from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class TestCorreo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=12&ct=1445012473&rver=6.4.6456.0&wp=MBI_SSL_SHARED&wreply=https:%2F%2Fmail.live.com%2Fdefault.aspx&lc=2058&id=64855&mkt=es-mx&cbcxt=mai')

    def test_prueba_titulo_de_outlook(self):
        self.assertEqual('Iniciar session', self.driver.title)

    def test_prueba_busqueda_de_un_termino_ingenieria_software(self):
        username = self.driver.find_element_by_id('i0116')
        username.send_keys('mariesparza426@outlook.com')

        passwd = self.driver.find_element_by_id('i0118')
        passwd.send_keys('linux125')

        btn_ok = self.driver.find_element_by_id('idSIButton9')
        btn_ok.click()

        # click al primer checkbox encontrado
        mensajes =  self.driver.find_elements_by_class_name('mlCheckbox')
        mensajes[0].click()

        # abrir un mensaje
        mensajes2 =  self.driver.find_element_by_id('ukzWdDdJVz5RGTdmw75afbaQ2')
        mensajes2.click()
        self.assertEqual(1,1)

        #opciones
        opciones = self.driver.find_element_by_id('inboxControl0fv-ReadMessageContainer')

        print opciones == None




if __name__=='__main__':
    unittest.main()
