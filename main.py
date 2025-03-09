from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from persiantools.jdatetime import JalaliDate
import base64
from login import login


def verifyLogin(driver):
    # I made the chat sidebar of the Eitaa WebAPP as my identifier if the user is logged in, your welcom to change it to whatever you want
    try:
        check_sidebar_exist = WebDriverWait(driver, 20).until(
            lambda d: d.find_element(By.XPATH, '//*[@id="column-left"]/div')
        )
    except NoSuchElementException:
        print("please Log in first........")
        try:
            login()
        except Exception as e:
            print("login failed with this error : {e}")


    except Exception as e:
        print("verifyLogin failed with this error : {e}")




    return 0

def target_user(driver):
    # data-peer-id is a CSS selector that is specific to each user find it using inspect in any browser and replace the number
    try:
        user_element = WebDriverWait(driver, 15).until(
            lambda d: d.find_element(By.CSS_SELECTOR ,'[data-peer-id="19755659"]') 
        )
        user_element.click()
    except Exception as e:
        print(e)
        return 1


def message_box(driver):
    message_box = WebDriverWait(driver, 20).until(
        lambda d: d.find_element(By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[1]/div[7]/div[1]/div[1]')
    )
    driver.execute_script("arguments[0].scrollIntoView();", message_box)
    message_box.click()
    sleep(1)

    return message_box

def find_clear_message_box(driver):
    message_box = WebDriverWait(driver, 20).until(
        lambda d: d.find_element(By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[1]/div[7]/div[1]/div[1]')
    )
    driver.execute_script("arguments[0].scrollIntoView();", message_box)
    message_box.click()
    sleep(1)

    # delete drafted messages
    message_box.send_keys(Keys.CONTROL, 'a')  # Select all text
    message_box.send_keys(Keys.BACKSPACE)  # Delete everything
    print("Message field cleared.")
    sleep(1)

    return message_box

def send_message_button(driver):
    send_button = driver.find_element(By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[4]/button/div')
    send_button.click()
    # clicks the send button which send your message
    return 1



def passing_file_fields(driver):
    try:
        message_title = WebDriverWait(driver, 20).until(
            lambda d: d.find_element(By.XPATH, '/html/body/div[5]/div/div[3]/div[1]')
        )
        message_title.send_keys(f'لیست قیمت {JalaliDate.today()}')
    except NoSuchElementException as e:
        print(e)
        return 1
    except Exception as e:
        print(e)
        return 1

def passing_file(driver):
    sleep(1.5)

    print("Trying to send the file.....")        
    print("Sending the file is Done;)")

    # path for the file you want to send
    path_to_file = r'D:\babak\In progress\Babak\DEV\Projects\Web scraping\Eitaa-Web-APP-API\.gitignore' # path for work laptop
    # path_to_file = r'E:\GitHub\Eita-Web-APP-API\.gitignore' # path for home laptop

    with open(path_to_file, "rb") as file:
        file_data = file.read()
        base64_file = base64.b64encode(file_data).decode("utf-8")

    print("running javascript for passing the file....")
    try:
        js_script = f"""
        async function pasteFile() {{
            // Decode the Base64 file data back into a Blob
            let byteCharacters = atob("{base64_file}");
            let byteNumbers = new Array(byteCharacters.length);
            for (let i = 0; i < byteCharacters.length; i++) {{
                byteNumbers[i] = byteCharacters.charCodeAt(i);
            }}
            let byteArray = new Uint8Array(byteNumbers);
            let blob = new Blob([byteArray], {{ type: "text/plain" }}); // Change type if needed

            // Create a File object
            let file = new File([blob], "test.txt", {{ type: blob.type }});

            // Use DataTransfer API
            let dataTransfer = new DataTransfer();
            dataTransfer.items.add(file);

            // Dispatch a paste event
            let event = new ClipboardEvent("paste", {{
                bubbles: true, 
                cancelable: true,
                clipboardData: dataTransfer
            }});

            document.dispatchEvent(event);
        }}

        pasteFile();
        """
        print("JavaScript finished....")

        sleep(0.5)

        print("Executing JavaScript....")
        driver.execute_script(js_script)
        print("JavaScript Done!")

        return 0
    except Exception as e:
        print("passing_file() failed, with this error : {e}")
        return 1



def send_file(driver):
    try:
        passing_file(driver) # Finds your file and passes it Eitaa for you to send the file, change the path to your file

        # if you want to send file with no title , just comment the line blew
        passing_file_fields(driver) # writes your title that you want to send the file with

        # clicks the send button
        try:
            send_file_btn = WebDriverWait(driver, 10).until(
                lambda d: d.find_element(By.CSS_SELECTOR, 'body > div.popup.popup-send-photo.popup-new-media.active > div > div.popup-header > button')
            )
            ActionChains(driver).move_to_element(send_file_btn).click().perform()
            # send_file_btn.click()
        except Exception as e:
            print("clicking send button failed, with this error : {e}")
            return 1
    except Exception as e:
        print("send_file() failed, with this error : {e}")
        return 1


def main():
    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=C:\Selenium")
    options.add_argument("profile-directory=Default")

    driver = webdriver.Chrome(options=options)
    driver.get("https://web.eitaa.com")


    verifyLogin()

    find_clear_message_box(driver)

    # message_box.send_keys('Your custom message')


if __name__ == "__main__":
    main()