import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class SeleniumClient:
    _driver: WebDriver

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

    def navigate_to_active_sprint_board(self):
        self._driver.get(
            f"{settings.JIRA_BASE_URL}/secure/RapidBoard.jspa?rapidView=1&projectKey={settings.JIRA_PROJECT_KEY}"
        )

    def open_issue(self, issue_key: str):
        pass
