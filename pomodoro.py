import sys
import os

import threading
import time

from datetime import datetime

import hou
from PySide2 import QtCore,  QtWidgets, QtUiTools, QtGui
from PySide2.QtWidgets import QVBoxLayout, QWidget, QMainWindow, QPushButton, QApplication, QLabel
from PySide2.QtCore import Qt, QTime, QTimer
from PySide2.QtUiTools import QUiLoader


sys.path.append(r"C:/Program Files/Side Effects Software/Houdini 19.5.702/houdini/python3.9libs/pomodoro")
sys.path.append(r"C:/Program Files/Side Effects Software/Houdini 19.5.702/houdini/python3.9libs/pomodoro/mainwindow.py")
#print(sys.path)

from mainwindow import Ui_MainWindow

print("**********TESTING**********")

script_path = os.path.dirname(__file__)
#print("Script path: " + script_path)

FOCUS_TIME = 3
LONG_BREAK_TIME = 2
SHORT_BREAK_TIME = 1

class PomodoroFrame(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Create timer
        self.timeLeft = FOCUS_TIME
        self.isOn = True
        self.isDoneFocus = True
        self.focusCounter = 0
        self.ui.TimeRemaining.setText(str(self.timeLeft))
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)

        self.ui.SettingsTool.clicked.connect(self.SettingsHandler)
        self.ui.CalendarTool.clicked.connect(self.CalendarHandler)
        self.ui.StartButton.clicked.connect(self.startButtonHandler)
        self.ui.BackToTimerSettings.clicked.connect(self.BackToTimerHandler)
        self.ui.BackToTimerCalendar.clicked.connect(self.BackToTimerHandler)
    
    def TimeoutHandler(self):
        self.timeLeft -= 1
        if self.timeLeft == 0:
            print("Time is up!!!!!!!")
            self.pomodorotimer.stop()
            self.isOn = True
            self.ui.StartButton.setText("START")
            if self.focusCounter > 0 and self.focusCounter % 4 == 0:
                self.timeLeft = LONG_BREAK_TIME
                self.ui.StatusLabel.setText("Treat yourself to a long break")
                self.isDoneFocus = False
                #include some sort of windows notif in case the user is on another app 
                print("Number of completed Focus sessions: " + str(self.focusCounter))
            elif self.isDoneFocus:
                self.focusCounter += 1
                self.timeLeft = SHORT_BREAK_TIME
                self.isDoneFocus = False
                self.ui.StatusLabel.setText("Treat yourself to a short break")
                #include some sort of windows notif in case the user is on another app 
                self.isDoneFocus = False
            elif not self.isDoneFocus:
                self.ui.StatusLabel.setText("Focus")
                self.timeLeft = FOCUS_TIME
                self.isDoneFocus = True
                #include some sort of windows notif in case the user is on another app 

        self.updateTimeLeft()

    def startButtonHandler(self):
        if self.isOn:
            print("START BUTTON PRESSED")
            self.ui.StartButton.setText("PAUSE")
            self.isOn = False
            self.pomodorotimer = QTimer()
            self.pomodorotimer.timeout.connect(self.TimeoutHandler)
            # Start timer and update every second
            self.pomodorotimer.start(1000)
        else:
            print("PAUSE BUTTON PRESSED")
            self.ui.StartButton.setText("START")
            self.pomodorotimer.stop()
            self.isOn = True
            self.pomodorotimer.timeout.connect(self.TimeoutHandler)

    
    def BackToTimerHandler(self):
        print("Back to main CLICKED")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)

    def SettingsHandler(self):
        print("SETTINGS CLICKED")
        self.ui.stackedWidget.setCurrentWidget(self.ui.SettingsPage)

    def CalendarHandler(self):
        print("CALENDAR PRESSED")
        self.ui.stackedWidget.setCurrentWidget(self.ui.CalendarPage)

    def updateTimeLeft(self):
        self.ui.TimeRemaining.setText(str(self.timeLeft))
