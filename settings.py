from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

JIRA_BASE_URL = os.getenv("JIRA_BASE_URL", "https://whole-note.atlassian.net")
JIRA_USERNAME = os.getenv("JIRA_USERNAME")
JIRA_PASSWORD = os.getenv("JIRA_PASSWORD")
JIRA_TOKEN = os.getenv("JIRA_TOKEN")
JIRA_PROJECT_KEY = os.getenv("JIRA_PROJECT_KEY", "WHLNT")
