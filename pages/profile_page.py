from locators import ProfileLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    url = "https://stellarburgers.nomoreparties.site/account/profile"

    def go_to_order_history(self):
        self.click(ProfileLocators.ORDER_HISTORY_TAB)

    def is_order_history_visible(self):
        return self.is_visible(ProfileLocators.ORDER_HISTORY_BLOCK)

    def logout(self):
        self.click(ProfileLocators.LOGOUT_BUTTON)
        