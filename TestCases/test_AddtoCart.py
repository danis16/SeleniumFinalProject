import unittest
from Base import InitiateDriver
from Pages import LoginPage
from Pages import CartPage
from Library import read_config

class AddtoCart(unittest.TestCase):

    manyproducts = ["add-to-cart-sauce-labs-backpack", "add-to-cart-sauce-labs-bike-light", "add-to-cart-sauce-labs-bolt-t-shirt", "add-to-cart-sauce-labs-fleece-jacket", "add-to-cart-sauce-labs-onesie"]
    product = "add-to-cart-sauce-labs-backpack"
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
    
    def test_add_to_cart_a_until_finish(self):
       
                self.login()

                
                self.cart_page.click_cart_product(self.product)
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
    
    def test_add_to_cart_b_more_than_one_product_until_finish(self):
                
                self.login()

                for products in self.manyproducts:
                    with self.subTest(products=products):
                        self.cart_page.click_cart_product(products)

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

    def test_add_to_cart_c_more_than_one_product_then_remove_one_product(self):
                
                self.login()

                for products in self.manyproducts:
                    with self.subTest(products=products):
                        self.cart_page.click_cart_product(products)


                self.cart_page.click_cart_page()

                self.assertTrue(self.cart_page.is_cart_page_successfull())

                self.cart_page.click_remove_sauce_labs_backpack(self.product)

                self.cart_page.click_checkout_button()

                self.cart_page.fill_first_name(self.first_name)

                self.cart_page.fill_last_name(self.last_name)

                self.cart_page.fill_postal_code(self.postal_code)

                self.cart_page.click_continue_button()

                self.cart_page.click_finish_button()

                self.assertTrue(self.cart_page.is_checkout_successfull())

                self.cart_page.click_back_to_home_button()

                self.login_page.logout()      



    @classmethod   
    def tearDownClass(cls):
        InitiateDriver.CloseBrowser()

if __name__ == '__main__':
    unittest.main()
    
    
    

    
    
    