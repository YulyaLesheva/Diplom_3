import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.main_page import MainPage
from utils.user_api import delete_test_user, create_test_user, login


@pytest.fixture(params=["firefox", "chrome"], scope="function")
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def login_user(driver):
    user = create_test_user()
    login(driver, user)
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(MainPage.url))
    yield user
    delete_test_user(user)


@pytest.fixture
def create_order(driver, login_user):
    from pages.main_page import MainPage

    page = MainPage(driver)
    page.open()
    page.add_ingredient_to_burger()
    page.click_place_order_button()

    def order_number_is_valid(driver):
        order_number = page.get_order_number()
        return order_number and order_number != "9999"

    WebDriverWait(driver, timeout=5).until(order_number_is_valid)
    return page.get_order_number()
