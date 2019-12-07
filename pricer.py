from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.maximize_window()
driver.get('https://us.myprotein.com/')

# find the search bar
wait.until(EC.presence_of_element_located((By.NAME, 'search')))
search = driver.find_element_by_name('search')

# search for impact whey protein
search.send_keys('impact whey protein')
search.send_keys(Keys.RETURN)

# find the flavor and select it
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'athenaProductVariations_dropdown')))
flavor = driver.find_element_by_class_name('athenaProductVariations_dropdown')

Select(flavor).select_by_visible_text('Strawberry Cream')

# select the 11 lb bag
wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '11 lb')]")))
driver.find_element_by_xpath("//*[contains(text(), '11 lb')]").click()  # TODO sometimes doesn't register before adding to cart

wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'productAddToBasket')))
driver.find_element_by_class_name('productAddToBasket').click()

wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Checkout')))
driver.find_element_by_link_text('Checkout').click()


if __name__ == "__main__":
    print("no errors!")