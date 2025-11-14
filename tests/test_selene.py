from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_github():
    browser.open("https://github.com")

    s(".header-search-button").click()
    s("#query-builder-test").send_keys("eroshenkoam/allure-example").press_enter()
    #s(".header-search-input").submit()

    s(by.link_text("eroshenkoam/allure-example")).click()

    s(".fgColor-default").click()

    #s(by.partial_text("#testOps integration")).should(be.visible)
    browser.element('a[title*="#85"]').should(be.visible)
