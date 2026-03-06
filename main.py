import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from config import BASE_URL, USERNAME, PASSWORD, PRODUCT_NAMES, PRODUCT_PRICES, SORT_OPTIONS
from utils.screenshot import take_screenshot


def perform_login(page):
    login_page = LoginPage(page)
    login_page.open(BASE_URL)
    login_page.login(USERNAME, PASSWORD)
    return login_page


def test_login_flow(page):
    """Test successful login to saucedemo.com."""
    login_page = perform_login(page)
    login_page.verify_login_success()
    take_screenshot(page, "test_login_flow")


#Assignment 
def test_add_fleece_jacket_to_cart(page):
    """Test adding Sauce Labs Fleece Jacket to cart and verifying it."""
    #Log in
    perform_login(page)
    expect(page).to_have_url(f"{BASE_URL}/inventory.html")
    page.wait_for_timeout(1500)

    # Add Fleece Jacket to cart
    inventory_page = InventoryPage(page)
    inventory_page.add_product_to_cart("sauce-labs-fleece-jacket")

    # Verify cart badge shows 1 item
    expect(inventory_page.get_cart_badge()).to_have_text("1")

    # Go to cart
    inventory_page.go_to_cart()
    expect(page).to_have_url(f"{BASE_URL}/cart.html")

    # Verify the correct product is in the cart
    cart_page = CartPage(page)
    cart_page.verify_product_in_cart("Sauce Labs Fleece Jacket")
    take_screenshot(page, "test_add_fleece_jacket_to_cart")


@pytest.mark.parametrize("sort_value,sort_name", SORT_OPTIONS)
def test_product_sorting(page, sort_value, sort_name):
    """Test that products are sorted correctly based on the selected sort option."""
    # Login first
    perform_login(page)
    expect(page).to_have_url(f"{BASE_URL}/inventory.html")
    page.wait_for_timeout(1500)

    # Select sort option
    inventory_page = InventoryPage(page)
    inventory_page.select_sort_option(sort_value)
    print(f"Selected sort option: {sort_name}")

    if sort_value == "az":
        expected = sorted(PRODUCT_NAMES)
        actual = inventory_page.get_product_names()
        assert actual == expected, f"Expected: {expected}, but got: {actual}"

    elif sort_value == "za":
        # Sort names Z-A and compare
        expected = sorted(PRODUCT_NAMES, reverse=True)
        actual = inventory_page.get_product_names()
        assert actual == expected, f"Expected: {expected}, but got: {actual}"

    elif sort_value == "lohi":
        # Sort prices low to high and compare
        expected = sorted(PRODUCT_PRICES)
        actual = inventory_page.get_product_prices()
        assert actual == expected, f"Expected: {expected}, but got: {actual}"

    elif sort_value == "hilo":
        # Sort prices high to low and compare
        expected = sorted(PRODUCT_PRICES, reverse=True)
        actual = inventory_page.get_product_prices()
        assert actual == expected, f"Expected: {expected}, but got: {actual}"

    print(f"✓ Sort option '{sort_name}' working correctly")
    take_screenshot(page, f"test_product_sorting_{sort_value}")
