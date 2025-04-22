import allure
from locators import LoginLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    url = "https://stellarburgers.nomoreparties.site/login"

    def go_to_reset_password_page(self):
        with allure.step("Переход на страницу восстановления пароля"):
            self.click(LoginLocators.RESET_LINK)

    def is_login_form_visible(self):
        with allure.step("Проверка, что форма входа отображается"):
            return self.is_visible(LoginLocators.LOGIN_FORM)
