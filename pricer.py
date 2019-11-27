import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('https://us.myprotein.com/')

# search for impact whey protein
search = driver.find_element_by_name('search')
search.send_keys('impact whey protein')

# find the flavor and select it
# TODO fix this so that it routes to select tag
strawberry_cream = driver.find_element_by_xpath("//option[contains(text(), 'Strawberry Cream')]")
# strawberry_cream = driver.find_element_by_xpath("//option[@value='2415']")
Select(strawberry_cream).select_by_visible_text('Strawberry Cream')

# select the 11 lb bag
driver.find_element_by_css_selector("input[value='16226']").click()


if __name__ == "__main__":
    print("asdf")