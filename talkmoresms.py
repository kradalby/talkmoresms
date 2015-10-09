import requests
import json

BASE_URL = 'https://www.talkmore.no'
LOGIN_ENDPOINT = '/talkmore3/servlet/Login'
SMS_ENDPOINT = '/talkmore3/servlet/SendSmsFromSelfcare'


class TalkmoreCannotLoginException:
    pass


class TalkmoreTooLongSMSException:
    pass


class TalkmoreSMSFailedToSendException:
    pass


class Talkmore:

    def __init__(self, number, password):
        self.number = number
        self.password = password
        self.session = requests.session()

    def login(self):
        login_payload = {
            'username': self.number,
            'password': self.password,
            'submit': 'submit'
        }
        request = self.session.post(BASE_URL + LOGIN_ENDPOINT, data=login_payload)
        if request.status_code != 200:
            raise TalkmoreCannotLoginException()

    def send(self, contacts, message):
        if len(message) > 480:
            raise TalkmoreTooLongSMSException()

        payload = {
            'message1': message,
            'list': contacts
        }

        request = self.session.post(BASE_URL + SMS_ENDPOINT, data=payload)

        if request.status_code != 200:
            raise TalkmoreSMSFailedToSendException()
