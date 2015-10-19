# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class TestCorreo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://mail.live.com?mkt=us-us')
        # self.driver.implicitly_wait(20)

    def test_prueba_titulo_de_outlook(self):
        self.assertEqual('Sign In', self.driver.title)

    def test_prueba_busqueda_de_ingresar_correo(self):
        username = self.driver.find_element_by_id('i0116')
        username.send_keys('mariesparza426@outlook.com')

        passwd = self.driver.find_element_by_id('i0118')
        passwd.send_keys('xxxx')

        btn_ok = self.driver.find_element_by_id('idSIButton9')
        btn_ok.click()

        time.sleep(10)

        # click al primer checkbox encontrado en la bandeja de correo
        print  self.driver.title
        check_messages =  self.driver.find_elements_by_class_name('mlCheckbox')
        check_messages[0].click()

        time.sleep(10)

        # abrir un mensaje
        message =  self.driver.find_element_by_id('ukzWdDdJVz5RGTdmw75afbaQ2')
        message.click()

        # menu de opciones disponibles al abrir un correo
        options_from_email = self.driver.find_element_by_id('inboxControl0fv-ReadMessageContainer')
        options_from_email_exist = options_from_email is None

        self.assertEqual(options_from_email_exist, False)



if __name__=='__main__':
    unittest.main()
