import pytest
import allure
from playwright.sync_api import sync_playwright

# @pytest.fixture(scope="session")
# def browser():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         yield browser
#         browser.close()

# @pytest.fixture
# def page(browser):
#     page = browser.new_page()
#     yield page
#     page.close()
# @pytest.fixture(scope="module")
# def browser():
#     with sync_playwright() as P:
#         browser=p.chromium.launch(headless=False)
#         yield browser
#         brower.close()
# @pytest.fixture
# def page(browser):
#     page=.browser.new_page()
#     yield page
#     page.close()
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:
            allure.attach(
                page.screenshot(),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )