from pages.search import YaSearchPage
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

