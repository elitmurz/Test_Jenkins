import allure
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from driver import driver
from selene import Browser, Config





def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(body=html, name='page_source', attachment_type=AttachmentType.HTML, extension='.html')


def add_video(browser):
    video_url = f"https://selenoid.autotests.cloud/video/{browser.driver.session_id}.mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(body=html, name='video_' + browser.driver.session_id, attachment_type=AttachmentType.HTML,
                  extension='.html')

    browser = Browser(Config(driver))
    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()