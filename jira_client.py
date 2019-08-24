from typing import List, Optional

from jira import JIRA, Issue


class JiraClient:
    _client: JIRA

    def __init__(self):
        self._client = JIRA(
            server='https://whole-note.atlassian.net',
            basic_auth=('poulad3@outlook.com', 'lalV0HEwmH0ehG1GaQGG6748')
        )

    def get_subtasks_for_story(self, issue_key: str) -> Optional[List[Issue]]:
        issue = self._client.issue(issue_key)
        subtasks = issue.fields.subtasks
        return subtasks if len(subtasks) > 0 else None
