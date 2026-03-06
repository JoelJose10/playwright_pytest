class CartPage:

    def __init__(self, page):
        self.page = page
        self._cart_item = page.locator(".cart_item")
        self._product_name = page.locator(".inventory_item_name")

    def is_cart_item_visible(self):
        """Check if cart item is visible."""
        return self._cart_item.is_visible()

    def get_product_name(self):
        """Get the product name in the cart."""
        return self._product_name.text_content()

    def verify_product_in_cart(self, expected_name):
        """Verify a specific product is in the cart."""
        assert self._cart_item.is_visible(), "Cart item not visible"
        actual_name = self._product_name.text_content()
        assert actual_name == expected_name, f"Expected: {expected_name}, got: {actual_name}"
