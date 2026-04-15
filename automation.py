from playwright.sync_api import sync_playwright
import time

BASE_URL = "http://127.0.0.1:5000"


def slow_action():
    time.sleep(1.2)


def run_steps(steps):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        for step in steps:
            print(f"Executing: {step}")

           
            if "open" in step:
                page.goto(BASE_URL)
                slow_action()

            
            elif "create user" in step:
                email = step.split()[-1]

                page.fill("input[name='email']", email)
                slow_action()

                page.click("text=Create User")
                slow_action()

           
            elif "reset password" in step:
                email = step.split()[-1]

                
                page.goto(BASE_URL)
                slow_action()

                try:
                    page.locator(f"li:has-text('{email}') >> text=Reset").click()
                    slow_action()
                except:
                    print(f"⚠️ Could not find Reset button for {email}")

            else:
                print(f"⚠️ Unknown step: {step}")

        print("\n All steps executed!")

        time.sleep(3)
        browser.close()