## start_meeting
* start
  - action_start
  - action_prompt
<!-- > progress_from_start -->

## view_story
<!-- > progress_from_start -->
* inform_story{"story_id":null}
  - slot{"story_id":"1"}
  - action_view_story

## change_workflow
<!-- > progress_from_start -->
* change_workflow{"story_id":"1","workflow":"backlog"}
  - slot{"workflow":null, "story_id":null}
  - action_change_progress

## create_story 
<!-- > progress_from_start -->
* create_story{"summary":""}
  - slot{"summary":null}
  - action_create_story

## create_subtask
<!-- > progress_from_start -->
* create_subtask{"story_id":"1","summary":""}
  - slot{"summary":null, "story_id":null}
  - action_create_subtask

<!-- ## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye -->
