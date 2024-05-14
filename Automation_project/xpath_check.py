from selenium import webdriver

# Step 1: Perform necessary actions to reach the target page
# For example:
driver = webdriver.Chrome()
driver.get("your_initial_webpage_url_here")
# Perform actions to navigate to the target page
# Example: Clicking buttons, filling forms, etc.

# Step 2: Navigate to the target page where you need to find the XPath
# Example:
driver.get("target_page_url_here")

# Step 3: Integrate XPath-finding code
container_xpath = "//div[@data-test='stories-element']//li[contains(@class, '_25kWt') and .//span[text()='Yes']]"
container_element = driver.find_element_by_xpath(container_xpath)
container_xpath = driver.execute_script(
    "function absoluteXPath(element) {" +
    # JavaScript function to find the absolute XPath of an element
    "} return absoluteXPath(arguments[0]);", container_element)

# Step 4: Print or Use the XPath
print("XPath of the container element:", container_xpath)

# Optionally, you can use the XPath in your testing logic
# Example:
# element = driver.find_element_by_xpath(container_xpath)
# Perform further actions based on the located element

# Close the WebDriver
driver.quit()
