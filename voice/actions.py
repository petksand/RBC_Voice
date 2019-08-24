from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from summarize import generate_summary, read_article
import os
from commands import say

os.system("pip3 install selenium")

from selenium import webdriver
import selenium_client
import threading

import asyncio

browser = selenium_client.SeleniumClient()


class ActionStartMeeting(Action):
    """ Starts meeting and opens browser """

    def name(self):
        return "action_start"

    def run(self, dispatcher, tracker, domain):
        
        def _run():
            say(dispatcher, "Welcome")
            try:
                browser.login("petksand@gmail.com", "Password1")
            except:
                pass
        asyncio.get_event_loop().run_in_executor(None, _run)
                

class ActionOpenBoard(Action):
    
    def name(self):
        return "action_open_board"

    def run(self, dispatcher, tracke, domain):
         
        say(dispatcher, "Navigating to board")
        browser.navigate_to_active_sprint_board("WHLNT")

        return []
            

class ActionPrompt(Action):
    """ Prompts the user """

    def name(self):
        return "action_prompt"

    def run(self, dispatcher, tracker, domain):
        say(dispatcher, "What would you like to do?")


class ActionViewStory(Action):
    """ Views story """
    
    def name(self):
        return "action_view_story"

    def run(self, dispatcher, tracker, domain):
        story_id = tracker.get_slot('story_id')
        if story_id == None:
            say(dispatcher, "Could not recognize issue ID")
        else:
            say(dispatcher, "Viewing issue {}".format(story_id))
        
class ActionChangeProgress(Action):
    """ Changes issue progress """

    def name(self):
        return "action_change_progress"

    def run(self, dispatcher, tracker, domain):
        story_id = tracker.get_slot('story_id')
        workflow = tracker.get_slot('workflow')
        if story_id == None:
            say(dispatcher, "Could not recognize issue ID")
        elif workflow == None:
            say(dispatcher, "Could not recognize workflow")
        else:
            say(dispatcher, "Changing issue {} to be {}".format(story_id, workflow))


class ActionCreateStory(Action):
    """ Creates a new story in a board """

    def name(self):
        return "action_create_story"

    def run(self, dispatcher, tracker, domain):
        summary = tracker.get_slot("summary")
        if summary == None:
            say(dispatcher, "Could not recognize summary")
        else:
            say(dispatcher, "Creating new story: {}".format(summary))


class ActionCreateSubtask(Action):
    """ Creatas a new subtask under a given story """

    def name(self):
        return "action_create_subtask"

    def run(self, dispatcher, tracker, domain):
        story_id = tracker.get_slot("story_id")
        summary = tracker.get_slot("summary")
        if story_id == None:
            say(dispatcher, "Could not recognize issue ID")
        elif summary == None:
            say(dispatcher, "Could not recongnize summary")
        else:
            say(dispatcher, "Creating a new subtask under story {}: {}".format(story_id, summary))


class ActionSummarize(Action):
    """ Summarizes the description in a JIRA issue """

    def name(self):
        return "action_summarize"

    def run(self, dispatcher, tracker, domain):
        story_id = tracker.get_slot("story_id")
        if story_id == None:
            say(dispatcher, "Could not recognize issue ID")
        else:
            say(dispatcher, "Summarize issue {}".format(story_id))
            # summarize

            sentences = "A contextual assistant that goes beyond simple FAQ-style interactions requires more than just an algorithm and a prayer. A conversational assistant needs to have collected important details needed to answer user questions in the right context. Otherwise, no happy path. Simple enough, and known as slot filling. But how do you gather and define the details that matter before taking action, or providing a response? Slot filling is made easy with our new addition of FormPolicy. This is a fresh feature that implements slot filling in an easy and effective way. How? FormPolicy allows you to cover all the happy paths with a single story. Forms also let you alter logic within a happy path, without needing to change the training data. So, how do you implement this new technique? Glad you asked. Here’s how to get FormPolicy working for you."
            sentences = sentences.split(".")
            generate_summary(sentences, 2)


class ActionAssign(Action):
    """ Assigns an issue to a user """

    def name(self):
        return "action_assign"

    def run(self, dispatcher, tracker, domain):
        names = tracker.get_slot("names")
        story_id = tracker.get_slot("story_id")
        if story_id == None:
            say(dispatcher, "Could not recognize story ID")
        elif names == None:
            say(dispatcher, "Could not recognize name")
        else:
            say(dispatcher, "Assigning issue {} to {}".format(story_id, names))


class ActionEnd(Action):

    def name(self):
        return "action_end"

    def run(self, dispatcher, tracker, domain):
        say(dispatcher, "Quitting web browser")
        browser.end()
        return []
