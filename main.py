from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time

ACCOUNT_EMAIL = "EMAIL"
ACCOUNT_PWD = "PASSWORD"
PHONE = "NUMBER"

service = Service("SERVICE")
driver = webdriver.Chrome(service=service)
driver.get(
    "URL")

sign_in_button = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
sign_in_button.click()
time.sleep(2)
email_field = driver.find_element(By.ID, "username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(ACCOUNT_PWD)
password_field.send_keys(Keys.ENTER)
time.sleep(2)


def make_apply(com):
    com.click()
    time.sleep(1)
    try:
        # driver.find_element_by_class_name('jobs-apply-button').click()
        driver.find_element(By.CSS_SELECTOR,
                            ".jobs-unified-top-card__content--two-pane button.jobs-apply-button").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "form .artdeco-button--primary").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "form .artdeco-button--primary").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".jobs-easy-apply-content .artdeco-button--primary").click()
        time.sleep(1)

        try:
            driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss").click()
            time.sleep(1)
            driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__actionbar .artdeco-button--primary").click()
        except NoSuchElementException:
            print('Applied!')
            try:
                driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss").click()
            except NoSuchElementException:
                print('There was no questions')
        else:
            print('Filling out a form is requied!')

    except NoSuchElementException:
        print('Already applied')
    except ElementNotInteractableException:
        print('LinkedIn application loading error')


companies = driver.find_elements(By.CLASS_NAME, "job-card-container--clickable")
print(len(companies))
# make_apply(companies[4])

for company in companies:
    make_apply(company)
    time.sleep(1)

driver.close()
