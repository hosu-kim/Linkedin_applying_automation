from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

print("Hello, I'm a job applying automator on Linkedin. Please provide your information below.")
time.sleep(3)
user_id = input("What is your email address on Linkedin?\nType here: ")
user_password = input("What's the password?\nType here: ")

user_search = input("What type of profession are you interested and where?\nType here(ex.Python developer/Berlin): ")
is_correct = input(f"You typed '{user_search}. Is it correct? Type Yes/No: ").lower()
while is_correct != "yes" or user_search.count("/") != 1:
    print(user_search.find("/"))
    print("It was an incorrect answer.")
    user_search = input("What type of profession are you interested and where?\nType here(ex.Python developer/Berlin): ")
    is_correct = input(f"You typed '{user_search}. Is it correct? Type Yes/No: ").lower()
user_job = user_search.split("/")[0]
user_location = user_search.split("/")[1]

user_browser = input("Which browser do you use? (Chrome/Edge/Firefox)\nType here: ").lower()
user_browser_setup = None

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

while not user_browser_setup:
    # This code keeps the browser on and is for the selenium setup.
    if user_browser == "edge":
        edge_options = webdriver.EdgeOptions()
        edge_options.add_experimental_option("detach", True)
        driver = webdriver.Edge(options=edge_options)
        user_browser_setup = True
    elif user_browser == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        user_browser_setup = True
    elif user_browser == "firefox":
        driver = webdriver.Firefox(keep_alive=True)
        user_browser_setup = True
    else:
        user_browser_setup = False
        user_browser = input("You typed a wrong answer. Please choose one in the list (Chrome, Edge, Firefox)"
                             "\nType here: ").lower()


driver.get("https://www.linkedin.com/home")
username_input = driver.find_element(by=By.ID, value="session_key")
username_input.send_keys(user_id)
password = driver.find_element(by=By.ID, value="session_password")
password.send_keys(user_password)
time.sleep(3)
password.send_keys(Keys.ENTER)
time.sleep(10)

jobs_button = driver.find_element(by=By.XPATH, value='//*[@id="global-nav"]/div/nav/ul/li[3]/a')
jobs_button.click()
time.sleep(3)
job_search_input = driver.find_element(by=By.XPATH, value='/html/body/div[6]/header/div/div/div/div[2]/div[2]/div/div/input[1]')
job_search_input.send_keys(user_job)
job_location_input = driver.find_element(by=By.XPATH, value='/html/body/div[6]/header/div/div/div/div[2]/div[3]/div/div/input[1]')
job_location_input.send_keys(user_location)
time.sleep(1)
job_location_input.send_keys(Keys.SPACE)
job_location_input.send_keys(Keys.ENTER)
time.sleep(3)
easy_apply_button = driver.find_element(by=By.XPATH, value='/html/body/div[6]/div[3]/div[4]/section/div/section/div/div/div/ul/li[7]/div/button')
easy_apply_button.click()

time.sleep(2)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")
for listing in all_listings:
    listing.click()
    time.sleep(3)
    apply_button = driver.find_element(by=By.XPATH, value='/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/div/div/button')
    apply_button.click()
    time.sleep(3)
    try:
        next_button1 = driver.find_element(by=By.XPATH,
                                          value='/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button')
        next_button1.click()
        time.sleep(3)
        next_button2 = driver.find_element(by=By.XPATH,
                                          value='/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]')
        next_button2.click()
        title = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/h3')
        if title.text == "Additional Questions" or title.text == "Additional" or title.text == "Screening questions":
            job_application_exit = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div/button')
            job_application_exit.click()
            job_application_discard = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[2]/div/div[3]/button[1]')
            job_application_discard.click()
        else:
            review_button = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]')
            review_button.click()
            submit_button = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[3]/button[2]')
            submit_button.click()
            job_application_exit = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div/button')
            job_application_exit.click()
    except NoSuchElementException:
        submit_button = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[3]/button[2]')
        submit_button.click()
    except ElementClickInterceptedException:
        submit_button = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button')
        submit_button.click()




