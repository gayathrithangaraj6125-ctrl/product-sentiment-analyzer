import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

product_id = "B0CHX1W1XY"

urls = [
f"https://www.amazon.in/product-reviews/{product_id}/?filterByStar=one_star",
f"https://www.amazon.in/product-reviews/{product_id}/?filterByStar=two_star",
f"https://www.amazon.in/product-reviews/{product_id}/?filterByStar=three_star",
f"https://www.amazon.in/product-reviews/{product_id}/?filterByStar=four_star",
f"https://www.amazon.in/product-reviews/{product_id}/?filterByStar=five_star"
]

reviews_list = []

print("Login to Amazon if needed")
driver.get(urls[0])
input("Press ENTER after login...")

for url in urls:

    driver.get(url)
    time.sleep(3)

    for page in range(1,4):

        print("Scraping page:", page)

        reviews = driver.find_elements(By.XPATH, "//span[@data-hook='review-body']")

        for r in reviews:
            reviews_list.append(r.text)

        try:
            next_button = driver.find_element(By.XPATH, "//li[@class='a-last']/a")
            next_button.click()
            time.sleep(3)
        except:
            break

print("Total reviews collected:", len(reviews_list))

df = pd.DataFrame(reviews_list, columns=["Review"])

df.to_csv("reviews.csv", index=False)

print("Saved reviews.csv")

driver.quit()