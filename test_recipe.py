from selenium import webdriver
from time import sleep
import pytest
from Pages import *




# creates the driver instance once for the series of tests
@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    driver.get('https://forteautomationtest.herokuapp.com')
    yield driver
    driver.get('https://forteautomationtest.herokuapp.com/reset')
    reset = driver.find_element_by_css_selector('button.btn-primary.btn') 
    reset.click()
    sleep(1)    # Add Selenium wait mechanism
    driver.close() 

   
# creates ShoppingList instance
@pytest.fixture(scope="function")
def shopping_list_page(driver):
    shopping_list_page = ShoppingList(driver)
    yield shopping_list_page
    
# creates ShoppingList instance
@pytest.fixture(scope="function")
def header(driver):
    header = Header(driver)
    yield header
    
@pytest.fixture(scope="function")
def navigate_shopping_list(header):
    header.nav_to_shoppinglist()
    
##################################################################
# Begin tests
##################################################################
    
# Verify name field is accepting data
@pytest.mark.build
@pytest.mark.SLregression    
def test_enter_item_name(shopping_list_page, navigate_shopping_list):
    shopping_list_page.enter_item_name("Milk")
    assert shopping_list_page.get_text(shopping_list_page.name_field) == "Milk"
    
# Verify amount field is accepting data
@pytest.mark.build
@pytest.mark.SLregression      
def test_enter_item_amt(shopping_list_page):
    shopping_list_page.enter_item_amt("2")
    assert shopping_list_page.get_text(shopping_list_page.amount_field) == "2"
    
# Verify unit field is accepting data
@pytest.mark.build
@pytest.mark.SLregression      
def test_enter_item_unit(shopping_list_page):
    shopping_list_page.enter_item_unit("gal")
    shopping_list_page.check_item_unit("gal")
 
# Verify add button works
@pytest.mark.build     
def test_add_item_milk(shopping_list_page):
    shopping_list_page.click_item_add()
    item = "Milk (2 - gal)"
    shopping_list_page.is_item_in_list(item)
    
      
# Verify name field empty after item added
@pytest.mark.build 
def test_item_name_clear(shopping_list_page):
    assert shopping_list_page.get_text(shopping_list_page.name_field) == ''

# Verify amount field empty after item added
@pytest.mark.build
def test_item_amount_clear(shopping_list_page):
    assert shopping_list_page.get_text(shopping_list_page.amount_field) == ''

# Verify unit field empty after item added
@pytest.mark.build
@pytest.mark.SLregression  
def test_item_unit_clear(shopping_list_page):
    pass # expand
   
# Verify item in list can be selected
@pytest.mark.build
@pytest.mark.SLregression  
def test_select_item(shopping_list_page):
    item = "Milk (2 - gal)"
    shopping_list_page.select_item_on_list(item)
    assert shopping_list_page.get_text(shopping_list_page.name_field) == 'Milk'
  
     
# Verify item can be deleted
# The verification in this test does not yet function. Additional error handling is required
# in cases in which I expect WebDriver to not find a web element. To be implented. 
@pytest.mark.build
@pytest.mark.SLregression
def test_delete_milk_item(shopping_list_page):
    item = "Milk (2 - gal)"
    shopping_list_page.click_item_delete()
    # assert not shopping_list_page.is_item_in_list(item) 
    
    
# Verify item name can be updated
@pytest.mark.build
@pytest.mark.SLregression
def test_item_name_update(shopping_list_page):
    shopping_list_page.add_item_to_list("Carrots", "1", "bag")
    item = "Carrots (1 - bag)"
    shopping_list_page.select_item_on_list(item)
    shopping_list_page.enter_item_name("Purple Carrots")
    shopping_list_page.click_item_add()
    item_updated = "Purple Carrots (1 - bag)"
    shopping_list_page.is_item_in_list(item_updated)
   

# Verify that updating an item does not create a duplicate (could create verions of this for all fields)
# The verification in this test does not yet function. Additional error handling is required
# in cases in which I expect WebDriver to not find a web element. To be implented. 
@pytest.mark.build
@pytest.mark.SLregression    
def test_update_does_not_create_duplicates(shopping_list_page):
    pass 
    # item_original = "Carrots (1 - bag)"
    # assert not shopping_list_page.is_item_in_list(item_original)
    

# Verify item amount can be updated
@pytest.mark.build
@pytest.mark.SLregression
def test_item_amount_update(shopping_list_page):
    item = "Purple Carrots (1 - bag)"
    shopping_list_page.select_item_on_list(item)
    shopping_list_page.enter_item_amt("2")
    shopping_list_page.click_item_add()
    item_amt_updated = "Purple Carrots (2 - bag)"
    shopping_list_page.is_item_in_list(item_amt_updated)
    

# Verify item unit can be updated
@pytest.mark.build
@pytest.mark.SLregression 
def test_item_unit_update(shopping_list_page):
    item = "Purple Carrots (2 - bag)"
    shopping_list_page.select_item_on_list(item)
    shopping_list_page.enter_item_unit("peck")
    shopping_list_page.click_item_add()
    item_unit_updated = "Purple Carrots (2 - peck)"
    shopping_list_page.is_item_in_list(item_unit_updated)
 
   
# Verify all item fields can be updated (could expand this to multiple configs)
@pytest.mark.build
@pytest.mark.SLregression
def test_item_all_fields_update(shopping_list_page):
    item = "Purple Carrots (2 - peck)"
    shopping_list_page.select_item_on_list(item)
    shopping_list_page.enter_item_name("Golden carrots")
    shopping_list_page.enter_item_amt("20")
    shopping_list_page.enter_item_unit("item")
    shopping_list_page.click_item_add()
    item_all_updated = "Golden carrots (20 - item)"
    shopping_list_page.is_item_in_list(item_all_updated)
    
    
# Verify multiple items can be added (1) 
@pytest.mark.build
@pytest.mark.SLregression
def test_add_multiple_items(shopping_list_page):
    shopping_list_page.add_item_to_list("Ketchup", "1", "item")
    item1 = ("Ketchup (1 - item)")
    shopping_list_page.add_item_to_list("Celery", "4", "bag")
    shopping_list_page.add_item_to_list("Tomato paste", "3", "tsp")
    shopping_list_page.is_item_in_list(item1) 
    

 
# Verify multiple items can be added (2)     
@pytest.mark.build
@pytest.mark.SLregression 
def test_check_second_item(shopping_list_page):
    item2 = ("Celery (4 - bag)")
    shopping_list_page.is_item_in_list(item2)
    

# Verify multiple items can be added (3)     
@pytest.mark.build
@pytest.mark.SLregression
def test_check_third_item(shopping_list_page):   
    item3 = ("Tomato paste (3 - tsp)")    
    shopping_list_page.is_item_in_list(item3) 
    

# Verify clear button works - name
@pytest.mark.build
@pytest.mark.SLregression
def test_does_clear_name_work(shopping_list_page):
    shopping_list_page.enter_item_name("Golden carrots")
    shopping_list_page.enter_item_amt("20")
    shopping_list_page.enter_item_unit("item")
    shopping_list_page.click_item_clear()
    assert shopping_list_page.get_text(shopping_list_page.name_field) == ""
       
# Verify clear button works - amount
@pytest.mark.build
@pytest.mark.SLregression
def test_does_clear_amount_work(shopping_list_page):
    assert shopping_list_page.get_text(shopping_list_page.amount_field) == ""

 
# Verify clear button works - unit
@pytest.mark.build
@pytest.mark.SLregression
def test_does_clear_amount_work(shopping_list_page):
    pass 
    

# Input validation tests (negative values) 
# The final three examples demonstrate the use of pytest markers. In this case, these 
# tests don't need to execute for every build, but would be useful for thorough
# regression testing if the page experienced recent changes. 
@pytest.mark.SLregression
def test_negative_item_amount():
    pass
    
# Input validation tests (decimal values)
@pytest.mark.SLregression
def test_decimal_item_amount():
    pass  
    
# Input validation tests (special characters)
@pytest.mark.SLregression
def test_special_character_input():
    pass

    

    
    



    


    







