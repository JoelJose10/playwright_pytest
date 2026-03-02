
import pytest
from playwright.sync_api import expect


# Credentials for Sauce Demo
VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"
BASE_URL = "https://www.saucedemo.com"

# product names 
PRODUCT_NAMES = [
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Fleece Jacket",
    "Sauce Labs Onesie",
    "Test.allTheThings() T-Shirt (Red)",
]

#  product prices
PRODUCT_PRICES = [29.99, 9.99, 15.99, 49.99, 7.99, 15.99]

# Sort options available on saucedemo.com
SORT_OPTIONS = [
    ("az", "Name (A to Z)"),
    ("za", "Name (Z to A)"),
    ("lohi", "Price (low to high)"),
    ("hilo", "Price (high to low)"),
]

def test_login_flow(page):
    page.goto(BASE_URL)
    page.fill("#user-name", VALID_USERNAME)
    page.fill("#password", VALID_PASSWORD)
    # page.wait_for_timeout(500)
    page.click("#login-button")

#Assignment 
def test_add_fleece_jacket_to_cart(page):
    """Test adding Sauce Labs Fleece Jacket to cart and verifying it."""
    #Log in
    test_login_flow(page)
    expect(page).to_have_url(f"{BASE_URL}/inventory.html")
    # page.wait_for_timeout(1500)

    #Adding Sauce Labs Fleece Jacket to cart
    page.click('[data-test="add-to-cart-sauce-labs-fleece-jacket"]')
    # page.wait_for_timeout(1500)

    #Verify cart badge shows 1 item
    cart_badge = page.locator(".shopping_cart_badge")
    expect(cart_badge).to_have_text("1")
    # page.wait_for_timeout(1500)

    # Go to cart
    page.click(".shopping_cart_link")
    expect(page).to_have_url(f"{BASE_URL}/cart.html")
    # page.wait_for_timeout(1500)

    #Verify the correct product is in the cart
    cart_item = page.locator(".cart_item")
    expect(cart_item).to_be_visible()

    product_name = page.locator(".inventory_item_name")
    expect(product_name).to_have_text("Sauce Labs Fleece Jacket")
    # page.wait_for_timeout(2000)


@pytest.mark.parametrize("sort_value,sort_name", SORT_OPTIONS)
def test_product_sorting(page, sort_value, sort_name):
    """Test that products are sorted correctly based on the selected sort option."""
    # Login first
    test_login_flow(page)
    expect(page).to_have_url(f"{BASE_URL}/inventory.html")
    # page.wait_for_timeout(1500)

    # Select the sort option from dropdown
    page.select_option(".product_sort_container", sort_value)
    print(f"Selected sort option: {sort_name}")

    if sort_value == "az":
        # Sort names A-Z and compare
        expected = sorted(PRODUCT_NAMES)
        actual = page.locator(".inventory_item_name").all_text_contents()
        # print(f"Expected: {expected}")
        # print(f"Actual:   {actual}")
        assert actual == expected, f"Expected: {expected}, but got: {actual}"

    elif sort_value == "za":
        # Sort names Z-A and compare
        expected = sorted(PRODUCT_NAMES, reverse=True)
        actual = page.locator(".inventory_item_name").all_text_contents()
        # print(f"Expected: {expected}")
        # print(f"Actual:   {actual}")
        assert actual == expected, f"Expected: {expected}, but got: {actual}"

    elif sort_value == "lohi":
        # Sort prices low to high and compare
        expected = sorted(PRODUCT_PRICES)
        price_texts = page.locator(".inventory_item_price").all_text_contents()
        actual = [float(price.replace("$", "")) for price in price_texts]
        # print(f"Expected: {expected}")
        # print(f"Actual:   {actual}")
        assert actual == expected, f"Expected: {expected}, but got: {actual}"

    elif sort_value == "hilo":
        # Sort prices high to low and compare
        expected = sorted(PRODUCT_PRICES, reverse=True)
        price_texts = page.locator(".inventory_item_price").all_text_contents()
        actual = [float(price.replace("$", "")) for price in price_texts]
        # print(f"Expected: {expected}")
        # print(f"Actual:   {actual}")
        assert actual == expected, f"Expected: {expected}, but got: {actual}"

    print(f"✓ Sort option '{sort_name}' working correctly")