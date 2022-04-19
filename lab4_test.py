from os import link
import string
from turtle import pos
from base import base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

TESTING_APP_LINK = "https://davidwalsh.name/"


class TestBlogSite(base.BaseSeleniumTestCase):
    name = "Blog Site"

    def test_short_description(self):
        self.driver.get(TESTING_APP_LINK)

        found_posts = self.find_all_posts()
        posts_count = len(found_posts)
        equals_count = 0

        descriptions = []
        links = []
        for post in found_posts:
            descriptions.append(self.get_post_preview_description(post)[0:-3])
            links.append(self.get_post_link(post))

        for i in range(posts_count):
            post_link = links[i]
            description = descriptions[i].translate(
                {ord(c): None for c in string.whitespace})

            self.open_post(post_link)
            article_text = self.driver \
                .find_element(By.CSS_SELECTOR, "article") \
                .text \
                .translate({ord(c): None for c in string.whitespace})
            if (description in article_text):
                equals_count += 1

        assert posts_count == equals_count

    def find_all_posts(self):
        return self.driver.find_elements(By.CSS_SELECTOR, ".post-list > li:not(.vert)")

    def get_post_preview_description(self, post: WebElement):
        return post.find_element(By.CSS_SELECTOR, ".preview > p").text

    def get_post_link(self, post: WebElement):
        return post.find_element(By.CSS_SELECTOR, 'a[itemprop="url"]').get_attribute("href")

    def open_post(self, link):
        self.open_new_tab()
        self.driver.get(link)
