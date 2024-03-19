import pytest
from selene import browser, be, have


@pytest.fixture(scope="session")
def chrome():
    browser.config.driver_name = 'chrome'
    browser.config.base_url = 'https://google.com'
    browser.config.window_height = 932
    browser.config.window_width = 430
    print("Открываем браузер!")
    yield
    print("Закрываем браузер!")


def test_google_search_extended_positive(chrome):
    browser.open('/')
    browser.element('[name="q"]').should(be.blank).type('Погода Пхукет').press_enter()
    browser.element('[id="search"]').should(have.text('Погода в Пхукете на сегодня'))


def test_google_search_extended_negative(chrome):
    browser.open('/')
    browser.element('[name="q"]').should(be.blank).type('аек57нувчпаке5кв').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
