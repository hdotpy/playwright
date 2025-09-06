import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    page = browser.new_page(viewport={"width": 1920, "height": 1080}  # Emulates start-maximized
                            )
    yield page
    page.close()
