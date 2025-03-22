from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
import requests
import io
import time

# Setting up Chrome WebDriver with the new method
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
wd = webdriver.Chrome(service=service, options=options)


def extract_category_links(url):
    wd.get(url)
    category_elements = wd.find_elements(By.CSS_SELECTOR, "a.inner")
    category_urls = [elem.get_attribute('href') for elem in category_elements]
    return category_urls


def get_images_from_category(url, delay):
    wd.get(url)
    # Scroll to load images
    wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(delay)

    # Extract image URLs
    images = wd.find_elements(By.CSS_SELECTOR, "img.fill.lazy-loaded")
    image_urls = [img.get_attribute('src') for img in images if img.get_attribute('src').startswith('https')]
    return image_urls


def download_image(download_path, url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        image = Image.open(io.BytesIO(response.content))
        image.save(f"{download_path}/{file_name}.jpg", "JPEG")
        print(f"Downloaded {file_name} successfully.")
    else:
        print(f"Failed to download {file_name}. Status code: {response.status_code}")


# Main program starts here
base_url = "https://www.wickeduncle.co.uk/categories"
category_urls = extract_category_links(base_url)

for url in category_urls:
    images = get_images_from_category(url, 2)
    for idx, img_url in enumerate(images):
        download_image("downloaded_images", img_url, f"{url.split('/')[-1]}_{idx}")

wd.quit()
