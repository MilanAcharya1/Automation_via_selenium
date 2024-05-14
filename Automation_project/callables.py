
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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