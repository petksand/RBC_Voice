from rasa_sdk import Action
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import settings
from selenium_context import SeleniumContext


class ActionStartMeeting(Action):
    """ Starts meeting and opens browser """

    def name(self):
        return "action_start"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Welcome")
        client = SeleniumContext.get_instance()
        client.login()
        client.navigate_to_active_sprint_board()


class ActionViewStory(Action):
    """ Views story """

    def name(self):
        return "action_view_story"

    def run(self, dispatcher, tracker, domain):
        issue_number = tracker.get_slot('story_id')
        dispatcher.utter_message(issue_number)

        client = SeleniumContext.get_instance()
        client.open_issue(f"{settings.JIRA_PROJECT_KEY}-{issue_number}")
