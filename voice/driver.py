from selenium_client import SeleniumClient
import time
import settings

controller = SeleniumClient()
controller.login()
controller.navigate_to_active_sprint_board()

time.sleep(3)
controller.open_issue(f"{settings.JIRA_PROJECT_KEY}-3")

time.sleep(2)
controller.assign_issue_to_user(f"{settings.JIRA_PROJECT_KEY}-3", "joe")
