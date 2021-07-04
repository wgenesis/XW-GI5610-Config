#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @File     : slide_message.py
# @Project  : Sleipnir
# @Software : PyCharm
# @Author   : why
# @Email    : weihaoyuan2@126.com
# @Time     : 2021/2/28 下午3:59
from PyQt5.QtCore import QTimer, QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel


class Message(QLabel):
    def __init__(self, geometry=None, parent=None):
        super(Message, self).__init__(parent)
        self.color = {'red': '255,0,0', 'green': '0,255,0', 'white': '255,255,255', 'black': '0,0,0', 'blue': '0,0,255',
                      'orange': '255,153,0'}
        self.setGeometry(QRect(geometry[0], geometry[1], geometry[2], geometry[3]))
        font = QFont()
        font.setPointSize(10)
        self.setFont(font)
        self.setObjectName("INS_GPS_message")
        self.time = QTimer()
        self.time.timeout.connect(self.gradients)
        self.transparent = 0
        self.backgroundColor = '0,0,0'
        self.textColor = '0,0,0'
        self.Text = ''

    def colorConstraint(self, color, type_):
        if type(color) is str:
            if color in self.color:
                if type_ == 'background':
                    self.backgroundColor = self.color[color]
                    return True
                elif type_ == 'text':
                    self.textColor = self.color[color]
                    return True
                else:
                    return False
            else:
                return False
        elif type(color) is list or type(color) is tuple:
            if len(color) == 3 and max(color) <= 255 and min(color) >= 0:
                if type_ == 'background':
                    self.backgroundColor = str(color)[1:-1]
                    return True
                elif type_ == 'text':
                    self.textColor = str(color)[1:-1]
                    return True
                else:
                    return False
            else:
                return False

    def setStatusMessage(self, Text, backgroundColor, textColor):
        self.transparent = 250
        self.setText(Text)
        self.time.start(50)
        if not self.colorConstraint(backgroundColor, 'background'):
            raise KeyError('颜色设置错误！')
        if not self.colorConstraint(textColor, 'text'):
            raise KeyError('颜色设置错误！')

    def gradients(self):
        if self.transparent >= 0:
            self.setStyleSheet('background-color:' + 'rgba(' + self.backgroundColor + ',' + str(self.transparent) +
                               ');color: rgba(' + self.textColor + ',' + str(self.transparent) + ');')
            self.transparent -= 10
        else:
            self.time.stop()
