from locators import LoginLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    url = "https://stellarburgers.nomoreparties.site/login"

    def go_to_reset_password_page(self):
        self.click(LoginLocators.RESET_LINK)

    def is_login_form_visible(self):
        return self.is_visible(LoginLocators.LOGIN_FORM)
