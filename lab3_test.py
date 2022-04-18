from base import base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

TESTING_APP_LINK = "https://yandex.ru/"


class TestSearchSite(base.BaseSeleniumTestCase):
    name = "Search Site"

    def test_search_results(self):
        SEARCH_TEXT = "Тестирование поисковых систем"

        self.driver.get(TESTING_APP_LINK)

        search_input = self.driver.find_element_by_name('text')
        search_button = self.driver.find_element_by_xpath(
            '//button[normalize-space()="Найти"]')

        search_input.send_keys(SEARCH_TEXT)
        search_button.click()

        WebDriverWait(self.driver, timeout=10).until(
            expected_conditions.url_contains("search"))

        result_links = self.find_search_result_links(self.driver)
        window_handles = []
        links_text_occurrences = []
        for link in result_links:
            self.open_link(link)
            window_handles.append(self.driver.current_window_handle)
            links_text_occurrences.append(
                self.count_text_occurrences(SEARCH_TEXT))

        sorted_window_handles = [x for _, x in sorted(
            zip(links_text_occurrences, window_handles), reverse=True)]
        self.close_tabs(sorted_window_handles)

    def find_search_result_links(self, driver: WebDriver):
        result = []
        found_links = driver.find_elements(
            By.CSS_SELECTOR, "#search-result .Path a")
        for link in found_links:
            href = link.get_attribute("href")

            # Пропускаем рекламные ссылки
            if ("yabs.yandex.ru" in href):
                continue

            result.append(href)

        return result

    def open_link(self, link):
        self.open_new_tab()
        self.driver.get(link)

    def count_text_occurrences(self, text):
        found = self.driver.find_elements(
            By.XPATH, '//*[contains(text(), "{}")]'.format(text))
        return len(found)

    def close_tabs(self, window_handles):
        for window in window_handles:
            self.driver.switch_to.window(window)
            self.driver.close()
