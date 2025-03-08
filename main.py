from time import sleep, time
from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.common.exceptions import NoSuchElementException # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from login import login
from selenium.webdriver.common.keys import Keys # type: ignore
from persiantools.jdatetime import JalaliDate
import pyautogui, pyperclip, subprocess

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


    # Locate the element with the specific data-peer-id
    try:
        user_element = WebDriverWait(driver, 15).until(
            lambda d: d.find_element(By.CSS_SELECTOR ,'[data-peer-id="19755659"]'))
        user_element = WebDriverWait(driver, 15).until(
            lambda d: d.find_element(By.CSS_SELECTOR ,'[data-peer-id="19755659"]'))
        user_element.click()
    except Exception as e:
        print(e)
        sleep(5000)

    message_box = WebDriverWait(driver, 20).until(
        lambda d: d.find_element(By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[1]/div[7]/div[1]/div[1]')
    )
    driver.execute_script("arguments[0].scrollIntoView();", message_box)
    message_box = WebDriverWait(driver, 20).until(
        lambda d: d.find_element(By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[1]/div[7]/div[1]/div[1]')
    )
    driver.execute_script("arguments[0].scrollIntoView();", message_box)
    message_box.click()
    sleep(5)
    sleep(5)

    # //*[@id="column-center"]/div/div/div[4]/div[1]/div[1]/div[7]/input
    # path_to_file = r'D:\babak\In progress\Babak\DEV\Projects\Web scraping\Eitaa-Web-APP-API\.gitignore' 
    path_to_file = r'E:\GitHub\Eita-Web-APP-API\.gitignore' # path for home laptop


    try:
        file_input = WebDriverWait(driver, 20).until(
            lambda d: d.find_element(By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div[1]/div[1]/div[7]/input')
        )
        # driver.execute_script("arguments[0].style.display = 'block';", file_input)
        print(file_input.is_displayed(), file_input.is_enabled())

        subprocess.run(f'explorer /select,"{path_to_file}"', shell=True)
        sleep(2)
        pyperclip.copy()
        # pyautogui.hotkey("ctrl", "c")
        print("File copied to clipboard.")
        sleep(1.5)

        print("Trying to send the file.....")
        action = ActionChains(driver)
        action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        print("Sending the file is Done;)")
    except Exception as e:
        print(e)

    print("------------")
    path_to_file = r'D:\babak\In progress\Babak\DEV\Projects\Web scraping\Eitaa-Web-APP-API\.gitignore' 
    # path_to_file = r'E:\GitHub\Eita-Web-APP-API\.gitignore' path for home laptop


    try:
        file_input = WebDriverWait(driver, 20).until(
            lambda d: d.find_element(By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div[1]/div[1]/div[7]/input'))
        # driver.execute_script("arguments[0].style.display = 'block';", file_input)
        print(file_input.is_displayed(), file_input.is_enabled())

        subprocess.run(f'explorer /select,"{path_to_file}"', shell=True)
        sleep(2)
        pyautogui.hotkey("ctrl", "c")
        print("File copied to clipboard.")
        sleep(1.5)

        print("Trying to send the file.....")        
        action = ActionChains(driver)
        action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        print("Sending the file is Done;)")
    except Exception as e:
        print(e)
    
    print("------------")
    print('pasted \n')

    try:
        message_title = WebDriverWait(driver, 20).until(
            lambda d: d.find_element(By.XPATH, '/html/body/div[5]/div/div[3]/div[1]')
            )
        message_title = WebDriverWait(driver, 20).until(
            lambda d: d.find_element(By.XPATH, '/html/body/div[5]/div/div[3]/div[1]')
            )
        message_title.send_keys(f'لیست قیمت ${JalaliDate.today()}')
    except NoSuchElementException as e:
        print(e)
        return 1
    except Exception as e:
        print(e)
        return 1
    
    # message_box.send_keys('Your custom message')
    try:
        send_file_btn = WebDriverWait.until(
            lambda d: d.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/button')
        )
        send_file_btn.click()
    except Exception as e:
        print(e)
    try:
        send_file_btn = WebDriverWait.until(
            lambda d: d.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/button'))
        send_file_btn.click()
    except Exception as e:
        print(e)

    # send_button = driver.find_element(By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[4]/button/div')
    # send_button.click()


if __name__ == "__main__":
    main()