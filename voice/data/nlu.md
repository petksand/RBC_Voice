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

## intent:create
- create
- new
- open

## intent:close
- close
- finish

## intent:inform_story
- look at story [1](story_id)
- open story [34](story_id)
- can we see number [789](story_id)
- look at story number [45](story_id)
- open story number [12345](story_id)
- let's see number [79](story_id)
- let's see [9](story_id)

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

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really


## intent:end
- goodbye
- end
- over

## intent:check_balance
- what is my balance <!-- no entity -->
- how much do I have on my [savings](source_account) <!-- entity "source_account" has value "savings" -->
- how much do I have on my [savings account](source_account:savings) <!-- synonyms, method 1-->
- Could I pay in [yen](currency)?  <!-- entity matched by lookup table -->

## regex:zipcode
- [0-9]{5}

<!-- ## lookup:additional_currencies  no list to specify lookup table file -->
<!-- path/to/currencies.txt -->

## intent:goodbye
- bye
- goodbye
- see you around
- see you later