class LoginPage:

    def __init__(self, page):
        self.page = page
        self._input_username = page.locator("#user-name")
        self._input_password = page.locator("#password")
        self._login_button = page.locator("#login-button")

    def open(self, url):
        self.page.goto(url)

    def login(self, username, password):
        self._input_username.fill(username)
        self._input_password.fill(password)
        self._login_button.click()

    def verify_login_success(self):
        self.page.wait_for_selector(".inventory_list")
        assert "inventory" in self.page.url
