from playwright.sync_api import Page, expect


def test_saucedemo(page: Page):

    page.goto("https://www.saucedemo.com/")

    # login process
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    expect(page).to_have_title("Swag Labs")
    page.wait_for_timeout(2000)

    products = page.locator(".inventory_item").all()

    for product in products:
        name = product.locator(".inventory_item_name").text_content()
        price = product.locator(".inventory_item_price").text_content()
        add_to_cart = product.get_by_text("Add to cart")
        add_to_cart.click()
        print(f"{name} with {price} is added to cart")

    shopping_cart_bage = page.locator(".shopping_cart_badge")
    expect(shopping_cart_bage).to_have_text("6")
    page.locator(".product_sort_container").select_option(
        "Price (high to low)")
    page.locator(".shopping_cart_link").click()
    page.get_by_text("Checkout").click()
    page.locator("#first-name").fill("User")
    page.locator("#last-name").fill("User")
    page.locator("#postal-code").fill("100123")
    page.get_by_text("Continue").click()
    page.get_by_text("Finish").click()
    page.screenshot(path="success.png", full_page=True)

    page.wait_for_timeout(5000)
