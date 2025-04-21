from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage

from locators import MainLocators


class MainPage(BasePage):
    url = "https://stellarburgers.nomoreparties.site/"

    def click_profile_button(self):
        self.click(MainLocators.PROFILE_BUTTON)

    def click_constructor_button(self):
        self.click(MainLocators.CONSTRUCTOR_BUTTON)

    def is_constructor_visible(self):
        return self.is_visible(MainLocators.BUN_SECTION)

    def click_order_feed_button(self):
        self.click(MainLocators.FEED_BUTTON)

    def click_ingredient(self):
        self.click(MainLocators.INGREDIENT)

    def is_ingredient_details_visible(self):
        return self.is_visible(MainLocators.INGREDIENT_DETAILS)

    def close_ingredient_details(self):
        self.click(MainLocators.INGREDIENT_DETAILS_CLOSE_BUTTON)

    def is_ingredient_details_closed(self):
        return self.is_closed(MainLocators.INGREDIENT_DETAILS)

    def add_ingredient_to_burger(self):
        self.drag_and_drop(MainLocators.INGREDIENT, MainLocators.BASKET_LIST)

    def is_ingredient_counter_incremented(self):
        return int(self.get_text(MainLocators.INGREDIENT_COUNTER)) > 0

    def click_place_order_button(self):
        self.click(MainLocators.PLACE_ORDER_BUTTON)

    def is_order_details_visible(self):
        return self.is_visible(MainLocators.ORDER_DETAILS)

    def get_order_number(self):
        return self.get_text(MainLocators.ORDER_NUMBER)
