from os import times_result
from selenium.webdriver.common.by import By
from Library import get_locator, read_config
import time
from selenium.webdriver.support.ui import Select

class InventoryPage:
    
    def __init__(self, browser):
        self.browser = browser        
        self.product_sort_container_locator = get_locator("Inventory","product_sort_container")
        self.back_to_products_locator = get_locator("Inventory","back-to-products")
        self.add_to_cart_locator = get_locator("Inventory","add-to-cart")
        self.burger_menu_locator = get_locator("Inventory","burger_menu")
        self.close_button_locator = get_locator("Inventory","close_button")
    
    def test_filter(self, value):
        """click test filter"""
        select_element = self.browser.find_element(By.XPATH, self.product_sort_container_locator)
        select = Select(select_element)
        select.select_by_value(value) 
        time.sleep(5)

    def test_show_product(self, product):
        self.browser.find_element(By.ID, product).click()
        time.sleep(3)
        self.browser.find_element(By.ID, self.back_to_products_locator).click()
        time.sleep(3)

    def show_product_and_add_to_cart(self, product):
        self.browser.find_element(By.ID, product).click()
        time.sleep(3)
        self.browser.find_element(By.ID,self.add_to_cart_locator).click()
        time.sleep(2)
        self.browser.find_element(By.ID, self.back_to_products_locator).click()
        time.sleep(3)
    
    def click_open_menu(self):
        self.browser.find_element(By.ID,self.burger_menu_locator).click()
        time.sleep(3)
    
    def click_close_menu(self):
        self.browser.find_element(By.ID,self.close_button_locator).click()
        time.sleep(2)
       



 
    
    
        
   
        




   