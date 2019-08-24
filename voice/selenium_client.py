import time

from jira import JIRA, User
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

import settings


class SeleniumClient:
    _driver: WebDriver
    _jira: JIRA

    def __init__(self):
        self._driver = webdriver.Chrome()
        self._jira = JIRA(server=settings.JIRA_BASE_URL, basic_auth=(settings.JIRA_USERNAME, settings.JIRA_TOKEN))

    def login(self):
        self._driver.get("https://id.atlassian.com/login")

        el_user = self._driver.find_element_by_id("username")
        el_user.clear()
        el_user.send_keys(settings.JIRA_USERNAME)

        el_btn = self._driver.find_element_by_id("login-submit")
        el_btn.click()
        time.sleep(1)
        el_pass = self._driver.find_element_by_id("password")
        el_pass.send_keys(settings.JIRA_PASSWORD)

        el_btn.click()

        time.sleep(3)

    def navigate_to_active_sprint_board(self):
        self._driver.get(
            f"{settings.JIRA_BASE_URL}/secure/RapidBoard.jspa?rapidView=1&projectKey={settings.JIRA_PROJECT_KEY}"
        )

    def open_issue(self, issue_key: str):
        self._driver.get(
            f"{settings.JIRA_BASE_URL}/secure/RapidBoard.jspa?rapidView=1&projectKey={settings.JIRA_PROJECT_KEY}&modal=detail&selectedIssue={issue_key}"
        )

    def close_issue_view(self):
        el = self._driver.find_element_by_css_selector("span[aria-label=\"Close\"]")
        el.click()

    def assign_issue_to_user(self, issue_key: str, username: str):
        prj = self._jira.project(settings.JIRA_PROJECT_KEY)
        users = self._jira.search_users(username)
        u: User
        if len(users) == 1:
            u = users[0]
        else:
            raise ValueError("Too many users!")

        self._jira.assign_issue(issue_key, u.name)
        self._driver.refresh()

    def transition_issue(self, issue_key: str, to_status: str):
        res = self._jira.transition_issue(issue_key, to_status)
        return res
