# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'displayGUI_INS.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(980, 531)
        MainWindow.setMinimumSize(QtCore.QSize(980, 531))
        MainWindow.setMaximumSize(QtCore.QSize(980, 531))
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 951, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("方正姚体")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(10, 50, 951, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.INS_inquiry = QtWidgets.QLabel(self.centralwidget)
        self.INS_inquiry.setGeometry(QtCore.QRect(20, 210, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.INS_inquiry.setFont(font)
        self.INS_inquiry.setObjectName("INS_inquiry")
        self.INS_cmd_send_message_send = QtWidgets.QPushButton(self.centralwidget)
        self.INS_cmd_send_message_send.setGeometry(QtCore.QRect(540, 140, 80, 26))
        self.INS_cmd_send_message_send.setObjectName("INS_cmd_send_message_send")
        self.INS_signal_source_QX = QtWidgets.QPushButton(self.centralwidget)
        self.INS_signal_source_QX.setGeometry(QtCore.QRect(19, 140, 91, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.INS_signal_source_QX.setFont(font)
        self.INS_signal_source_QX.setObjectName("INS_signal_source_QX")
        self.INS_save_config = QtWidgets.QPushButton(self.centralwidget)
        self.INS_save_config.setGeometry(QtCore.QRect(680, 420, 281, 31))
        self.INS_save_config.setObjectName("INS_save_config")
        self.INS_signal_source_radio_station = QtWidgets.QPushButton(self.centralwidget)
        self.INS_signal_source_radio_station.setGeometry(QtCore.QRect(19, 180, 91, 26))
        self.INS_signal_source_radio_station.setObjectName("INS_signal_source_radio_station")
        self.INS_GPS_data = QtWidgets.QLabel(self.centralwidget)
        self.INS_GPS_data.setGeometry(QtCore.QRect(30, 460, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.INS_GPS_data.setFont(font)
        self.INS_GPS_data.setObjectName("INS_GPS_data")
        self.INS_inquiry_navigation_status = QtWidgets.QPushButton(self.centralwidget)
        self.INS_inquiry_navigation_status.setGeometry(QtCore.QRect(20, 240, 91, 26))
        self.INS_inquiry_navigation_status.setObjectName("INS_inquiry_navigation_status")
        self.INS_inquiry_odometer_status = QtWidgets.QPushButton(self.centralwidget)
        self.INS_inquiry_odometer_status.setGeometry(QtCore.QRect(20, 400, 91, 26))
        self.INS_inquiry_odometer_status.setObjectName("INS_inquiry_odometer_status")
        self.INS_cmd_send_message_clear = QtWidgets.QPushButton(self.centralwidget)
        self.INS_cmd_send_message_clear.setGeometry(QtCore.QRect(540, 180, 80, 26))
        self.INS_cmd_send_message_clear.setObjectName("INS_cmd_send_message_clear")
        self.INS_cmd_send = QtWidgets.QLabel(self.centralwidget)
        self.INS_cmd_send.setGeometry(QtCore.QRect(160, 110, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.INS_cmd_send.setFont(font)
        self.INS_cmd_send.setObjectName("INS_cmd_send")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(640, 120, 20, 331))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.INS_inquiry_COM_output = QtWidgets.QPushButton(self.centralwidget)
        self.INS_inquiry_COM_output.setGeometry(QtCore.QRect(20, 320, 91, 26))
        self.INS_inquiry_COM_output.setObjectName("INS_inquiry_COM_output")
        self.INS_information_receive = QtWidgets.QLabel(self.centralwidget)
        self.INS_information_receive.setGeometry(QtCore.QRect(160, 280, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.INS_information_receive.setFont(font)
        self.INS_information_receive.setObjectName("INS_information_receive")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(130, 120, 20, 331))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.INS_inquiry_GNSS = QtWidgets.QPushButton(self.centralwidget)
        self.INS_inquiry_GNSS.setGeometry(QtCore.QRect(20, 360, 91, 26))
        self.INS_inquiry_GNSS.setObjectName("INS_inquiry_GNSS")
        self.INS_information_receive_message = QtWidgets.QTextEdit(self.centralwidget)
        self.INS_information_receive_message.setGeometry(QtCore.QRect(160, 310, 371, 141))
        self.INS_information_receive_message.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.INS_information_receive_message.setObjectName("INS_information_receive_message")
        self.INS_inquiry_COM_configure = QtWidgets.QPushButton(self.centralwidget)
        self.INS_inquiry_COM_configure.setGeometry(QtCore.QRect(20, 280, 91, 26))
        self.INS_inquiry_COM_configure.setObjectName("INS_inquiry_COM_configure")
        self.INS_information_receive_message_clear = QtWidgets.QPushButton(self.centralwidget)
        self.INS_information_receive_message_clear.setGeometry(QtCore.QRect(540, 310, 80, 26))
        self.INS_information_receive_message_clear.setObjectName("INS_information_receive_message_clear")
        self.INS_GPS_data_text = QtWidgets.QLabel(self.centralwidget)
        self.INS_GPS_data_text.setGeometry(QtCore.QRect(90, 460, 871, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.INS_GPS_data_text.setFont(font)
        self.INS_GPS_data_text.setObjectName("INS_GPS_data_text")
        self.INS_signal_source = QtWidgets.QLabel(self.centralwidget)
        self.INS_signal_source.setGeometry(QtCore.QRect(20, 110, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.INS_signal_source.setFont(font)
        self.INS_signal_source.setObjectName("INS_signal_source")
        self.INS_cmd_send_message = QtWidgets.QTextEdit(self.centralwidget)
        self.INS_cmd_send_message.setGeometry(QtCore.QRect(160, 140, 371, 141))
        self.INS_cmd_send_message.setObjectName("INS_cmd_send_message")
        self.INS_port_select_ = QtWidgets.QComboBox(self.centralwidget)
        self.INS_port_select_.setGeometry(QtCore.QRect(80, 70, 221, 20))
        self.INS_port_select_.setObjectName("INS_port_select_")
        self.INS_port_select = QtWidgets.QLabel(self.centralwidget)
        self.INS_port_select.setGeometry(QtCore.QRect(10, 70, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.INS_port_select.setFont(font)
        self.INS_port_select.setObjectName("INS_port_select")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(660, 120, 311, 291))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 291, 240))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setHorizontalSpacing(6)
        self.formLayout_2.setVerticalSpacing(8)
        self.formLayout_2.setObjectName("formLayout_2")
        self.INS_COM_protocol_config_COM = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.INS_COM_protocol_config_COM.setFont(font)
        self.INS_COM_protocol_config_COM.setObjectName("INS_COM_protocol_config_COM")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.INS_COM_protocol_config_COM)
        self.INS_COM_protocol_config_COM_text = QtWidgets.QComboBox(self.formLayoutWidget)
        self.INS_COM_protocol_config_COM_text.setObjectName("INS_COM_protocol_config_COM_text")
        self.INS_COM_protocol_config_COM_text.addItem("")
        self.INS_COM_protocol_config_COM_text.addItem("")
        self.INS_COM_protocol_config_COM_text.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.INS_COM_protocol_config_COM_text)
        self.INS_COM_protocol_config_baudrate = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.INS_COM_protocol_config_baudrate.setFont(font)
        self.INS_COM_protocol_config_baudrate.setObjectName("INS_COM_protocol_config_baudrate")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.INS_COM_protocol_config_baudrate)
        self.INS_COM_protocol_config_baudrate_text = QtWidgets.QComboBox(self.formLayoutWidget)
        self.INS_COM_protocol_config_baudrate_text.setIconSize(QtCore.QSize(10, 16))
        self.INS_COM_protocol_config_baudrate_text.setObjectName("INS_COM_protocol_config_baudrate_text")
        self.INS_COM_protocol_config_baudrate_text.addItem("")
        self.INS_COM_protocol_config_baudrate_text.addItem("")
        self.INS_COM_protocol_config_baudrate_text.addItem("")
        self.INS_COM_protocol_config_baudrate_text.addItem("")
        self.INS_COM_protocol_config_baudrate_text.addItem("")
        self.INS_COM_protocol_config_baudrate_text.addItem("")
        self.INS_COM_protocol_config_baudrate_text.addItem("")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.INS_COM_protocol_config_baudrate_text)
        self.INS_COM_protocol_config_parity = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.INS_COM_protocol_config_parity.setFont(font)
        self.INS_COM_protocol_config_parity.setObjectName("INS_COM_protocol_config_parity")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.INS_COM_protocol_config_parity)
        self.INS_COM_protocol_config_stopbit = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.INS_COM_protocol_config_stopbit.setFont(font)
        self.INS_COM_protocol_config_stopbit.setObjectName("INS_COM_protocol_config_stopbit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.INS_COM_protocol_config_stopbit)
        self.INS_COM_protocol_config_mode = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.INS_COM_protocol_config_mode.setFont(font)
        self.INS_COM_protocol_config_mode.setObjectName("INS_COM_protocol_config_mode")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.INS_COM_protocol_config_mode)
        self.INS_COM_protocol_config_type = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.INS_COM_protocol_config_type.setFont(font)
        self.INS_COM_protocol_config_type.setObjectName("INS_COM_protocol_config_type")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.INS_COM_protocol_config_type)
        self.INS_COM_protocol_config_parity_text = QtWidgets.QComboBox(self.formLayoutWidget)
        self.INS_COM_protocol_config_parity_text.setObjectName("INS_COM_protocol_config_parity_text")
        self.INS_COM_protocol_config_parity_text.addItem("")
        self.INS_COM_protocol_config_parity_text.addItem("")
        self.INS_COM_protocol_config_parity_text.addItem("")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.INS_COM_protocol_config_parity_text)
        self.INS_COM_protocol_config_stopbit_text = QtWidgets.QComboBox(self.formLayoutWidget)
        self.INS_COM_protocol_config_stopbit_text.setObjectName("INS_COM_protocol_config_stopbit_text")
        self.INS_COM_protocol_config_stopbit_text.addItem("")
        self.INS_COM_protocol_config_stopbit_text.addItem("")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.INS_COM_protocol_config_stopbit_text)
        self.INS_COM_protocol_config_mode_text = QtWidgets.QComboBox(self.formLayoutWidget)
        self.INS_COM_protocol_config_mode_text.setObjectName("INS_COM_protocol_config_mode_text")
        self.INS_COM_protocol_config_mode_text.addItem("")
        self.INS_COM_protocol_config_mode_text.addItem("")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.INS_COM_protocol_config_mode_text)
        self.INS_COM_protocol_config_type_text = QtWidgets.QComboBox(self.formLayoutWidget)
        self.INS_COM_protocol_config_type_text.setObjectName("INS_COM_protocol_config_type_text")
        self.INS_COM_protocol_config_type_text.addItem("")
        self.INS_COM_protocol_config_type_text.addItem("")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.INS_COM_protocol_config_type_text)
        self.INS_COM_protocol_config_confirm = QtWidgets.QPushButton(self.tab)
        self.INS_COM_protocol_config_confirm.setGeometry(QtCore.QRect(90, 230, 131, 26))
        self.INS_COM_protocol_config_confirm.setObjectName("INS_COM_protocol_config_confirm")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 291, 117))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_7 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_7.setContentsMargins(0, 0, 0, 0)
        self.formLayout_7.setHorizontalSpacing(6)
        self.formLayout_7.setVerticalSpacing(8)
        self.formLayout_7.setObjectName("formLayout_7")
        self.INS_COM_output_config_COM = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.INS_COM_output_config_COM.setFont(font)
        self.INS_COM_output_config_COM.setObjectName("INS_COM_output_config_COM")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.INS_COM_output_config_COM)
        self.INS_COM_output_config_COM_text = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.INS_COM_output_config_COM_text.setObjectName("INS_COM_output_config_COM_text")
        self.INS_COM_output_config_COM_text.addItem("")
        self.INS_COM_output_config_COM_text.addItem("")
        self.INS_COM_output_config_COM_text.addItem("")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.INS_COM_output_config_COM_text)
        self.INS_COM_output_config_type = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.INS_COM_output_config_type.setFont(font)
        self.INS_COM_output_config_type.setObjectName("INS_COM_output_config_type")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.INS_COM_output_config_type)
        self.INS_COM_output_config_type_text = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.INS_COM_output_config_type_text.setObjectName("INS_COM_output_config_type_text")
        self.INS_COM_output_config_type_text.addItem("")
        self.INS_COM_output_config_type_text.addItem("")
        self.INS_COM_output_config_type_text.addItem("")
        self.INS_COM_output_config_type_text.addItem("")
        self.INS_COM_output_config_type_text.addItem("")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.INS_COM_output_config_type_text)
        self.INS_COM_output_config_rate = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.INS_COM_output_config_rate.setFont(font)
        self.INS_COM_output_config_rate.setObjectName("INS_COM_output_config_rate")
        self.formLayout_7.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.INS_COM_output_config_rate)
        self.INS_COM_output_config_rate_text = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.INS_COM_output_config_rate_text.setObjectName("INS_COM_output_config_rate_text")
        self.INS_COM_output_config_rate_text.addItem("")
        self.INS_COM_output_config_rate_text.addItem("")
        self.INS_COM_output_config_rate_text.addItem("")
        self.INS_COM_output_config_rate_text.addItem("")
        self.INS_COM_output_config_rate_text.addItem("")
        self.INS_COM_output_config_rate_text.addItem("")
        self.INS_COM_output_config_rate_text.addItem("")
        self.formLayout_7.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.INS_COM_output_config_rate_text)
        self.INS_COM_output_config_confirm = QtWidgets.QPushButton(self.tab_2)
        self.INS_COM_output_config_confirm.setGeometry(QtCore.QRect(90, 230, 131, 26))
        self.INS_COM_output_config_confirm.setObjectName("INS_COM_output_config_confirm")
        self.INS_COM_output_config_clear = QtWidgets.QPushButton(self.tab_2)
        self.INS_COM_output_config_clear.setGeometry(QtCore.QRect(90, 160, 131, 26))
        self.INS_COM_output_config_clear.setObjectName("INS_COM_output_config_clear")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 291, 117))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_9 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_9.setContentsMargins(0, 0, 0, 0)
        self.formLayout_9.setHorizontalSpacing(6)
        self.formLayout_9.setVerticalSpacing(8)
        self.formLayout_9.setObjectName("formLayout_9")
        self.INS_COM_through_config_COM = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.INS_COM_through_config_COM.setFont(font)
        self.INS_COM_through_config_COM.setObjectName("INS_COM_through_config_COM")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.INS_COM_through_config_COM)
        self.INS_COM_through_config_COM_text = QtWidgets.QComboBox(self.formLayoutWidget_3)
        self.INS_COM_through_config_COM_text.setObjectName("INS_COM_through_config_COM_text")
        self.INS_COM_through_config_COM_text.addItem("")
        self.INS_COM_through_config_COM_text.addItem("")
        self.INS_COM_through_config_COM_text.addItem("")
        self.INS_COM_through_config_COM_text.addItem("")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.INS_COM_through_config_COM_text)
        self.INS_COM_through_config_type = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.INS_COM_through_config_type.setFont(font)
        self.INS_COM_through_config_type.setObjectName("INS_COM_through_config_type")
        self.formLayout_9.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.INS_COM_through_config_type)
        self.INS_COM_through_config_type_text = QtWidgets.QComboBox(self.formLayoutWidget_3)
        self.INS_COM_through_config_type_text.setObjectName("INS_COM_through_config_type_text")
        self.INS_COM_through_config_type_text.addItem("")
        self.INS_COM_through_config_type_text.addItem("")
        self.formLayout_9.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.INS_COM_through_config_type_text)
        self.INS_COM_through_config_rate = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.INS_COM_through_config_rate.setFont(font)
        self.INS_COM_through_config_rate.setObjectName("INS_COM_through_config_rate")
        self.formLayout_9.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.INS_COM_through_config_rate)
        self.INS_COM_through_config_rate_text = QtWidgets.QComboBox(self.formLayoutWidget_3)
        self.INS_COM_through_config_rate_text.setObjectName("INS_COM_through_config_rate_text")
        self.INS_COM_through_config_rate_text.addItem("")
        self.INS_COM_through_config_rate_text.addItem("")
        self.INS_COM_through_config_rate_text.addItem("")
        self.INS_COM_through_config_rate_text.addItem("")
        self.formLayout_9.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.INS_COM_through_config_rate_text)
        self.INS_COM_through_config_confirm = QtWidgets.QPushButton(self.tab_3)
        self.INS_COM_through_config_confirm.setGeometry(QtCore.QRect(90, 230, 131, 26))
        self.INS_COM_through_config_confirm.setObjectName("INS_COM_through_config_confirm")
        self.tabWidget.addTab(self.tab_3, "")
        self.INS_port_select_baudrate = QtWidgets.QLabel(self.centralwidget)
        self.INS_port_select_baudrate.setGeometry(QtCore.QRect(320, 70, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.INS_port_select_baudrate.setFont(font)
        self.INS_port_select_baudrate.setObjectName("INS_port_select_baudrate")
        self.INS_port_select_baudrate_ = QtWidgets.QComboBox(self.centralwidget)
        self.INS_port_select_baudrate_.setGeometry(QtCore.QRect(370, 70, 131, 20))
        self.INS_port_select_baudrate_.setObjectName("INS_port_select_baudrate_")
        self.INS_port_select_baudrate_.addItem("")
        self.INS_port_select_baudrate_.addItem("")
        self.INS_port_select_baudrate_.addItem("")
        self.INS_port_select_baudrate_.addItem("")
        self.INS_port_select_baudrate_.addItem("")
        self.INS_port_select_baudrate_.addItem("")
        self.INS_port_select_baudrate_.addItem("")
        self.INS_port_select_parity = QtWidgets.QLabel(self.centralwidget)
        self.INS_port_select_parity.setGeometry(QtCore.QRect(520, 70, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.INS_port_select_parity.setFont(font)
        self.INS_port_select_parity.setObjectName("INS_port_select_parity")
        self.INS_port_select_parity_ = QtWidgets.QComboBox(self.centralwidget)
        self.INS_port_select_parity_.setGeometry(QtCore.QRect(580, 70, 91, 20))
        self.INS_port_select_parity_.setObjectName("INS_port_select_parity_")
        self.INS_port_select_parity_.addItem("")
        self.INS_port_select_parity_.addItem("")
        self.INS_port_select_parity_.addItem("")
        self.INS_port_select_stopbit = QtWidgets.QLabel(self.centralwidget)
        self.INS_port_select_stopbit.setGeometry(QtCore.QRect(690, 70, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.INS_port_select_stopbit.setFont(font)
        self.INS_port_select_stopbit.setObjectName("INS_port_select_stopbit")
        self.INS_port_select_stopbit_ = QtWidgets.QComboBox(self.centralwidget)
        self.INS_port_select_stopbit_.setGeometry(QtCore.QRect(750, 70, 91, 20))
        self.INS_port_select_stopbit_.setObjectName("INS_port_select_stopbit_")
        self.INS_port_select_stopbit_.addItem("")
        self.INS_port_select_stopbit_.addItem("")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 100, 951, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "惯性组合导航配置"))
        self.INS_inquiry.setText(_translate("MainWindow", "查询:"))
        self.INS_cmd_send_message_send.setText(_translate("MainWindow", "发送"))
        self.INS_signal_source_QX.setToolTip(_translate("MainWindow", "差分信号来源于千寻"))
        self.INS_signal_source_QX.setText(_translate("MainWindow", "千寻"))
        self.INS_save_config.setText(_translate("MainWindow", "保存配置"))
        self.INS_signal_source_radio_station.setToolTip(_translate("MainWindow", "差分信号来源于基站"))
        self.INS_signal_source_radio_station.setText(_translate("MainWindow", "基站"))
        self.INS_GPS_data.setText(_translate("MainWindow", "GPS信息:"))
        self.INS_inquiry_navigation_status.setToolTip(_translate("MainWindow", "查看当前导航状态"))
        self.INS_inquiry_navigation_status.setText(_translate("MainWindow", "导航状态"))
        self.INS_inquiry_odometer_status.setToolTip(_translate("MainWindow", "查看里程计模式"))
        self.INS_inquiry_odometer_status.setText(_translate("MainWindow", "里程计状态"))
        self.INS_cmd_send_message_clear.setText(_translate("MainWindow", "清除"))
        self.INS_cmd_send.setText(_translate("MainWindow", "配置命令发送:"))
        self.INS_inquiry_COM_output.setToolTip(_translate("MainWindow", "查看各个COM口输出数据"))
        self.INS_inquiry_COM_output.setText(_translate("MainWindow", "COM输出"))
        self.INS_information_receive.setText(_translate("MainWindow", "消息接收:"))
        self.INS_inquiry_GNSS.setToolTip(_translate("MainWindow", "查询GNSS配置"))
        self.INS_inquiry_GNSS.setText(_translate("MainWindow", "GNSS杆臂"))
        self.INS_inquiry_COM_configure.setToolTip(_translate("MainWindow", "查看各个COM配置"))
        self.INS_inquiry_COM_configure.setText(_translate("MainWindow", "COM配置"))
        self.INS_information_receive_message_clear.setText(_translate("MainWindow", "清除"))
        self.INS_GPS_data_text.setText(_translate("MainWindow", "0"))
        self.INS_signal_source.setText(_translate("MainWindow", "配置:"))
        self.INS_port_select.setText(_translate("MainWindow", "串口选择:"))
        self.INS_COM_protocol_config_COM.setText(_translate("MainWindow", "COM口:"))
        self.INS_COM_protocol_config_COM_text.setItemText(0, _translate("MainWindow", "com0"))
        self.INS_COM_protocol_config_COM_text.setItemText(1, _translate("MainWindow", "com1"))
        self.INS_COM_protocol_config_COM_text.setItemText(2, _translate("MainWindow", "com2"))
        self.INS_COM_protocol_config_baudrate.setText(_translate("MainWindow", "波特率:"))
        self.INS_COM_protocol_config_baudrate_text.setItemText(0, _translate("MainWindow", "9600"))
        self.INS_COM_protocol_config_baudrate_text.setItemText(1, _translate("MainWindow", "19200"))
        self.INS_COM_protocol_config_baudrate_text.setItemText(2, _translate("MainWindow", "38400"))
        self.INS_COM_protocol_config_baudrate_text.setItemText(3, _translate("MainWindow", "57600"))
        self.INS_COM_protocol_config_baudrate_text.setItemText(4, _translate("MainWindow", "115200"))
        self.INS_COM_protocol_config_baudrate_text.setItemText(5, _translate("MainWindow", "230400"))
        self.INS_COM_protocol_config_baudrate_text.setItemText(6, _translate("MainWindow", "460800"))
        self.INS_COM_protocol_config_parity.setText(_translate("MainWindow", "校验位:"))
        self.INS_COM_protocol_config_stopbit.setText(_translate("MainWindow", "停止位:"))
        self.INS_COM_protocol_config_mode.setText(_translate("MainWindow", "模  式:"))
        self.INS_COM_protocol_config_type.setText(_translate("MainWindow", "类  型:"))
        self.INS_COM_protocol_config_parity_text.setItemText(0, _translate("MainWindow", "odd"))
        self.INS_COM_protocol_config_parity_text.setItemText(1, _translate("MainWindow", "even"))
        self.INS_COM_protocol_config_parity_text.setItemText(2, _translate("MainWindow", "none"))
        self.INS_COM_protocol_config_stopbit_text.setItemText(0, _translate("MainWindow", "1"))
        self.INS_COM_protocol_config_stopbit_text.setItemText(1, _translate("MainWindow", "2"))
        self.INS_COM_protocol_config_mode_text.setItemText(0, _translate("MainWindow", "RS232"))
        self.INS_COM_protocol_config_mode_text.setItemText(1, _translate("MainWindow", "RS422"))
        self.INS_COM_protocol_config_type_text.setItemText(0, _translate("MainWindow", "log"))
        self.INS_COM_protocol_config_type_text.setItemText(1, _translate("MainWindow", "rtk"))
        self.INS_COM_protocol_config_confirm.setText(_translate("MainWindow", "配置"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "COM口协议配置"))
        self.INS_COM_output_config_COM.setText(_translate("MainWindow", "COM口:"))
        self.INS_COM_output_config_COM_text.setItemText(0, _translate("MainWindow", "com0"))
        self.INS_COM_output_config_COM_text.setItemText(1, _translate("MainWindow", "com1"))
        self.INS_COM_output_config_COM_text.setItemText(2, _translate("MainWindow", "com2"))
        self.INS_COM_output_config_type.setText(_translate("MainWindow", "类  型:"))
        self.INS_COM_output_config_type_text.setItemText(0, _translate("MainWindow", "gpfpd"))
        self.INS_COM_output_config_type_text.setItemText(1, _translate("MainWindow", "gprmc"))
        self.INS_COM_output_config_type_text.setItemText(2, _translate("MainWindow", "rawimu"))
        self.INS_COM_output_config_type_text.setItemText(3, _translate("MainWindow", "gtimu"))
        self.INS_COM_output_config_type_text.setItemText(4, _translate("MainWindow", "mark1pva"))
        self.INS_COM_output_config_rate.setText(_translate("MainWindow", "频  率:"))
        self.INS_COM_output_config_rate_text.setItemText(0, _translate("MainWindow", "100Hz"))
        self.INS_COM_output_config_rate_text.setItemText(1, _translate("MainWindow", "20Hz"))
        self.INS_COM_output_config_rate_text.setItemText(2, _translate("MainWindow", "10Hz"))
        self.INS_COM_output_config_rate_text.setItemText(3, _translate("MainWindow", "5Hz"))
        self.INS_COM_output_config_rate_text.setItemText(4, _translate("MainWindow", "2Hz"))
        self.INS_COM_output_config_rate_text.setItemText(5, _translate("MainWindow", "1Hz"))
        self.INS_COM_output_config_rate_text.setItemText(6, _translate("MainWindow", "null"))
        self.INS_COM_output_config_confirm.setText(_translate("MainWindow", "配置"))
        self.INS_COM_output_config_clear.setText(_translate("MainWindow", "清除COM口输出"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "COM口输出配置"))
        self.INS_COM_through_config_COM.setText(_translate("MainWindow", "COM口:"))
        self.INS_COM_through_config_COM_text.setItemText(0, _translate("MainWindow", "com0"))
        self.INS_COM_through_config_COM_text.setItemText(1, _translate("MainWindow", "com1"))
        self.INS_COM_through_config_COM_text.setItemText(2, _translate("MainWindow", "com2"))
        self.INS_COM_through_config_COM_text.setItemText(3, _translate("MainWindow", "com3"))
        self.INS_COM_through_config_type.setText(_translate("MainWindow", "类  型:"))
        self.INS_COM_through_config_type_text.setItemText(0, _translate("MainWindow", "rangecmpd"))
        self.INS_COM_through_config_type_text.setItemText(1, _translate("MainWindow", "rawephemb"))
        self.INS_COM_through_config_rate.setText(_translate("MainWindow", "频  率:"))
        self.INS_COM_through_config_rate_text.setItemText(0, _translate("MainWindow", "5Hz"))
        self.INS_COM_through_config_rate_text.setItemText(1, _translate("MainWindow", "1Hz"))
        self.INS_COM_through_config_rate_text.setItemText(2, _translate("MainWindow", "new"))
        self.INS_COM_through_config_rate_text.setItemText(3, _translate("MainWindow", "null"))
        self.INS_COM_through_config_confirm.setText(_translate("MainWindow", "配置"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "COM口透传配置"))
        self.INS_port_select_baudrate.setText(_translate("MainWindow", "波特率:"))
        self.INS_port_select_baudrate_.setCurrentText(_translate("MainWindow", "115200"))
        self.INS_port_select_baudrate_.setItemText(0, _translate("MainWindow", "9600"))
        self.INS_port_select_baudrate_.setItemText(1, _translate("MainWindow", "19200"))
        self.INS_port_select_baudrate_.setItemText(2, _translate("MainWindow", "38400"))
        self.INS_port_select_baudrate_.setItemText(3, _translate("MainWindow", "57600"))
        self.INS_port_select_baudrate_.setItemText(4, _translate("MainWindow", "115200"))
        self.INS_port_select_baudrate_.setItemText(5, _translate("MainWindow", "230400"))
        self.INS_port_select_baudrate_.setItemText(6, _translate("MainWindow", "460800"))
        self.INS_port_select_parity.setText(_translate("MainWindow", "校验位:"))
        self.INS_port_select_parity_.setItemText(0, _translate("MainWindow", "none"))
        self.INS_port_select_parity_.setItemText(1, _translate("MainWindow", "odd"))
        self.INS_port_select_parity_.setItemText(2, _translate("MainWindow", "even"))
        self.INS_port_select_stopbit.setText(_translate("MainWindow", "停止位:"))
        self.INS_port_select_stopbit_.setItemText(0, _translate("MainWindow", "1"))
        self.INS_port_select_stopbit_.setItemText(1, _translate("MainWindow", "2"))
