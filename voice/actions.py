from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from Exceptions import UnrecognizedInputException
# from selenium import webdriver


class ActionStartMeeting(Action):
    """ Starts meeting and opens browser """

    def name(self):
        return "action_start"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Welcome")
        # driver.get("http://www.google.com")


class ActionPrompt(Action):
    """ Prompts the user """

    def name(self):
        return "action_prompt"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("What would you like to do?")


class ActionViewStory(Action):
    """ Views story """
    
    def name(self):
        return "action_view_story"

    def run(self, dispatcher, tracker, domain):
        story_id = tracker.get_slot('story_id')
        if story_id == None:
            dispatcher.utter_message("Could recognize issue ID")
        else:
            dispatcher.utter_message("Viewing issue {}".format(story_id))
        
class ActionChangeProgress(Action):
    """ Changes issue progress """

    def name(self):
        return "action_change_progress"

    def run(self, dispatcher, tracker, domain):
        story_id = tracker.get_slot('story_id')
        workflow = tracker.get_slot('workflow')
        if story_id == None:
            dispatcher.utter_message("Could not recognize issue ID")
        elif workflow == None:
            dispatcher.utter_message("Could not recognize workflow")
        else:
            dispatcher.utter_message("Changing issue {} to be {}".format(story_id, workflow))


class ActionCreateStory(Action):
    """ Creates a new story in a board """

    def name(self):
        return "action_create_story"

    def run(self, dispatcher, tracker, domain):
        summary = tracker.get_slot('summary')
        if summary == None:
            dispatcher.utter_message("Could not recognize summary")
        else:
            dispatcher.utter_message("Creating new story: {}".format(summary))


class ActionCreateSubtask(Action):
    """ Creatas a new subtask under a given story """

    def name(self):
        return "action_create_subtask"

    def run(self, dispatcher, tracker, domain):
        story_id = tracker.get_slot("story_id")
        summary = tracker.get_slot("summary")
        if story_id == None:
            dispatcher.utter_message("Could not recognize issue ID")
        elif summary == None:
            dispatcher.utter_message("Could not recongnize summary")
        else:
            dispatcher.utter_message("Creating a new subtask under {}: {}".format(story_id, summary))


class ActionSummarize(Action):
    """ Summarizes the description in a JIRA issue """

    def name(self):
        return "action_summarize"

    def run(self, dispatcher, tracker, domain):
        story_id = tracker.get_slot("story_id")
        if story_id == None:
            dispatcher.utter_message("Could not recognize issue ID")
        else:
            dispatcher.utter_message("Summarize issue {}".format(story_id))


class ActionAssign(Action):
    """ Assigns an issue to a user """

    def name(self):
        return "action_assign"

    def run(self, dispatcher, tracker, domain):
        name = tracker.get_slot("name")
        story_id = tracker.get_slot("story_id")
        if story_id == None:
            dispatcher.utter_message("Could not recognize story ID")
        elif name == None:
            dispatcher.utter_message("Could not recognize name")
        else:
            dispatcher.utter_message("Assigning issue {} to {}".format(story_id, name))
