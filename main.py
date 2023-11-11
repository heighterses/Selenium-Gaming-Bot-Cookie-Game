# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=chrome_options)
#
# driver.get("https://www.islamicfinder.org/special-islamic-days/")
# Islamic_events = driver.find_elements(By.CLASS_NAME, "date-box")
# dic = []
#
# for n in Islamic_events:
#     print(n.text)
#     type = string(n)
#     dic.append(n)
#
# print(dic)
#
#
# driver.quit()
#
#
#
#

# https://www.youtube.com/feed/trending?bp=4gINGgt5dG1hX2NoYXJ0cw%3D%3D

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")
# Top_song = driver.find_elements(By.ID, "video-title")
# title_list = []
# for titles in Top_song:
#     title_list.append(titles.text)
# print(title_list)

# Search = driver.find_element(By.NAME, "search_query")
# link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(link)
#
# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

blogs = []

blog_link = driver.find_elements(By.CSS_SELECTOR, '.blog-widget a')

for link in blog_link:
    text = link.text  # Removed print statement
    blogs.append(text)

length = len(blogs)  # Calculate length directly without print statement
print(length)

blog_time = driver.find_elements_by_css_selector("time ")

for blog_index in range(length):
    for time in blog_time:
        print(time.text)

driver.quit()