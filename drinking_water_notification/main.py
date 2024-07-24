from notifypy import Notify
from time import sleep
def action():
    notification = Notify()
    notification.title  = "Drink Water"
    notification.message = "Pani khaaa machikneyy \n" *10
    notification.audio = "ring.wav"

    while (True):
        notification.send()
        sleep(0)

action()