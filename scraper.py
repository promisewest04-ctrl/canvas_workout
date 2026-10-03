from playwright.sync_api import sync_playwright
from playwright_stealth import Stealth
from bs4 import BeautifulSoup
from random import randint

with sync_playwright() as p:
    url = "https://jumia.com.ng"
    browser = p.chromium.launch(
        headless=False,
        channel="chrome",
        args=[
            "--disable-blink-features=AutomationControlled",
            "--start-maximmized",
            "--no-sandbox",
            "--disable-infobars"
        ]
    )
    context = browser.new_context(
        viewport={"width": 1366, "height": 768},
        user_agent="Mozilla/5.0 (windows NT 10.0; win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        locale="en-US"
    )
    page = context.new_page()

    page.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        });
    """)
    Stealth().apply_stealth_sync(page)

    print("Navigating to page....")
    page.goto(url, wait_until="domcontentloaded", timeout=60000)

    page.wait_for_timeout(randint(1500, 3500))

    html = page.content()
    print(f"Page title: {page.title()}")
    input("Press Enter in terminal to close")

    # Handle cookies banner
    try:
        btn = page.locator("#consentForm button[value='all']").evaluate("el => el.click()")
        # btn.wait_for(state="visible", timeout=5000)
        # btn.click()
        print("Cookie banner dismissed successfully.")
    except Exception as e:
        print(f"Standard click failed: {e}")


    # page.get_by_placeholder("Search products, brands and categories").fill("phones")
    page.get_by_role("button", name="Search").click()

    browser.close()
    # page.pause()
soup = BeautifulSoup(html, "lxml")

title = soup.find()



