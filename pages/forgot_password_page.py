from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import ResetPasswordLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    url = "https://stellarburgers.nomoreparties.site/forgot-password"

    def enter_email(self, email):
        self.type(ResetPasswordLocators.EMAIL_INPUT, email)

    def click_restore_button(self):
        self.click(ResetPasswordLocators.RESTORE_BUTTON)

    def toggle_password_visibility(self):
        icon = self.wait_for_element_visible(ResetPasswordLocators.SHOW_PASSWORD_ICON)
        self.driver.execute_script("arguments[0].click();", icon)

    def password_field_type(self):
        input_password = self.wait_for_element_visible(ResetPasswordLocators.RESET_PASSWORD_INPUT)
        return input_password.get_attribute("type")
    