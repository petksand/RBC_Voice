import requests
import speech_recognition as sr
import threading
from typing import Optional, Tuple
from dotenv import load_dotenv
import logging
from os import environ


def listen(recog: sr.Recognizer):
    with sr.Microphone() as source:
        audio = recog.listen(source=source)
        return audio


class VoiceClient:
    """
    Voice client to take in voice and output to Rasa.
    """
    def __init__(self, sender_name: str, url: str, credentials: Tuple[str, str]):
        """
        :param sender_name: The name of the sender used for this session.
        """
        self.sender_name = sender_name
        self.url = url
        self.credentials = credentials

        self.is_running: bool = False
        self.runner: Optional[threading.Thread] = None

    def _send_speech_text(self, message: str):
        resp = requests.get(self.url, auth=self.credentials, data={
            'sender': self.sender_name,
            'message': message
        })
        if resp.status_code == 200:
            r_json = resp.json()
            logging.debug(str(r_json))
            return r_json
        else:
            return None

    def run(self):
        """
        Begins a recording session where voice is recorded and sent to rasa for processing.
        :return:
        """
        self.is_running = True

        def _run():
            recog = sr.Recognizer()
            while self.is_running:
                with sr.Microphone() as source:
                    audio = recog.listen(source=source)
                try:
                    recorded: str = recog.recognize_google(audio)
                    logging.info('Recorded: ' + recorded)
                    self._send_speech_text(self.url, recorded)
                    return recorded
                except Exception as e:
                    logging.info(e)
        self.runner = threading.Thread(target=_run)
        self.runner.run()

    def stop(self):
        """
        Stops the session.
        :return:
        """
        self.is_running = False
        if self.runner is not None:
            try:
                self.runner.join(3000)
            except Exception as err:
                logging.error('Error stopping the Voice Client runner.\n' + str(err))
            finally:
                self.runner = None


if __name__ == '__main__':
    load_dotenv()
    vc = VoiceClient(
        'Scrummie the Scrum Bot',
        environ.get('RASA_URL') or 'http://localhost:5055',
        (environ['JIRA_USERNAME'], environ['JIRA_TOKEN'])
    )
    try:
        vc.run()
    finally:
        vc.stop()
