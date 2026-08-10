from playwright.sync_api import Page
class inventory:
    def __init__(self,page : Page):
        self.backpack=page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')
        self.bikelight=page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]')
    def add_backpack(self):
        self.backpack.click()
    def add_bikelight(self):
        self.bikelight.click()
