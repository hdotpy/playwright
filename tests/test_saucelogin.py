from playwright.sync_api import Page, expect
from pages.saucedemo_login_page import LoginPage
from pages.saucedemo_product_page import ProductPage


def test_example(page: Page):

    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    page.get_by_role("button", name="Open Menu").click()
    page.locator("[data-test=\"logout-sidebar-link\"]").click()

    login_page = LoginPage(page)
    login_page.login()

    product_page = ProductPage(page)
    expect(product_page.get_title()).to_be_visible()
    product_page.logout()
