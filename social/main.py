import argparse
from time import sleep

import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

parser = argparse.ArgumentParser()
parser.add_argument("--email", type=str, default="None", help="Enter email")
parser.add_argument("--password", type=str, default="None", help="Enter password")

if __name__ == '__main__':
    args = parser.parse_args()
    driver = webdriver.Firefox(executable_path="data/geckodriver")
    wait = WebDriverWait(driver, 20)
    driver.get("https://badoo.com/signin/?f=top")

    elem = wait.until(ec.visibility_of_element_located((By.ID, "signin-name")))
    elem.send_keys(args.email + Keys.RETURN)

    elem = wait.until(ec.visibility_of_element_located((By.ID, "signin-password")))
    elem.send_keys(args.password + Keys.RETURN)

    sleep(30)

    for _ in range(10):
        try:
            button = pyautogui.locateOnScreen("data/heart.png")
            pyautogui.click(button)
            for _ in range(1000):
                pyautogui.click(button)
                sleep(0.5)
        except OSError:
            pass
