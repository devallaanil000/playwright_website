from playwright.sync_api import Page

class checkoutpage:
    def __init__(self,page):
        self.cart=page.locator('[data-test="shopping-cart-link"]')
        self.checkout=page.locator('[data-test="checkout"]')
    def go_to_cart(self):
        self.cart.click()
    def checkout_cart(self):
        self.checkout.click()