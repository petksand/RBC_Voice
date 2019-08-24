import speech_recognition as sr


def listen(recog: sr.Recognizer):
    with sr.Microphone() as source:
        audio = recog.listen(source=source)
        return audio


def main():
    recog = sr.Recognizer()
    audio = listen(recog)
    while True:
        try:
            recorded: str = recog.recognize_google(audio)
            print('Recorded: ' + recorded)

        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
