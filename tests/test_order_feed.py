from pages.feed_page import FeedPage


class TestOrderFeed:
    def test_open_order_details_from_feed(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open()
        feed_page.click_order()
        assert feed_page.is_order_details_visible()

    def test_user_orders_appear_in_feed(self, driver, login_user, create_order):
        feed_page = FeedPage(driver)
        feed_page.open()
        assert feed_page.has_order_from_user(create_order)

    def test_total_done_counter_increases(self, driver, login_user, request):
        feed_page = FeedPage(driver)
        feed_page.open()
        before = feed_page.get_total_done()
        request.getfixturevalue("create_order")
        feed_page.open()
        after = feed_page.get_total_done()
        assert after > before

    def test_today_done_counter_increases(self, driver, login_user, request):
        feed_page = FeedPage(driver)
        feed_page.open()
        before = FeedPage(driver).get_today_done()
        request.getfixturevalue("create_order")
        feed_page.open()
        after = feed_page.get_today_done()
        assert after > before

    def test_new_order_appears_in_progress(self, driver, login_user, create_order):
        feed_page = FeedPage(driver)
        feed_page.open()
        assert feed_page.is_order_in_progress(create_order)
