## start_meeting
* start
  - action_start
  - action_open_board
  - action_prompt

## close_window
* close_issue
  - action_close_window

## view_story
* inform_story{"story_id":null}
  - slot{"story_id":"1"}
  - action_view_story

## change_workflow
* change_workflow{"story_id":"1","workflow":"backlog"}
  - slot{"workflow":null, "story_id":null}
  - action_change_progress

## create_story 
* create_story{"summary":""}
  - slot{"summary":null}
  - action_create_story

## create_subtask
* create_subtask{"story_id":"1","summary":""}
  - slot{"summary":null, "story_id":null}
  - action_create_subtask

## get_summary
* summarize{"story_id":"1"}
  - slot{"story_id":null}
  - action_summarize

## assign_issue
* assign{"names":"", "story_id":"1"}
  - slot{"names":null, "story_id":null}
  - action_assign

## restart
* end
  - action_end
  - action_restart
