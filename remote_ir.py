import serial
import ctypes
from pynput.keyboard import Key, Controller

import config

keyboard = Controller()

last_command = 'default'
hold_count = 0


def main():
    print("hey!")

    with serial.Serial(config.SERIAL_PORT, config.SERIAL_RATE, timeout=config.SERIAL_TIMEUOT) as ser:
        while True:
            line = ser.readline().strip()  # read a '\n' terminated line
            if len(line) > 0:
                command = command_controller(line)
                if command != 'repeat_last':
                    last_command = command
                    run_command(command)
                    hold_count = 0
                else:
                    if hold_count > config.IR_HOLD_COUNT:
                        run_command(last_command)
                    else:
                        hold_count += 1


def run_command(command):
    print(command)
    cases = {
        'ch': lock_screen,
        'eq': fast_clean,
        'vol+': vol_up,
        'vol-': vol_down,
        'play_pause': media_play_pause,
        'prev': media_prev,
        'next': media_next,
        '1': test_fnct,
        'default': default_case,
    }
    func = cases.get(command, lambda: "unknown_command")
    func()


def test_fnct():
    if check_lock():
        print('locked')
    else:
        print('not locked')
    # press_f()


def media_prev():
    keyboard.touch(Key.media_previous, True)


def media_next():
    keyboard.touch(Key.media_next, True)


def media_play_pause():
    keyboard.touch(Key.media_play_pause, True)


def vol_down():
    keyboard.touch(Key.media_volume_down, True)


def vol_up():
    keyboard.touch(Key.media_volume_up, True)


def lock_screen():
    ctypes.windll.user32.LockWorkStation()


def fast_clean():
    keyboard.press(Key.cmd_l)
    keyboard.press('d')
    keyboard.release(Key.cmd_l)
    keyboard.release('d')


def press_f():
    keyboard.press('f')
    keyboard.release('f')


def default_case():
    print("unknown_command")


def check_lock():
    if (ctypes.windll.user32.GetForegroundWindow() % 10 == 0):
        return True
    return False


def command_controller(command):
    for comm_code, comm_line in config.IR_COMMANDS.items():
        if comm_code == command:
            return comm_line
    return False


if __name__ == '__main__':
    main()
