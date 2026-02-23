
from playwright.sync_api import expect


# Credentials for Sauce Demo
VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"
BASE_URL = "https://www.saucedemo.com"

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