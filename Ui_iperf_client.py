# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\git\iperf_gui\iperf_client.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(590, 729)
        MainWindow.setMinimumSize(QtCore.QSize(590, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem)
        self.pushButton_a = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_a.setFont(font)
        self.pushButton_a.setObjectName("pushButton_a")
        self.horizontalLayout_14.addWidget(self.pushButton_a)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem1)
        self.pushButton_s = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_s.setFont(font)
        self.pushButton_s.setObjectName("pushButton_s")
        self.horizontalLayout_14.addWidget(self.pushButton_s)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_iperf3 = QtWidgets.QWidget(self.groupBox_4)
        self.widget_iperf3.setObjectName("widget_iperf3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_iperf3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.label_32 = QtWidgets.QLabel(self.widget_iperf3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_33.addWidget(self.label_32)
        self.label_res_rx = QtWidgets.QLabel(self.widget_iperf3)
        self.label_res_rx.setMinimumSize(QtCore.QSize(105, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_res_rx.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_res_rx.setFont(font)
        self.label_res_rx.setText("")
        self.label_res_rx.setObjectName("label_res_rx")
        self.horizontalLayout_33.addWidget(self.label_res_rx)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_33)
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.label_34 = QtWidgets.QLabel(self.widget_iperf3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_34.addWidget(self.label_34)
        self.label_res_tx = QtWidgets.QLabel(self.widget_iperf3)
        self.label_res_tx.setMinimumSize(QtCore.QSize(105, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_res_tx.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_res_tx.setFont(font)
        self.label_res_tx.setText("")
        self.label_res_tx.setObjectName("label_res_tx")
        self.horizontalLayout_34.addWidget(self.label_res_tx)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_34)
        self.gridLayout_5.addLayout(self.horizontalLayout_15, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem3, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.widget_iperf3)
        self.widget_iperf2 = QtWidgets.QWidget(self.groupBox_4)
        self.widget_iperf2.setObjectName("widget_iperf2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.widget_iperf2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem4, 0, 1, 1, 1)
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.label_31 = QtWidgets.QLabel(self.widget_iperf2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_32.addWidget(self.label_31)
        self.label_res_th = QtWidgets.QLabel(self.widget_iperf2)
        self.label_res_th.setMinimumSize(QtCore.QSize(105, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_res_th.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_res_th.setFont(font)
        self.label_res_th.setText("")
        self.label_res_th.setObjectName("label_res_th")
        self.horizontalLayout_32.addWidget(self.label_res_th)
        self.gridLayout_9.addLayout(self.horizontalLayout_32, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget_iperf2)
        self.horizontalLayout_31.addLayout(self.verticalLayout)
        self.label_countDown = QtWidgets.QLabel(self.groupBox_4)
        self.label_countDown.setMaximumSize(QtCore.QSize(100, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_countDown.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_countDown.setFont(font)
        self.label_countDown.setAlignment(QtCore.Qt.AlignCenter)
        self.label_countDown.setObjectName("label_countDown")
        self.horizontalLayout_31.addWidget(self.label_countDown)
        self.gridLayout_10.addLayout(self.horizontalLayout_31, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.label_error = QtWidgets.QLabel(self.tab)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_error.setPalette(palette)
        self.label_error.setText("")
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setObjectName("label_error")
        self.verticalLayout_2.addWidget(self.label_error)
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.gridLayout_6.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_24 = QtWidgets.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_24.addWidget(self.label_24)
        self.lineEdit_task = QtWidgets.QLineEdit(self.tab_5)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_task.setFont(font)
        self.lineEdit_task.setObjectName("lineEdit_task")
        self.horizontalLayout_24.addWidget(self.lineEdit_task)
        self.checkBox_lock = QtWidgets.QCheckBox(self.tab_5)
        self.checkBox_lock.setObjectName("checkBox_lock")
        self.horizontalLayout_24.addWidget(self.checkBox_lock)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_24)
        self.groupBox_test = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_test.setObjectName("groupBox_test")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_test)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.checkBox_cc = QtWidgets.QCheckBox(self.groupBox_test)
        self.checkBox_cc.setText("")
        self.checkBox_cc.setObjectName("checkBox_cc")
        self.horizontalLayout_9.addWidget(self.checkBox_cc)
        self.label_7 = QtWidgets.QLabel(self.groupBox_test)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.spinBox_cCount = QtWidgets.QSpinBox(self.groupBox_test)
        self.spinBox_cCount.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_cCount.setFont(font)
        self.spinBox_cCount.setMinimum(0)
        self.spinBox_cCount.setMaximum(9999)
        self.spinBox_cCount.setObjectName("spinBox_cCount")
        self.horizontalLayout_9.addWidget(self.spinBox_cCount)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_9)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem6)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_test)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_10.addWidget(self.label_11)
        self.spinBox_cInterval = QtWidgets.QSpinBox(self.groupBox_test)
        self.spinBox_cInterval.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_cInterval.setFont(font)
        self.spinBox_cInterval.setObjectName("spinBox_cInterval")
        self.horizontalLayout_10.addWidget(self.spinBox_cInterval)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_10)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem7)
        self.gridLayout_4.addLayout(self.horizontalLayout_13, 1, 0, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.checkBox_save = QtWidgets.QCheckBox(self.groupBox_test)
        self.checkBox_save.setText("")
        self.checkBox_save.setObjectName("checkBox_save")
        self.horizontalLayout_11.addWidget(self.checkBox_save)
        self.label_12 = QtWidgets.QLabel(self.groupBox_test)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_11.addWidget(self.label_12)
        self.label_path = QtWidgets.QLabel(self.groupBox_test)
        self.label_path.setMinimumSize(QtCore.QSize(100, 0))
        self.label_path.setText("")
        self.label_path.setObjectName("label_path")
        self.horizontalLayout_11.addWidget(self.label_path)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem8)
        self.pushButton_save = QtWidgets.QPushButton(self.groupBox_test)
        self.pushButton_save.setEnabled(False)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout_11.addWidget(self.pushButton_save)
        self.gridLayout_4.addLayout(self.horizontalLayout_11, 2, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.groupBox_test)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.checkBox_script = QtWidgets.QCheckBox(self.tab_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_script.setFont(font)
        self.checkBox_script.setObjectName("checkBox_script")
        self.horizontalLayout_19.addWidget(self.checkBox_script)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem9)
        self.pushButton_refresh = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.horizontalLayout_19.addWidget(self.pushButton_refresh)
        self.verticalLayout_8.addLayout(self.horizontalLayout_19)
        self.verticalLayout_5.addLayout(self.verticalLayout_8)
        self.scrollArea = QtWidgets.QScrollArea(self.tab_5)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 105))
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 105))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 633, 117))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_script_add = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_script_add.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_script_add.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_script_add.setObjectName("pushButton_script_add")
        self.verticalLayout_7.addWidget(self.pushButton_script_add)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem10)
        self.label_index = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_index.setAlignment(QtCore.Qt.AlignCenter)
        self.label_index.setObjectName("label_index")
        self.verticalLayout_7.addWidget(self.label_index)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem11)
        self.horizontalLayout_20.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_12.addWidget(self.label_16)
        self.comboBox_script_pro = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_script_pro.setMinimumSize(QtCore.QSize(80, 0))
        self.comboBox_script_pro.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_script_pro.setFont(font)
        self.comboBox_script_pro.setObjectName("comboBox_script_pro")
        self.comboBox_script_pro.addItem("")
        self.comboBox_script_pro.addItem("")
        self.comboBox_script_pro.addItem("")
        self.horizontalLayout_12.addWidget(self.comboBox_script_pro)
        self.label_pro_ip = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_pro_ip.setFont(font)
        self.label_pro_ip.setObjectName("label_pro_ip")
        self.horizontalLayout_12.addWidget(self.label_pro_ip)
        self.lineEdit_script_ip = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_script_ip.setMinimumSize(QtCore.QSize(135, 0))
        self.lineEdit_script_ip.setMaximumSize(QtCore.QSize(135, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_script_ip.setFont(font)
        self.lineEdit_script_ip.setText("")
        self.lineEdit_script_ip.setObjectName("lineEdit_script_ip")
        self.horizontalLayout_12.addWidget(self.lineEdit_script_ip)
        self.comboBox_serial = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_serial.setMinimumSize(QtCore.QSize(90, 0))
        self.comboBox_serial.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_serial.setFont(font)
        self.comboBox_serial.setObjectName("comboBox_serial")
        self.horizontalLayout_12.addWidget(self.comboBox_serial)
        self.pushButton_script_more = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_script_more.setMinimumSize(QtCore.QSize(25, 0))
        self.pushButton_script_more.setMaximumSize(QtCore.QSize(25, 16777215))
        self.pushButton_script_more.setObjectName("pushButton_script_more")
        self.horizontalLayout_12.addWidget(self.pushButton_script_more)
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_12.addWidget(self.label_13)
        self.comboBox_opp = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_opp.setMinimumSize(QtCore.QSize(75, 0))
        self.comboBox_opp.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_opp.setFont(font)
        self.comboBox_opp.setObjectName("comboBox_opp")
        self.comboBox_opp.addItem("")
        self.comboBox_opp.addItem("")
        self.comboBox_opp.addItem("")
        self.horizontalLayout_12.addWidget(self.comboBox_opp)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem12)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_18.addWidget(self.label_17)
        self.lineEdit_script = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_script.setObjectName("lineEdit_script")
        self.horizontalLayout_18.addWidget(self.lineEdit_script)
        self.verticalLayout_6.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_17.addWidget(self.label_18)
        self.lineEdit_re = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_re.setObjectName("lineEdit_re")
        self.horizontalLayout_17.addWidget(self.lineEdit_re)
        self.verticalLayout_6.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_20.addLayout(self.verticalLayout_6)
        self.gridLayout_12.addLayout(self.horizontalLayout_20, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_5.addWidget(self.scrollArea)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.checkBox_report = QtWidgets.QCheckBox(self.tab_5)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.checkBox_report.setFont(font)
        self.checkBox_report.setObjectName("checkBox_report")
        self.horizontalLayout_21.addWidget(self.checkBox_report)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem13)
        self.verticalLayout_5.addLayout(self.horizontalLayout_21)
        self.groupBox_report = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_report.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.groupBox_report.setFont(font)
        self.groupBox_report.setTitle("")
        self.groupBox_report.setObjectName("groupBox_report")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.groupBox_report)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_19 = QtWidgets.QLabel(self.groupBox_report)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_22.addWidget(self.label_19)
        self.comboBox_report_proto = QtWidgets.QComboBox(self.groupBox_report)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.comboBox_report_proto.setFont(font)
        self.comboBox_report_proto.setObjectName("comboBox_report_proto")
        self.comboBox_report_proto.addItem("")
        self.horizontalLayout_22.addWidget(self.comboBox_report_proto)
        self.label_21 = QtWidgets.QLabel(self.groupBox_report)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_22.addWidget(self.label_21)
        self.comboBox_report_method = QtWidgets.QComboBox(self.groupBox_report)
        self.comboBox_report_method.setObjectName("comboBox_report_method")
        self.comboBox_report_method.addItem("")
        self.comboBox_report_method.addItem("")
        self.comboBox_report_method.addItem("")
        self.horizontalLayout_22.addWidget(self.comboBox_report_method)
        self.label_23 = QtWidgets.QLabel(self.groupBox_report)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_22.addWidget(self.label_23)
        self.comboBox_report_formart = QtWidgets.QComboBox(self.groupBox_report)
        self.comboBox_report_formart.setObjectName("comboBox_report_formart")
        self.comboBox_report_formart.addItem("")
        self.comboBox_report_formart.addItem("")
        self.comboBox_report_formart.addItem("")
        self.horizontalLayout_22.addWidget(self.comboBox_report_formart)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem14)
        self.verticalLayout_9.addLayout(self.horizontalLayout_22)
        self.gridLayout_17.addLayout(self.verticalLayout_9, 0, 0, 1, 1)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_22 = QtWidgets.QLabel(self.groupBox_report)
        self.label_22.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_23.addWidget(self.label_22)
        self.lineEdit_report_ip = QtWidgets.QLineEdit(self.groupBox_report)
        self.lineEdit_report_ip.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_report_ip.setObjectName("lineEdit_report_ip")
        self.horizontalLayout_23.addWidget(self.lineEdit_report_ip)
        self.label_20 = QtWidgets.QLabel(self.groupBox_report)
        self.label_20.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_23.addWidget(self.label_20)
        self.comboBox_report_uri = QtWidgets.QComboBox(self.groupBox_report)
        self.comboBox_report_uri.setEditable(True)
        self.comboBox_report_uri.setObjectName("comboBox_report_uri")
        self.comboBox_report_uri.addItem("")
        self.horizontalLayout_23.addWidget(self.comboBox_report_uri)
        self.gridLayout_17.addLayout(self.horizontalLayout_23, 1, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.groupBox_report)
        self.label_error_t = QtWidgets.QLabel(self.tab_5)
        self.label_error_t.setText("")
        self.label_error_t.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error_t.setObjectName("label_error_t")
        self.verticalLayout_5.addWidget(self.label_error_t)
        self.gridLayout_13.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 352, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem15, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_ver = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_ver.setMinimumSize(QtCore.QSize(40, 0))
        self.comboBox_ver.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.comboBox_ver.setFont(font)
        self.comboBox_ver.setObjectName("comboBox_ver")
        self.comboBox_ver.addItem("")
        self.comboBox_ver.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_ver)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem16)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.comboBox_pro = QtWidgets.QComboBox(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.comboBox_pro.setFont(font)
        self.comboBox_pro.setObjectName("comboBox_pro")
        self.comboBox_pro.addItem("")
        self.comboBox_pro.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_pro)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem17)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.lineEdit_c_param = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_c_param.setFont(font)
        self.lineEdit_c_param.setObjectName("lineEdit_c_param")
        self.horizontalLayout_8.addWidget(self.lineEdit_c_param)
        self.gridLayout_3.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_3.addWidget(self.label_14)
        self.lineEdit_c_ip = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_c_ip.setFont(font)
        self.lineEdit_c_ip.setObjectName("lineEdit_c_ip")
        self.horizontalLayout_3.addWidget(self.lineEdit_c_ip)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.spinBox_time = QtWidgets.QSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_time.setFont(font)
        self.spinBox_time.setMaximum(999999)
        self.spinBox_time.setObjectName("spinBox_time")
        self.horizontalLayout_3.addWidget(self.spinBox_time)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem18)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.spinBox_p = QtWidgets.QSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.spinBox_p.setFont(font)
        self.spinBox_p.setObjectName("spinBox_p")
        self.horizontalLayout_3.addWidget(self.spinBox_p)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem19)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.label_error_c = QtWidgets.QLabel(self.tab_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_error_c.setPalette(palette)
        self.label_error_c.setText("")
        self.label_error_c.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error_c.setObjectName("label_error_c")
        self.verticalLayout_4.addWidget(self.label_error_c)
        self.gridLayout_8.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem20, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_3.setMinimumSize(QtCore.QSize(40, 0))
        self.comboBox_3.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox_3)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem21)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox_4)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem22)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.groupBox = QtWidgets.QGroupBox(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_s_ip = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_s_ip.setFont(font)
        self.lineEdit_s_ip.setObjectName("lineEdit_s_ip")
        self.horizontalLayout.addWidget(self.lineEdit_s_ip)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem23)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lineEdit_s_param = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_s_param.setFont(font)
        self.lineEdit_s_param.setObjectName("lineEdit_s_param")
        self.horizontalLayout_5.addWidget(self.lineEdit_s_param)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.label_error_s = QtWidgets.QLabel(self.tab_3)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_error_s.setPalette(palette)
        self.label_error_s.setText("")
        self.label_error_s.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error_s.setObjectName("label_error_s")
        self.verticalLayout_3.addWidget(self.label_error_s)
        self.gridLayout_7.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem24, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_15 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_16.addWidget(self.label_15)
        self.label_res_path = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_res_path.setFont(font)
        self.label_res_path.setText("")
        self.label_res_path.setObjectName("label_res_path")
        self.horizontalLayout_16.addWidget(self.label_res_path)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem25)
        self.gridLayout_16.addLayout(self.horizontalLayout_16, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.tab_4)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.tableWidget_ver2 = QtWidgets.QTableWidget(self.page)
        self.tableWidget_ver2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_ver2.setObjectName("tableWidget_ver2")
        self.tableWidget_ver2.setColumnCount(7)
        self.tableWidget_ver2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ver2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ver2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ver2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ver2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ver2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ver2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ver2.setHorizontalHeaderItem(6, item)
        self.gridLayout_11.addWidget(self.tableWidget_ver2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.tableWidget_ver3 = QtWidgets.QTableWidget(self.page_2)
        self.tableWidget_ver3.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_ver3.setObjectName("tableWidget_ver3")
        self.tableWidget_ver3.setColumnCount(8)
        self.tableWidget_ver3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ver3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ver3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ver3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ver3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ver3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ver3.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ver3.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ver3.setHorizontalHeaderItem(7, item)
        self.gridLayout_15.addWidget(self.tableWidget_ver3, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout_16.addWidget(self.stackedWidget, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.textBrowser_v2 = QtWidgets.QTextBrowser(self.tab_6)
        self.textBrowser_v2.setObjectName("textBrowser_v2")
        self.gridLayout_14.addWidget(self.textBrowser_v2, 0, 0, 1, 1)
        self.textBrowser_v3 = QtWidgets.QTextBrowser(self.tab_6)
        self.textBrowser_v3.setObjectName("textBrowser_v3")
        self.gridLayout_14.addWidget(self.textBrowser_v3, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_6, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(5)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Iperf Client"))
        self.pushButton_a.setText(_translate("MainWindow", "START"))
        self.pushButton_s.setText(_translate("MainWindow", "STOP"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Test Result"))
        self.label_32.setText(_translate("MainWindow", "Rx:"))
        self.label_34.setText(_translate("MainWindow", "Tx:"))
        self.label_31.setText(_translate("MainWindow", "Throughput:"))
        self.label_countDown.setText(_translate("MainWindow", "360000"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Testing"))
        self.label_24.setText(_translate("MainWindow", "任务："))
        self.lineEdit_task.setText(_translate("MainWindow", "TestTask"))
        self.checkBox_lock.setText(_translate("MainWindow", "锁定"))
        self.groupBox_test.setTitle(_translate("MainWindow", "Test Setting"))
        self.label_7.setText(_translate("MainWindow", "循环次数:"))
        self.label_11.setText(_translate("MainWindow", "循环间隔/s："))
        self.label_12.setText(_translate("MainWindow", "数据自动保存路径："))
        self.pushButton_save.setText(_translate("MainWindow", "浏览"))
        self.checkBox_script.setText(_translate("MainWindow", "Script"))
        self.pushButton_refresh.setText(_translate("MainWindow", "Rfresh"))
        self.pushButton_script_add.setText(_translate("MainWindow", "+"))
        self.label_index.setText(_translate("MainWindow", "0"))
        self.label_16.setText(_translate("MainWindow", "Protocol:"))
        self.comboBox_script_pro.setItemText(0, _translate("MainWindow", "SSH2"))
        self.comboBox_script_pro.setItemText(1, _translate("MainWindow", "TELNET"))
        self.comboBox_script_pro.setItemText(2, _translate("MainWindow", "SERIAL"))
        self.label_pro_ip.setText(_translate("MainWindow", "IP:"))
        self.pushButton_script_more.setText(_translate("MainWindow", "..."))
        self.label_13.setText(_translate("MainWindow", "运行:"))
        self.comboBox_opp.setItemText(0, _translate("MainWindow", "测试后"))
        self.comboBox_opp.setItemText(1, _translate("MainWindow", "测试中"))
        self.comboBox_opp.setItemText(2, _translate("MainWindow", "测试前"))
        self.label_17.setText(_translate("MainWindow", "运行脚本:"))
        self.label_18.setText(_translate("MainWindow", "结果匹配:"))
        self.checkBox_report.setText(_translate("MainWindow", "Report"))
        self.label_19.setText(_translate("MainWindow", "接口协议："))
        self.comboBox_report_proto.setItemText(0, _translate("MainWindow", "HTTP"))
        self.label_21.setText(_translate("MainWindow", "请求方法："))
        self.comboBox_report_method.setItemText(0, _translate("MainWindow", "POST"))
        self.comboBox_report_method.setItemText(1, _translate("MainWindow", "GET"))
        self.comboBox_report_method.setItemText(2, _translate("MainWindow", "PUT"))
        self.label_23.setText(_translate("MainWindow", "数据格式："))
        self.comboBox_report_formart.setItemText(0, _translate("MainWindow", "JSON"))
        self.comboBox_report_formart.setItemText(1, _translate("MainWindow", "TXT"))
        self.comboBox_report_formart.setItemText(2, _translate("MainWindow", "RAW"))
        self.label_22.setText(_translate("MainWindow", "IP：PORT"))
        self.lineEdit_report_ip.setText(_translate("MainWindow", "10.110.30.86:8080"))
        self.label_20.setText(_translate("MainWindow", "URI："))
        self.comboBox_report_uri.setItemText(0, _translate("MainWindow", "/test/iperf/"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Test Setting"))
        self.label_2.setText(_translate("MainWindow", "iperf version:"))
        self.comboBox_ver.setItemText(0, _translate("MainWindow", "2"))
        self.comboBox_ver.setItemText(1, _translate("MainWindow", "3"))
        self.label_9.setText(_translate("MainWindow", "测试协议:"))
        self.comboBox_pro.setItemText(0, _translate("MainWindow", "TCP"))
        self.comboBox_pro.setItemText(1, _translate("MainWindow", "UDP"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Client端设置"))
        self.label_8.setText(_translate("MainWindow", "参数:"))
        self.lineEdit_c_param.setText(_translate("MainWindow", "-l 1024 -i 1"))
        self.label_14.setText(_translate("MainWindow", "IP:"))
        self.lineEdit_c_ip.setText(_translate("MainWindow", "192.168.10.210"))
        self.label_3.setText(_translate("MainWindow", "Time:"))
        self.label_4.setText(_translate("MainWindow", "线程数:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Client Setting"))
        self.label_6.setText(_translate("MainWindow", "iperf version:"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "2"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "3"))
        self.label_10.setText(_translate("MainWindow", "测试协议:"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "TCP"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "UDP"))
        self.groupBox.setTitle(_translate("MainWindow", "Server端设置"))
        self.label.setText(_translate("MainWindow", "Server 端 IP："))
        self.lineEdit_s_ip.setText(_translate("MainWindow", "255.255.255.255"))
        self.label_5.setText(_translate("MainWindow", "参数:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Server Setting"))
        self.label_15.setText(_translate("MainWindow", "Excel:"))
        item = self.tableWidget_ver2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Protocol"))
        item = self.tableWidget_ver2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Throughput/Mbps"))
        item = self.tableWidget_ver2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Loss"))
        item = self.tableWidget_ver2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Delay/ms"))
        item = self.tableWidget_ver2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Up/Down"))
        item = self.tableWidget_ver2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Time"))
        item = self.tableWidget_ver2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "备注"))
        item = self.tableWidget_ver3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Protocol"))
        item = self.tableWidget_ver3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tx/Mbps"))
        item = self.tableWidget_ver3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Rx/Mpbs"))
        item = self.tableWidget_ver3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Loss"))
        item = self.tableWidget_ver3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Delay/ms"))
        item = self.tableWidget_ver3.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Up/Down"))
        item = self.tableWidget_ver3.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Time"))
        item = self.tableWidget_ver3.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "备注"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Result"))
        self.textBrowser_v2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"doc\"></a><span style=\" font-family:\'Lato\'; font-size:x-large; font-weight:600; color:#69665e;\">i</span><span style=\" font-family:\'Lato\'; font-size:x-large; font-weight:600; color:#69665e;\">Perf 2用户文档</span></h2>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:x-large; font-weight:600;\"><br /></p>\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\">\n"
"<tr>\n"
"<td colspan=\"3\" bgcolor=\"#cccccc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">常规选项</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">命令行选项</span></p></td>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">环境变量选项</span></p></td>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">描述</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"format\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">f</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，-- </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">format [bkmaBKMA]</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">$ IPERF_FORMAT</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">一个字母，指定用于打印带宽数字的格式。支持的格式为 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:15px; color:#69665e;\">    \'b\'=比特/秒\'B\'=字节/秒</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:15px; color:#69665e;\">    \'k\'=千比特/秒\'K\'=千字节/秒</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:15px; color:#69665e;\">    \'m\'=兆比特/秒\'M\'=兆字节/秒</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:15px; color:#69665e;\">    \'g\'=千兆位/秒\'G\'=千兆字节/秒</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:15px; color:#69665e;\">    \'a\'=自适应比特/秒\'A\'=自适应字节/秒</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">自适应格式可以在千和兆之间进行选择。带宽以外的其他字段始终打印字节，但其他字段遵循请求的格式。默认值为“ a”。 <br /></span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">注意：</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">在处理字节时，此处Kilo = 1024，Mega = 1024 ^ 2和Giga = 1024 ^ 3。通常在网络中，Kilo = 1000，Mega = 1000 ^ 2和Giga = 1000 ^ 3，因此我们在处理位时会用到它。如果这确实困扰您，请使用-fb并进行数学运算。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"interval\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">i</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--interval </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">＃</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">$ IPERF_INTERVAL</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">设置定期带宽，抖动和损耗报告之间的间隔时间（以秒为单位）。如果不为零，则 自上一次报告以来，每隔带宽</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">间隔</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">秒便会报告一次。如果为零，则不打印任何定期报告。默认值为零。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"len\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">l</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--len </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">＃[KM]</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">$ IPERF_LEN</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">读取或写入的缓冲区的长度。iPerf通过多次写入</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">len</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">个字节的数组来工作。TCP的默认值为8 KB，UDP的默认值为1470字节。对于UDP，请注意，这是数据报的大小，使用IPv6寻址时，应将其减小到1450或更小以避免碎片。另请参见</span><a href=\"https://iperf.fr/iperf-doc.php#num\"><span style=\" font-family:\'Lato\'; font-size:15px; text-decoration: underline; color:#0000ff;\">-n</span></a><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\"> 和</span><a href=\"https://iperf.fr/iperf-doc.php#time\"><span style=\" font-family:\'Lato\'; font-size:15px; text-decoration: underline; color:#0000ff;\">-t</span></a><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\"> 选项。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"print_mss\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">m</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--print_mss</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">$ IPERF_PRINT_MSS</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">打印报告的TCP MSS大小（通过TCP_MAXSEG选项）和观察到的读取大小，这些大小通常与MSS相关。MSS通常是MTU-TCP / IP标头的40个字节。由于IP选项的额外标头空间，通常报告的MSS略小。还打印了与MTU对应的接口类型（以太网，FDDI等）。在许多操作系统上都没有实现此选项，但是读取的大小可能仍指示MSS。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"port\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">p</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--port </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">＃</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">$ IPERF_PORT</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">服务器用于侦听和客户端连接的服务器端口。客户端和服务器中这应该相同。默认值为5001，与ttcp相同。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"udp\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">u</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--udp</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">$ IPERF_UDP</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">使用UDP而不是TCP。另请参见</span><a href=\"https://iperf.fr/iperf-doc.php#bandwidth\"><span style=\" font-family:\'Lato\'; font-size:15px; text-decoration: underline; color:#0000ff;\">-b</span></a><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\"> 选项。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"window\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">w</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--window </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">＃[KM]</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">$ TCP_WINDOW_SIZE</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">将套接字缓冲区大小设置为指定值。对于TCP，这将设置TCP窗口大小。对于UDP，接收数据报的只是缓冲区，因此限制了最大可接收数据报的大小。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"bind\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">B</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--bind </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">主机</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">$ IPERF_BIND</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">绑定到</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">主机</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，这台机器的地址之一。对于客户端，这将设置出站接口。对于服务器，这将设置传入接口。这仅在具有多个网络接口的多宿主主机上有用。 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">对于UDP服务器模式下的iPerf，这也用于绑定并加入多播组。使用224.0.0.0到239.255.255.255之间的地址进行多播。另请参见</span><a href=\"https://iperf.fr/iperf-doc.php#ttl\"><span style=\" font-family:\'Lato\'; font-size:15px; text-decoration: underline; color:#0000ff;\">-T</span></a><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\"> 选项。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"compatibility\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">C</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，-兼容性</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">$ IPERF_COMPAT</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">兼容模式允许与旧版本的iPerf一起使用。互操作性不需要此模式，但强烈建议使用此模式。在某些情况下，使用代表流传输时，可能会导致1.7服务器崩溃或导致意外的连接尝试。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"mss\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">M</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--mss </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">＃[KM}</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">$ IPERF_MSS</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">尝试通过TCP_MAXSEG选项设置TCP最大段大小（MSS）。MSS通常是MTU-TCP / IP标头的40个字节。对于以太网，MSS为1460字节（1500字节MTU）。许多操作系统上未实现此选项。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"nodelay\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">N</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--nodelay</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">$ IPERF_NODELAY</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">设置“ TCP no delay”选项，禁用Nagle的算法。通常，仅对交互式应用程序（如telnet）禁用此功能。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-V</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">（从v1.6或更高版本开始）</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">。</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">绑定到IPv6地址<br />服务器端：<br />$ iperf -s -V </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">客户端：<br />$ iperf -c &lt;服务器IPv6地址&gt; -V<br /> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">注意：在版本1.6.3和更高版本中，不需要将特定的IPv6地址与</span><a href=\"https://iperf.fr/iperf-doc.php#bind\"><span style=\" font-family:\'Lato\'; font-size:15px; text-decoration: underline; color:#0000ff;\">-B</span></a><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">选项绑定，而先前的1.6版本则需要。同样，在大多数使用此选项的操作系统上，也会使用IPv4映射的地址响应IPv4客户端。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"help\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">h</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，-帮助</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\"> </span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">打印出命令摘要并退出。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"version\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">v</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--version</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\"> </span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">打印版本信息并退出。如果使用POSIX线程编译，则输出“ pthreads”；如果使用Microsoft Win32线程编译，则输出“ win32线程”；如果不使用线程编译，则输出“单线程”。</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"3\" style=\" vertical-align:top;\"></td></tr>\n"
"<tr>\n"
"<td colspan=\"3\" bgcolor=\"#cccccc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">服务器特定选项</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">命令行选项</span></p></td>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">环境变量选项</span></p></td>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">描述</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"server\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">s</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--server</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">$ IPERF_SERVER</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">在服务器模式下运行iPerf。（iPerf2可以处理多个客户端请求）</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-D</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">（从v1.2或更高版本开始）</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">。</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">作为守护程序运行服务器（Unix平台）<br />在有服务的Win32平台上，iPerf将开始作为服务运行。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-R</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">（仅适用于Windows，从v1.2或更高版本开始）</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">。</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">删除iPerf服务（如果正在运行）。 </span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-o</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">（仅适用于Windows，从v1.2或更高版本开始）</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">。</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">将输出重定向到给定的文件。 </span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"sclient\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">c</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--client </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">主机</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">$ IPERF_CLIENT</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">如果iPerf处于服务器模式，则使用-c指定主机将把iPerf接受的连接限制为指定的 </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">主机</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">。不适用于UDP。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"sparallel\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">P</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--parallel </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">＃</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">$ IPERF_PARALLEL</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">服务器在关闭之前要处理的连接数。默认值为0（表示永远接受连接）。</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"3\" style=\" vertical-align:top;\"></td></tr>\n"
"<tr>\n"
"<td colspan=\"3\" bgcolor=\"#cccccc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">客户特定选项</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">命令行选项</span></p></td>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">环境变量选项</span></p></td>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">描述</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"bandwidth\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">b</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--bandwidth </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">＃[KM]</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">$ IPERF_BANDWIDTH</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">以bps为单位发送的UDP带宽。这意味着-u选项。默认值为1 Mbit /秒。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"client\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">c</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--client </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">主机</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">$ IPERF_CLIENT</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">运行iperf的客户端模式，连接到上运行的iperf的服务器 </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">主机</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"dualtest\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">d</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，-双重测试</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">$ IPERF_DUALTEST</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">在双重测试模式下运行iPerf。这将导致服务器在</span><a href=\"https://iperf.fr/iperf-doc.php#listenport\"><span style=\" font-family:\'Lato\'; font-size:15px; text-decoration: underline; color:#0000ff;\">-L</span></a><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">选项中指定的端口上连接回客户端 （或默认为客户端连接到服务器的端口）。立即执行此操作，因此同时运行测试。如果要进行交替测试，请尝试</span><a href=\"https://iperf.fr/iperf-doc.php#tradeoff\"><span style=\" font-family:\'Lato\'; font-size:15px; text-decoration: underline; color:#0000ff;\">-r。</span></a></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"num\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">n</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--num </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">＃[KM]</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">$ IPERF_NUM</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">要传输的缓冲区数。通常，iPerf发送10秒钟。-n选项将覆盖此内容，并发送</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">len</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\"> 个字节</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">num</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">次的数组，而不管它花费多长时间。另请参见</span><a href=\"https://iperf.fr/iperf-doc.php#len\"><span style=\" font-family:\'Lato\'; font-size:15px; text-decoration: underline; color:#0000ff;\">-l</span></a><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\"> 和</span><a href=\"https://iperf.fr/iperf-doc.php#time\"><span style=\" font-family:\'Lato\'; font-size:15px; text-decoration: underline; color:#0000ff;\">-t</span></a><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\"> 选项。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"tradeoff\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">r</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，-权衡</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">$ IPERF_TRADEOFF</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">在权衡测试模式下运行iPerf。这将导致服务器在</span><a href=\"https://iperf.fr/iperf-doc.php#listenport\"><span style=\" font-family:\'Lato\'; font-size:15px; text-decoration: underline; color:#0000ff;\">-L</span></a><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">选项中指定的端口上连接回客户端 （或默认为客户端连接到服务器的端口）。这是在客户端连接终止之后完成的，因此交替运行测试。如果要同时进行测试，请尝试 </span><a href=\"https://iperf.fr/iperf-doc.php#dualtest\"><span style=\" font-family:\'Lato\'; font-size:15px; text-decoration: underline; color:#0000ff;\">-d。</span></a></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"time\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">t</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--time </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">＃</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">$ IPERF_TIME</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">传输时间（以秒为单位）。iPerf通常通过重复发送</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">len</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">个字节的数组达</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">时间</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">秒来工作。默认值为10秒。另请参见</span><a href=\"https://iperf.fr/iperf-doc.php#len\"><span style=\" font-family:\'Lato\'; font-size:15px; text-decoration: underline; color:#0000ff;\">-l</span></a><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\"> 和</span><a href=\"https://iperf.fr/iperf-doc.php#num\"><span style=\" font-family:\'Lato\'; font-size:15px; text-decoration: underline; color:#0000ff;\">-n</span></a><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\"> 选项。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"listenport\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">L</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--listenport </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">＃</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">$ IPERF_LISTENPORT</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">这指定服务器将连接回客户端的端口。它默认为用于从客户端连接到服务器的端口。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"parallel\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">P</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--parallel </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">＃</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">$ IPERF_PARALLEL</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">到服务器的同时连接数。默认值为1。在客户端和服务器上都需要线程支持。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"tos\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">S</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--tos </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">＃</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">$ IPERF_TOS</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">传出数据包的服务类型。（许多路由器会忽略TOS字段。）您可以使用十六进制值（0x）作为前缀，使用八进制数（0）作为前缀，或者使用十进制来指定值。例如，\'0x10\'十六进制=\'020\'八进制=\'16\'十进制。RFC 1349中指定的TOS编号为： </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:15px; color:#69665e;\">    IPTOS_LOWDELAY最小化延迟0x10</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:15px; color:#69665e;\">    IPTOS_THROUGHPUT最大化吞吐量0x08</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:15px; color:#69665e;\">    IPTOS_RELIABILITY最大化可靠性0x04</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:15px; color:#69665e;\">    IPTOS_LOWCOST最小化成本0x02</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"ttl\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">T</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--ttl </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">＃</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">$ IPERF_TTL</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">传出组播数据包的生存时间。这实际上是要经过的路由器跃点数，也用于范围界定。默认值为1，本地链接。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-F</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">（从v1.2或更高版本开始）</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">。</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">使用代表性的流来测量带宽，例如：- <br />$ iperf -c &lt;服务器地址&gt; -F &lt;文件名&gt;</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-I</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">（从v1.2或更高版本开始）</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">。</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">与-F相同，从stdin输入。</span></p></td></tr></table>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_v3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3doc\"></a><span style=\" font-family:\'Lato\'; font-size:x-large; font-weight:600; color:#69665e;\">i</span><span style=\" font-family:\'Lato\'; font-size:x-large; font-weight:600; color:#69665e;\">Perf 3用户文档</span></h2>\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\">\n"
"<tr>\n"
"<td colspan=\"2\" bgcolor=\"#cccccc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">常规选项</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">命令行选项</span></p></td>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">描述</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3port\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">p</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--port </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">n</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">服务器用于侦听和客户端连接的服务器端口。客户端和服务器中这应该相同。默认值为5201。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3cport\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-cport </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">n</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">指定客户端端口的选项。（iPerf 3.1中的新功能）</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3format\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">f</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，-- </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">format [kmKM]</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">一个字母，指定用于打印带宽数字的格式。支持的格式为 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:15px; color:#69665e;\">    \'k\'=千比特/秒\'K\'=千字节/秒</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:15px; color:#69665e;\">    \'m\'=兆比特/秒\'M\'=兆字节/秒</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">自适应格式可以在千和兆之间进行选择。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3interval\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">i</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--interval </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">n</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">设置定期带宽，抖动和损耗报告之间的间隔时间（以秒为单位）。如果不为零，则 自上一次报告以来，每隔带宽</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">间隔</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">秒便会报告一次。如果为零，则不打印任何定期报告。默认值为零。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3filname\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">F</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，-文件名</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">客户端：</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">从文件读取并写入网络，而不是使用随机数据；<br /></span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">服务器端：</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">从网络读取并写入文件，而不是丢弃数据。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3affinity\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">A</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，-亲和力</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">n / n，mF</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">设置CPU关联（如果可能）（仅限Linux和FreeBSD）。在客户端和服务器上，都可以使用此参数的n形式（其中n是CPU编号）来设置本地亲缘关系。此外，在客户端，您可以使用n，m形式的参数来覆盖服务器仅对一项测试的相似性。请注意，使用此功能时，一个进程将仅绑定到一个CPU（而不是包含可能的多个CPU的集合）。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3bind\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">B</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--bind </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">主机</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">绑定到</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">主机</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，这台机器的地址之一。对于客户端，这将设置出站接口。对于服务器，这将设置传入接口。这仅在具有多个网络接口的多宿主主机上有用。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3verbose\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">V</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，-冗长</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">提供更详细的输出</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3json\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">J</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--json</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">以JSON格式输出</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3logfile\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-logfile</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">文件</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">将输出发送到日志文件。（iPerf 3.1中的新功能）</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3debug\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-d</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，- </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">调试</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">发出调试输出。主要（也许专门）用于开发人员。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3version\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">v</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--version</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">显示版本信息并退出。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3help\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">h</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，-帮助</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">显示帮助简介并退出。</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"2\" style=\" vertical-align:top;\"></td></tr>\n"
"<tr>\n"
"<td colspan=\"2\" bgcolor=\"#cccccc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">服务器特定选项</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">命令行选项</span></p></td>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">描述</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3server\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">s</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--server</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">在服务器模式下运行iPerf。（这一次将仅允许一个iperf连接）</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3daemon\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">D</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，-守护进程</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">作为后台程序在后台运行服务器。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3pidfile\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">I</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--pidfile </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">文件</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">编写具有进程ID的文件，这在作为守护程序运行时最有用。（iPerf 3.1中的新功能）</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"2\" style=\" vertical-align:top;\"></td></tr>\n"
"<tr>\n"
"<td colspan=\"2\" bgcolor=\"#cccccc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">客户特定选项</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">命令行选项</span></p></td>\n"
"<td bgcolor=\"#cccccc\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">描述</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3client\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">c</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--client </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">主机</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">运行iperf的客户端模式，连接到上运行的iperf的服务器</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">主机</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3sctp\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-sctp</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">使用SCTP而不是TCP（Linux，FreeBSD和Solaris）。（iPerf 3.1中的新功能）</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3udp\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">u</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--udp</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">使用UDP而不是TCP。另请参见</span><a href=\"https://iperf.fr/iperf-doc.php#3bandwidth\"><span style=\" font-family:\'Lato\'; font-size:15px; text-decoration: underline; color:#0000ff;\">-b</span></a><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">选项。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3bandwidth\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">b</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--bandwidth </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">n [KM]</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">将目标带宽设置为n位/秒（对于UDP默认为1 Mbit /秒，对于TCP为无限制）。如果有多个流（-P标志），则带宽限制将分别应用于每个流。您还可以在带宽说明符中添加一个“ /”和一个数字。这称为“突发模式”。它会发送给定数量的数据包而不会暂停，即使该数据包暂时超过了指定的带宽限制。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3time\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">t</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，-时间</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">n</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">传输时间（以秒为单位）。iPerf通常通过重复发送</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">len</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">个字节的数组达</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">时间</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">秒来工作。默认值为10秒。另请参见</span><a href=\"https://iperf.fr/iperf-doc.php#3len\"><span style=\" font-family:\'Lato\'; font-size:15px; text-decoration: underline; color:#0000ff;\">-l</span></a><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，</span><a href=\"https://iperf.fr/iperf-doc.php#3blockcount\"><span style=\" font-family:\'Lato\'; font-size:15px; text-decoration: underline; color:#0000ff;\">-k</span></a><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">和</span><a href=\"https://iperf.fr/iperf-doc.php#3num\"><span style=\" font-family:\'Lato\'; font-size:15px; text-decoration: underline; color:#0000ff;\">-n</span></a><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">选项。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3num\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">n</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--num </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">n [KM]</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">要传输的缓冲区数。通常，iPerf发送10秒钟。-n选项将覆盖此内容，并发送</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">len</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\"> 个字节</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">num</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">次的数组，而不管它花费多长时间。另请参见</span><a href=\"https://iperf.fr/iperf-doc.php#3len\"><span style=\" font-family:\'Lato\'; font-size:15px; text-decoration: underline; color:#0000ff;\">-l</span></a><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，</span><a href=\"https://iperf.fr/iperf-doc.php#3blockcount\"><span style=\" font-family:\'Lato\'; font-size:15px; text-decoration: underline; color:#0000ff;\">-k</span></a><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">和</span><a href=\"https://iperf.fr/iperf-doc.php#3time\"><span style=\" font-family:\'Lato\'; font-size:15px; text-decoration: underline; color:#0000ff;\">-t</span></a><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">选项。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3blockcount\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">k</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--blockcount </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">n [KM]</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">要传输的块（数据包）数。（而不是-t或-n）另请参阅</span><a href=\"https://iperf.fr/iperf-doc.php#3time\"><span style=\" font-family:\'Lato\'; font-size:15px; text-decoration: underline; color:#0000ff;\">-t</span></a><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，</span><a href=\"https://iperf.fr/iperf-doc.php#3len\"><span style=\" font-family:\'Lato\'; font-size:15px; text-decoration: underline; color:#0000ff;\">-l</span></a><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">和</span><a href=\"https://iperf.fr/iperf-doc.php#3num\"><span style=\" font-family:\'Lato\'; font-size:15px; text-decoration: underline; color:#0000ff;\">-n</span></a><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">选项。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3len\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">l</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--length </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">n [KM]</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">读取或写入的缓冲区的长度。iPerf通过多次写入</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">len</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">个字节的数组来工作。TCP的默认值为128 KB，UDP的默认值为8 KB。另请参见</span><a href=\"https://iperf.fr/iperf-doc.php#3num\"><span style=\" font-family:\'Lato\'; font-size:15px; text-decoration: underline; color:#0000ff;\">-n</span></a><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，</span><a href=\"https://iperf.fr/iperf-doc.php#3blockcount\"><span style=\" font-family:\'Lato\'; font-size:15px; text-decoration: underline; color:#0000ff;\">-k</span></a><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">和</span><a href=\"https://iperf.fr/iperf-doc.php#3time\"><span style=\" font-family:\'Lato\'; font-size:15px; text-decoration: underline; color:#0000ff;\">-t</span></a><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">选项。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3parallel\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">P</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，-平行</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">n</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">到服务器的同时连接数。默认值为1。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3reverse\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">R</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，-反向</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">以反向模式运行（服务器发送，客户端接收）。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3window\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">w</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--window </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">n [KM]</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">将套接字缓冲区大小设置为指定值。对于TCP，这将设置TCP窗口大小。（这将发送到服务器并在该侧使用）</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3mss\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">M</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--set-mss </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">n</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">尝试设置TCP最大段大小（MSS）。MSS通常是MTU-TCP / IP标头的40个字节。对于以太网，MSS为1460字节（1500字节MTU）。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3nodelay\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">N</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，-无延迟</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">设置“ TCP no delay”选项，禁用Nagle的算法。通常，仅对交互式应用程序（如telnet）禁用此功能。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3version4\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">4</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--version4</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">仅使用IPv4。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3version6\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">6</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--version4</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">仅使用IPv6。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3tos\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">S</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--tos </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">n</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">传出数据包的服务类型。（许多路由器会忽略TOS字段。）您可以使用十六进制值（0x）作为前缀，使用八进制数（0）作为前缀，或者使用十进制来指定值。例如，\'0x10\'十六进制=\'020\'八进制=\'16\'十进制。RFC 1349中指定的TOS编号为： </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:15px; color:#69665e;\">    IPTOS_LOWDELAY最小化延迟0x10</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:15px; color:#69665e;\">    IPTOS_THROUGHPUT最大化吞吐量0x08</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:15px; color:#69665e;\">    IPTOS_RELIABILITY最大化可靠性0x04</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:15px; color:#69665e;\">    IPTOS_LOWCOST最小化成本0x02</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3flowlabel\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">L</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--flowlabel </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">n</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">设置IPv6流标签（当前仅在Linux上受支持）。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3zerocopy\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">Z</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--zerocopy</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">使用发送数据的“零复制”方法，例如sendfile（2），而不是通常的write（2）。这将使用更少的CPU。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3omit\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">O</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，-省略</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">n</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">省略测试的前n秒，以跳过TCP </span><a href=\"https://en.wikipedia.org/wiki/Slow-start\"><span style=\" font-family:\'Lato\'; font-size:15px; text-decoration: underline; color:#0000ff;\">TCP慢启动</span></a><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">周期。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3title\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">T，--title </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">str</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">使用此字符串为每条输出行添加前缀。</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"3congestion\"></a><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">-</span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; color:#69665e;\">C</span><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">，--linux-congestion </span><span style=\" font-family:\'Lato\'; font-size:15px; font-weight:600; font-style:italic; color:#69665e;\">算法</span></p></td>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">设置</span><a href=\"https://en.wikipedia.org/wiki/TCP_congestion-avoidance_algorithm\"><span style=\" font-family:\'Lato\'; font-size:15px; text-decoration: underline; color:#0000ff;\">拥塞控制算法</span></a><span style=\" font-family:\'Lato\'; font-size:15px; color:#69665e;\">（仅适用于iPerf 3.0的Linux，适用于iPerf 3.1的Linux和FreeBSD）。</span></p></td></tr></table></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Help"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
