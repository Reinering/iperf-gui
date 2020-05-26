# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QLabel, QTableWidgetItem, QVBoxLayout
from PyQt5.QtCore import pyqtSlot, QThread, pyqtSignal, Qt, QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5 import QtWidgets, QtCore
import sip
import subprocess, threading
from pyexcel import writeExcel
import os
import datetime, time
import re, decimal
import serial, serial.tools.list_ports
from rn_common.ssh import SSH
from rn_common.serial import Serial
from rn_common.telnet import Telnet
from rn_common.netTools import getLinkState
from Ui_iperf_client import Ui_MainWindow
from script_more import Dialog


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.translate = QCoreApplication.translate
        self.cc_state = False
        self.save_state = False
        self.filePath = ''
        self.iperfVer = '2'
        self.throughputdTh = ThroughputThread(self.tableWidget)
        self.throughputdTh.signal_result.connect(self.setThroughputResult)
        self.tDTh = TimeDownThread()
        self.tDTh.signal_Time.connect(self.setTimeDown)
        self.cCount = 0
        self.total = 0
        self.failTotal = 0
        self.rowCount = 0
        self.isScript = False
        self.scriptNum = 1
        self.scriptKey = 0
        self.horizontalLayout_script_List = {}
        self.serList = []
        self.initWidget()

    def initWidget(self):
        self.tabWidget.setTabEnabled(3, False)
        self.tabWidget.setCurrentIndex(0)
        self.widget_iperf3.hide()
        self.label_countDown.setText('0')
        self.pushButton_s.setEnabled(False)
        self.spinBox_time.setValue(60)
        self.tableWidget.removeColumn(0)
        self.tableWidget.removeColumn(0)
        self.tableWidget.setColumnWidth(0, 110)
        self.tableWidget.setColumnWidth(1, 190)
        self.tableWidget.setColumnWidth(2, 180)
        self.clearTableWidgetEntry(self.tableWidget)

        self.comboBox_serial.setHidden(True)
        self.pushButton_refresh.setHidden(True)
        self.scrollArea.setEnabled(False)
        self.horizontalLayout_script_List['0'] = [self.horizontalLayout_20, self.verticalLayout_7, self.pushButton_script_add, self.label_index,
                                                  self.verticalLayout_6, self.horizontalLayout_12, self.label_16, self.comboBox_script_pro, self.label_pro_ip,
                                                  self.lineEdit_script_ip, self.comboBox_serial, self.pushButton_script_more, self.label_13, self.comboBox_opp,
                                                  self.horizontalLayout_18, self.label_17, self.lineEdit_script, self.horizontalLayout_17, self.label_18,
                                                  self.lineEdit_re, {'baudbit': 115200, 'user': 'root', 'passwd': 'nE7jA%5m'}]

        self.label_count = QLabel()
        font = QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_count.setFont(font)
        self.label_count.setObjectName("label_count")
        self.statusBar.addPermanentWidget(self.label_count)
        self.on_pushButton_refresh_clicked()
        self.statusBar.showMessage('Ready')

    def setTabState(self, checked):
        self.tabWidget.setTabEnabled(1, checked)
        self.tabWidget.setTabEnabled(2, checked)
        # self.tabWidget.setTabEnabled(3, checked)
        self.groupBox_test.setEnabled(checked)

    def setTimeDown(self, p0):
            self.label_countDown.setText(str(p0) + ' s')

    def updateStatusBar(self):
        self.label_count.setText('共计：{}次  成功：{}次  失败：{}次'.format(self.total, self.total-self.failTotal, self.failTotal))

    def addInfo(self, tableWidget, *args):
        row = tableWidget.rowCount()
        tableWidget.setRowCount(row + 1)
        i = 0
        for arg in args:
            argType = type(arg)
            if argType == int:
                self.addTableWidgetEntry(row, i, str(arg), tableWidget)
            elif argType == datetime.datetime:
                self.addTableWidgetEntry(row, i, self.datetime_toString(arg), tableWidget)
            elif argType == decimal.Decimal:
                self.addTableWidgetEntry(row, i, str(arg), tableWidget)
            else:
                self.addTableWidgetEntry(row, i, arg, tableWidget)
            i += 1
        self.tableWidget.scrollToBottom()

    def addTableWidgetEntry(self, x, y, p0, tbWidget):
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        if x == 1 and self.iperfVer == '2':
            item.setFlags(Qt.ItemIsEditable)
        elif x == 2 and self.iperfVer == '3':
            item.setFlags(Qt.ItemIsEditable)
        else:
            pass
        item.setText(self.translate("MainWindow", p0))
        # item.setFont(self.setCellFont())
        tbWidget.setItem(x, y, item)

    def clearTableWidgetEntry(self, tbWidget):
        row = tbWidget.rowCount()
        for i in range(row):
            tbWidget.removeRow(0)

    def setThroughputResult(self, p0):
        if "testing" == p0[0]:
            self.label_error.setText("吞吐量测试中，请稍等...")
            return
        elif "ping fail" == p0[0]:
            self.label_error.setText("吞吐量测试， 网络连接失败， 请检查后重试")
            self.failTotal += 1

        elif "connect fail" == p0[0]:
            self.label_error.setText("吞吐量测试， 连接服务端失败， 请检查后重试")
            self.failTotal += 1
        elif "fail" == p0[0]:
            self.label_error.setText("吞吐量测试， 测试失败，未获取到测试结果")
            self.failTotal += 1
        elif "result" == p0[0]:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.label_error.setText(self.translate("GeneralWindow", "吞吐量测试已完成"))
            if self.iperfVer == 3:
                self.label_res_tx.setText(self.translate("GeneralWindow", p0[1] + ' Mbps'))
                self.label_res_rx.setText(self.translate("GeneralWindow", p0[2] + ' Mbps'))
                self.addInfo(self.tableWidget, (p0[1] + ' Mbps', p0[2] + ' Mbps', '', '编辑', now))
                if self.save_state:
                    writeExcel(self.filePath, 'Iperf3 吞吐量', (self.rowCount, p0[1], p0[2], now))
                    self.rowCount += 1
            else:
                self.label_res_th.setText(self.translate("GeneralWindow", p0[1] + ' Mbps'))
                self.addInfo(self.tableWidget, (p0[1] + ' Mbps', '', '编辑', now))
                if self.save_state:
                    writeExcel(self.filePath, 'Iperf2 吞吐量', (self.rowCount, p0[1], now))
                    self.rowCount += 1

        self.total += 1
        self.updateStatusBar()
        self.statusBar.showMessage('Stop')
        self.cCount -= 1
        if self.cCount > 0:
            self.label_error.setText("等待中...")
            cInterval = self.spinBox_cInterval.value()
            if cInterval < 5:
                time.sleep(5)
            else:
                time.sleep(self.spinBox_cInterval.value())
            if self.isScript:
                self.index = 0
                self.scriptTh.start()
                if self.waitNum == 0:
                    self.throughputdTh.start()
                    self.statusBar.showMessage('Start')
            else:
                self.throughputdTh.start()
                self.statusBar.showMessage('Start')
            if self.iperfVer == 2:
                self.label_res_th.clear()
            elif self.iperfVer == 3:
                self.label_res_rx.clear()
                self.label_res_tx.clear()
        else:
            self.setTabState(True)
            self.pushButton_a.setEnabled(True)
            self.pushButton_s.setEnabled(False)
            self.statusBar.showMessage('Finish', 5000)

    def getScriptArgs(self):
        if self.isScript:
            scriptArgs = []
            tmp = []
            count = 0

            # tmp.append(self.comboBox_script_pro.currentText())
            # tmp.append(self.lineEdit_script_ip.text())
            # tmp.append(self.comboBox_serial.currentText())
            # opp = self.comboBox_opp.currentText()
            # if "运行前" in opp:
            #     count += 1
            # tmp.insert(0, opp)
            # tmp.append(self.lineEdit_script.text())
            # tmp.append(self.lineEdit_re.text())
            # tmp.append(self.horizontalLayout_script_List['0'][-1])
            # scriptArgs.append(tmp)

            for i in self.horizontalLayout_script_List:
                horizontalLayout_script = self.horizontalLayout_script_List[i]
                # tmp.clear()
                tmp.append(horizontalLayout_script[7].currentText())
                tmp.append(horizontalLayout_script[9].text())
                tmp.append(horizontalLayout_script[10].currentText())
                opp = horizontalLayout_script[13].currentText()
                if "运行前" in opp:
                    count += 1
                tmp.insert(0, opp)
                tmp.append(horizontalLayout_script[16].text())
                tmp.append(horizontalLayout_script[19].text())
                tmp.append(horizontalLayout_script[-1])
                scriptArgs.append(tmp)
            return scriptArgs, count
        else:
            return None, None

    def runThrouTh(self):
        print("STARTING")
        self.index += 1
        if self.index == self.waitNum:
            self.throughputdTh.start()

    @pyqtSlot(bool)
    def on_checkBox_cc_clicked(self, checked):
        """
        Slot documentation goes here.

        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.spinBox_cCount.setEnabled(checked)
        self.spinBox_cInterval.setEnabled(checked)

    @pyqtSlot(bool)
    def on_checkBox_save_clicked(self, checked):
        """
        Slot documentation goes here.

        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.label_path.setEnabled(checked)
        self.pushButton_save.setEnabled(checked)

    @pyqtSlot(str)
    def on_comboBox_ver_activated(self, p0):
        """
        Slot documentation goes here.

        @param p0 DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.iperfVer = p0
        if p0 == '2':
            self.widget_iperf2.show()
            self.widget_iperf3.hide()
            self.tableWidget.removeColumn(0)
            # self.tableWidget.setColumnCount(4)
            item = QTableWidgetItem()
            item.setText(self.translate("MainWindow", "Throughput/Mbps"))
            self.tableWidget.setHorizontalHeaderItem(0, item)
            self.tableWidget.setColumnWidth(0, 110)
            self.tableWidget.setColumnWidth(1, 190)
            self.tableWidget.setColumnWidth(2, 180)
        elif p0 == '3':
            self.widget_iperf2.hide()
            self.widget_iperf3.show()
            # self.tableWidget.setColumnCount(5)
            self.tableWidget.insertColumn(0)
            item = QTableWidgetItem()
            item.setText(self.translate("MainWindow", "Tx/Mbps"))
            self.tableWidget.setHorizontalHeaderItem(0, item)
            item = QTableWidgetItem()
            item.setText(self.translate("MainWindow", "Rx/Mpbs"))
            self.tableWidget.setHorizontalHeaderItem(1, item)
            self.tableWidget.setColumnWidth(0, 60)
            self.tableWidget.setColumnWidth(1, 60)
            self.tableWidget.setColumnWidth(2, 180)
            self.tableWidget.setColumnWidth(3, 180)
        else:
            pass

    @pyqtSlot()
    def on_pushButton_a_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.label_error.clear()

        pro = self.comboBox_pro.currentText()
        c_ip = self.lineEdit_c_param.text()
        if not c_ip:
            self.label_error.setText("请先进行设置再开始")
            return
        c_time = self.spinBox_time.value()
        if not c_time:
            self.label_error.setText("测试时长未设置，请设置后开始")
            return
        c_param = self.lineEdit_c_param.text()
        if not c_param:
            self.label_error.setText("测试参数未设置，请设置后开始")
            return

        self.setTabState(False)
        self.pushButton_a.setEnabled(False)
        self.pushButton_s.setEnabled(True)
        if pro == "UDP":
            c_param = c_param + ' -u '
        c_p = self.spinBox_p.value()
        if c_p > 0:
            c_param = c_param + ' -p ' + str(self.spinBox_p.value())
        self.throughputdTh.setParam(self.iperfVer, c_ip, c_param, c_time, self.tDTh)

        if self.isScript:
            self.index = 0
            self.args, self.waitNum = self.getScriptArgs()
            self.scriptTh = ScriptThread(c_time, self.args)
            self.scriptTh.signal_index.connect(self.runThrouTh)
            self.scriptTh.start()
            if self.waitNum == 0:
                self.throughputdTh.start()
                self.statusBar.showMessage('Start')
        else:
            self.throughputdTh.start()
            self.statusBar.showMessage('Start')

    @pyqtSlot()
    def on_pushButton_s_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.setTabState(True)
        self.pushButton_a.setEnabled(True)
        self.pushButton_s.setEnabled(False)

        try:
            self.throughputdTh.close()
            if self.isScript:
                self.scriptTh.stop()
        except Exception as e:
            print(e)
        self.statusBar.showMessage('Stop')

    @pyqtSlot()
    def on_pushButton_save_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        fileName, ok = QFileDialog.getSaveFileName(self,
                                                     "文件保存",
                                                     "./",
                                                     "Excel Files (*.xls)")
        # print(fileName, ok)
        if fileName:
            self.label_path.setText(fileName.replace('/', '\\'))
            self.rowCount = 0
            self.clearTableWidgetEntry(self.tableWidget)

    @pyqtSlot()
    def on_lineEdit_c_ip_editingFinished(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.label_error_c.clear()
        c_ip = self.lineEdit_c_ip.text()
        if c_ip == '':
            return
        if not re.match(r'^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$', c_ip):
            self.lineEdit_c_ip.clear()
            self.label_error_c.setText("IP地址格式错误，请重新输入")
            return

    @pyqtSlot()
    def on_lineEdit_c_param_editingFinished(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.label_error_c.clear()

        if self.iperfVer == '2':
            self.label_res_th.clear()
        elif self.iperfVer == '3':
            self.label_res_rx.clear()
            self.label_res_tx.clear()

        c_param = self.lineEdit_c_param.text()
        # print(c_param)
        if '-t ' in c_param:
            self.lineEdit_c_param.clear()
            self.label_error_c.setText("iperf 参数无法设置-t 测试时间参数，请重新设置")
            return

        if '-c ' in c_param:
            self.lineEdit_c_param.clear()
            self.label_error_c.setText("iperf 参数无法设置-c 测试IP参数，请重新设置")
            return

        if 'iperf' in c_param:
            self.lineEdit_c_param.clear()
            self.label_error_c.setText("iperf 参数无法设置iperf版本参数，请重新设置")
            return

    @pyqtSlot()
    def on_lineEdit_script_ip_editingFinished(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.label_error_t.clear()
        script_ip = self.lineEdit_script_ip.text()
        if script_ip == '':
            return
        if not re.match(r'^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$', script_ip):
            self.lineEdit_script_ip.clear()
            self.label_error_t.setText("IP地址格式错误，请重新输入")
            return

    def on__lineEdit_script_ip_editingFinished(self, _lineEdit_script_ip):
        self.label_error_t.clear()
        script_ip = _lineEdit_script_ip.text()
        if script_ip == '':
            return
        if not re.match(r'^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$', script_ip):
            _lineEdit_script_ip.clear()
            self.label_error_t.setText("IP地址格式错误，请重新输入")
            return

    @pyqtSlot(bool)
    def on_checkBox_script_clicked(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.scrollArea.setEnabled(checked)
        self.pushButton_refresh.setEnabled(checked)
        self.isScript = checked
    
    @pyqtSlot()
    def on_pushButton_script_add_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        if self.scriptNum < 8:
            key = str(self.scriptKey + 1)
            horizontalLayout_script = []
            _horizontalLayout_20 = QtWidgets.QHBoxLayout()
            _horizontalLayout_20.setObjectName("horizontalLayout_script_" + str(self.scriptNum))
            horizontalLayout_script.append(_horizontalLayout_20)
            _verticalLayout_7 = QtWidgets.QVBoxLayout()
            _verticalLayout_7.setObjectName("verticalLayout_script_" + str(self.scriptNum))
            horizontalLayout_script.append(_verticalLayout_7)
            _pushButton_script_del = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            _pushButton_script_del.setMinimumSize(QtCore.QSize(25, 25))
            _pushButton_script_del.setMaximumSize(QtCore.QSize(25, 25))
            _pushButton_script_del.setObjectName("pushButton_script_del_" + str(self.scriptNum))
            _pushButton_script_del.clicked.connect(lambda: self.on_pushButton_script_del_clicked(key))
            _verticalLayout_7.addWidget(_pushButton_script_del)
            horizontalLayout_script.append(_pushButton_script_del)
            _spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            _verticalLayout_7.addItem(_spacerItem9)
            _label_index = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            _label_index.setAlignment(QtCore.Qt.AlignCenter)
            _label_index.setObjectName("label_index_" + str(self.scriptNum))
            _verticalLayout_7.addWidget(_label_index)
            horizontalLayout_script.append(_label_index)
            _spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            _verticalLayout_7.addItem(_spacerItem10)
            _horizontalLayout_20.addLayout(_verticalLayout_7)
            _verticalLayout_6 = QtWidgets.QVBoxLayout()
            _verticalLayout_6.setObjectName("verticalLayout_6_script_" + str(self.scriptNum))
            horizontalLayout_script.append(_verticalLayout_6)
            _horizontalLayout_12 = QtWidgets.QHBoxLayout()
            _horizontalLayout_12.setObjectName("horizontalLayout_12_script_" + str(self.scriptNum))
            horizontalLayout_script.append(_horizontalLayout_12)
            _label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            _label_16.setObjectName("label_16_script_" + str(self.scriptNum))
            font = QFont()
            font.setPointSize(12)
            _label_16.setFont(font)
            _horizontalLayout_12.addWidget(_label_16)
            horizontalLayout_script.append(_label_16)
            _comboBox_script_pro = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
            _comboBox_script_pro.setObjectName("_comboBox_script_pro_" + str(self.scriptNum))
            _comboBox_script_pro.setMinimumSize(QtCore.QSize(80, 0))
            _comboBox_script_pro.setMaximumSize(QtCore.QSize(80, 16777215))
            _comboBox_script_pro.addItem("")
            _comboBox_script_pro.addItem("")
            _comboBox_script_pro.addItem("")
            font = QFont()
            font.setPointSize(12)
            _comboBox_script_pro.setFont(font)
            _comboBox_script_pro.activated.connect(lambda: self.on__comboBox_script_pro_activated(key))
            _horizontalLayout_12.addWidget(_comboBox_script_pro)
            horizontalLayout_script.append(_comboBox_script_pro)
            _label_pro_ip = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            _label_pro_ip.setObjectName("label_pro_ip_" + str(self.scriptNum))
            font = QFont()
            font.setPointSize(12)
            _label_pro_ip.setFont(font)
            _horizontalLayout_12.addWidget(_label_pro_ip)
            horizontalLayout_script.append(_label_pro_ip)
            _lineEdit_script_ip = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
            _lineEdit_script_ip.setObjectName("lineEdit_script_ip_" + str(self.scriptNum))
            _lineEdit_script_ip.setMinimumSize(QtCore.QSize(135, 0))
            _lineEdit_script_ip.setMaximumSize(QtCore.QSize(135, 16777215))
            font = QFont()
            font.setPointSize(12)
            _lineEdit_script_ip.setFont(font)
            _lineEdit_script_ip.editingFinished.connect(lambda: self.on__lineEdit_script_ip_editingFinished(_lineEdit_script_ip))
            _horizontalLayout_12.addWidget(_lineEdit_script_ip)
            horizontalLayout_script.append(_lineEdit_script_ip)
            _comboBox_serial = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
            _comboBox_serial.setObjectName("comboBox_serial_script_" + str(self.scriptNum))
            _comboBox_serial.setMinimumSize(QtCore.QSize(90, 0))
            _comboBox_serial.setMaximumSize(QtCore.QSize(90, 16777215))
            font = QFont()
            font.setPointSize(12)
            _comboBox_serial.setFont(font)
            _horizontalLayout_12.addWidget(_comboBox_serial)
            horizontalLayout_script.append(_comboBox_serial)
            _comboBox_serial.setHidden(True)
            _pushButton_script_more = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            _pushButton_script_more.setMinimumSize(QtCore.QSize(25, 0))
            _pushButton_script_more.setMaximumSize(QtCore.QSize(25, 16777215))
            _pushButton_script_more.setObjectName("pushButton_script_more")
            _horizontalLayout_12.addWidget(_pushButton_script_more)
            horizontalLayout_script.append(_pushButton_script_more)
            _pushButton_script_more.clicked.connect(lambda:self.on__pushButton_script_more_clicked(key))
            _label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            font = QFont()
            font.setPointSize(12)
            _label_13.setFont(font)
            _label_13.setObjectName("label_13_" + str(self.scriptNum))
            _horizontalLayout_12.addWidget(_label_13)
            horizontalLayout_script.append(_label_13)
            _comboBox_opp = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
            _comboBox_opp.setMinimumSize(QtCore.QSize(75, 0))
            _comboBox_opp.setMaximumSize(QtCore.QSize(75, 16777215))
            font = QFont()
            font.setPointSize(12)
            _comboBox_opp.setFont(font)
            _comboBox_opp.setObjectName("comboBox_opp_script_" + str(self.scriptNum))
            _comboBox_opp.addItem("")
            _comboBox_opp.addItem("")
            _comboBox_opp.addItem("")
            _horizontalLayout_12.addWidget(_comboBox_opp)
            horizontalLayout_script.append(_comboBox_opp)
            _verticalLayout_6.addLayout(_horizontalLayout_12)
            _spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            _horizontalLayout_12.addItem(_spacerItem10)
            _verticalLayout_6.addLayout(_horizontalLayout_12)
            _horizontalLayout_18 = QtWidgets.QHBoxLayout()
            _horizontalLayout_18.setObjectName("horizontalLayout_18_script_" + str(self.scriptNum))
            horizontalLayout_script.append(_horizontalLayout_18)
            _label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            font = QFont()
            font.setPointSize(12)
            _label_17.setFont(font)
            _label_17.setObjectName("label_17_script_" + str(self.scriptNum))
            _horizontalLayout_18.addWidget(_label_17)
            horizontalLayout_script.append(_label_17)
            _lineEdit_script = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
            _lineEdit_script.setObjectName("lineEdit_script_" + str(self.scriptNum))
            _horizontalLayout_18.addWidget(_lineEdit_script)
            horizontalLayout_script.append(_lineEdit_script)
            _verticalLayout_6.addLayout(_horizontalLayout_18)
            _horizontalLayout_17 = QtWidgets.QHBoxLayout()
            _horizontalLayout_17.setObjectName("horizontalLayout_17_script_" + str(self.scriptNum))
            horizontalLayout_script.append(_horizontalLayout_17)
            _label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            font = QFont()
            font.setPointSize(12)
            _label_18.setFont(font)
            _label_18.setObjectName("label_18_" + str(self.scriptNum))
            _horizontalLayout_17.addWidget(_label_18)
            horizontalLayout_script.append(_label_18)
            _lineEdit_re = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
            _lineEdit_re.setObjectName("lineEdit_re_" + str(self.scriptNum))
            _horizontalLayout_17.addWidget(_lineEdit_re)
            horizontalLayout_script.append(_lineEdit_re)
            _verticalLayout_6.addLayout(_horizontalLayout_17)
            _horizontalLayout_20.addLayout(_verticalLayout_6)
            self.gridLayout_12.addLayout(_horizontalLayout_20, self.scriptNum, 0, 1, 1)
            horizontalLayout_script.append({'baudbit': 115200, 'user': 'root', 'passwd': 'nE7jA%5m'})
            self.horizontalLayout_script_List[key] = horizontalLayout_script

            _pushButton_script_del.setText(self.translate("MainWindow", "-"))
            _label_index.setText(self.translate("MainWindow", str(self.scriptNum)))
            _label_16.setText(self.translate("MainWindow", "Protocol:"))
            _comboBox_script_pro.setItemText(0, self.translate("MainWindow", "SSH2"))
            _comboBox_script_pro.setItemText(1, self.translate("MainWindow", "SERIAL"))
            _comboBox_script_pro.setItemText(2, self.translate("MainWindow", "TELNET"))
            _label_pro_ip.setText(self.translate("MainWindow", "IP:"))
            self.setSerialList(_comboBox_serial, self.serList)
            _label_13.setText(self.translate("MainWindow", "运行:"))
            _comboBox_opp.setItemText(0, self.translate("MainWindow", "测试后"))
            _comboBox_opp.setItemText(1, self.translate("MainWindow", "测试中"))
            _comboBox_opp.setItemText(2, self.translate("MainWindow", "测试前"))
            _pushButton_script_more.setText(self.translate("MainWindow", "..."))
            _label_17.setText(self.translate("MainWindow", "运行脚本:"))
            _label_18.setText(self.translate("MainWindow", "结果匹配(正则表达式):"))

            self.scriptNum += 1
            self.scriptKey += 1

    def on_pushButton_script_del_clicked(self, key):
        horizontalLayout_script = self.horizontalLayout_script_List[key]
        for item in horizontalLayout_script[:-1]:
            item.setParent(None)
        self.gridLayout_12.removeItem(horizontalLayout_script[0])
        self.horizontalLayout_script_List.pop(key)
        sip.delete(horizontalLayout_script[0])
        del horizontalLayout_script

        if self.scriptNum > 1:
            self.scriptNum -= 1

    def isSelectSer(self):
        if "SERIAL" in self.comboBox_script_pro.currentText():
            return True

        for i in self.horizontalLayout_script_List:
           if "SERIAL" in self.horizontalLayout_script_List[i][7].currentText():
               return True
        return False

    @pyqtSlot(str)
    def on_comboBox_script_pro_activated(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        if "SSH" in p0 or "TELNET" in p0:
            self.lineEdit_script_ip.setHidden(False)
            self.comboBox_serial.setHidden(True)
            self.label_pro_ip.setText(self.translate("MainWindow", "IP:"))
        elif "SERIAL" in p0:
            self.lineEdit_script_ip.setHidden(True)
            self.comboBox_serial.setHidden(False)
            self.label_pro_ip.setText(self.translate("MainWindow", "COM:"))

        if self.isSelectSer():
            self.pushButton_refresh.setHidden(False)
        else:
            self.pushButton_refresh.setHidden(True)

    def on__comboBox_script_pro_activated(self, key):
        horizontalLayout_script = self.horizontalLayout_script_List[key]
        p0 = horizontalLayout_script[7].currentText()

        if "SSH" in p0 or "TELNET" in p0:
            horizontalLayout_script[8].setText(self.translate("MainWindow", "IP:"))
            horizontalLayout_script[9].setHidden(False)
            horizontalLayout_script[10].setHidden(True)
        elif "SERIAL" in p0:
            horizontalLayout_script[8].setText(self.translate("MainWindow", "COM:"))
            horizontalLayout_script[9].setHidden(True)
            horizontalLayout_script[10].setHidden(False)

        if self.isSelectSer():
            self.pushButton_refresh.setHidden(False)
        else:
            self.pushButton_refresh.setHidden(True)

    def setSerialList(self, comboBox, serList):
        i = 0
        comboBox.clear()
        for ser in serList:
            plist_0 = list(ser)
            comboBox.addItem('')
            comboBox.setItemText(i, self.translate("MainWindow", plist_0[0]))
            i += 1

    @pyqtSlot()
    def on_pushButton_refresh_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.serList = list(serial.tools.list_ports.comports())
        if len(self.serList) <= 0:
            # print("The Serial port can't find!")
            # self.label_error_t("未找到可用串口")
            return
        self.setSerialList(self.comboBox_serial, self.serList)
        for i in self.horizontalLayout_script_List:
            self.setSerialList(self.horizontalLayout_script_List[i][10], self.serList)
    
    @pyqtSlot()
    def on_pushButton_script_more_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.more = Dialog()
        self.more.signal_param.connect(self.receiveDialog)
        self.more.setAttribute(Qt.WA_DeleteOnClose, False)
        # self.more.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.more.setModal(True)
        self.more.setKey('0')
        if "SERIAL" not in self.comboBox_script_pro.currentText():
            self.more.widget.setHidden(True)
        self.more.show()

    def on__pushButton_script_more_clicked(self, key):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.more = Dialog()
        self.more.signal_param.connect(self.receiveDialog)
        self.more.setAttribute(Qt.WA_DeleteOnClose, False)
        self.more.setModal(True)
        self.more.setKey(key)
        if "SERIAL" not in self.horizontalLayout_script_List[key][7].currentText():
            self.more.widget.setHidden(True)
        self.more.show()

    def receiveDialog(self, args):
        if self.horizontalLayout_script_List.get(args[0]):
            self.horizontalLayout_script_List[args[0]][-1]['baudbit'] = args[1]
            self.horizontalLayout_script_List[args[0]][-1]['user'] = args[2]
            self.horizontalLayout_script_List[args[0]][-1]['passwd'] = args[3]



class ThroughputThread(QThread):

    signal_result = pyqtSignal(tuple)

    def __init__(self, tbWidget, parent=None):
        super(ThroughputThread, self).__init__(parent)
        self.tbWidget = tbWidget
        self.stopBool = False
        self.cmd = ''
        self.iperfVer = 2
        self.pResult = False

    def setParam(self, iperfVer, c_ip, param, tTime, tDTh):
        self.iperfVer = iperfVer
        self.c_ip = c_ip
        self.param = param
        self.tTime = tTime
        self.tDTh = tDTh
        if " -P " in self.cmd:
            self.pResult = True
        else:
            self.pResult = False

    def run(self):
        if not getLinkState(self.c_ip):
            self.signal_result.emit(("ping fail",))
            return
        self.param = ' -c ' + self.c_ip + self.param
        if self.iperfVer == '2':
            self.param = 'iperf ' + self.param
        elif self.iperfVer == '2':
            self.param = 'iperf3 ' + self.param
        else:
            self.signal_result.emit(("fail",))
            return

        self.tDTh.setTime(self.tTime)
        self.stopBool = False

        self.tDTh.start()
        print(os.getcwd() + '\\iperf\\' + self.param)
        self.process = subprocess.Popen(os.getcwd() + '\\iperf\\' + self.param,
                                        stdin=subprocess.PIPE,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE,
                                        shell=True)
        self.signal_result.emit(("testing",))
        self.tbWidget.append("testing")

        if self.iperfVer == 2:
            self.getIperfResult()
        elif self.iperfVer == 3:
            self.getIperf3Result()

        self.tDTh.stop()

    def stop(self):
        self.stopBool = True
        self.tDTh.stop()

    def close(self):
        self.stopBool = True
        self.tDTh.stop()
        self.process = subprocess.Popen("taskkill /f /im iperf*",
                                        stdin=subprocess.PIPE,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE,
                                        shell=True)

    def getIperfResult(self):
        tmp = ''
        while not self.stopBool:
            out = str(self.process.stdout.readline(), encoding="gb2312", errors="ignore")
            self.tbWidget.append(out)
            if not out:
                break
            elif "read failed" in out or "connect failed" in out \
                    or "WARNING: did not receive ack of last datagram after 10 tries" in out:
                self.close()
                self.signal_result.emit(("connect fail",))
                return

            if "0.0-"+str(self.tTime)+'.' in out:
                if self.pResult and "[SUM]" in out:
                    tmp = out
                elif not self.pResult:
                    tmp = out
        print("tmp", tmp)
        result = None
        if "0.0-"+str(self.tTime)+'.' in tmp:
            result = re.findall(r'[\d.]* \w*/sec', tmp)[0].split(' ')[0]
            self.signal_result.emit(("result", result))
        else:
            self.signal_result.emit(("fail",))

    def getIperf3Result(self):
        tmp = []
        while not self.stopBool:
            out = str(self.process.stdout.readline(), encoding="gb2312", errors="ignore")
            self.tbWidget.append(out)
            if not out:
                break
            elif "read failed" in out or "connect failed" in out \
                    or "WARNING: did not receive ack of last datagram after 10 tries" in out \
                    or "iperf3: error" in out:
                self.close()
                self.signal_result.emit(("connect fail",))
                return
            elif "0.00-"+str(self.tTime)+'.' in out:
                if self.pResult and "[SUM]" in out:
                    tmp.append(out)
                elif not self.pResult:
                    tmp.append(out)
        print("tmp", tmp)
        sender = None
        receiver = None
        for line in tmp:
            if "sender" in line:
                sender = re.findall(r'[\d.]* \w*/sec', line)[0].split(' ')[0]
            elif "receiver" in line:
                receiver = re.findall(r'[\d.]* \w*/sec', line)[0].split(' ')[0]
        self.signal_result.emit(("result", sender, receiver))

class TimeDownThread(QThread):

    signal_Time = pyqtSignal(int)

    def __init__(self, parent=None):
        super(TimeDownThread, self).__init__(parent)
        self.stopBool = False
        self.tTime = 0
        self.intervalTime = 1

    def setTime(self, p0, inTime=1):
        self.tTime = p0
        self.intervalTime = inTime

    def run(self):
        # print("倒计时开始")
        self.stopBool = False
        tempTime = self.intervalTime - 0.01
        self.signal_Time.emit(self.tTime)
        while not self.stopBool and self.tTime > 0:
            time.sleep(tempTime)
            self.tTime = self.tTime - self.intervalTime
            self.signal_Time.emit(self.tTime)

    def stop(self):
        self.stopBool = True

class ScriptThread(QThread):

    signal_sRes = pyqtSignal(tuple)
    signal_index = pyqtSignal()

    def __init__(self, c_time, args, parent=None):
        """
        :param args: [index, opp, proMode, [ip|serial, baudrate], script, re]
        :param c_time:
        :param parent:
        """
        super(ScriptThread, self).__init__(parent)
        self.stopBool = False
        self.args = args
        self.c_time = c_time
        self.opp = ["测试前", "测试中", "测试后"]

    def run(self):
        self.stopBool = False
        i = 0
        while not self.stopBool and i < 3:
            index = 0
            for arg in self.args:
                print('arg ', arg)
                if arg[0] == self.opp[i]:
                    if "SSH" in arg[1]:
                        s = threading.Thread(runSSH, args=(self.signal_sRes, self.signal_index, index, arg[0], arg[2], arg[-1][1], arg[-1][2], arg[3], arg[4]))
                        s.start()
                    elif "TELNET" in arg[1]:
                        tl = threading.Thread(self.runTelnet, args=(index, arg[0], arg[2], arg[-1][1], arg[-1][2], arg[3], arg[4]))
                        tl.start()
                    elif "SERIAL" in arg[1]:
                        ser = threading.Thread(self.runSerial, args=(index, arg[0], arg[3], arg[-1][0], arg[-1][1], arg[-1][2], arg[4], arg[5]))
                        ser.start()
                    else:
                        pass
                index += 0


            time.sleep(self.c_time/2)
            i += 1

    def stop(self):
        self.stopBool = True

    def runSerial(self, index, opp, com, bitNum, user, passwd, cmd, res_re):
        print("run serial")
        if not cmd:
            self.signal_sRes.emit((index, 'Fail', ''))
        else:
            ser = Serial()
            try:
                ser.connect(com, bitNum)
                ser.auth('root', 'nE7jA%5m')
                ser.write(cmd)
                out = ser.read()
                p = re.findall(res_re, out)
                self.signal_sRes.emit((index, 'success', p))
            except Exception as e:
                print(e)
                self.signal_sRes.emit((index, 'Fail', ''))
        if "运行前" in opp:
            self.signal_index.emit()


    def runTelnet(self, index, opp, ip, user, passwd, cmd, res_re):
        print("run telnet")
        if cmd:
            pass
        else:
            self.signal_sRes.emit((index, 'Fail', ''))

        if "运行前" in opp:
            self.signal_index.emit()


def runSSH(signal_sRes, signal_index, index, opp, ip, user, passwd, cmd, res_re):
    print("run SSH")
    if cmd:
        pass
    else:
        signal_sRes.emit((index, 'Fail', ''))

    if "运行前" in opp:
        signal_index.emit()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
    
