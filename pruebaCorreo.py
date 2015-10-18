from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class TestCorreo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=12&ct=1445012473&rver=6.4.6456.0&wp=MBI_SSL_SHARED&wreply=https:%2F%2Fmail.live.com%2Fdefault.aspx&lc=2058&id=64855&mkt=es-mx&cbcxt=mai')

    def test_prueba_titulo_de_google(self):
        self.assertEqual('Iniciar session', self.driver.title)

    def test_prueba_busqueda_de_un_termino_ingenieria_software(self):
        username = self.driver.find_element_by_id('i0116')
        username.send_keys('mariesparza426@outlook.com')

        passwd = self.driver.find_element_by_id('i0118')
        passwd.send_keys('linux125')

        btn_ok = self.driver.find_element_by_id('idSIButton9')
        btn_ok.click()

        mensaje = self.driver.find_element_by_class_name('c-MessageRow')
        mensaje.click()


if __name__=='__main__':
    unittest.main()
