from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://us.myprotein.com/')

# need to maximize window to standardize results (errors occur in minimized window)
# driver.maximize_window()
# driver.find_element_by_class_name('headerSearch_toggleForm').click()  PROBABLY DONT NEED

# search for impact whey protein
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'search')))
search = driver.find_element_by_name('search')

search.send_keys('impact whey protein')
search.send_keys(Keys.RETURN)

# find the flavor and select it
# TODO fix this so that it routes to select tag
strawberry_cream = driver.find_element_by_xpath("//option[contains(text(), 'Strawberry Cream')]")
# strawberry_cream = driver.find_element_by_xpath("//option[@value='2415']")
Select(strawberry_cream).select_by_visible_text('Strawberry Cream')

# select the 11 lb bag
driver.find_element_by_css_selector("input[value='16226']").click()


if __name__ == "__main__":
    print("asdf")