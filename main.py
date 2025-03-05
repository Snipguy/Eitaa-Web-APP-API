from time import sleep, time
from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
import pickle

def verifyLogin():
    sleep(10000)

def main():
    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=C:\Selenium")
    options.add_argument("profile-directory=Default")
    # options.add_argument("--remote-debugging-port=9222") 

    driver = webdriver.Chrome(options=options)


    driver.execute_script("window.open('https://web.eitaa.com', '_blank');")  # Open new tab
    driver.switch_to.window(driver.window_handles[1])  # Switch to the new tab


    # with open('cookies.pkl', 'rb') as file:
    #     cookies = pickle.load(file)
    #     for cookie in cookies:
    #         driver.add_cookie(cookie)
    
    # driver.refresh()
    sleep(10)

    # verifyLogin()

    # Locate the element with the specific data-peer-id
    try:
        user_element = driver.find_element(By.CSS_SELECTOR ,'[data-peer-id="19755659"]')
        user_element.click()
    except Exception as e:
        print(e)
        sleep(5000)


    # Send a message to the user
    message_box = driver.find_element(By.XPATH ,'//*[@id="column-center"]/div/div/div[4]/div/div[1]/div[7]/div[1]/div[1]')
    message_box.send_keys('Your custom message')
    send_button = driver.find_element(By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[4]/button/div')
    send_button.click()


if __name__ == "__main__":
    main()