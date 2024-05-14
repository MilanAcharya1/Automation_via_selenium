from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import credentials
from translator2 import translate_to_english
from unidecode import unidecode


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
log_in.click()

time.sleep(5)

# Wait for the button to be clickable
wait = WebDriverWait(driver, 10)
lesson_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-test='skill-path-level-0 skill-path-level-skill']")))

# Scroll to the button
actions = ActionChains(driver)
actions.move_to_element(lesson_button).perform()

# Click on the button
lesson_button.click()

time.sleep(2)
# Wait for the button to be clickable
wait = WebDriverWait(driver, 10)
practice_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-test='skill-path-state-passed skill-path-unit-test-0']")))

# Click on the button
practice_button.click()


# Locate the element containing the question text
question_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='_2kEEj']"))
)
# Get the text content of the question element
question1 = question_element.text.strip()

# Assuming you have already extracted the question text into the variable question1

answer_elements = driver.find_elements(By.XPATH, "//div[@data-test='challenge-choice']")
Answer_1 = translate_to_english(question1, "es")
Answer_1_decoded = unidecode.unidecode(Answer_1)

for answer_element in answer_elements:
    # Get the text content of the answer element
    answer_text = answer_element.find_element(By.XPATH, ".//span[@data-test='challenge-judge-text']").text.strip()

    # Check if the answer matches the translated question
    if answer_text.lower() == Answer_1_decoded.lower():
        button = answer_element.find_element(By.XPATH, ".//span[@data-test='challenge-judge-text']/..")
        button.click()
        break
    else:
        print("Incorrect answer:", answer_text)


check_button = driver.find_element(By.XPATH, "//span[text()='Check']")
check_button.click()

time.sleep(2)

Continue_button_1 = driver.find_element(By.XPATH, "//span[text()='Continue']")
Continue_button_1.click()

time.sleep(5)

driver.quit()

try:
    # Locate the "Can't listen now" button
    cant_listen_now_button = driver.find_element(By.XPATH, "//button[contains(., \"Can't listen now\")]")

    # Click the "Can't listen now" button
    cant_listen_now_button.click()

    print("Clicked the 'Can't listen now' button.")
    Continue_button_1 = driver.find_element(By.XPATH, "//span[text()='Continue']")
    Continue_button_1.click()
except NoSuchElementException:
    print("The 'Can't listen now' button is not found.")

time.sleep(2)

try:
    SKIP = driver.find_element(By.XPATH ,"//span[text()='Skip']")
    SKIP.click()

except NoSuchElementException:
    print("No Skippable option available")

