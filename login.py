from selenium import webdriver
import pickle
from time import time, sleep
from selenium.webdriver.common.by import By


def main():
    driver = webdriver.Chrome()


    driver.get('https://web.eitaa.com')
    driver.execute_script("return document.readyState") == "complete"
    driver.find_element(By.XPATH, '//*[@id="auth-pages"]/div/div[2]/div[1]/div/div[3]/div[2]/div[1]').send_keys("9944714198")

    driver.find_element(By.XPATH, '//*[@id="auth-pages"]/div/div[2]/div[1]/div/div[3]/button/div').click()


    verification_code = input("Enter the 5-digit verification code sent to your phone: ")

    while len(verification_code) != 5 or not verification_code.isdigit():
        print("Invalid code. Please enter a 5-digit number.")
        verification_code = input("Enter the 5-digit verification code sent to your phone: ")


    verification_box = driver.find_element(By.XPATH, '//*[@id="auth-pages"]/div/div[2]/div[3]/div/div[3]/div/input')
    verification_box.send_keys(verification_code)


    sleep(20)



    # Save cookies to a file
    with open('cookies.pkl', 'wb') as file:
        pickle.dump(driver.get_cookies(), file)

    driver.quit()


if __name__ == "__main__":
    main()