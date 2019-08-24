import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class SeleniumClient:
    _driver: WebDriver
    _base_url = "https://whole-note.atlassian.net"

    def __init__(self):
        self._driver = webdriver.Chrome()

    def login(self, email, password):
        self._driver.get("https://whole-note.atlassian.net/login")

        el_user = self._driver.find_element_by_id("username")
        el_user.clear()
        el_user.send_keys(email)

        el_btn = self._driver.find_element_by_id("login-submit")
        el_btn.click()
        time.sleep(1)
        el_pass = self._driver.find_element_by_id("password")
        el_pass.send_keys(password)

        el_btn.click()

        time.sleep(3)

        return True


    def navigate_to_active_sprint_board(self, project_key):
        self._driver.get("{}/secure/RapidBoard.jspa?rapidView=1&projectKey={}".format(self._base_url, project_key))
        return True

    def open_issue(self, issue_key: str):
        pass

    def end(self):
        self._driver.quit()