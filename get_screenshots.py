from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

print("started")

# Setup Selenium with ChromeDriver
chrome_driver_path = r'path\to\chromedriver.exe'  # Update this path
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
options.add_argument('--window-size=1920x1080')  # Optional, set window size
browser = webdriver.Chrome(service=service, options=options)

# Define the path where screenshots will be saved
screenshots_path = 'path\\to\\screenshots\\'

# Read URLs from the file
df = pd.read_csv('countries.csv')

# Loop through each URL and take a screenshot
for index, row in df.iterrows():
    url = row['url_prefix'] + row['url']
    print(url)
    try:
        browser.get(url)
        screenshot_filename = f'screenshot_{row["id"]}.png'  # Generate a unique filename for the screenshot based on the country id
        browser.get_screenshot_as_file(screenshots_path + screenshot_filename)
    except Exception as e:
        print(f"Failed to take screenshot of {url}: {e}")

# Close the browser once done
browser.quit()
