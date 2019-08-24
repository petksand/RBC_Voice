import speech_recognition as sr


def listen(recog: sr.Recognizer):
    with sr.Microphone() as source:
        print('Started recording')
        audio = recog.listen(source=source, phrase_time_limit==2000)
        print('Finished recording')
        return audio


def main():
    recog = sr.Recognizer()
    audio = listen(recog)
    try:
        print('Analyzing with Google...')
        recorded: str = recog.recognize_google(audio)
        print('Recorded: ' + recorded)
        return recorded
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()