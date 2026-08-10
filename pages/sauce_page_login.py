from playwright.sync_api import Page

class login_page:

    def __init__(self, page: Page):
        self.user_name = page.locator('[data-test="username"]')
        self.pass_word = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')

    def enter_user(self, user_name):
        self.user_name.fill(user_name)

    def enter_password(self, pass_word):
        self.pass_word.fill(pass_word)

    def click_login_button(self):
        self.login_button.click()

    def login_action(self, user_name, pass_word):
        self.user_name.fill(user_name)
        self.pass_word.fill(pass_word)
        self.login_button.click()
