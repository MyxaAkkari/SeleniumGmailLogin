from selenium.webdriver.common.by import By
import time
import undetected_chromedriver

# Hardcoded username and password
USERNAME = "email"
PASSWORD = "password"

# Start Chrome WebDriver
driver = undetected_chromedriver.Chrome()

# Open the Flask app login page
driver.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ifkv=AaSxoQxgLxsezoPpx0EuAI3Gl_CT1NwYXpgY04ncAMZyoqfC1r74-PowDmhoh3H7U7Vssn7MuDev6Q&osid=1&passive=1209600&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1996607879%3A1715881772899660&ddm=0")

# Wait for the page to load
time.sleep(2)

# Find username and next button and fill them
username_field = driver.find_element(By.XPATH,"//*[@id ='identifierId']").send_keys(USERNAME)
submit_button = driver.find_element(By.ID,"identifierNext").click()

time.sleep(2)

# Find password and next button and fill them
password_field = driver.find_element(By.NAME, "Passwd").send_keys(PASSWORD)
submit_button = driver.find_element(By.ID,"passwordNext").click()

# Wait for the page to load
time.sleep(50) # i needed to approve 2FA on my phone (because of undetected chrome driver)

# Check if login was successful by checking if "INBOX" element is there
welcome_message = driver.find_element(By.CLASS_NAME, "TO")
print("yess")

# Close the browser
driver.quit()
