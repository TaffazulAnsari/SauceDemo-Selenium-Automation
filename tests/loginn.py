
import os

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


BASE_URL = os.getenv(
    "BASE_URL", "https://www.saucedemo.com/"
)
USERNAME = os.getenv("STANDARD_USER", "standard_user")
PASSWORD = os.getenv("STANDARD_PASSWORD", "secret_sauce")
LOCKED_USER = os.getenv("LOCKED_OUT_USER", "locked_out_user")
WAIT_SECONDS = int(os.getenv("WAIT_SECONDS", "10"))


@pytest.fixture
def driver():
    """Start a fresh Chrome browser for every test."""
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1440,1000")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    if os.getenv("HEADLESS", "false").lower() in (
        "true", "1", "yes"
    ):
        options.add_argument("--headless=new")

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(0)

    yield browser

    browser.quit()


def wait_for(driver, locator):
    """Wait until an element becomes visible."""
    return WebDriverWait(driver, WAIT_SECONDS).until(
        EC.visibility_of_element_located(locator)
    )


def login(driver, username):
    """Log in to SauceDemo with the specified username."""
    driver.get(BASE_URL)

    wait_for(driver, (By.ID, "user-name")).send_keys(username)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()


def test_login_with_valid_credentials(driver):
    """Test 1: Verify successful login."""
    login(driver, USERNAME)

    wait_for(driver, (By.CLASS_NAME, "inventory_list"))

    assert driver.current_url.endswith("/inventory.html")
    assert wait_for(
        driver, (By.CLASS_NAME, "title")
    ).text == "Products"


def test_add_item_to_cart_and_complete_checkout(driver):
    """Test 2: Add a product and complete the checkout flow."""
    login(driver, USERNAME)

    # Add Sauce Labs Backpack to the cart.
    wait_for(
        driver, (By.ID, "add-to-cart-sauce-labs-backpack")
    ).click()

    # Verify the cart count.
    assert wait_for(
        driver, (By.CLASS_NAME, "shopping_cart_badge")
    ).text == "1"

    # Open the cart and verify the product.
    driver.find_element(
        By.CLASS_NAME, "shopping_cart_link"
    ).click()

    assert wait_for(
        driver, (By.CLASS_NAME, "inventory_item_name")
    ).text == "Sauce Labs Backpack"

    # Start checkout.
    driver.find_element(By.ID, "checkout").click()

    # Enter checkout information.
    wait_for(driver, (By.ID, "first-name")).send_keys("Test")
    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("12345")

    driver.find_element(By.ID, "continue").click()

    # Complete the order.
    wait_for(driver, (By.ID, "finish")).click()

    # Verify order confirmation.
    confirmation = wait_for(
        driver, (By.CLASS_NAME, "complete-header")
    ).text

    assert confirmation == "Thank you for your order!"
    assert driver.current_url.endswith("/checkout-complete.html")


def test_locked_out_user_sees_error_message(driver):
    """Test 3: Verify that a locked-out user cannot log in."""
    login(driver, LOCKED_USER)

    error = wait_for(
        driver, (By.CSS_SELECTOR, '[data-test="error"]')
    ).text

    assert "Sorry, this user has been locked out." in error
    assert not driver.current_url.endswith("/inventory.html")
