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
        self._driver.maximize_window()

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
        time.sleep(4)

    def navigate_to_active_sprint_board(self):
        # navigate to project board
        self._driver.get(
            f"{settings.JIRA_BASE_URL}/secure/RapidBoard.jspa?rapidView=1&projectKey={settings.JIRA_PROJECT_KEY}"
        )

    def open_issue_view(self, issue_key: str):
        try:
            _ = int(issue_key)
            issue_key = f"{settings.JIRA_PROJECT_KEY}-{issue_key}"
        except ValueError:
            pass

        # wait until board appears
        self._wait.until(ec.visibility_of_element_located(
            (By.XPATH, "//span[@id=\"subnav-title\"]/span[@class=\"subnavigator-title\"]"))
        )
        # view issue
        self._driver.get(
            f"{settings.JIRA_BASE_URL}/secure/RapidBoard.jspa?rapidView=1&projectKey={settings.JIRA_PROJECT_KEY}&modal=detail&selectedIssue={issue_key}"
        )
        time.sleep(2)
        self._wait.until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, "#jira-issue-header, span[arial-label=\"Close\"]"))
        )

    def close_issue_view(self):
        el = self._wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "span[aria-label=\"Close\"]")))
        el.click()

    def assign_issue_to_user(self, issue_key: str, username: str):
        try:
            _ = int(issue_key)
            issue_key = f"{settings.JIRA_PROJECT_KEY}-{issue_key}"
        except ValueError:
            pass

        users = self._jira.search_users(username)
        u: User
        if len(users) == 1:
            u = users[0]
        else:
            raise ValueError("Too many matching users!")
        self._jira.assign_issue(issue_key, u.name)
        self._driver.refresh()

    def transition_issue(self, issue_key: str, to_status: str):
        try:
            _ = int(issue_key)
            issue_key = f"{settings.JIRA_PROJECT_KEY}-{issue_key}"
        except ValueError:
            pass

        self._jira.transition_issue(issue_key, to_status)
        self._driver.refresh()

    def end(self):
        self._driver.quit()
