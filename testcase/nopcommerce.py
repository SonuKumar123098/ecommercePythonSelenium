import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
# launch the website on chrome browser
search_input = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# search the product
search_input.send_keys("shoes")
search_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Search']")
search_btn.click()
time.sleep(1)
# select item to add to your cart
select_add_to_cart_btn = driver.find_elements(By.XPATH, "//div[@class='item-grid']//div[@class='buttons']")
for btn in select_add_to_cart_btn:
    btn.click()
    break
# time.sleep(1)
# driver.back()
# select size of the product
size_dropdown = driver.find_element(By.ID, "product_attribute_6")
size_options = Select(size_dropdown)
size_options.select_by_index(1)
# select color of the product
color_dropdown = driver.find_element(By.ID, "product_attribute_7")
color_options = Select(color_dropdown)
color_options.select_by_index(1)
# select print option
prints = driver.find_elements(By.XPATH, "//ul[@id='image-squares-8']//li")
for print in prints:
    print.click()
    break
# add the product in your cart
add_to_cart_btn = driver.find_element(By.ID, "add-to-cart-button-24")
add_to_cart_btn.click()

# go to your cart
shoppingcart_btn = driver.find_element(By.ID, "topcartlink")
shoppingcart_btn.click()


def proceed_to_checkout():
    # accept term of services
    checkbox = driver.find_element(By.ID, "termsofservice")
    if checkbox.is_selected() != True:
        checkbox.click()
    # proceed to checkout
    checkout_btn = driver.find_element(By.ID, "checkout")
    checkout_btn.click()


proceed_to_checkout()


def login(username, password):
    user_input = driver.find_element(By.ID, "Email")
    user_input.send_keys(username)
    password_input = driver.find_element(By.ID, "Password")
    password_input.send_keys(password)
    login_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Log in']")
    login_btn.click()


def register(username, password):
    registration_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Register']")
    registration_btn.click()
    select_gender = driver.find_element(By.ID, "gender-male")
    if (select_gender.is_selected() != True):
        select_gender.click()
    first_name = driver.find_element(By.ID, "FirstName")
    first_name.send_keys("Somesh")
    last_name = driver.find_element(By.ID, "LastName")
    last_name.send_keys("Thakur")
    email = driver.find_element(By.ID, "Email")
    email.clear()
    email.send_keys(username)
    password_input = driver.find_element(By.ID, "Password")
    password_input.send_keys(password)
    confirm_password_input = driver.find_element(By.ID, "ConfirmPassword")
    confirm_password_input.send_keys(password)
    register_btn = driver.find_element(By.ID, "register-button")
    register_btn.click()


# login or register to checkout
username = "sonu@gmail.com"
password = "Somesh"
login(username, password)
# register(username, password)
proceed_to_checkout()


def give_shipping_address():
    country_dropdown = driver.find_element(By.ID, "BillingNewAddress_CountryId")
    country_options = Select(country_dropdown)
    country_options.select_by_visible_text("India")
    city = driver.find_element(By.ID, "BillingNewAddress_City")
    city.send_keys("Bengaluru")
    address1 = driver.find_element(By.ID, "BillingNewAddress_Address1")
    address1.send_keys("JP Nagar")
    postal_code = driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode")
    postal_code.send_keys("560076")
    billing_address_phone = driver.find_element(By.ID, "BillingNewAddress_PhoneNumber")
    billing_address_phone.send_keys("6200475847")
    continue_btn = (driver.find_element(By.XPATH,
                                        "//button[@onclick='if (!window.__cfRLUnblockHandlers) return false; Billing.save()']"))
    continue_btn.click()


# give_shipping_address()

def select_shipping_method():
    continue_btn = driver.find_element(By.XPATH, "//button[@class='button-1 shipping-method-next-step-button']")
    continue_btn.click()


select_shipping_method()
# def ship_to_the_same_address():

time.sleep(20)
