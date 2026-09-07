from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
from pages.sauce_page_login import login_page
from pages.sauce_inventoty_page import inventory
from pages.sauce_checkout_page import checkoutpage
from pages.sauce_addresspage import enteraddress
def test_login(page):
    page.goto("https://www.saucedemo.com/")
    loginpage=login_page(page)
    loginpage.enter_user("standard_user")
    loginpage.enter_password("secret_sauce")
    loginpage.click_login_button()
    inventorypage=inventory(page)
    inventorypage.add_backpack()
    inventorypage.add_bikelight()
    checkoutpages=checkoutpage(page)
    checkoutpages.go_to_cart()
    checkoutpages.checkout_cart()
    addressinformation=enteraddress(page)
    addressinformation.enter_firstname("anil")
    addressinformation.enter_lastname("lina")
    addressinformation.enter_postalcode("7462346")
    page.locator("#continue").click()
    page.locator('[data-test="finish"]').click()
    expect(page.get_by_text("Thank you for your order!")).to_be_visible()
    expect(page.get_by_text("Your order has been dispatched, and will arrive just as fast as the pony can get there!")).to_be_visible()