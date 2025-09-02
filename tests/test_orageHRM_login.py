from playwright.sync_api import Page, expect
from pages.orangeHRM_loginPage import LoginPage
from pages.orangeHRM_landingPage import LandingPage


def test_example(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    loginpage = LoginPage(page)
    loginpage.login_user()

    landingpage = LandingPage(page)
    expect(landingpage.dashboard_is_visible()).to_be_visible()
