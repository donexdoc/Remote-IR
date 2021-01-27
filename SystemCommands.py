"""
    Библиотека функций контроля компьютера
"""

import ctypes
from pynput.keyboard import Key, Controller


class CommandsControl:
    def __init__(self):
        self.keyboard = Controller()
        self.commands = {
            "media_prev": self.media_prev,
            "media_next": self.media_next,
            "media_play_pause": self.media_play_pause,
            "vol_down": self.vol_down,
            "vol_up": self.vol_up,
            "lock_screen": self.lock_screen,
            "fast_clean": self.fast_clean,
            "empty": self.__base_command(),
        }

    def run_command(self, cmd_name):
        func = self.commands.get(cmd_name, self.__base_command())
        func()

    def media_prev(self):
        self.keyboard.touch(Key.media_previous, True)

    def media_next(self):
        self.keyboard.touch(Key.media_next, True)

    def media_play_pause(self):
        self.keyboard.touch(Key.media_play_pause, True)

    def vol_down(self):
        self.keyboard.touch(Key.media_volume_down, True)

    def vol_up(self):
        self.keyboard.touch(Key.media_volume_up, True)

    def lock_screen(self):
        ctypes.windll.user32.LockWorkStation()

    def fast_clean(self):
        self.keyboard.press(Key.cmd_l)
        self.keyboard.press('d')
        self.keyboard.release(Key.cmd_l)
        self.keyboard.release('d')

    def __base_command(self):
        print("command is not defend")