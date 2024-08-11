# List of imports
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Load WebDriver for Chrome or Firefox
def init_driver(browser):
    if browser == 'chrome':
        return webdriver.Chrome()
    elif browser == 'firefox':
        return webdriver.Firefox()

# Function to take a full-page screenshot with numbering
def scroll_and_capture(full_page_height, width, height, page_number, driver, browser):
    viewport_height = height
    screenshot_number = 1
    for offset in range(0, full_page_height, viewport_height):
        driver.execute_script(f"window.scrollTo(0, {offset});")
        time.sleep(1)  # Wait for content to appear

        # Construct the filename with browser name, webpage number, resolution, and screenshot number
        screenshot_name = f'{browser}_web-{page_number}_screenshot_{width}x{height}_part-{screenshot_number}.png'
        driver.save_screenshot(screenshot_name)
        print(f"Screenshot {screenshot_number} taken for {browser} web-{page_number} at {width}x{height} resolution, offset {offset}")
        screenshot_number += 1

# Main function to run the process for both Chrome and Firefox
def capture_screenshots():
    for browser in ['chrome', 'firefox']:
        driver = init_driver(browser)

        # Visit the sitemap page
        driver.get('https://www.getcalley.com/page-sitemap.xml')

        # Find and store the first 5 links in an array
        top_links = []
        links = driver.find_elements(By.TAG_NAME, 'a')  # tags which contain the URLs

        for link in links[:8]:
            top_links.append(link.text)  # Extract the URL from <a> tag

        # Output the stored links
        top_link = top_links[3:]
        print(top_link)

        for page_number, url in enumerate(top_link, start=1):
            screen_resolutions = [
                (1920, 1080),  # Desktop
                (1366, 768),   # Desktop
                (1536, 864),   # Desktop
                (360, 640),    # Mobile
                (414, 896),    # Mobile
                (375, 667)     # Mobile
            ]
            print(url)
            # Target webpage
            driver.get(url)

            # Wait for the page to fully load
            time.sleep(5)

            # Iterate over each resolution and take full-page screenshots
            for resolution in screen_resolutions:
                width, height = resolution
                driver.set_window_size(width, height)  # Set browser window size

                # Wait for any layout adjustments to complete
                time.sleep(2)

                # Get the total height of the page
                full_page_height = driver.execute_script("return document.body.scrollHeight")

                # Capture screenshots while scrolling
                scroll_and_capture(full_page_height, width, height, page_number, driver, browser)

        # Close browser
        driver.quit()

# Run the screenshot capturing process
capture_screenshots()
