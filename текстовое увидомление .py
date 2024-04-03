#чтобы заработало pip install plyer

from plyer import notification
notification.notify(
    title='Ожидается кратко временный дожди',
    message='Какие там дожди апокалипсис ёбаный в рот',
    timeout=10
)
