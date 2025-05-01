from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import os
import time

# Constants
URL = "https://blog.bytebytego.com/archive?sort=new"
EXCEL_FILE = "locked_non_ep_blogs.xlsx"

def setup_driver():
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=options)

def scroll_to_bottom(driver, pause_time=1):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def fetch_locked_non_ep_blogs():
    driver = setup_driver()
    driver.get(URL)
    scroll_to_bottom(driver)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    blog_entries = []

    containers = soup.find_all("div", class_="container-Qnseki")

    for container in containers:
        # Check for lock icon (premium content)
        if not container.find("svg", class_="lucide-lock"):
            continue

        # Extract blog <a> tag
        link_tag = container.find("a", attrs={"data-testid": "post-preview-title"})
        if link_tag:
            title = link_tag.text.strip()
            link = link_tag["href"].strip()
            if "EP" not in title:
                blog_entries.append((title, link))

    return blog_entries

def update_excel(blog_entries):
    if os.path.exists(EXCEL_FILE):
        df_existing = pd.read_excel(EXCEL_FILE)
    else:
        df_existing = pd.DataFrame(columns=["Blog Name", "Blog Link"])

    existing_set = set(zip(df_existing["Blog Name"], df_existing["Blog Link"]))
    new_entries = [entry for entry in blog_entries if entry not in existing_set]

    if new_entries:
        df_new = pd.DataFrame(new_entries, columns=["Blog Name", "Blog Link"])
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        df_combined.to_excel(EXCEL_FILE, index=False)
        print(f"✅ Added {len(new_entries)} new locked non-EP blog(s) to {EXCEL_FILE}")
    else:
        print("🔄 No new blogs found.")

def main():
    blog_entries = fetch_locked_non_ep_blogs()
    update_excel(blog_entries)

if __name__ == "__main__":
    main()
