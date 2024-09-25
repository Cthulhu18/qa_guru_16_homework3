import pytest
from selene import browser, be, have


@pytest.fixture(scope="module")
def setup_browser():
    # Настройка браузера перед тестами
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 1280
    browser.config.window_height = 720
    browser.open('https://www.google.com/ncr')  # Ссылка на международную версию Google
    yield
    # Завершение работы браузера после тестов
    browser.quit()


def test_google_search_with_results(setup_browser):
    # Ввод запроса и нажатие Enter
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()

    # Проверка результата поиска
    browser.element('[id="search"]').should(have.text('oriented Web UI browser tests in Python'))



def test_google_search_without_results(setup_browser):
    search_string = 'zxyqlvnwrp23847hfglxq'

    # Очистка поисковой строки перед вводом нового запроса
    browser.element('[name="q"]').clear().type(search_string).press_enter()

    # Проверка результата поиска
    browser.element('//p[@role="heading"]').should(have.text(f'Your search - {search_string} - did not match any documents.'))