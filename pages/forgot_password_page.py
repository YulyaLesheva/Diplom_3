import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import ResetPasswordLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    url = "https://stellarburgers.nomoreparties.site/forgot-password"

    def enter_email(self, email):
        with allure.step(f"Ввод email: {email} в поле восстановления пароля"):
            self.type(ResetPasswordLocators.EMAIL_INPUT, email)

    def click_restore_button(self):
        with allure.step("Клик по кнопке 'Восстановить'"):
            self.click(ResetPasswordLocators.RESTORE_BUTTON)

    def toggle_password_visibility(self):
        with allure.step("Переключение видимости пароля"):
            icon = self.wait_for_element_visible(ResetPasswordLocators.SHOW_PASSWORD_ICON)
            self.driver.execute_script("arguments[0].click();", icon)

    def password_field_type(self):
        with allure.step("Получение типа поля для ввода нового пароля"):
            input_password = self.wait_for_element_visible(ResetPasswordLocators.RESET_PASSWORD_INPUT)
            return input_password.get_attribute("type")
