from selenium.webdriver.common.by import By

from pages.search import YaSearchPage, YaImageSearch
from pages.result import YaResultPage

def test_basic_ya_search(browser):
    QUERY = 'панда'
    search_page = YaSearchPage(browser)
    search_page.load()
    search_page.search(QUERY)

    result_page = YaResultPage(browser)
    assert QUERY == result_page.search_input_value()
    for res_text in result_page.phrase_results_texts():
        assert QUERY in res_text.lower()

def test_complicated_ya_search(browser):
    # search with adds or some additional information
    QUERY = 'россия'
    search_page = YaSearchPage(browser)
    search_page.load()
    search_page.search(QUERY)

    result_page = YaResultPage(browser)
    assert QUERY == result_page.search_input_value()
    count_query = 0
    for res_text in result_page.phrase_results_texts():
        count_query += int(QUERY in res_text.lower())
    assert count_query > 0

def test_image_search(browser):
    QUERY = 'лошадь'

    # Search for query in the engine
    search_page = YaSearchPage(browser)
    search_page.load()
    search_page.search(QUERY)

    # Load query images
    image_search = YaImageSearch(browser)
    image_search.load_images()
    # Open the first image
    image_search.load_image()
    # Search in the engine by this image
    image_search.search_by_image()
    # Check that result contains query in the title
    assert QUERY in image_search.card_title().lower()



