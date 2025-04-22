import allure
from locators import ProfileLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    url = "https://stellarburgers.nomoreparties.site/account/profile"

    def go_to_order_history(self):
        with allure.step("Переход во вкладку 'История заказов'"):
            self.click(ProfileLocators.ORDER_HISTORY_TAB)

    def is_order_history_visible(self):
        with allure.step("Проверка, что отображается история заказов"):
            return self.is_visible(ProfileLocators.ORDER_HISTORY_BLOCK)

    def logout(self):
        with allure.step("Выход из личного кабинета"):
            self.click(ProfileLocators.LOGOUT_BUTTON)
