from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class TestGooglePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.google.com.mx/')
        
    def test_prueba_titulo_de_google(self):
        self.assertEqual('Google', self.driver.title)

    def test_prueba_busqueda_de_un_termino_ingenieria_software(self):
        buscar = self.driver.find_element_by_id('lst-ib')
        buscar.send_keys('ingenieria de software')
        buscar.send_keys(Keys.RETURN)

    #   self.assertIn('ingenieria de software', self.driver.title)

        elementos = self.driver.find_elements_by_class_name('r')
        self.assertFalse(len(elementos), 0)
    #    boton = self.driver.find_element_by_name('btnK')
    #    boton.click()

    def tearDown(self):
        self.driver.close()

if __name__=='__main__':
    unittest.main()
