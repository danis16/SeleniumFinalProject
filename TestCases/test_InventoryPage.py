from traceback import print_tb
import unittest
from Base import InitiateDriver
from Pages import InventoryPage
from Pages import LoginPage
from Library import read_config
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Inventory(unittest.TestCase):

    filter = ["lohi","hilo","za","az"]

    @classmethod
    def setUpClass(cls):
        cls.browser = InitiateDriver.StartBrowser()
        cls.login_page = LoginPage(cls.browser)   
        cls.inventory_page = InventoryPage(cls.browser) 
        
        # Retrieve credentials from config file
        cls.username = read_config("Credentials", "username")
        cls.password = read_config("Credentials", "password")
    
    def login(self):
                self.login_page.enter_username(self.username)
                self.login_page.enter_password(self.password)
                self.login_page.click_login()
                # Verifikasi login berhasil
                self.assertTrue(self.login_page.is_login_successfull())

    def test_a_filter(self):
        self.login()
        for filters in self.filter:
                    with self.subTest(filters=filters):
                        self.inventory_page.test_filter(filters)

       
    @classmethod   
    def tearDownClass(cls):
        InitiateDriver.CloseBrowser()

if __name__ == '__main__':
    unittest.main()
    
    
    

    
    
    