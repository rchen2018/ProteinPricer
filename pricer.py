from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, \
    ElementClickInterceptedException
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 2)

driver.maximize_window()
driver.get('https://us.myprotein.com/')

soup = BeautifulSoup(driver.page_source, 'html.parser')

# find the search bar
search = wait.until(EC.presence_of_element_located((By.NAME, 'search')))

# search for impact whey protein
search.send_keys('impact whey protein')
search.send_keys(Keys.RETURN)

notWorking = True
while notWorking:
    try:
        # find the flavor and select it
        flavor = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'athenaProductVariations_dropdown')))
        Select(flavor).select_by_visible_text('Strawberry Cream')

        # select the 11 lb bag
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), '11 lb')]")))
        element.click()
        time.sleep(2)  # wait 2 seconds to allow page to catch up

        # check that product is 11 pound strawberry cream
        strawberry_11 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-variation-container = 'athenaProductVariations']")))
        if strawberry_11.get_attribute('data-information-url') != 'sports-nutrition/impact-whey-protein-strawberry-cream-11lb/10852509.html':
            continue

        # add to cart
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'productAddToBasket')))
        driver.find_element_by_class_name('productAddToBasket').click()
        time.sleep(2)  # wait 2 seconds to allow page to catch up

        product = driver.find_element_by_class_name('athenaAddedToBasketModal_itemName')
        if "11lb" in product.text and "Strawberry Cream" in product.text:
            notWorking = False
            # go to cart
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Checkout')))
            driver.find_element_by_link_text('Checkout').click()

    except (StaleElementReferenceException, TimeoutException) as e:
        print(e)
        driver.refresh()

    except ElementClickInterceptedException:
        close = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'emailReengagement_close_button')))
        close.click()
        continue

# sale = soup.find(class_='countDownTimer_link').text
# print(sale)

if __name__ == "__main__":
    print("success")