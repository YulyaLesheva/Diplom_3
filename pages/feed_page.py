from selenium.webdriver.common.by import By

from locators import FeedLocators
from pages.base_page import BasePage


class FeedPage(BasePage):
    url = "https://stellarburgers.nomoreparties.site/feed"

    def go_to_feed(self):
        self.click(FeedLocators.FEED_HEADER)

    def is_feed_loaded(self):
        return self.is_visible(FeedLocators.ORDER_STARTED_TEXT)

    def click_order(self):
        self.click(FeedLocators.ORDER)

    def is_order_details_visible(self):
        return self.is_visible(FeedLocators.ORDER_DETAILS)

    def has_order_from_user(self, order_number):
        xpath = FeedLocators.USER_ORDER.format(order_number)
        return self.is_visible((By.XPATH, xpath))

    def get_total_done(self):
        return int(self.get_text(FeedLocators.DONE_TOTAL))

    def get_today_done(self):
        return int(self.get_text(FeedLocators.DONE_TODAY))

    def is_order_in_progress(self, order_number):
        xpath = FeedLocators.USER_ORDER.format(order_number)
        return self.is_visible((By.XPATH, xpath))
