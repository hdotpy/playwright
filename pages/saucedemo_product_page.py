from playwright.sync_api import Page


class ProductPage:

    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator("[data-test=\"title\"]")
        self.menu_options = page.get_by_role("button", name="Open Menu")
        self.logout_button = page.locator(
            "[data-test=\"logout-sidebar-link\"]")

    def get_title(self):
        return self.title

    def logout(self):
        self.menu_options.click()
        self.logout_button.click()
