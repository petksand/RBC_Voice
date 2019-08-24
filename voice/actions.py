from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# from selenium import webdriver

# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []

# browser =  webdriver.Chrome()


class ActionStartMeeting(Action):
    """ Starts meeting and opens browser """

    def name(self):
        return "action_start"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Welcome")
        # driver.get("http://www.google.com")


class ActionViewStory(Action):
    """ Views story """
    
    def name(self):
        return "action_view_story"

    def run(self, dispatcher, tracker, domain):
        story_id = tracker.get_slot('story_id')
        dispatcher.utter_message(story_id)
        
