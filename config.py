# settings of application

SERIAL_PORT = 'COM3'
SERIAL_RATE = 9600
SERIAL_TIMEUOT = 1

# IR commands
IR_COMMANDS = {
    b'FFA25D': 'ch-',
    b'FF629D': 'ch',
    b'FFE21D': 'ch+',

    b'FF22DD': 'prev',
    b'FF02FD': 'next',
    b'FFC23D': 'play_pause',

    b'FFE01F': 'vol-',
    b'FFA857': 'vol+',
    b'FF906F': 'eq',

    b'FF6897': '0',
    b'FF9867': '100+',
    b'FFB04F': '200+',

    b'FF30CF': '1',
    b'FF18E7': '2',
    b'FF7A85': '3',

    b'FF10EF': '4',
    b'FF38C7': '5',
    b'FF5AA5': '6',

    b'FF42BD': '7',
    b'FF4AB5': '8',
    b'FF52AD': '9',

    b'FFFFFFFF': 'repeat_last',
}

IR_HOLD_COUNT = 7
