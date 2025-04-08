from traceback import print_tb
import unittest
from Base import InitiateDriver
from Pages import LoginPage
from Pages import CartPage
from Library import read_config
import time
from selenium.webdriver.common.by import By

class AddtoCartFailed(unittest.TestCase):

    manyproducts = ["add-to-cart-sauce-labs-bike-light", "add-to-cart-sauce-labs-bolt-t-shirt", "add-to-cart-sauce-labs-fleece-jacket", "add-to-cart-sauce-labs-onesie"]
    product = "add-to-cart-sauce-labs-backpack"
    remove_product = "remove-sauce-labs-bike-light"
    first_name = "Rose"
    last_name ="Diana"
    postal_code = "123456"
    
    @classmethod
    def setUpClass(cls):
        cls.browser = InitiateDriver.StartBrowser()
        cls.login_page = LoginPage(cls.browser)     
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
    
    def test_a_checkout_no_product(self):
       
                self.login()
                
                self.cart_page.click_cart_page()

                self.assertTrue(self.cart_page.is_cart_page_successfull())

                self.cart_page.click_checkout_button()

                self.cart_page.fill_first_name(self.first_name)

                self.cart_page.fill_last_name(self.last_name)

                self.cart_page.fill_postal_code(self.postal_code)

                self.cart_page.click_continue_button()

                self.cart_page.click_finish_button()

                self.assertTrue(self.cart_page.is_checkout_successfull())

                self.cart_page.click_back_to_home_button()

                self.login_page.logout()    

                print("add_to_cart_a_until_finish done")

    def test_b_checkout_no_product_not_fill_first_name_last_name_post_code(self):
       
                self.login()
                
                self.cart_page.click_cart_page()

                self.assertTrue(self.cart_page.is_cart_page_successfull())

                self.cart_page.click_checkout_button()

                self.cart_page.fill_first_name("")

                self.cart_page.fill_last_name("")

                self.cart_page.fill_postal_code("")

                self.cart_page.click_continue_button()

                error_message = self.browser.find_element(By.CSS_SELECTOR,'[data-test="error"]').text
                self.assertIn('First Name is required', error_message)

                self.login_page.logout()    

                print("checkout_no_product_not_fill_first_name_last_name_post_code done")
    
   

    def test_c_checkout_no_product_not_fill_first_name(self):
       
                self.login()
                
                self.cart_page.click_cart_page()

                self.assertTrue(self.cart_page.is_cart_page_successfull())

                self.cart_page.click_checkout_button()

                self.cart_page.fill_first_name("")

                self.cart_page.fill_last_name(self.last_name)

                self.cart_page.fill_postal_code(self.postal_code)

                self.cart_page.click_continue_button()

                error_message = self.browser.find_element(By.CSS_SELECTOR,'[data-test="error"]').text
                self.assertIn('First Name is required', error_message)

                self.login_page.logout()    

                print("checkout_no_product_not_fill_first_name done")
        
    def test_d_checkout_no_product_not_fill_last_name(self):
       
                self.login()
                
                self.cart_page.click_cart_page()

                self.assertTrue(self.cart_page.is_cart_page_successfull())

                self.cart_page.click_checkout_button()

                self.cart_page.fill_first_name(self.first_name)

                self.cart_page.fill_last_name("")

                self.cart_page.fill_postal_code(self.postal_code)

                self.cart_page.click_continue_button()

                error_message = self.browser.find_element(By.CSS_SELECTOR,'[data-test="error"]').text
                self.assertIn('Last Name is required', error_message)

                self.login_page.logout()    

                print("checkout_no_product_not_fill_last_name done")

    def test_e_checkout_no_product_not_fill_last_name(self):
       
                self.login()
                
                self.cart_page.click_cart_page()

                self.assertTrue(self.cart_page.is_cart_page_successfull())

                self.cart_page.click_checkout_button()

                self.cart_page.fill_first_name(self.first_name)

                self.cart_page.fill_last_name(self.last_name)

                self.cart_page.fill_postal_code("")

                self.cart_page.click_continue_button()

                error_message = self.browser.find_element(By.CSS_SELECTOR,'[data-test="error"]').text
                self.assertIn('Postal Code is required', error_message)

                self.login_page.logout()    

                print("checkout_no_product_not_fill_last_name done")
    
   

    @classmethod   
    def tearDownClass(cls):
        InitiateDriver.CloseBrowser()

if __name__ == '__main__':
    unittest.main()
    
    
    

    
    
    