from base import base
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

TESTING_APP_LINK = "https://www.artlebedev.ru/case/"


class TestTextConverter(base.BaseSeleniumTestCase):
    name = "Text Converter"

    def test_convert_to_uppercase(self):
        TEXT_TO_CONVERT = "текст должен быть в верхнем регистре"
        CONVERTED_TEXT = TEXT_TO_CONVERT.upper()

        self.driver.get(TESTING_APP_LINK)

        to_uppercase_button = self.driver \
            .find_element_by_link_text("ВЕРХНИЙ РЕГИСТР")
        self.driver.execute_script(
            "arguments[0].click();", to_uppercase_button)

        source_textarea = self.driver.find_element_by_name("source")
        result_textarea = self.driver.find_element_by_name("target")

        source_textarea.send_keys(TEXT_TO_CONVERT)

        assert result_textarea.get_attribute("value") == CONVERTED_TEXT

    def test_convert_to_lowercase(self):
        TEXT_TO_CONVERT = "ТЕКСТ ДОЛЖЕН БЫТЬ В НИЖНЕМ РЕГИСТРЕ"
        CONVERTED_TEXT = TEXT_TO_CONVERT.lower()

        self.driver.get(TESTING_APP_LINK)

        to_lowercase_button = self.driver \
            .find_element_by_link_text("нижний регистр")
        self.driver.execute_script(
            "arguments[0].click();", to_lowercase_button)

        source_textarea = self.driver.find_element_by_name("source")
        result_textarea = self.driver.find_element_by_name("target")

        source_textarea.send_keys(TEXT_TO_CONVERT)

        assert result_textarea.get_attribute("value") == CONVERTED_TEXT
    
    def test_capitalization(self):
        TEXT_TO_CONVERT = "слова должны начинатся с заглавной буквы"
        CONVERTED_TEXT = TEXT_TO_CONVERT.title()

        self.driver.get(TESTING_APP_LINK)

        capitalize_button = self.driver \
            .find_element_by_link_text("Заглавные Буквы")
        self.driver.execute_script(
            "arguments[0].click();", capitalize_button)

        source_textarea = self.driver.find_element_by_name("source")
        result_textarea = self.driver.find_element_by_name("target")

        source_textarea.send_keys(TEXT_TO_CONVERT)

        assert result_textarea.get_attribute("value") == CONVERTED_TEXT
    
    def test_case_invert(self):
        TEXT_TO_CONVERT = "РеГиСтр долЖен быть ИнверТиРОван"
        CONVERTED_TEXT = TEXT_TO_CONVERT.swapcase()

        self.driver.get(TESTING_APP_LINK)

        invert_case_button = self.driver \
            .find_element_by_link_text("иНВЕРСИЯ рЕГИСТРА")
        self.driver.execute_script(
            "arguments[0].click();", invert_case_button)

        source_textarea = self.driver.find_element_by_name("source")
        result_textarea = self.driver.find_element_by_name("target")

        source_textarea.send_keys(TEXT_TO_CONVERT)

        assert result_textarea.get_attribute("value") == CONVERTED_TEXT
    
    def test_sentence_capitalization(self):
        TEXT_TO_CONVERT = "каждое предложение. должно. начинаться с заглавной."
        CONVERTED_TEXT = "Каждое предложение. Должно. Начинаться с заглавной."

        self.driver.get(TESTING_APP_LINK)

        capitalize_sentences_button = self.driver \
            .find_element_by_link_text("По предложениям")
        self.driver.execute_script(
            "arguments[0].click();", capitalize_sentences_button)

        source_textarea = self.driver.find_element_by_name("source")
        result_textarea = self.driver.find_element_by_name("target")

        source_textarea.send_keys(TEXT_TO_CONVERT)

        assert result_textarea.get_attribute("value") == CONVERTED_TEXT