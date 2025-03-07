from time import sleep, time
from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.common.exceptions import NoSuchElementException # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore

from login import login
from selenium.webdriver.common.keys import Keys # type: ignore
from persiantools.jdatetime import JalaliDate
# import pyautogui, pyperclip

def verifyLogin():
    if login == True:
        return 0
    else:
        login()

def main():
    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=C:\Selenium")
    options.add_argument("profile-directory=Default")
    # options.add_argument("--remote-debugging-port=9222") 

    driver = webdriver.Chrome(options=options)


    driver.get("https://web.eitaa.com")

    # verifyLogin()

    # with open('cookies.pkl', 'rb') as file:
    #     cookies = pickle.load(file)
    #     for cookie in cookies:
    #         driver.add_cookie(cookie)

    # driver.refresh()
    sleep(10)


    # Locate the element with the specific data-peer-id
    try:
        user_element = driver.find_element(By.CSS_SELECTOR ,'[data-peer-id="19755659"]')
        user_element.click()
    except Exception as e:
        print(e)
        sleep(5000)

    message_box = driver.find_element(By.XPATH ,'//*[@id="column-center"]/div/div/div[4]/div/div[1]/div[7]/div[1]/div[1]')
    message_box.click()

    # //*[@id="column-center"]/div/div/div[4]/div[1]/div[1]/div[7]/input
    path_to_file = r'E:\GitHub\Eita-Web-APP-API\.gitignore'

    file_input = WebDriverWait(driver, 20).until(driver.find_element(By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div[1]/div[1]/div[7]/input')).send_keys(path_to_file)
    file_input
    
    print('pasted \n')

    try:
        message_title = WebDriverWait(driver, 20).until(driver.find_element(By.XPATH, '/html/body/div[5]/div/div[3]/div[1]'))
        message_title.send_keys(f'لیست قیمت ${JalaliDate.today()}')
    except NoSuchElementException as e:
        print(e)
        return 1
    except Exception as e:
        print(e)
        return 1
    
    # message_box.send_keys('Your custom message')
    send_file_btn = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/button')
    send_file_btn.click()


    # send_button = driver.find_element(By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[4]/button/div')
    # send_button.click()


if __name__ == "__main__":
    main()