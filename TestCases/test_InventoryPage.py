from traceback import print_tb
import unittest
from Base import InitiateDriver
from Pages import InventoryPage
from Pages import LoginPage
from Pages import CartPage
from Library import read_config
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Inventory(unittest.TestCase):

    filter = ["lohi","hilo","za","az"]
    product = ["item_4_title_link", "item_3_title_link","item_2_title_link","item_1_title_link"]

    @classmethod
    def setUpClass(cls):
        cls.browser = InitiateDriver.StartBrowser()
        cls.login_page = LoginPage(cls.browser)   
        cls.inventory_page = InventoryPage(cls.browser) 
        cls.cart_page = CartPage(cls.browser)
        
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
        print("success filter")
        self.login_page.logout()     

    def test_open_product(self):
        self.login()
        for products in self.product:
                    with self.subTest(products=products):
                        self.inventory_page.test_show_product(products)
        print("success show product")

        self.login_page.logout()     
    
    def test_open_product_and_addtocart(self):
        self.login()
        for products in self.product:
                    with self.subTest(products=products):
                        self.inventory_page.show_product_and_add_to_cart(products)
        print("success show product")
        self.cart_page.click_cart_page()
        time.sleep(5)
        self.login_page.logout()     
    
    def test_open_and_close_menu(self):
        self.login()
        self.inventory_page.click_open_menu()
        self.inventory_page.click_close_menu()
    


       
    @classmethod   
    def tearDownClass(cls):
        InitiateDriver.CloseBrowser()

if __name__ == '__main__':
    unittest.main()
    
    
    

    
    
    