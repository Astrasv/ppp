
from plyer import notification


def send_nag():
    try:
        notification.notify(
            title='⚠️ DISAPPOINTMENT DETECTED',
            message='The code is rotting while you watch this.',
            timeout=4
        )
    except:
        pass
