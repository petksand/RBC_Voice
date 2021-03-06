## intent:start
- hey
- hello
- hi
- good morning
- hey there
- let's begin
- let's get started
- let's start
- let's go
- start
- begin
- begin session
- start session
- initiate automated scrum session

## intent:inform_story
- look at story [1](story_id)
- open story [34](story_id)
- can we see number [789](story_id)
- look at story number [45](story_id)
- open story number [12345](story_id)
- let's see number [79](story_id)
- let's see [9](story_id)
- let's see story number [09](story_id)
- view issue [6](story_id)
- open issue [898](story_id)

## intent:summarize
- summarize issue [5784](story_id)
- summarize story [44](story_id)
- summarize subtask [3](story_id)

## intent:assign
- assign [Poulad](names) to issue [67](story_id)
- assign [Sandra Petkovic](names) to subtask [987](story_id)
- assign [Joe](names) to story [67](story_id)
- assign [Joe](names) to [67](story_id)
- assign [Matt](names) to [456](story_id)
- assign issue [90](story_id) to [Joe](names)
- assign [567](story_id) to [Margaret](names)
- assign story [345678](story_id) to [Bill Mosely](names)
- assign subtask [6](story_id) to [Parth Smith](names)

<!-- ## lookup:names
../names.txt -->

## intent:change_workflow
- put [23](story_id) [in progress](workflow)
- put [299](story_id) in [in progress](workflow)
- change [390](story_id) to [backlog](workflow)
- move [1](story_id) to [done](workflow)
- move [16](story_id) to [to do](workflow)

## intent:create_story
- create a new story for [deployment](summary)
- make a new story for [deploy to prod](summary)
- open a story for [pipeline deploy](summary)
- make a new story for [bug fixes](summary)
- open a story for [fix bugs](summary)
- create a story for [deployment](summary)

## intent:create_subtask
- create a subtask for story [67](story_id) called [deploy to prod](summary)
- open a subtask under [456](story_id) for [code review](summary)
- create a new subtask for [98](story_id) for [bug fixes](summary)
- create a subtask for story [67](story_id) called [fixing bugs](summary)
- open a subtask under [456](story_id) for [SAI deployment](summary)
- create a new subtask for [98](story_id) for [reviewing code](summary)

## synonyms:summary
- deployment
- bugs
- reviewing code
- code review
- fixing bugs
- deploy to prod
- deploy to sai
- deploy to dev
- deployment

## intent:risk
- raise
- risk

## intent:confirm
- yeah
- yes
- yup
- indeed
- of course
- that sounds good
- correct
- absolutely
- yuh

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

## intent:close_issue
- close this
- close the window
- view the board again
- back to the board

## intent:end
- goodbye
- end
- over
- stop
- restart
