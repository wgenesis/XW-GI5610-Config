#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @File     : my_port.py
# @Project  : Sleipnir
# @Software : PyCharm
# @Author   : why
# @Email    : weihaoyuan2@126.com
# @Time     : 2021/2/28 下午4:22

from PyQt5.QtCore import QTimer, pyqtSignal, QIODevice
from PyQt5.QtWidgets import QWidget
from PyQt5.QtSerialPort import QSerialPortInfo, QSerialPort


class MyPort(QWidget):
    portDataStrSig = pyqtSignal(str)
    portDataBytersSig = pyqtSignal(bytes)
    availablePortSig = pyqtSignal(list)
    portOpenSig = pyqtSignal(bool)

    def __init__(self, parent=None):
        super(MyPort, self).__init__(parent)
        self.ser = None
        self.port = QSerialPort()

        self.portOpen = False
        self.portInfo = QSerialPortInfo()
        self.availablePorts = []
        self.port = QSerialPort()
        self.paritySet = {'even': QSerialPort.EvenParity, 'odd': QSerialPort.OddParity, 'none': QSerialPort.NoParity}
        self.time = QTimer()
        self.portInfo = QSerialPortInfo()
        self.time.timeout.connect(self.updatePort)
        self.time.start(500)

    def closePort(self):
        self.portOpen = False
        self.port.close()

    def openPort(self, portConfig):
        global mySystem
        try:
            self.port.setPortName(self.portInfo.availablePorts()[portConfig['portIndex']].portName())
        except:
            return False
        if not self.port.setBaudRate(int(portConfig['baudrate']), QSerialPort.AllDirections):
            return False
        if not self.port.setStopBits(int(portConfig['stopbits'])):
            return False
        if not self.port.setParity(self.paritySet[portConfig['parity']]):
            return False
        if not self.port.open(QIODevice.ReadWrite):
            return False
        self.portOpen=True
        return True

    def readLineData(self):
        if self.portOpen:  # 如果串口打开
            # rxData = bytes(self.port.readAll())
            # data=rxData.decode('UTF-8')
            if self.port.canReadLine():
                data = str(self.port.readLine())
                self.portDataStrSig.emit(data)

    def readBytes(self):
        if self.portOpen:
            if self.port.bytesAvailable():
                data = self.port.readAll()
                # data = data.toHex()
                data = data.data()
                self.portDataBytersSig.emit(data)

    def updatePort(self):
        if len(self.availablePorts) != len(QSerialPortInfo().availablePorts()):  # 如果串口信息改变
            self.availablePorts = self.portInfo.availablePorts()  # 更新串口信息
            self.portOpen = False  # 串口标志位关闭
            self.port.close()  # 关闭串口
            availablePortList = []
            for port in self.availablePorts:
                availablePortList.append(port.description() + ' (' + port.portName() + ')')
            self.availablePortSig.emit(availablePortList)  # 发送新的串口信息
            self.portOpenSig.emit(self.portOpen)  # GUI按钮状态改变

    def forceUpdatePort(self):
        self.availablePorts = self.portInfo.availablePorts()  # 更新串口信息
        self.portOpen = False  # 串口标志位关闭
        self.port.close()  # 关闭串口
        availablePortList = []
        for port in self.availablePorts:
            availablePortList.append(port.description() + ' (' + port.portName() + ')')
        self.availablePortSig.emit(availablePortList)  # 发送新的串口信息
        self.portOpenSig.emit(self.portOpen)  # GUI按钮状态改变


class GPSPort(MyPort):
    gpsDataSig = pyqtSignal(str)
    gpsCmdSig = pyqtSignal(str)

    def __init__(self, parent=None):
        super(GPSPort, self).__init__(parent)
        self.headerList = ['GPHPD', 'GTIMU', 'GPFPD', 'GPRMC']
        self.portDataStrSig.connect(self.emitGPSData)
        self.port.readyRead.connect(self.readLineData)

    def emitGPSData(self, data):
        data = str(data)
        for header in self.headerList:
            if header in data:
                self.gpsDataSig.emit(data)
                break
        else:
            if '$' in data:
                self.gpsCmdSig.emit(data)

class ScreenPort(MyPort):
    screenDataSig=pyqtSignal(str)
    def __init__(self, parent=None):
        super(ScreenPort, self).__init__(parent)
        self.port.readyRead.connect(self.readBytes)
        self.portDataBytersSig.connect(self.emitScreenData)
        self.endSig='fffcffff'
        self.portData=''

    def emitScreenData(self,data):
        self.portData+=data.hex()
        if len(self.portData)>=len(self.endSig) and self.portData[-len(self.endSig):]==self.endSig:
            self.screenDataSig.emit(self.portData)
            self.portData=''

