from playwright.sync_api import Playwright, sync_playwright
import time

def run(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=200)
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        extra_http_headers={
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://www.google.com/"
        },
        viewport={"width": 1280, "height": 800}
    )

    page = context.new_page()

    # Step 1: Go to LinkedIn login page
    page.goto("https://www.linkedin.com/login")
    page.wait_for_load_state("networkidle")

    # Step 2: Fill your credentials (replace these)
    page.get_by_label("Email or Phone").fill("2srinath262003@gmail.com")
    page.get_by_label("Password").fill("#Srinath123")
    page.get_by_role("button", name="Sign in", exact=True).click()

    # Step 3: Wait for login to complete
    time.sleep(5)

    # Step 4: Profile URLs
    linkedin_profiles = [
        # Add profile URLs here, e.g.
        # "https://www.linkedin.com/in/some-profile/"
    "https://www.linkedin.com/in/dpjmcgregor/",
    "https://www.linkedin.com/in/salliekrawcheck/",
    "https://www.linkedin.com/in/jamesaltucher/",
    "https://www.linkedin.com/in/rholmes/",
    "https://www.linkedin.com/in/ariannahuffington/",
    "https://www.linkedin.com/in/riteshtagrawal1/",
    "https://www.linkedin.com/in/deepigoyal/",
    "https://www.linkedin.com/in/kunalbahl/",
    "https://www.linkedin.com/in/reidhoffman/",
    "https://www.linkedin.com/in/chamathp/",
    "https://www.linkedin.com/in/daltonc/",
    "https://www.linkedin.com/in/robertfsmith/",
    "https://www.linkedin.com/in/guillermoflor/",
    "https://www.linkedin.com/in/mrunaljhaveri/",
    "https://www.linkedin.com/in/peterthiel/",
    "https://www.linkedin.com/in/alexisohanian/",
    "https://www.linkedin.com/in/johndoerr/",
    "https://www.linkedin.com/in/pmarca/",
    "https://www.linkedin.com/in/timoreilly/",
    "https://www.linkedin.com/in/garyvaynerchuk/"
    ]

    # Step 5: Scrape profile data safely
    for url in linkedin_profiles:
        print(f"\n🔗 Visiting: {url}")
        page.goto(url)
        time.sleep(3)

        try:
            name = page.locator("h1").first.inner_text() if page.locator("h1").count() else "N/A"
        except:
            name = "N/A"

        try:
            headline = page.locator(".text-body-medium.break-words").first.inner_text() if page.locator(".text-body-medium.break-words").count() else "N/A"
        except:
            headline = "N/A"

        try:
            location = page.locator(".text-body-small.inline.t-black--light.break-words").first.inner_text() if page.locator(".text-body-small.inline.t-black--light.break-words").count() else "N/A"
        except:
            location = "N/A"

        print(f"✅ Name: {name.strip()}")
        print(f"🧠 Headline: {headline.strip()}")
        print(f"📍 Location: {location.strip()}")

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
