import gammu

# ?
sm = gammu.StateMachine()
# Чтение файла .gammurc
sm.ReadConfig()
# Подключение к модему
sm.Init()

message = {
    'Text': 'python-gammu testing message',
    'SMSC': {'Location': 1},
    'Number': '+79510237264',
}

sm.SendSMS(message)
