from playwright.sync_api import Page


class LandingPage:
    def __init__(self, page: Page):
        self.page = page
        self.dashboard = page.get_by_role("heading", name="Dashboard")

    def dashboard_is_visible(self):
        return self.dashboard
