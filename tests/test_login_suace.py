import allure
from playwright.sync_api import expect

from pages.sauce_page_login import login_page
from pages.sauce_inventoty_page import inventory
from pages.sauce_checkout_page import checkoutpage
from pages.sauce_addresspage import enteraddress


@allure.title("Verify End-to-End Order Placement")
@allure.description(
    "Verify user can login, add products, checkout and place an order successfully."
)
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("E-Commerce")
@allure.story("Place Order")
def test_login(page):

    with allure.step("Launch SauceDemo application"):
        page.goto("https://www.saucedemo.com/")

    with allure.step("Login with valid credentials"):
        loginpage = login_page(page)
        loginpage.enter_user("standard_user")
        loginpage.enter_password("secret_sauce")
        loginpage.click_login_button()

    with allure.step("Verify inventory page is displayed"):
        expect(page).to_have_url(
            "https://www.saucedemo.com/inventory.html"
        )

    with allure.step("Add Backpack to cart"):
        inventorypage = inventory(page)
        inventorypage.add_backpack()

    with allure.step("Add Bike Light to cart"):
        inventorypage.add_bikelight()

    with allure.step("Navigate to cart"):
        checkoutpages = checkoutpage(page)
        checkoutpages.go_to_cart()
    with allure.step("Proceed to checkout"):
        checkoutpages.checkout_cart()

    with allure.step("Enter shipping details"):
        addressinformation = enteraddress(page)
        addressinformation.enter_firstname("anil")
        addressinformation.enter_lastname("lina")
        addressinformation.enter_postalcode("7462346")

    with allure.step("Continue checkout"):
        page.locator("#continue").click()

    with allure.step("Complete order"):
        page.locator('[data-test="finish"]').click()

    with allure.step("Verify order confirmation"):
        expect(
            page.get_by_text("Thank you for your order!")
        ).to_be_visible()

        expect(
            page.get_by_text(
                "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
            )
        ).to_be_visible()

    with allure.step("Capture final confirmation screenshot"):
        allure.attach(
            page.screenshot(),
            name="Order Confirmation",
            attachment_type=allure.attachment_type.PNG
        )

    allure.attach(
        page.url,
        name="Final URL",
        attachment_type=allure.attachment_type.TEXT
    )