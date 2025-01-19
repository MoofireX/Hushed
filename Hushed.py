from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")

service = Service('~/moofire/chromedriver-linux64/chromedriver')  # Specify path to chromedriver
driver = webdriver.Chrome(service=service, options=chrome_options)

music = input("What type of music would you like to play? The options are Instrumental, LoFi, and Electric. ")
url = ""

if music == "Instrumental":
    url = "https://www.youtube.com/results?search_query=instrumental"
elif music == "LoFi":
    url = "https://www.youtube.com/results?search_query=LoFi"
elif music == "Electric":
    url = "https://www.youtube.com/results?search_query=electronic+background+music"

driver.get(url)
time.sleep(5)

vid_links = []
vids = driver.find_elements(By.CSS_SELECTOR, "a#video-title")
for vid in vids[:100]:
    link = vid.get_attribute("href")

    if link:
        vid_links.append(link)

driver.quit()

for indx, link in enumerate(vid_links):
    print(f"Video {indx + 1}: link")
