from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException, StaleElementReferenceException
from callables import click_continue_button
import credentials
import time


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

time.sleep(10)

# Here is where the loop should begin


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
                                      "//div[@data-test='story-title' and text()='Good Morning']/preceding-sibling::div/button[@class='_1uX8J']")
    next_button.click()
    time.sleep(2)

    # Locate the "READ +5 XP" button within the pop-up message
    read_button = driver.find_element(By.XPATH, "//a[@data-test='story-start-button']")
    read_button.click()
    time.sleep(2)

    # Call the function whenever you need to click the "Continue" button
    for _ in range(4):  # Example: Click the button 5 times
        if not click_continue_button(driver):
            print("Continue button not found or clickable")
            break

    options_elements = driver.find_elements(By.XPATH, "//li[contains(@class, '_25kWt _1nWdI')]")

    for option_element in options_elements:
        text_element_1 = option_element.find_element(By.XPATH, ".//span[@class='v9pTQ _3AnZj _2ziOV']")
        option_text = text_element_1.text

        if option_text == "Yes":
            button_element = option_element.find_element(By.XPATH, ".//button[@data-test='stories-choice']")
            button_element.click()
            break

    time.sleep(1)

    for _ in range(2):  # Example: Click the button 5 times
        if not click_continue_button(driver):
            print("Continue button not found or clickable")
            break


    for _ in range(2):
        if not click_continue_button(driver):
            print("Continue button not found or clickable")
            break

    time.sleep(2)
    phrases = ["Necesito", "las llaves", "de", "mi", "carro"]

    for phrase in phrases:
        button_xpath = f"//button[contains(@data-test, '{phrase}')]"
        button = driver.find_element(By.XPATH, button_xpath)
        button.click()
        time.sleep(0.5)
    print("I need my car keys, bitchboy")


    for _ in range(3):  # Example: Click the button 5 times
        if not click_continue_button(driver):
            print("Continue button not found or clickable")
            break

    button_xpath = "//button[contains(@data-test, 'cansada')]"
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

        if option_text == "looking":
            button_element = option_element.find_element(By.XPATH, ".//button[@data-test='stories-choice']")
            button_element.click()
            break

    for _ in range(7):  # Example: Click the button 5 times
        if not click_continue_button(driver):
            print("Continue button not found or clickable")
            break

    elements = driver.find_elements(By.CLASS_NAME, '_2s38C')

    # Iterate through each element to find the one containing the text "salt"
    for element in elements:
        if "salt" in element.text:
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
             'please', 'favor',
             'work', 'trabajo',
             'keys', 'llaves',
             'tired', 'cansada',
             'salt', 'sal',
             'necesito', 'need',
             'quiero', 'want',
             'necesitas', 'need',
             'quieres', 'want']

    for word in words:
        # Extract the first word from the data-test attribute
        first_word = word.split()[0]
        first_word_lower = first_word.lower()
        button_xpath = f"//button[@data-test='{first_word_lower}-challenge-tap-token']"
        try:
            button = driver.find_element(By.XPATH, button_xpath)
            button.click()
            time.sleep(0.5)

        except NoSuchElementException:
            try:
                # Look for span with class '_3VyQa' containing the word
                span = driver.find_element(By.XPATH, f"//span[@class='_3VyQa' and contains(text(), '{word}')]")
                span.click()
                time.sleep(0.5)
            except NoSuchElementException:
                print(f"No button or span found for '{word}'. Skipping...")
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


