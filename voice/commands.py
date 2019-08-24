import os

def say(dispatcher, text):
    """
    Runs os "say" command
    """
    dispatcher.utter_message(text)
    os.system("say -r 180 -v Fiona {}".format(text))
    return True