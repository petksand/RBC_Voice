from typing import List, Optional

from jira import JIRA, Issue

import settings


class JiraClient:
    _client: JIRA

    def __init__(self):
        self._client = JIRA(
            server=settings.JIRA_BASE_URL,
            basic_auth=(settings.JIRA_USERNAME, settings.JIRA_TOKEN)
        )

    def get_subtasks_for_story(self, issue_key: str) -> Optional[List[Issue]]:
        issue = self._client.issue(issue_key)
        subtasks = issue.fields.subtasks
        return subtasks if len(subtasks) > 0 else None
