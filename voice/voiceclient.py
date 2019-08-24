import requests
import speech_recognition as sr
import threading
from typing import Optional
from dotenv import load_dotenv
import logging
from os import environ


class VoiceClient:
    """
    Voice client to take in voice and output to Rasa.
    """
    def __init__(self, sender_name: str, url: str):
        """
        :param sender_name: The name of the sender used for this session.
        """
        self.sender_name = sender_name
        self.url = url

        self.is_running: bool = False
        self.runner: Optional[threading.Thread] = None

    def _send_speech_text(self, message: str):
        print('sending speech')
        resp = requests.get(self.url, data={
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

        def _run(_self: VoiceClient):
            recog = sr.Recognizer()
            while _self.is_running:
                with sr.Microphone() as source:
                    logging.info('Recording voice...')
                    audio = recog.listen(source=source)
                    logging.info('Recorded voice.')
                try:
                    recorded: str = recog.recognize_google(audio)
                    logging.info('Recorded: ' + recorded)
                    _self._send_speech_text(recorded)
                    return recorded
                except Exception as e:
                    logging.info(e)
        self.runner = threading.Thread(target=_run, args=[self])
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


def main():
    """
    Initialize the project
    """
    name = 'Scrummie the Scrum Bot'
    url = environ.get('RASA_URL') or 'http://localhost:5055'
    vc = VoiceClient(name, url)
    log_fmt = '%(asctime)-15s %(name)-8s %(message)s'
    logging.basicConfig(format=log_fmt, level=logging.DEBUG)

    logging.info('Starting Application:')
    logging.info('RASA URL: ' + url)
    logging.info('Bot Name: ' + name)
    try:
        vc.run()
    finally:
        vc.stop()


if __name__ == '__main__':
    load_dotenv()
    main()
