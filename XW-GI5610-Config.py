#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File     : path.py
# @Project  : Sleipnir
# @Software : PyCharm
# @Author   : why
# @Email    : weihaoyuan2@126.com
# @Time     : 2020/7/30 上午10:45
from src.displayGUI_INS import *

from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QWidget,QMainWindow,QApplication
from PyQt5.QtSerialPort import QSerialPortInfo

from custom_widgets.my_port import *
from custom_widgets.slide_message import *
from custom_widgets.switch_button import *

import qdarkstyle
import sys

class MyWindows(QMainWindow,Ui_MainWindow,QWidget):
    def __init__(self,parent=None):
        super(MyWindows,self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
        self.openPortBtn=SwitchBtn(geometry=(860,70,60,25),parent=self)
        self.command={'navigationStatus':'$cmd,get,navmode*ff',
                      'COMConfigure':'$cmd,get,com*ff',
                      'COMOutput':'$cmd,get,output*ff',
                      'GNSSLeverarm':'$cmd,get,leverarm*ff',
                      'odometerStatus':'$cmd,get,pulse*ff',
                      'saveConfig':'$cmd,save,config*ff',
                      'QX':['$cmd,output,com2,null*ff','$cmd,output,com2,gpgga,1*ff','$cmd,save,config*ff'],
                      'radioStation':['$cmd,output,com2,null*ff','$cmd,save,config*ff']}

        self.rate2speed={'1Hz':'1','2Hz':'0.5','5Hz':'0.2','10Hz':'0.1','20Hz':'0.05','100Hz':'0.01','null':'Null','new':'New'}
        self.myPort=GPSPort()
        self.INS_GPS_message=Message(geometry=(0, 480, 981, 30),parent=self.centralwidget)
        self.setConnect()

    def setConnect(self):
        self.openPortBtn.checkedChanged.connect(self.switchPort)
        self.INS_port_select_.currentIndexChanged.connect(self.closePort)
        self.INS_inquiry_GNSS.clicked.connect(self.inquirtConfig)
        self.INS_inquiry_navigation_status.clicked.connect(self.inquirtConfig)
        self.INS_inquiry_odometer_status.clicked.connect(self.inquirtConfig)
        self.INS_inquiry_COM_configure.clicked.connect(self.inquirtConfig)
        self.INS_inquiry_COM_output.clicked.connect(self.inquirtConfig)
        self.INS_signal_source_QX.clicked.connect(self.modeConfig)
        self.INS_signal_source_radio_station.clicked.connect(self.modeConfig)
        self.INS_COM_protocol_config_confirm.clicked.connect(self.comProcotolConfig)
        self.INS_COM_output_config_confirm.clicked.connect(self.comOutputConfig)
        self.INS_COM_through_config_confirm.clicked.connect(self.comThroughConfig)
        self.INS_save_config.clicked.connect(self.saveConfig)
        self.INS_cmd_send_message_send.clicked.connect(self.cmdSendWindow)
        self.INS_cmd_send_message_clear.clicked.connect(self.cmdSendWindow)
        self.INS_information_receive_message_clear.clicked.connect(self.infoReceiveWindowClear)
        self.myPort.availablePortSig.connect(self.updateAvailablePortSig)
        self.myPort.gpsCmdSig.connect(self.infoReceiveWindow)
        self.myPort.gpsDataSig.connect(self.displayGPSData)
        self.myPort.portOpenSig.connect(self.openPortBtn.statusSwitch)
        self.INS_COM_output_config_clear.clicked.connect(self.comOutputClear)


    def comOutputClear(self):
        cmd = '$cmd,output,' + self.INS_COM_output_config_COM_text.currentText() + ',null,' + '*ff'
        flage = self.writePort(cmd)
        if flage:
            self.INS_GPS_message.setStatusMessage('清除成功', 'green', 'white')
        elif flage is False:
            self.INS_GPS_message.setStatusMessage('清除失败', 'red', 'white')

    def updateAvailablePortSig(self,ports):
        self.INS_GPS_message.setStatusMessage('端口更新', 'orange', 'white')
        self.INS_port_select_.clear()
        for port in ports:
            self.INS_port_select_.addItem(port)

    def cmdSendWindow(self):
        sender = self.sender()
        if sender.text() == '发送':
            Str=self.INS_cmd_send_message.toPlainText()
            if Str == '':
                self.INS_GPS_message.setStatusMessage('请输入发送消息', 'orange', 'white')
            else:
                Str=Str.replace('\n','\r\n')
                flag=self.writePort(Str)
                if  flag is True:
                    self.INS_GPS_message.setStatusMessage('消息发送成功', 'green', 'white')
                elif flag is False:
                    self.INS_GPS_message.setStatusMessage('消息发送失败！', 'red', 'white')
        elif sender.text()=='清除':
            self.INS_cmd_send_message.clear()

    def saveConfig(self):
        flage=self.writePort(self.command['saveConfig'])
        if flage:
            self.INS_GPS_message.setStatusMessage('保存成功', 'green', 'white')
        elif flage is False:
            self.INS_GPS_message.setStatusMessage('保存失败', 'red', 'white')

    def comProcotolConfig(self):
        cmd='$cmd,set,'+self.INS_COM_protocol_config_COM_text.currentText()+','+self.INS_COM_protocol_config_baudrate_text.currentText()+','\
            +self.INS_COM_protocol_config_parity_text.currentText()+',8,'+self.INS_COM_protocol_config_stopbit_text.currentText()+','\
            +self.INS_COM_protocol_config_mode_text.currentText()+','+self.INS_COM_protocol_config_type_text.currentText()+'*ff'
        flage = self.writePort(cmd)
        if flage:
            self.INS_GPS_message.setStatusMessage('配置成功', 'green', 'white')
        elif flage is False:
            self.INS_GPS_message.setStatusMessage('配置失败', 'red', 'white')

    def comOutputConfig(self):
        cmd='$cmd,output,'+self.INS_COM_output_config_COM_text.currentText()+','+self.INS_COM_output_config_type_text.currentText()+','\
            +self.rate2speed[self.INS_COM_output_config_rate_text.currentText()]+'*ff'
        flage = self.writePort(cmd)
        if flage:
            self.INS_GPS_message.setStatusMessage('配置成功', 'green', 'white')
        elif flage is False:
            self.INS_GPS_message.setStatusMessage('配置失败', 'red', 'white')

    def comThroughConfig(self):
        cmd='$cmd,through,'+self.INS_COM_through_config_COM_text.currentText()+','+self.INS_COM_through_config_type_text.currentText()+','\
            +self.rate2speed[self.INS_COM_through_config_rate_text.currentText()]+'*ff'
        flage = self.writePort(cmd)
        if flage:
            self.INS_GPS_message.setStatusMessage('配置成功', 'green', 'white')
        elif flage is False:
            self.INS_GPS_message.setStatusMessage('配置失败', 'red', 'white')

    def inquirtConfig(self):
        sender=self.sender()
        flage=False
        if sender.text() == '导航状态':
            flage=self.writePort(self.command['navigationStatus'])
        elif sender.text() == 'COM配置':
            flage=self.writePort(self.command['COMConfigure'])
        elif sender.text() == 'COM输出':
            flage=self.writePort(self.command['COMOutput'])
        elif sender.text() == 'GNSS杆臂':
            flage=self.writePort(self.command['GNSSLeverarm'])
        elif sender.text() == '里程计状态':
            flage=self.writePort(self.command['odometerStatus'])
        if flage:
            self.INS_GPS_message.setStatusMessage('查询成功', 'green', 'white')
        elif flage is False:
            self.INS_GPS_message.setStatusMessage('查询失败', 'red', 'white')

    def modeConfig(self):
        sender=self.sender()
        flage=False
        if sender.text() == '千寻':
            flage=self.writePort(self.command['QX'])
        elif sender.text() == '基站':
            flage=self.writePort(self.command['radioStation'])
        if flage:
            self.INS_GPS_message.setStatusMessage('配置成功', 'green', 'white')
        elif flage is False:
            self.INS_GPS_message.setStatusMessage('配置失败', 'red', 'white')

    def switchPort(self):
        if self.myPort.portOpen == False:
            selectPortIndex=self.INS_port_select_.currentIndex()
            baudrate=self.INS_port_select_baudrate_.currentText()
            stopbits=self.INS_port_select_stopbit_.currentText()
            parity = self.INS_port_select_parity_.currentText()
            portConfig={'portIndex':selectPortIndex,'baudrate':baudrate,
                        'stopbits':stopbits,'parity':parity}
            if self.myPort.openPort(portConfig):
                self.myPort.portOpen = True
                self.INS_GPS_message.setStatusMessage('端口打开成功', 'green', 'white')
            else:
                self.INS_GPS_message.setStatusMessage('端口打开失败！','red','white')
                self.openPortBtn.statusSwitch(False)
        elif self.myPort.portOpen==True:
            self.myPort.closePort()
            self.INS_GPS_message.setStatusMessage('端口关闭成功', 'green', 'white')


    def closePort(self):
        self.openPortBtn.statusSwitch(False)

    def infoReceiveWindow(self,msg):
        self.INS_information_receive_message.append(msg)
        self.INS_information_receive_message.moveCursor(QTextCursor.End)

    def infoReceiveWindowClear(self):
        self.INS_information_receive_message.clear()

    def displayGPSData(self,data):
        self.INS_GPS_data_text.setText(data)

    def writePort(self,data):
        if self.myPort.portOpen:
            try:
                if type(data) is str:
                    self.myPort.port.write(bytes(data+'\n\r', encoding='utf-8'))
                elif type(data) is list:
                    for cmd in data:
                        self.myPort.port.write(bytes(cmd + '\n\r', encoding='utf-8'))
                return True
            except:
                return False

        else:
            self.INS_GPS_message.setStatusMessage('端口未打开！','red','white')
            return None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    portInfo=QSerialPortInfo()
    myWin=MyWindows()
    dark_stylesheet = qdarkstyle.load_stylesheet_pyqt5()
    app.setStyleSheet(dark_stylesheet)
    myWin.show()

    app.exec_()
    sys.exit(0)
