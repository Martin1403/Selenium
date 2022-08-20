import argparse
from time import sleep

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


url = "https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin"

parser = argparse.ArgumentParser()
parser.add_argument("--gmail", type=str, default="None", help="Enter gmail")
parser.add_argument("--password", type=str, default="None", help="Enter password")

if __name__ == "__main__":
    args = parser.parse_args()
    # Open browser url
    driver = uc.Chrome(use_subprocess=True)
    wait = WebDriverWait(driver, 20)
    driver.get(url)
    # Enter email + enter
    elem = wait.until(ec.visibility_of_element_located((By.ID, "identifierId")))
    elem.send_keys(args.gmail + "\n")
    # Enter password + enter
    elem = wait.until(ec.visibility_of_element_located((By.NAME, "password")))
    elem.send_keys(args.password + "\n")
    sleep(20)
