from jira_client import JiraClient


def test_get_subtasks():
    jira = JiraClient()
    subtasks = jira.get_subtasks_for_story('WHLNT-3')
    assert len(subtasks) == 4


def test_fail_gettings_non_existing_subtasks():
    jira = JiraClient()
    subtasks = jira.get_subtasks_for_story('WHLNT-1')
    assert subtasks == None
