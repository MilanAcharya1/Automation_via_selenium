from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException, StaleElementReferenceException

import credentials
import time


def click_continue_button(driver):
    try:
        # Wait for the "Continue" button to become clickable
        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-test='stories-player-continue']")))
        continue_button.click()
        time.sleep(1)  # Optional: Add a small delay after clicking the button
        return True
    except:
        return False

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                         options=options)

driver.get("https://www.duolingo.com/")
driver.maximize_window()

time.sleep(1)

button = driver.find_element(By.XPATH,
                             "//button[@class='_8AMBh _2vfJy _3Qy5R -TeUZ _2Ccfj' "
                             "and @data-test='have-account']")
button.click()

time.sleep(1)

username_input = driver.find_element(By.XPATH, "//input[@data-test='email-input']")
username_input.send_keys(credentials.username1)

pp_input = driver.find_element(By.XPATH, "//input[@data-test='password-input']")
pp_input.send_keys(credentials.password1)

time.sleep(2)

log_in = driver.find_element(By.XPATH,
                             "//button[@data-test='register-button']")

time.sleep(10)

# Here is where the look should begin


for _ in range(5):
    practice = driver.find_element(By.XPATH, "//a[@data-test='practice-hub-nav']")
    practice.click()
    time.sleep(3)

    # Scroll the button into view
    stories_button = WebDriverWait(driver, 10). \
        until(EC.visibility_of_element_located((By.XPATH, "//button[@data-test='practice-hub-collection-button']"
                                                          "//span[@class='RgiqJ' and text()='Stories']/ancestor::button")))
    driver.execute_script("arguments[0].scrollIntoView(true);", stories_button)

    stories_button.click()
    time.sleep(2)

    # Locate the button element by XPath
    next_button = driver.find_element(By.XPATH,
                                      "//div[@data-test='story-title' and text()='A Date']/preceding-sibling::div/button[@class='_1uX8J']")
    next_button.click()
    time.sleep(2)

    # Locate the "READ +5 XP" button within the pop-up message
    read_button = driver.find_element(By.XPATH, "//a[@data-test='story-start-button']")
    read_button.click()
    time.sleep(2)

    # Call the function whenever you need to click the "Continue" button
    for _ in range(6):  # Example: Click the button x times
        if not click_continue_button(driver):
            print("Continue button not found or clickable")
            break

    try:
        time.sleep(2)
        button = driver.find_element(By.XPATH,
                                     "//button[contains(@class, '_1YnrO _2qc6a') and contains(text(), 'partido')]")
        # Click the button
        button.click()
        time.sleep(1)
        # Optionally, you can add some waiting time or other actions after clicking the button
        # For example:
    except:
        print('not available')
    time.sleep(1)

    for _ in range(3):  # Example: Click the button 5 times
        if not click_continue_button(driver):
            print("Continue button not found or clickable")
            break

    time.sleep(2)

    span_playing = driver.find_element(By.XPATH, "//span[contains(text(), 'playing')]")

    # Find the ancestor <li> element containing the button
    li_element = span_playing.find_element(By.XPATH, "./ancestor::li")

    # Find the button within the <li> element
    button = li_element.find_element(By.TAG_NAME, "button")

    # Click the button
    button.click()

    for _ in range(5):  # Example: Click the button 5 times
        if not click_continue_button(driver):
            print("Continue button not found or clickable")
            break




    phrases = ["Cuba", "madre", "México"]
    time.sleep(4)
    for phrase in phrases:
        button_xpath = f"//button[contains(@data-test, '{phrase}')]"
        button = driver.find_element(By.XPATH, button_xpath)
        button.click()
        time.sleep(0.5)
    print("Thats where I am from bitch")



    for _ in range(6):  # Example: Click the button 5 times
        if not click_continue_button(driver):
            print("Continue button not found or clickable")
            break

    button_xpath = "//button[contains(@data-test, 'también')]"
    tired_button = driver.find_element(By.XPATH, button_xpath)
    tired_button.click()
    time.sleep(0.5)

    for _ in range(5):  # Example: Click the button 5 times
        if not click_continue_button(driver):
            print("Continue button not found or clickable")
            break

    options_elements = driver.find_elements(By.XPATH, "//li[contains(@class, '_25kWt _1nWdI')]")

    for option_element in options_elements:
        text_element_1 = option_element.find_element(By.XPATH, ".//span[@class='v9pTQ _3AnZj _2ziOV']")
        option_text = text_element_1.text
        print(option_text)

        if option_text == "were":
            button_element = option_element.find_element(By.XPATH, ".//button[@data-test='stories-choice']")
            button_element.click()
            break

    for _ in range(4):  # Example: Click the button 5 times
        if not click_continue_button(driver):
            print("Continue button not found or clickable")
            break

    elements = driver.find_elements(By.CLASS_NAME, '_2s38C')

    # Iterate through each element to find the one containing the text "salt"
    for element in elements:
        if "lied" in element.text:
            # If found, click the button associated with that option
            button = element.find_element(By.XPATH, "./ancestor::li/button[@data-test='stories-choice']")
            button.click()
            break

    for _ in range(1):
        if not click_continue_button(driver):
            print("Continue button not found or clickable")
            break

    # Below code for the final test where 5 sets of words exist, but they change

    words = ['sorry', 'perdón',
             'sugar', 'azúcar',
             'love', 'amor',
             'table', 'mesa',
             'here', 'aquí',
             'morning', 'buenos',
             'coffee', 'café',
             'car', 'carro',
             'please', 'por favor',
             'work', 'trabajo',
             'keys', 'llaves',
             'tired', 'cansada',
             'salt', 'sal',
             'need', 'necesi',
             'want', 'quier',]

    for word in words:
        # Extract the first word from the data-test attribute
        first_word = word.split()[0]
        button_xpath = f"//button[@data-test='{first_word}-challenge-tap-token']"
        try:
            button = driver.find_element(By.XPATH, button_xpath)
            button.click()
            time.sleep(0.5)
        except NoSuchElementException:
            try:
                button_xpath = f"//button[contains(@data-test, '{word}')]"
                print(f"container tried for '{word}' not found exact word match")
                button.click()
                time.sleep(0.5)
            except (NoSuchElementException,StaleElementReferenceException, WebDriverException):
                print(f"No button found for '{word}'. Skipping...")
                continue
    for _ in range(2):
        if not click_continue_button(driver):
            print("Continue button not found or clickable")
            break

    button = driver.find_element(By.XPATH,
                                 "//button[@class='_8AMBh _2vfJy _3Qy5R _2fxL4 _2AtRJ']")
    button.click()

    def final_continue_button(driver):
        try:
            continue_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@data-test='stories-player-done']")))
            continue_button.click()
            time.sleep(1)  # Optional: Add a small delay after clicking the button
            return True
        except:
            return False


    for _ in range(1):
        if not final_continue_button(driver):
            print("Continue button not found or clickable")
            break


