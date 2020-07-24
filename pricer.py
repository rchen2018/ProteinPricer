from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, \
    ElementClickInterceptedException

from db_connect import add_scan

import re
import time

STRAWBERRY_11LB_SELECTOR = "div[data-variation-container = 'athenaProductVariations']"
STRAWBERRY_11LB_VALUE = 'sports-nutrition/impact-whey-protein-strawberry-cream-11lb/10852509.html'

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 2)

driver.maximize_window()
driver.get('https://us.myprotein.com/')


def main():
    search_for_protein()

    not_working = True
    while not_working:
        try:
            select_strawberry_11lb()

            # Check that product is 11 pound strawberry cream
            strawberry_11 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, STRAWBERRY_11LB_SELECTOR)))
            if strawberry_11.get_attribute('data-information-url') != STRAWBERRY_11LB_VALUE:
                continue

            not_working = add_and_go_to_cart(not_working)

        except (StaleElementReferenceException, TimeoutException):
            driver.refresh()

        # Ad popup blocks window
        except ElementClickInterceptedException:
            close = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'emailReengagement_close_button')))
            close.click()
            continue

    find_and_apply_discount()
    add_scan('Strawberry Cream', sale_price, sale_text)


def search_for_protein():
    # Find the search bar
    search = wait.until(EC.presence_of_element_located((By.NAME, 'search')))

    # Search for impact whey protein
    search.send_keys('impact whey protein')
    search.send_keys(Keys.RETURN)


def select_strawberry_11lb():
    # Find the flavor and select it
    flavor = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'athenaProductVariations_dropdown')))
    Select(flavor).select_by_visible_text('Strawberry Cream')

    # Select the 11 lb bag
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), '11 lb')]")))
    element.click()
    time.sleep(2)  # Wait 2 seconds to allow page to catch up


def add_and_go_to_cart(not_working):
    # Add to cart
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'productAddToBasket')))
    driver.find_element_by_class_name('productAddToBasket').click()
    time.sleep(2)  # Wait 2 seconds to allow page to catch up

    product = driver.find_element_by_class_name('athenaAddedToBasketModal_itemName')
    if "11lb" in product.text and "Strawberry Cream" in product.text:
        not_working = False

        # Go to cart
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Checkout')))
        driver.find_element_by_link_text('Checkout').click()

    return not_working


def find_and_apply_discount():
    global original_price, sale_text, code, sale_price

    price_element = driver.find_element_by_xpath('//*[@id="10852509"]/div[4]')
    original_price = price_element.text
    original_price = float(original_price.replace('$', ''))

    # Entire sale banner text
    sale_element = driver.find_element_by_xpath('//*[@id="checkout"]/div[1]/a/p')
    sale_text = sale_element.text

    # Get just the code
    code = re.search(r'CODE:.*$', sale_text).group()
    code = code.split(': ')[1]

    code_box = wait.until(EC.presence_of_element_located((By.NAME, 'discountCode')))
    code_box.send_keys(code)
    code_box.send_keys(Keys.RETURN)
    time.sleep(1)

    sale_price_element = driver.find_element_by_xpath('//*[@id="10852509"]/div[4]')
    sale_price = sale_price_element.text
    sale_price = float(sale_price.replace('$', ''))


if __name__ == "__main__":
    main()
    print('done')
