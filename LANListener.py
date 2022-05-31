import inotify.adapters

from SMSSender import SMSSender

i = inotify.adapters.Inotify()

i.add_watch('messages')

while True:
    for event in i.event_gen(yield_nones=False):
        status = event[1][0]
        message_file = event[3]
        if status == 'IN_MOVED_TO' and message_file != '':
            print(status, message_file)
            smssender = SMSSender()
            smssender.run(f'messages/{message_file}')
