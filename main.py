from selenium import webdriver 
# webdriver is what is performing the actions
from selenium.webdriver.common.keys import Keys 
# gives access to enter and escape keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
# choosing the appropriate web browser used:
driver = webdriver.Chrome(PATH)

# loading up a page after running the program
driver.get("https://www.google.com/")

# to get title of the web page:
print(driver.title)

# to search for what is found from google's inspect element search bar:
search = driver.find_element_by_name("q")

# send text to search box (Enter is refer as RETURN):
search.send_keys("test")
search.send_keys(Keys.RETURN)

# print out the page source:
# print(driver.page_source)

# wait for a specific thing to exist on a page before looking:
try:
    main = WebDriverWait(driver, 10).until( # 10 second max
        EC.presence_of_element_located((By.ID, "rcnt"))
    )
    # once inside "saerch," find all elements inside "search"":
    searches = main.findElements(By.CLASS_NAME, "yuRUbf")
    # iterate through each and print out each name:
    for title in searches:
        name = title.findElement(By.CLASS_NAME, "LC20lb DKV0Md")
        print(name.text)
finally:
    driver.quit()

# once in the page, look at the page elements to see what else you can do:
# main = driver.find_element_by_id("search")
# print(main.text)

# delays program from closing immediately
time.sleep(5)

# to close a web page:
driver.close()

# to close entire browser: 
# driver.quit()
