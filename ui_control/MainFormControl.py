import serial, serial.tools.list_ports, threading, json
from datetime import datetime
from serial.serialutil import SerialException

from PySide2 import QtCore, QtGui
from PySide2.QtCore import QSize
from PySide2.QtWidgets import QMainWindow

from PySide2.QtGui import QIcon
from ui_design.pyforms.MainWindowForm import Ui_MainWindow
import sys
import config_gui
from SystemCommands import CommandsControl

#<div>Icons made by <a href="http://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>


class MainWindow(QMainWindow):
    """
    Обработка главной формы приложения
    """

    def __init__(self):
        super(MainWindow, self).__init__()

        # Инициализация пользовательского интерфейса
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # загружаем иконки приложения
        self.icon_reload = QIcon()
        self.icon_reload.addFile(u"assets/icons/sync-solid.svg", QSize(), QIcon.Normal, QIcon.Off)

        self.icon_save = QIcon()
        self.icon_save.addFile(u"assets/icons/save-solid.svg", QSize(), QIcon.Normal, QIcon.Off)

        self.icon_add = QIcon()
        self.icon_add.addFile(u"assets/icons/plus-solid.svg", QSize(), QIcon.Normal, QIcon.Off)

        self.icon_delete = QIcon()
        self.icon_delete.addFile(u"assets/icons/trash-solid.svg", QSize(), QIcon.Normal, QIcon.Off)

        self.icon_play = QIcon()
        self.icon_play.addFile(u"assets/icons/play-solid.svg", QSize(), QIcon.Normal, QIcon.Off)

        self.icon_pause = QIcon()
        self.icon_pause.addFile(u"assets/icons/pause-solid.svg", QSize(), QIcon.Normal, QIcon.Off)

        # настройка кнопок с иконками
        self.ui.updatePortListBtn.setIcon(self.icon_reload)
        self.ui.addCommandBtn.setIcon(self.icon_add)
        self.ui.deleteCommandBtn.setIcon(self.icon_delete)
        self.ui.saveCommandBtn.setIcon(self.icon_save)

        # Настройки потока
        self.listen_serial = False

        # инициализируем функции интерактивных элементов
        self.ui.receiveChangeBtn.clicked.connect(self.receive_change)
        self.ui.serialPortCmbx.currentIndexChanged.connect(self.serial_combobox_index_changed)
        self.ui.updatePortListBtn.clicked.connect(self.serial_ports_check)
        self.ui.addCommandBtn.clicked.connect(self.add_command)
        self.ui.deleteCommandBtn.clicked.connect(self.delete_command)
        self.ui.signalLw.itemSelectionChanged.connect(self.signal_selected)
        self.ui.saveCommandBtn.clicked.connect(self.selected_action_save)

        # настройки пртов
        self.selected_port = False
        self.available_ports = list()

        # инициализация библиотеки контроля
        self.control_commands = CommandsControl()

        # глобальные переменные относящиеся к сигналам
        self.last_signal = ""
        self.bound_signals = []
        self.selected_signal = -1

        # запускаемые функции при старте графической части
        self.check_status()
        self.serial_ports_check()
        self.signal_editor_elements_state(False)
        self.load_commands()

        # временные
        # {"code": "FF906F", "command": "fast_clean"},
        # self.bound_signals = [
        #     {
        #         "code": "FFE01F",
        #         "command": "vol_up"
        #     },
        #     {
        #         "code": "FFA857",
        #         "command": "vol_down"
        #     }
        # ]


    def save_commands(self):
        json_str = json.dumps(self.bound_signals)
        with open('commands.json', 'w+') as f:
            f.write(json_str)

    def load_commands(self):
        with open('commands.json') as json_file:
            data = json.load(json_file)
            self.bound_signals = data
        self.reload_bounded_signals()

    def reload_bounded_signals(self):
        """
        Генерируем список сигналов из того, что находится в памяти программы
        :return:
        """
        self.ui.signalLw.clear()
        for command in self.bound_signals:
            cmd_code = command.get("code")
            cmd_name = command.get("command")
            self.ui.signalLw.addItem(f"{cmd_code} - {cmd_name}")
        self.save_commands()

    def signal_editor_elements_state(self, enable_status):
        """
        Активируем и деактивируем поля редактрирования сигнала
        :param enable_status:
        :return:
        """
        self.ui.signalCodeLe.setEnabled(enable_status)
        self.ui.actionSelectCmbx.setEnabled(enable_status)
        self.ui.saveCommandBtn.setEnabled(enable_status)
        self.ui.deleteCommandBtn.setEnabled(enable_status)
        if not enable_status:
            self.ui.signalCodeLe.setText("")
            self.ui.actionSelectCmbx.clear()

    def action_list_generate(self, command):
        """
        Генерируем список доступных функций из библиотеки,
        если видим ту, которая используется сейчас то ставим на нее фокус
        :param command:
        :return:
        """
        for number, cmd in enumerate(self.control_commands.commands.keys()):
            self.ui.actionSelectCmbx.addItem(cmd)
            if command == cmd:
                founded_index = number
                self.ui.actionSelectCmbx.setCurrentIndex(founded_index)

    def signal_selected(self):
        """
        При выборе сигнала из списка, открывается доступ к редактированию этого сигнала и его команды
        :return:
        """
        if self.ui.signalLw.selectedIndexes():
            selected_index = self.ui.signalLw.selectedIndexes()[0].row()
            self.selected_signal = selected_index

            item = self.bound_signals[selected_index]

            self.signal_editor_elements_state(True)
            self.ui.signalCodeLe.setText(item["code"])

            self.action_list_generate(item["command"])
        else:
            self.signal_editor_elements_state(False)

    def check_status(self):
        """
        Вспомогательная функция проверки статуса прослушки порта
        при прослушке порта отключаются все функции, которые могут повлиять на переменную активного порта
        :return:
        """
        if self.listen_serial:
            self.ui.receiveChangeBtn.setIcon(self.icon_pause)
            self.ui.serialPortCmbx.setEnabled(False)
            self.ui.updatePortListBtn.setEnabled(False)
            self.ui.statusbar.showMessage(f"Listening commands from port [{self.selected_port}]")
        else:
            self.ui.receiveChangeBtn.setIcon(self.icon_play)
            self.ui.serialPortCmbx.setEnabled(True)
            self.ui.updatePortListBtn.setEnabled(True)
            self.ui.statusbar.showMessage(f"Waiting actions from user")

    def receive_change(self):
        """
        Обработка нажатия на кнопку начал приема сообщений
        :return:
        """
        if self.listen_serial:
            self.listen_serial = False
        else:
            self.listen_serial = True
            self.thread_listing_start()

        self.check_status()

    def thread_listing_start(self):
        """
        Стартуем поток для прослушки порта
        :return:
        """
        self.add_to_log("Starting listen")
        threading.Thread(target=self.connect_serial).start()

    def closeEvent(self, event):
        """
        Операции еред выходом
        :param event:
        :return:
        """
        # выходим из цикла, чтобы программа не висела с процессом в диспетчере
        self.ui.statusbar.showMessage(f"Finishing thread")
        self.listen_serial = False

    def connect_serial(self):
        """
        Функция для прослушки выбранного порта.
        Запускаете в отдельном потоке, когда идет работа прослушки.
        :return:
        """
        if self.selected_port:
            try:
                with serial.Serial(
                        self.selected_port, config_gui.SERIAL_RATE,
                        timeout=config_gui.SERIAL_TIMEOUT) as ser:
                    while self.listen_serial:
                        self.ui.statusbar.showMessage(f"Listening commands from port [{self.selected_port}]")
                        line = ser.readline().strip().decode("utf-8")
                        if line != "FFFFFFFF" and line != self.last_signal:
                            self.last_signal = line
                        if len(line) > 0:
                            if line != 'FFFFFFFF':
                                self.call_command(line)
                                hold_count = 0
                                self.add_to_log(line)
                            else:
                                if hold_count > config_gui.IR_HOLD_COUNT:
                                    self.call_command(self.last_signal)
                                else:
                                    hold_count += 1
            except SerialException as serial_error:
                print(f"Serial not connected: {serial_error}")
                self.add_to_log(f"Serial port connecting error: {serial_error}")
            except:
                print("unexpected error")
                self.add_to_log("unexpected error")
        else:
            print("port is not selected")
            self.add_to_log("port is not selected")

        self.add_to_log("Stopping listen")
        self.listen_serial = False
        self.check_status()

    def call_command(self, signal):
        for i_signal in self.bound_signals:
            if i_signal["code"] == signal:
                self.control_commands.run_command(i_signal["command"])
                return
        self.add_to_log(f"Not bound signal code {signal}")

    def serial_ports_check(self):
        """
        Проверяем доступные порты
        :return:
        """
        ports_list = serial.tools.list_ports.comports()
        if self.available_ports != ports_list:
            self.available_ports = ports_list
            self.update_serial_combobox()
        self.add_to_log(f"List of ports is updated")

    def update_serial_combobox(self):
        """
        Обновляем список доступных портов в combobox
        :return:
        """
        self.ui.serialPortCmbx.clear()
        for port in self.available_ports:
            self.ui.serialPortCmbx.addItem(port.device)

    def serial_combobox_index_changed(self):
        """
        Действие при изменении выбранного элемента в cobobox
        :return:
        """
        self.selected_port = self.ui.serialPortCmbx.currentText()
        print(f"current selected port: {self.selected_port}")
        self.ui.statusbar.showMessage(f"port changed to [{self.selected_port}]")

    def add_to_log(self, text):
        """
        Добавляем запись в лог на экране
        :param text:
        :return:
        """
        now_time = datetime.now().strftime("%H:%M:%S")
        self.ui.logTe.insertPlainText(f"[{now_time}] - {text}\n")
        self.ui.logTe.moveCursor(QtGui.QTextCursor.End)

    def add_command(self):
        """
        Добавляем пустую команду
        :return:
        """
        self.bound_signals.append({
            "code": "FFFFFF",
            "command": "empty"
        })
        self.reload_bounded_signals()
        self.selected_signal = -1

    def delete_command(self):
        """
        Удаляем выбранную команду
        :return:
        """
        if self.selected_signal != -1:
            self.bound_signals.remove(self.bound_signals[self.selected_signal])
        self.reload_bounded_signals()
        self.selected_signal = -1

    def selected_action_save(self):
        """
        Сохраняем выбранную команду
        :return:
        """
        if self.selected_signal != -1:
            self.bound_signals[self.selected_signal]["command"] = self.ui.actionSelectCmbx.currentText()
            self.bound_signals[self.selected_signal]["code"] = self.ui.signalCodeLe.text()
        self.reload_bounded_signals()
        self.selected_signal = -1