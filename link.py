from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create a ChromeOptions object to set options
chrome_options = webdriver.ChromeOptions()

# Disable automatic closing of the browser on script exit
chrome_options.add_experimental_option("detach", True)

# Create the Chrome WebDriver instance with options
driver = webdriver.Chrome(options=chrome_options)

# Opening LinkedIn's login page
driver.get("https://www.linkedin.com/login")

# Waiting for the page to load
time.sleep(5)

# Entering username
username = driver.find_element(By.ID, "username")
username.send_keys("vishnuvamsi147@gmail.com")

# Entering password
password = driver.find_element(By.ID, "password")
password.send_keys("V@msi2004")

# Clicking the login button
driver.find_element(By.XPATH, "//button[text()='Sign in']").click()

# Wait for the LinkedIn feed page to load (you can adjust the waiting time as needed)
time.sleep(5)

# Navigate to your LinkedIn profile page
driver.get("https://www.linkedin.com/school/srmuap/")

# The browser will stay open until you manually close it.

# You can add further actions or wait for events as needed.
