from selenium.webdriver.common.by import By
from Library import get_locator, read_config
import time

class CartPage:
    
    def __init__(self, browser):
        self.browser = browser        
      
        self.burger_menu_locator = get_locator("Inventory","burger_menu")
        self.logout_button_locator = get_locator("Inventory","logout_button")
        self.cart_button_page_locator = get_locator("Inventory","cart_button_page")
        self.checkout_button = get_locator("Inventory","checkout_button")
        self.remove_sauce_labs_backpack_locator = get_locator("Inventory","remove_sauce_labs_backpack")
        self.continue_shopping_button_locator = get_locator("Inventory","continue_shopping")

        self.continue_button = get_locator("Checkout","continue_button")
        self.first_name_locator = get_locator("Checkout","first_name")
        self.last_name_locator = get_locator("Checkout","last_name")
        self.postal_code_locator = get_locator("Checkout","postal_code")
        

        self.finish_button = get_locator("Finish","finish_button")
        self.back_to_home_button = get_locator("Finish","back_to_home_button")

        
 
    def click_cart_product(self, product):        
        """Click the cart button."""
        self.browser.find_element(By.ID, product).click()
        time.sleep(2)
        
  
    def click_cart_page(self):
        """click cart page"""
        self.browser.find_element(By.ID, self.cart_button_page_locator).click()
        time.sleep(3)

    def is_cart_page_successfull(self):
        """Success open cart page."""
        get_url = self.browser.current_url
        
        if '/cart.html'in get_url:
            print("Success open cart page")
            return True
        else:
            print("Failed")
            return False

    def click_checkout_button(self):
        """click checkout button"""
        self.browser.find_element(By.ID, self.checkout_button).click()
        time.sleep(3)

    def fill_first_name(self, firstname):
        """Clear and enter the first name."""
        self.browser.find_element(By.ID, self.first_name_locator).send_keys(firstname)
        time.sleep(3)

    def fill_last_name(self, lastname):
        """Clear and enter the last name."""
        self.browser.find_element(By.ID, self.last_name_locator).send_keys(lastname)
        time.sleep(3)

    def fill_postal_code(self, postalcode):
        """Clear and enter the postal code."""
        self.browser.find_element(By.ID, self.postal_code_locator).send_keys(postalcode)
        time.sleep(3)

    def click_continue_button(self):
        """click continue button"""
        self.browser.find_element(By.ID, self.continue_button).click()
        time.sleep(3)
 
    def click_finish_button(self):
        self.browser.find_element(By.ID, self.finish_button).click()
        time.sleep(3)

    def is_checkout_successfull(self):
        """Verify successful checkout by checking the URL."""
        get_url = self.browser.current_url
        
        if '/checkout-complete.html'in get_url:
            print("Checkout is successfully")
            return True
        else:
            print("Failed")
            return False

    

    def click_back_to_home_button(self):
        self.browser.find_element(By.ID, self.back_to_home_button).click()
        time.sleep(3)
    
     
    def click_remove_sauce_labs_backpack(self, remove_product):        
        """Click the remove button."""
        self.browser.find_element(By.ID, remove_product).click()
        time.sleep(2)
 
    def click_continue_shopping(self):
        self.browser.find_element(By.ID, self.continue_shopping_button_locator).click()
        time.sleep(2)

   
 
    
    
        
   
        




   