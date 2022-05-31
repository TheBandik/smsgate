import json

import gammu


class SMSSender():
    def __init__(self):
        # self.usb = usb

        self.sm = gammu.StateMachine()
        self.sm.ReadConfig()
        self.sm.Init()
    
    def coding(self):
        pass

    def config(self):
        pass

    def send(self, text, number):
        message = {
            'Text': text,
            'SMSC': {'Location': 1},
            'Number': number,
            'Coding': 'Unicode_No_Compression'
        }

        self.sm.SendSMS(message)
    
    def run(self, message_file):
        with open(message_file, 'r') as f:
            data = json.load(f)

        for number in data['numbers']:
            print('Отправка сообщения...')
            self.send(data['message'], number)
