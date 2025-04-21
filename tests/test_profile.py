from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class TestProfile:
    def test_go_to_profile(self, driver, login_user):
        MainPage(driver).click_profile_button()
        assert ProfilePage(driver).is_opened()

    def test_go_to_order_history(self, driver, login_user):
        MainPage(driver).click_profile_button()
        page = ProfilePage(driver)
        page.go_to_order_history()
        assert "order-history" in driver.current_url

    def test_logout(self, driver, login_user):
        MainPage(driver).click_profile_button()
        page = ProfilePage(driver)
        page.logout()
        assert LoginPage(driver).is_opened()
        