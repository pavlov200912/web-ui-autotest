from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class YaSearchPage:
    URL = "https://ya.ru/"

    SEARCH_INPUT = (By.NAME, 'text')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self, query):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(query + Keys.RETURN)

class YaImageSearch:
    IMAGES_TAB = (By.CLASS_NAME, 'service_name_images')
    LINK = (By.CLASS_NAME, 'link')
    SEARCH_ITEM = (By.CLASS_NAME, 'serp-item')
    LINK_TAG = (By.TAG_NAME, 'a')
    IMAGE_SEARCH = (By.CLASS_NAME, 'MMViewerButtons-SearchByImage')
    CARD_TITLE = (By.CLASS_NAME, 'CbirObjectResponse-Title')

    def __init__(self, browser):
        self.browser = browser

    def load_images(self):
        images_btn = self.browser.find_element(*self.IMAGES_TAB).find_element(*self.LINK)
        images_btn.click()
        # link opened in the new tab, go there
        self.browser.switch_to.window(self.browser.window_handles[1])

    def load_image(self):
        image_preview = self.browser.find_elements(*self.SEARCH_ITEM)[0].find_element(*self.LINK_TAG)
        image_preview.click()

    def search_by_image(self):
        image_search = self.browser.find_element(*self.IMAGE_SEARCH)
        image_search.click()

    def card_title(self):
        return self.browser.find_element(*self.CARD_TITLE).text