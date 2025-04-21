from abc import abstractmethod

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @property
    @abstractmethod
    def url(self): ...

    def open(self):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(self.url))

    def is_opened(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(self.url))

    def click(self, locator):
        WebDriverWait(self.driver, timeout=10).until(expected_conditions.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def is_visible(self, locator):
        WebDriverWait(self.driver, timeout=5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).is_displayed()

    def is_closed(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
        return not self.driver.find_element(*locator).is_displayed()

    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def get_text(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text

    def drag_and_drop(self, source_locator, target_locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)

        source = wait.until(EC.presence_of_element_located(source_locator))
        target = wait.until(EC.presence_of_element_located(target_locator))

        actions = ActionChains(self.driver)
        actions.click_and_hold(source).move_to_element(target).release().perform()
