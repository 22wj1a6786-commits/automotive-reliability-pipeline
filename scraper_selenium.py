from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

USERNAME = "data_scrapper-a"
PASSWORD = "D@t@5crap"

driver = webdriver.Chrome()

# open login
driver.get("https://www.team-bhp.com/forum/login.php")
time.sleep(3)

# login
driver.find_element(By.NAME, "vb_login_username").send_keys(USERNAME)
driver.find_element(By.NAME, "vb_login_password").send_keys(PASSWORD + Keys.RETURN)

time.sleep(5)

print("After login URL:", driver.current_url)
print("Title:", driver.title)

# go to thread
driver.get("https://www.team-bhp.com/forum/motorbikes/292410-2025-hero-xpulse-210-review.html")
time.sleep(5)

print("Thread URL:", driver.current_url)
print("Title:", driver.title)

html = driver.page_source

# DEBUG CHECK
if "post_message_" in html:
    print("Posts found")
else:
    print("Posts NOT found → blocked or wrong page")

# PARSE HTML
soup = BeautifulSoup(html, "html.parser")

# EXTRACT POSTS
posts = soup.select("div[id^='post_message_']")

data = []

for post in posts:
    data.append(post.get_text(" ", strip=True))

# SAVE
with open("posts.txt", "w", encoding="utf-8") as f:
    for p in data:
        f.write(p + "\n\n---\n\n")
users = soup.select("a.bigusername")

for i, (user, post) in enumerate(zip(users, posts)):
    print(f"{user.text}: {post.get_text(' ', strip=True)[:200]}")
driver.quit()