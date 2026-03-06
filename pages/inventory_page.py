class InventoryPage:

    def __init__(self, page):
        self.page = page
        self._sort_dropdown = page.locator(".product_sort_container")
        self._product_names = page.locator(".inventory_item_name")
        self._product_prices = page.locator(".inventory_item_price")
        self._cart_badge = page.locator(".shopping_cart_badge")
        self._cart_link = page.locator(".shopping_cart_link")

    def add_product_to_cart(self, product_id):
        """Add a product to cart by its data-test id."""
        self.page.click(f'[data-test="add-to-cart-{product_id}"]')

    def select_sort_option(self, sort_value):
        """Select a sort option from the dropdown."""
        self._sort_dropdown.select_option(sort_value)

    def get_product_names(self):
        """Get all product names as a list."""
        return self._product_names.all_text_contents()

    def get_product_prices(self):
        """Get all product prices as a list of floats."""
        price_texts = self._product_prices.all_text_contents()
        return [float(price.replace("$", "")) for price in price_texts]

    def get_cart_badge(self):
        """Get the cart badge locator for assertions."""
        return self._cart_badge

    def get_cart_count(self):
        """Get the cart badge count as text."""
        return self._cart_badge.text_content()

    def go_to_cart(self):
        """Click on the cart link."""
        self._cart_link.click()
