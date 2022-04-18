import pytest
import selenium.webdriver

@pytest.fixture
def browser():
    b = selenium.webdriver.Firefox()
    b.implicitly_wait(10)
    yield b
    b.quit()