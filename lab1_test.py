from random import sample
from typing import Iterable, List
from base import base


class TestBrowserHandle(base.BaseSeleniumTestCase):
    name = "Browser Handle"

    def test_open_site_links(self):
        file_name = "lab1_in.txt"

        source_links = self.get_links_from_file(file_name)
        shuffled_links = sample(source_links, len(source_links))

        self.open_links(shuffled_links)

        self.close_tabs_backwards()

        self.update_file_content(file_name, shuffled_links)

    def get_links_from_file(self, file_name: str) -> list[str]:
        with open(file_name) as f:
            lines = f.read().splitlines()
            return lines

    def update_file_content(self, file_name: str, content_lines: Iterable[str]):
        with open(file_name, "w") as f:
            content = '\n'.join(content_lines)
            f.write(content)

    def open_links(self, links: Iterable[str]):
        self.driver.get(links[0])

        for link in links[1:]:
            self.open_new_tab()
            self.driver.get(link)

    def close_tabs_backwards(self):
        for window in reversed(self.driver.window_handles):
            self.driver.switch_to.window(window)
            self.driver.close()
