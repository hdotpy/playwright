from playwright.sync_api import Page, expect


def test_rss_shopping(page: Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/")
    page.locator(".search-keyword").first.fill("ber")
    page.wait_for_timeout(2000)
    products = page.locator("div[class='product']").all()

    for product in products:
        product.get_by_text("ADD TO CART").click()

    expect(page.locator("span[class='cart-count']")).to_have_text("3")

    page.locator("a[class='cart-icon']").click()
    page.get_by_text("PROCEED TO CHECKOUT").click()
    page.locator("input[placeholder='Enter promo code']").fill("rahulshetty")
    page.get_by_text("Apply").click()
    page.wait_for_timeout(2000)
    page.get_by_text("Place Order").click()
    page.locator("select[style='width: 200px;']").select_option("India")
    page.locator(".chkAgree").check()
    page.get_by_text("Proceed").click()
