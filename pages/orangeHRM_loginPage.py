from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role(
            "textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")

    def login_user(self):
        self.username_input.fill("Admin")
        self.password_input.fill("admin123")
        self.login_button.click()
