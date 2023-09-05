import time
from selenium import webdriver

def like_post_replies(post_url):
    driver = webdriver.Chrome()
    driver.get(post_url)

    # Find the post replies
    reply_elements = driver.find_elements_by_class_name("like")

    # Like each reply
    for reply_element in reply_elements:
        reply_element.click()
        time.sleep(1)

    driver.close()

if __name__ == "__main__":
    post_url = "https://www.linkedin.com/posts/[YOUR_LINKEDIN_USERNAME]/[POST_ID]"
    like_post_replies(post_url)
