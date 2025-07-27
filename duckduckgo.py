from selene import browser, be, have

def test_duckduckgo(open_duckduckgo):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('GitHub - yashaka/selene: User-oriented Web UI browser tests in Python'))

def test_search(open_duckduckgo):
    browser.element('[name="q"]').type('hkjhkhkjhkjhkjgjhgfjgfghfhgfhfgfghfgh').press_enter()
    browser.element('html').should(have.text('По запросу «hkjhkhkjhkjhkjgjhgfjgfghfhgfhfgfghfgh» ничего не найдено.'))