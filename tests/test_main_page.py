from pages.feed_page import FeedPage
from pages.main_page import MainPage


class TestMainPage:
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_constructor_button()
        assert main_page.is_constructor_visible()

    def test_go_to_order_feed(self, driver, login_user):
        MainPage(driver).click_order_feed_button()
        assert driver.current_url == FeedPage.url

    def test_open_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        assert main_page.is_ingredient_details_visible()

    def test_close_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        main_page.close_ingredient_details()
        assert main_page.is_ingredient_details_closed()

    def test_ingredient_counter_increment(self, driver):
        main_page = MainPage(driver)
        main_page.add_ingredient_to_burger()
        assert main_page.is_ingredient_counter_incremented()

    def test_create_order_when_logged_in(self, driver, login_user):
        main_page = MainPage(driver)
        main_page.add_ingredient_to_burger()
        main_page.click_place_order_button()
        assert MainPage(driver).is_order_details_visible()
