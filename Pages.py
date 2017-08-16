from Base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium import webdriver  


#######################################################
# HEADER METHODS AND FUNCTIONS
#######################################################

class Header(BasePage):
    
    recipes_header = (By.LINK_TEXT, "Recipes")
    shopping_list_header = (By.LINK_TEXT, "Shopping List")
    
    def nav_to_recipes(self):
        self.click_button(self.recipes_header)
        
    def nav_to_shoppinglist(self):
        self.click_button(self.shopping_list_header)
        
        

#######################################################
# RECIPE BOOK METHODS AND FUNCTIONS
#######################################################

class RecipeBook(BasePage):

    pass
    
    
#######################################################
# RECIPE METHODS AND FUNCTIONS
#######################################################

class Recipe(BasePage):

    pass


#######################################################
# SHOPPING LIST METHODS AND FUNCTIONS
#######################################################

class ShoppingList(BasePage):    
    
    # Locators
    name_field = (By.ID, 'name')
    amount_field = (By.ID, 'amount')
    unit_field = (By.ID, 'unit')
    add_btn = (By.CSS_SELECTOR, 'button.btn.btn-success')
    clear_btn = (By.CSS_SELECTOR, 'button.btn.btn-primary')
    delete_btn = (By.CSS_SELECTOR, 'button.btn.btn-danger')
    

    
    def enter_item_name(self, text):
        self.clear_text(self.name_field)
        self.enter_text(self.name_field, text)
    
    def enter_item_amt(self, amount):
        self.clear_text(self.amount_field)
        self.enter_text(self.amount_field, amount);
       
    def enter_item_unit(self, unit):
        unit_field_dropdown = Select(self.driver.find_element(*self.unit_field))
        unit_field_dropdown.select_by_visible_text(unit)
    
    def check_item_unit(self, unit):
        unit_field_dropdown = Select(self.driver.find_element(*self.unit_field))
        selected = unit_field_dropdown.first_selected_option
        assert selected.get_attribute("value") == unit
        
    def click_item_add(self): 
        self.click_button(self.add_btn) # Would expand this to differentiate Add and Update bottons
        
    def click_item_clear(self):
        self.click_button(self.clear_btn)
        
    def click_item_delete(self):
        self.click_button(self.delete_btn)
        
    def clear_item_name(self):
        self.clear_text(self.name_field)
        
    def clear_item_amount(self):
        self.clear_text(self.amount_field)
        
    def clear_item_unit(self):
        self.clear_text(self.unit_field)
      
    def add_item_to_list(self, name, amount, unit):
        self.enter_item_name(name)
        self.enter_item_amt(amount)
        self.enter_item_unit(unit)
        self.click_item_add()
        
    def select_item_on_list(self, item):
        list_item = (By.LINK_TEXT, item)
        item_link = self.driver.find_element(*list_item)
        item_link.click()
        
    def is_item_in_list(self, item):
        list_item = (By.LINK_TEXT, item)
        assert self.is_element_present(list_item)
       
        
  


        

        
        
   

        
    
            
        

    
