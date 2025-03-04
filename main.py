from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle

def verifyLogin():
    time.sleep(10000)

def main():
    driver = webdriver.Chrome()

    with open('cookies.pkl', 'rb') as file:
        cookies = pickle.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)

    driver.get('https://web.eitaa.com/')

    time.sleep(10)

    verifyLogin()

    # Locate the element with the specific data-peer-id
    user_element = driver.find_element(By.CSS_SELECTOR ,'[data-peer-id="specific-peer-id"]')
    user_element.click()

    # Send a message to the user
    message_box = driver.find_element(By.XPATH ,'//*[@id="column-center"]/div/div/div[4]/div/div[1]/div[7]/div[1]/div[1]')
    message_box.send_keys('Your custom message')
    send_button = driver.find_element(By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[4]/button/div')
    send_button.click()


if __name__ == "__main__":
    main()