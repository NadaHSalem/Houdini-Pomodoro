# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pomodoroui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2 import QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(818, 632)
        MainWindow.setStyleSheet(u"background-color: rgb(90, 90, 90);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 6, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 5, 2, 1, 1)

        self.StatusLabel = QLabel(self.page)
        self.StatusLabel.setObjectName(u"StatusLabel")
        self.StatusLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.gridLayout.addWidget(self.StatusLabel, 3, 1, 1, 1)

        self.SettingsTool = QToolButton(self.page)
        self.SettingsTool.setObjectName(u"SettingsTool")
        self.SettingsTool.setStyleSheet(u"background-color: rgb(0, 85, 0);\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"color: white;")

        self.gridLayout.addWidget(self.SettingsTool, 3, 2, 1, 1)

        self.PomodoroPage = QLabel(self.page)
        self.PomodoroPage.setObjectName(u"PomodoroPage")
        self.PomodoroPage.setStyleSheet(u"font: 75 44pt;\n"
"color: rgb(255, 255, 255);\n"
"")

        self.gridLayout.addWidget(self.PomodoroPage, 0, 1, 1, 1)

        self.TimeRemaining = QLabel(self.page)
        self.TimeRemaining.setObjectName(u"TimeRemaining")
        self.TimeRemaining.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.gridLayout.addWidget(self.TimeRemaining, 5, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 6, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 4, 1)

        self.CalendarTool = QToolButton(self.page)
        self.CalendarTool.setObjectName(u"CalendarTool")
        self.CalendarTool.setStyleSheet(u"background-color: rgb(0, 85, 0);\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"color: white;")

        self.gridLayout.addWidget(self.CalendarTool, 1, 2, 1, 1)

        self.StartButton = QPushButton(self.page)
        self.StartButton.setObjectName(u"StartButton")
        self.StartButton.setStyleSheet(u"background-color: rgb(225, 112, 0);\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"color: white;")

        self.gridLayout.addWidget(self.StartButton, 6, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.SettingsPage = QWidget()
        self.SettingsPage.setObjectName(u"SettingsPage")
        self.gridLayout_4 = QGridLayout(self.SettingsPage)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.SettingsGrid = QGridLayout()
        self.SettingsGrid.setObjectName(u"SettingsGrid")
        self.ShortEdit = QPlainTextEdit(self.SettingsPage)
        self.ShortEdit.setObjectName(u"ShortEdit")

        self.SettingsGrid.addWidget(self.ShortEdit, 2, 2, 1, 1)

        self.label_7 = QLabel(self.SettingsPage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.SettingsGrid.addWidget(self.label_7, 3, 1, 1, 1)

        self.BackToTimerSettings = QPushButton(self.SettingsPage)
        self.BackToTimerSettings.setObjectName(u"BackToTimerSettings")
        self.BackToTimerSettings.setStyleSheet(u"background-color: rgb(225, 112, 0);\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"color: white;")

        self.SettingsGrid.addWidget(self.BackToTimerSettings, 5, 1, 1, 2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.SettingsGrid.addItem(self.horizontalSpacer_4, 1, 3, 1, 1)

        self.LongEdit = QPlainTextEdit(self.SettingsPage)
        self.LongEdit.setObjectName(u"LongEdit")

        self.SettingsGrid.addWidget(self.LongEdit, 3, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.SettingsGrid.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.FocusTimeEdit = QPlainTextEdit(self.SettingsPage)
        self.FocusTimeEdit.setObjectName(u"FocusTimeEdit")

        self.SettingsGrid.addWidget(self.FocusTimeEdit, 1, 2, 1, 1)

        self.label_5 = QLabel(self.SettingsPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.SettingsGrid.addWidget(self.label_5, 1, 1, 1, 1)

        self.SoundButton = QPushButton(self.SettingsPage)
        self.SoundButton.setObjectName(u"SoundButton")
        self.SoundButton.setStyleSheet(u"background-color: rgb(225, 112, 0);\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"color: white;")

        self.SettingsGrid.addWidget(self.SoundButton, 4, 1, 1, 2)

        self.label_6 = QLabel(self.SettingsPage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.SettingsGrid.addWidget(self.label_6, 2, 1, 1, 1)

        self.SettingsLabel = QLabel(self.SettingsPage)
        self.SettingsLabel.setObjectName(u"SettingsLabel")
        self.SettingsLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 44pt;\n"
"")

        self.SettingsGrid.addWidget(self.SettingsLabel, 0, 1, 1, 2)


        self.gridLayout_4.addLayout(self.SettingsGrid, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.SettingsPage)
        self.CalendarPage = QWidget()
        self.CalendarPage.setObjectName(u"CalendarPage")
        self.gridLayout_6 = QGridLayout(self.CalendarPage)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.CalendarGrid = QGridLayout()
        self.CalendarGrid.setObjectName(u"CalendarGrid")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.CalendarGrid.addItem(self.horizontalSpacer_5, 0, 3, 1, 1)

        self.CalendarLabel = QLabel(self.CalendarPage)
        self.CalendarLabel.setObjectName(u"CalendarLabel")
        self.CalendarLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 44pt;\n"
"")

        self.CalendarGrid.addWidget(self.CalendarLabel, 0, 1, 1, 2)

        self.BackToTimerCalendar = QPushButton(self.CalendarPage)
        self.BackToTimerCalendar.setObjectName(u"BackToTimerCalendar")
        self.BackToTimerCalendar.setStyleSheet(u"background-color: rgb(225, 112, 0);\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"color: white;")

        self.CalendarGrid.addWidget(self.BackToTimerCalendar, 3, 1, 1, 2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.CalendarGrid.addItem(self.horizontalSpacer_6, 0, 0, 1, 1)

        self.Calendar = QCalendarWidget(self.CalendarPage)
        self.Calendar.setObjectName(u"Calendar")

        self.CalendarGrid.addWidget(self.Calendar, 2, 1, 1, 1)


        self.gridLayout_6.addLayout(self.CalendarGrid, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.CalendarPage)

        self.gridLayout_3.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 818, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.StatusLabel.setText(QCoreApplication.translate("MainWindow", u"Focus", None))
        self.SettingsTool.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.PomodoroPage.setText(QCoreApplication.translate("MainWindow", u"Pomodoro", None))
        self.TimeRemaining.setText(QCoreApplication.translate("MainWindow", u"Time remaining", None))
        self.CalendarTool.setText(QCoreApplication.translate("MainWindow", u"Calendar", None))
        self.StartButton.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Long break time:", None))
        self.BackToTimerSettings.setText(QCoreApplication.translate("MainWindow", u"Back to timer", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Focus time:", None))
        self.SoundButton.setText(QCoreApplication.translate("MainWindow", u"Sound on/off", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Short break time:", None))
        self.SettingsLabel.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.CalendarLabel.setText(QCoreApplication.translate("MainWindow", u"Calendar", None))
        self.BackToTimerCalendar.setText(QCoreApplication.translate("MainWindow", u"Back to timer", None))
    # retranslateUi

