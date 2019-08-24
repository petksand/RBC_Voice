from jira import JIRA, User
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time

import settings


class SeleniumClient:
    _driver: WebDriver
    _wait: WebDriverWait
    _jira: JIRA

    def __init__(self):
        self._driver = webdriver.Chrome()
        self._wait = WebDriverWait(self._driver, 10)
        self._jira = JIRA(server=settings.JIRA_BASE_URL, basic_auth=(settings.JIRA_USERNAME, settings.JIRA_TOKEN))

    def login(self):
        self._driver.get("https://id.atlassian.com/login")

        # enter username
        el_user = self._driver.find_element_by_id("username")
        el_user.clear()
        el_user.send_keys(settings.JIRA_USERNAME)

        # wait for pass to appear, then fill
        el_btn = self._driver.find_element_by_id("login-submit")
        el_btn.click()
        el_pass = self._wait.until(ec.visibility_of_element_located((By.ID, "password")))
        el_pass.send_keys(settings.JIRA_PASSWORD)

        # click to login
        el_btn.click()
        time.sleep(3)

    def navigate_to_active_sprint_board(self):
        # navigate to project board
        self._driver.get(
            f"{settings.JIRA_BASE_URL}/secure/RapidBoard.jspa?rapidView=1&projectKey={settings.JIRA_PROJECT_KEY}"
        )

    def open_issue(self, issue_key: str):
        # wait until board appears
        self._wait.until(ec.visibility_of_element_located(
            (By.XPATH, "//span[@id=\"subnav-title\"]/span[@class=\"subnavigator-title\"]"))
        )
        # view issue
        self._driver.get(
            f"{settings.JIRA_BASE_URL}/secure/RapidBoard.jspa?rapidView=1&projectKey={settings.JIRA_PROJECT_KEY}&modal=detail&selectedIssue={issue_key}"
        )

    def close_issue_view(self):
        el = self._driver.find_element_by_css_selector("span[aria-label=\"Close\"]")
        el.click()

    def assign_issue_to_user(self, issue_key: str, username: str):
        # open issue if not already open
        if not self._driver.find_element_by_xpath(
                '//span[@class="css-eaycls"][text()="{}-{}"]'.format(settings.JIRA_PROJECT_KEY, issue_key)
        ):
            self.open_issue(issue_key)
        # assign given issue to given user
        self._jira.project(settings.JIRA_PROJECT_KEY)
        users = self._jira.search_users(username)
        u: User
        if len(users) == 1:
            u = users[0]
        else:
            raise ValueError("Too many matching users!")
        self._jira.assign_issue(issue_key, u.name)
        self._driver.refresh()

    def transition_issue(self, issue_key: str, to_status: str):
        res = self._jira.transition_issue(issue_key, to_status)
        return res