from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class YaResultPage:
    SEARCH_INPUT = (By.NAME, 'text')
    QUERY_RESULTS = (By.CLASS_NAME, 'serp-item')

    def __init__(self, browser):
        self.browser = browser

    def phrase_results_texts(self):
        phrase_results = self.browser.find_elements(*self.QUERY_RESULTS)
        return [res.text for res in phrase_results]

    def search(self, query):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(Keys.CONTROL + 'a')
        search_input.send_keys(Keys.DELETE)
        search_input.send_keys(query + Keys.RETURN)

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        return search_input.get_attribute('value')