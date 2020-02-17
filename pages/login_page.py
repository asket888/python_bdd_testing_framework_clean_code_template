from behave.runner import Context
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    # static xpath. used as is
    _MAIN_PAGE_LOGIN_BUTTON = (By.XPATH, "//a[contains(@href,'login')]/span")
    _LOGIN_PAGE_LOGIN_BUTTON = (By.XPATH, "//button[@data-test='form-login-submit']")
    _LOGIN_PAGE_USERNAME = (By.NAME, "username")
    _LOGIN_PAGE_PASSWORD = (By.NAME, "password")

    def __init__(self, context: Context):
        super().__init__(context.driver, context.env)

    def login_with_correct_credentials(self):
        """
        Go to url set to config.json and login to application with correct parameters
        """
        self.goto_url(self.env["url"])
        self.click(self._MAIN_PAGE_LOGIN_BUTTON)
        self.fill(self._LOGIN_PAGE_USERNAME, self.env["login"])
        self.fill(self._LOGIN_PAGE_PASSWORD, self.env["password"])
        self.click(self._LOGIN_PAGE_LOGIN_BUTTON)
