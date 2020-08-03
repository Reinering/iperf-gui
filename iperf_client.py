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
import os, sys
import datetime, time
import re, decimal
import serial, serial.tools.list_ports
from rn_common.ssh import SSH
from rn_common.serial import Serial
from rn_common.telnet import Telnet
from rn_common.netTools import getLinkState
from Ui_iperf_client import Ui_MainWindow
from script_more import Dialog
import logging
from collections import deque
import requests
import json

OPTION = (('-f', '-i', '-l', '-m', '-o', '-p', '-u', '-w', '-B', '-C', '-M', '-N', '-V'),
          ('-s', '-D', '-R'),
          ('-b', '-c', '-d', '-n', '-r', '-t', '-F', '-I', '-L', '-P', '-T'),
          )
OPTION3 = (('-p', '-f', '-i', '-F', '-B', '-V', '-J', '--logfile', '-d', '-v', '-h'),
           ('-s', '-D', '-I', '-l'),
           ('-c', '-u', '-b', '-t', '-n', '-k', '-l', '--cport', '-P', '-R', '-w', '-M', '-N', '-4', '-6', '-S', '-Z', '-O', '-T', '--get-server-output', '--udp-counters-64bit'),
           )


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
        self.stopBool = False
        self.cc_state = False
        self.save_state = False
        self.filePath = ''
        self.iperfVer = '2'
        self.protocol = "TCP"
        self.throughputdTh = ThroughputThread()
        self.throughputdTh.signal_result.connect(self.setThroughputResult)
        self.throughputdTh.signal_tb.connect(self.appendTB)
        self.tDTh = TimeDownThread()
        self.tDTh.signal_Time.connect(self.setTimeDown)
        self.cctdTh = TimeDownThread()
        self.cctdTh.signal_TimeOver.connect(self.recieveIntervCC)
        self.cCount = 0
        self.total = 0
        self.failTotal = 0
        self.rowCount = 0
        self.rowC2 = 0
        self.rowC3 = 0
        self.isScript = False
        self.isReport = False
        self.scriptNum = 1
        self.scriptKey = 0
        self.isScrollDown = False
        self.horizontalLayout_script_List = {}
        self.serList = []
        self.initWidget()

    def initWidget(self):
        self.tabWidget.setTabEnabled(3, False)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.textBrowser_v3.hide()
        self.widget_iperf3.hide()
        self.label_countDown.setText('0')
        self.pushButton_s.setEnabled(False)
        self.spinBox_time.setValue(60)
        self.comboBox_serial.setHidden(True)
        self.pushButton_refresh.setHidden(True)
        self.scrollArea.setEnabled(False)
        self.horizontalLayout_script_List['0'] = [self.horizontalLayout_20, self.verticalLayout_7, self.pushButton_script_add, self.label_index,
                                                  self.verticalLayout_6, self.horizontalLayout_12, self.label_16, self.comboBox_script_pro, self.label_pro_ip,
                                                  self.lineEdit_script_ip, self.comboBox_serial, self.pushButton_script_more, self.label_13, self.comboBox_opp,
                                                  self.horizontalLayout_18, self.label_17, self.lineEdit_script, self.horizontalLayout_17, self.label_18,
                                                  self.lineEdit_re, {'baudbit': 115200, 'user': 'root', 'passwd': 'nE7jA%5m'}]
        self.tableWidget_ver2.setColumnHidden(4, True)
        self.tableWidget_ver2.setColumnHidden(5, True)
        self.tableWidget_ver2.setColumnHidden(6, True)
        self.tableWidget_ver2.setColumnWidth(0, 60)
        self.tableWidget_ver2.setColumnWidth(1, 120)
        self.tableWidget_ver2.setColumnWidth(2, 40)
        self.tableWidget_ver2.setColumnWidth(3, 60)
        self.tableWidget_ver2.setColumnWidth(4, 120)
        self.tableWidget_ver2.setColumnWidth(5, 40)
        self.tableWidget_ver2.setColumnWidth(6, 60)
        self.tableWidget_ver2.setColumnWidth(7, 70)
        self.tableWidget_ver2.setColumnWidth(8, 120)
        self.tableWidget_ver2.setColumnWidth(9, 50)
        self.tableWidget_ver3.setColumnWidth(0, 60)
        self.tableWidget_ver3.setColumnWidth(1, 60)
        self.tableWidget_ver3.setColumnWidth(2, 60)
        self.tableWidget_ver3.setColumnWidth(3, 40)
        self.tableWidget_ver3.setColumnWidth(4, 60)
        self.tableWidget_ver3.setColumnWidth(5, 70)
        self.tableWidget_ver3.setColumnWidth(6, 120)
        self.tableWidget_ver3.setColumnWidth(7, 50)


        self.label_count = QLabel()
        font = QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_count.setFont(font)
        self.label_count.setObjectName("label_count")
        self.statusBar.addPermanentWidget(self.label_count)
        self.on_pushButton_refresh_clicked()
        self.statusBar.showMessage('Ready')

        self.lineEdit_c_ip.setText("192.168.1.81")
        self.lineEdit_c_ip.setText("192.168.188.251")
        self.lineEdit_script.setText("cat /proc/version")
        self.lineEdit_re.setText("r'[\d]*\.[\d]*\.[\d]*|[\w]*@jenkins|PREEMPT [\w: ]*'")

    def setTabState(self, checked):
        self.tabWidget.setTabEnabled(1, checked)
        self.tabWidget.setTabEnabled(2, checked)
        # self.tabWidget.setTabEnabled(3, checked)
        self.groupBox_test.setEnabled(checked)

    def setTimeDown(self, p0):
        self.label_countDown.setText(str(p0) + ' s')

    def updateStatusBar(self):
        self.label_count.setText('共计：{}次  成功：{}次  失败：{}次'.format(self.total, self.total-self.failTotal, self.failTotal))

    def addInfo(self, tableWidget, args):
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
        tableWidget.scrollToBottom()

    def addTableWidgetEntry(self, x, y, p0, tbWidget):
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        # tableWidget禁止编辑
        # if x == 1 and self.iperfVer == '2':
        #     item.setFlags(Qt.ItemIsEditable)
        # elif x == 2 and self.iperfVer == '3':
        #     item.setFlags(Qt.ItemIsEditable)
        # else:
        #     pass
        item.setText(self.translate("MainWindow", p0))
        # item.setFont(self.setCellFont())
        tbWidget.setItem(x, y, item)

    def clearTableWidgetEntry(self, tbWidget):
        row = tbWidget.rowCount()
        for i in range(row):
            tbWidget.removeRow(0)

    def setScriptResult(self, p0):
        if "script" == p0[0]:
            print("script", p0[1])
            self.scriptRes.append(p0[1])
        else:
            pass

    def setThroughputResult(self, p0):
        print("result", p0)
        if not p0:
            print("吞吐量测试, 错误返回值")
        elif "testing" == p0[0]:
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
        elif "report" == p0[0]:
            pass
        elif "result" == p0[0]:
            if p0[1]:
                result = p0[2]
                self.label_error.setText(self.translate("GeneralWindow", "吞吐量测试已完成"))
                if self.iperfVer == "3":
                    if self.protocol == "UDP":
                        pass
                    self.label_res_tx.setText(self.translate("GeneralWindow", result["tx"] + ' ' + result["unit"]))
                    self.label_res_rx.setText(self.translate("GeneralWindow", result["rx"] + ' ' + result["unit"]))
                    self.addInfo(self.tableWidget_ver3, (result["proto"], result["tx"], result["rx"], result["loss"], result["delay"], result["direct"], result["time"], ""))
                    if self.save_state:
                        self.excelTh.setParam(self.filePath, 'iperf3', self.rowC3, result)
                        self.excelTh.start()
                        self.rowC3 += 1
                else:
                    if self.protocol == "UDP":
                        pass
                    self.label_res_th.setText(self.translate("GeneralWindow", result["throughput"] + ' ' + result["unit"]))
                    self.addInfo(self.tableWidget_ver2, (result["proto"], result["throughput"], result["loss"], result["delay"], result["direct"], result["time"], ""))
                    if self.save_state:
                        self.excelTh.setParam(self.filePath, 'iperf', self.rowC2, result)
                        self.excelTh.start()
                        self.rowC2 += 1
                if self.isReport:
                    if self.isScript:
                        count = 0
                        while count < 5:
                            if self.scriptRunNum[0] + self.scriptRunNum[1] + self.scriptRunNum[2] == len(self.args):
                                break
                            time.sleep(1)
                            count += 1
                        self.reportTh.setData({"task": self.lineEdit_task.text(), "throughput": result, "script": self.scriptRes, })
                    else:
                        self.reportTh.setData({"task": self.lineEdit_task.text(), "throughput": result, "script": []})
                    self.reportTh.start()
            else:
                self.failTotal += 1
                self.label_error.setText(self.translate("GeneralWindow", "吞吐量测试， 测试失败，未获取到测试结果"))

        self.total += 1
        self.statusBar.showMessage('Stop')
        self.cCount -= 1
        if self.cCount > 0 and not self.stopBool:
            self.label_count.setText('(循环剩余：{}次)  共计：{}次  成功：{}次  失败：{}次'.format(self.cCount, self.total, self.total-self.failTotal, self.failTotal))
            print("循环等待中", self.cCount)
            self.label_error.setText("等待中...")
            cInterval = self.spinBox_cInterval.value()
            if cInterval < 5 and not self.stopBool:
                self.cctdTh.setTime(5, 0)
            else:
                self.cctdTh.setTime(self.spinBox_cInterval.value(), 0)
            self.cctdTh.start()
        else:
            self.label_count.setText('共计：{}次  成功：{}次  失败：{}次'.format(self.total, self.total-self.failTotal, self.failTotal))
            self.setTabState(True)
            self.pushButton_a.setEnabled(True)
            self.pushButton_s.setEnabled(False)
            self.statusBar.showMessage('Finish', 5000)
            self.stopBool = True
            if not self.checkBox_lock.isChecked():
                text = self.lineEdit_task.text()
                tmp = text.split('_')
                if len(tmp) <= 1:
                    self.lineEdit_task.setText(tmp[0] + '_1')
                else:
                    try:
                        self.lineEdit_task.setText(text.replace(tmp[-1], str(int(tmp[-1]) + 1)))
                    except Exception as e:
                        print(e)
                        self.lineEdit_task.setText(text + '_1')

    def recieveIntervCC(self, p0):
        if not self.stopBool:
            if self.isScript:
                self.scriptRunNum.clear()
                self.scriptTh.start()
                if self.waitNum == 0:
                    self.throughputdTh.start()
                    self.statusBar.showMessage('Start')
            else:
                self.throughputdTh.start()
                self.statusBar.showMessage('Start')
                if self.iperfVer == "2":
                    self.label_res_th.clear()
                elif self.iperfVer == "3":
                    self.label_res_rx.clear()
                    self.label_res_tx.clear()

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

    def runThrouTh(self, p0):
        print("STARTING")

        try:
            self.scriptRunNum[p0] += 1
        except Exception as e:
            print(e)

        if self.scriptRunNum[0] == self.waitNum:
            self.throughputdTh.start()

    def appendTB(self, p0):
        if type(p0) == str:
            self.textBrowser.append(p0)

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
        if checked:
            self.excelTh = ExcelThread()
        else:
            del self.excelTh

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
            self.textBrowser_v2.show()
            self.textBrowser_v3.hide()
            item = QTableWidgetItem()
            item.setText(self.translate("MainWindow", "Throughput/Mbps"))
            self.stackedWidget.setCurrentIndex(0)
        elif p0 == '3':
            self.widget_iperf2.hide()
            self.widget_iperf3.show()
            self.textBrowser_v2.hide()
            self.textBrowser_v3.show()
            item = QTableWidgetItem()
            item.setText(self.translate("MainWindow", "Tx/Mbps"))
            item = QTableWidgetItem()
            item.setText(self.translate("MainWindow", "Rx/Mpbs"))
            self.stackedWidget.setCurrentIndex(1)
        else:
            pass

    @pyqtSlot(str)
    def on_comboBox_pro_activated(self, p0):
        """
        Slot documentation goes here.

        @param p0 DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.protocol = p0
        # c_param = self.lineEdit_c_param.text()
        if p0 == 'UDP':
            self.tableWidget_ver2.setColumnHidden(4, False)
            self.tableWidget_ver2.setColumnHidden(5, False)
            self.tableWidget_ver2.setColumnHidden(6, False)
            self.lineEdit_c_param.setText("-i 1")
        else:
            self.lineEdit_c_param.setText("-i 1")
            self.tableWidget_ver2.setColumnHidden(4, True)
            self.tableWidget_ver2.setColumnHidden(5, True)
            self.tableWidget_ver2.setColumnHidden(6, True)
            self.lineEdit_c_param.setText("-l 1024 -i 1")

    @pyqtSlot()
    def on_pushButton_a_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        logging.info("start")
        self.stopBool = False
        self.label_error.clear()
        if self.iperfVer == "2":
            self.label_res_th.clear()
        elif self.iperfVer == "3":
            self.label_res_rx.clear()
            self.label_res_tx.clear()

        pro = self.comboBox_pro.currentText()
        c_ip = self.lineEdit_c_ip.text()
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
        if c_p > 1 and ' -P' not in c_param:
            c_param = c_param + ' -P ' + str(self.spinBox_p.value())
        self.throughputdTh.setParam(self.iperfVer, c_ip, c_param, c_time, self.tDTh)

        if self.checkBox_cc.isChecked():
            self.cCount = self.spinBox_cCount.value()

        if self.isReport:
            ipPort = self.lineEdit_report_ip.text()
            if not ipPort:
                self.label_error_t.setText("结果上报：IP:PORT不能为空")
                return
            uri = self.comboBox_report_uri.currentText()
            if not uri:
                uri = '/'
            self.reportTh.setParam(self.iperfVer, self.comboBox_report_proto.currentText(), self.comboBox_report_method.currentText(), ipPort, uri, self.comboBox_report_formart.currentText())

        if self.isScript:
            self.scriptRunNum.clear()
            self.args, self.waitNum = self.getScriptArgs()
            self.scriptTh = ScriptThread(c_time, self.args)
            self.scriptTh.signal_index.connect(self.runThrouTh)
            self.scriptTh.signal_sRes.connect(self.setScriptResult)
            self.scriptTh.signal_tb.connect(self.appendTB)
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
        logging.info("stop...")
        self.stopBool = True
        try:
            self.throughputdTh.close()
            if self.checkBox_cc.isChecked():
                self.cCount = 0
                self.cctdTh.stop()
            if self.isScript:
                self.scriptTh.stop()
            self.label_error.setText("已停止")
        except Exception as e:
            print(e)
            logging.error(e)

        self.statusBar.showMessage('Stop')
        self.setTabState(True)
        self.pushButton_a.setEnabled(True)
        self.pushButton_s.setEnabled(False)

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
            self.rowC2 = 0
            self.rowC3 = 0
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
        c_param = self.lineEdit_c_param.text()
        if self.iperfVer == '2':
            self.label_res_th.clear()
            for p in OPTION[1]:
                if p in c_param and not OPTION[0].count(p)and not OPTION[2].count(p):
                    self.label_error_c.setText("参数填写错误")
        elif self.iperfVer == '3':
            self.label_res_rx.clear()
            self.label_res_tx.clear()
            for p in OPTION3[1]:
                if p in c_param and not OPTION3[0].count(p) and not OPTION3[2].count(p):
                    self.label_error_c.setText("参数填写错误")
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
        if checked:
            self.scriptRes = []
            self.scriptRunNum = []
    
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
    
    @pyqtSlot()
    def on_textBrowser_textChanged(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        QApplication.processEvents()
        if self.isScrollDown:
            self.textBrowser.moveCursor(self.textBrowser.textCursor().End)

    @pyqtSlot(bool)
    def on_checkBox_report_clicked(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.groupBox_report.setEnabled(checked)
        self.isReport = checked
        if checked:
            self.reportTh = ReportThread()
            # self.reportTh.signal_result.connect(self.setThroughputResult)
            self.reportTh.signal_tb.connect(self.appendTB)
        else:
            try:
                del self.reportTh
            except Exception as e:
                print(e)

    @pyqtSlot()
    def on_lineEdit_report_ip_editingFinished(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.label_error_t.clear()
        r_ip = self.lineEdit_report_ip.text()
        if r_ip == '':
            return
        if not re.match(r'^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}:(?:[1-9]\d{1,3}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])$', r_ip):
            self.label_error_t.setText("IP:PORT地址格式错误，请重新输入")
            return
    
    @pyqtSlot(bool)
    def on_checkBox_lock_clicked(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        if checked:
            self.lineEdit_task.setEnabled(False)
        else:
            self.lineEdit_task.setEnabled(True)



class ThroughputThread(QThread):

    signal_result = pyqtSignal(tuple)
    signal_tb = pyqtSignal(str)

    def __init__(self, parent=None):
        super(ThroughputThread, self).__init__(parent)
        self.stopBool = False
        self.cmd = ''
        self.iperfVer = "2"
        self.pResult = False
        self.maxlen = 10

    def setParam(self, iperfVer, c_ip, param, tTime, tDTh):
        self.iperfVer = iperfVer
        self.c_ip = c_ip
        self.param = param
        self.tTime = tTime
        self.tDTh = tDTh
        # self.tDTh.signal_TimeOver.connect(self.timeOver)

        p = re.findall(r'-P[ ]?([\d])+', param)
        if p:
            p = int(p[0])
            if p < 5:
                self.maxlen = 10
            else:
                self.maxlen = 2*p

    def timeOver(self, p0):
        if p0 == "stop":
            if ' -d' in self.param and not self.stopBool:
                self.close()
                return
            if not self.stopBool:
                self.close()
                # self.signal_result.emit(("fail",))

    def run(self):

        if not getLinkState(self.c_ip):
            self.signal_result.emit(("ping fail",))
            return
        paramTemp = ' -c ' + self.c_ip + ' ' + self.param + ' -t ' + str(self.tTime)
        if self.iperfVer == '2':
            paramTemp = 'iperf ' + paramTemp
        elif self.iperfVer == '3':
            paramTemp = 'iperf3 ' + paramTemp
        else:
            self.signal_result.emit(("fail",))
            return

        self.tDTh.setTime(self.tTime)
        self.stopBool = False

        self.tDTh.start()
        tmp = sys.argv[0]
        cmd = tmp.replace(tmp.split('\\')[-1], 'iperf\\' + paramTemp)
        # print(os.getcwd() + '\\iperf\\' + paramTemp)
        print(cmd)
        self.process = subprocess.Popen(cmd,
                                        stdin=subprocess.PIPE,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE,
                                        shell=True)
        self.signal_result.emit(("testing",))
        self.signal_tb.emit("Testing")

        if self.iperfVer == "2":
            self.getIperfResult()
        elif self.iperfVer == "3":
            self.getIperf3Result()

        self.tDTh.stop()
        self.stopBool = True

    def stop(self):
        self.stopBool = True
        self.tDTh.stop()

    def close(self):
        self.stopBool = True
        self.tDTh.stop()
        self.process = subprocess.Popen('taskkill /f /fi "imagename eq iperf* " /fi "imagename ne iperf_client*"',
                                        stdin=subprocess.PIPE,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE,
                                        shell=True)

    def getIperfResult(self):
        lines = deque(maxlen=self.maxlen)
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = {"iperfVer": 2, "proto": "", "throughput": "", "unit": "Mbps", "loss": "", "delay": "", "direct": "down", "time": now, }
        if "-R" in self.param:
            result["direct"] = "up"
        resBool = False
        while not self.stopBool:
            out = str(self.process.stdout.readline(), encoding="gb2312", errors="ignore")
            print("out:", out)
            if not out:
                break
            elif "read failed" in out or "connect failed" in out \
                    or "iperf: ignoring extra argument" in out \
                    or "write failed: Connection reset by peer" in out \
                    or "write failed: Software caused connection abort" in out \
                    or "recvfrom failed: Interrupted function call" in out \
                    or "read failed: Message too long" in out:
                self.signal_result.emit(("connect fail",))
                self.close()
                return
            else:
                lines.append(out)
            self.signal_tb.emit(out)

        if ' -u ' in self.param and ' -P' in self.param:
            result["proto"] = "udp"
            tag = False
            for line in lines:
                if 'Server Report:' in line:
                    tag = True
                elif "0.0-"+str(self.tTime)+'.' in line and tag:
                    tmp = re.findall(r'[\d.]* \w*/sec|[\d.]* \w*ms|[\d]*%', line)
                    tag = False
                    if len(result) == 3:
                        result["loss"] = tmp[2].split(' ')[0]
                    if len(result) >= 2:
                        result["delay"] = tmp[1].split(' ')[0]
                    if len(result) >= 1:
                        result["throughput"] = tmp[0].split(' ')[0]
                    resBool = True
                elif "[SUM]" in line and "0.0-"+str(self.tTime)+'.' in line:
                    tmp = re.findall(r'[\d.]* \w*/sec|[\d.]* \w*ms|[\d]*%', line)
                    if len(result) == 3:
                        result["loss"] = tmp[2].split(' ')[0]
                    if len(result) >= 2:
                        result["delay"] = tmp[1].split(' ')[0]
                    if len(result) >= 1:
                        result["throughput"] = tmp[0].split(' ')[0]
                    resBool = True
                else:
                    pass

        elif ' -u ' in self.param:
            result["proto"] = "udp"
            tag = False
            for line in lines:
                if 'Server Report:' in line:
                    tag = True
                elif "0.0-"+str(self.tTime)+'.' in line:
                    if tag:
                        tmp = re.findall(r'[\d.]* \w*/sec|[\d.]* \w*ms|[\d]*%', line)
                        tag = False
                        if len(result) == 3:
                            result["loss"] = tmp[2].split(' ')[0]
                        if len(result) >= 2:
                            result["delay"] = tmp[1].split(' ')[0]
                        if len(result) >= 1:
                            result["throughput"] = tmp[0].split(' ')[0]
                        resBool = True
                    else:
                        tmp = re.findall(r'[\d.]* \w*/sec|[\d.]* \w*ms|[\d]*%', line)
                        if len(result) == 3:
                            result["loss"] = tmp[2].split(' ')[0]
                        if len(result) >= 2:
                            result["delay"] = tmp[1].split(' ')[0]
                        if len(result) >= 1:
                            result["throughput"] = tmp[0].split(' ')[0]
                        resBool = True
                else:
                    pass
        elif ' -P' in self.param:
            result["proto"] = "tcp"
            for line in lines:
                if "[SUM]" in "0.0-"+str(self.tTime)+'.' in line:
                    result["throughput"] = re.findall(r'([\d.]*) \w*/sec', line)[0]
                    resBool = True
        else:
            result["proto"] = "tcp"
            for line in lines:
                if "0.0-"+str(self.tTime)+'.' in line:
                    result["throughput"] = re.findall(r'([\d.]*) \w*/sec', line)[0]
                    resBool = True

        self.signal_result.emit(("result", resBool, result))

    def getIperf3Result(self):
        lines = deque(maxlen=self.maxlen)
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = {"iperfVer": "3", "proto": "", "rx": "", "tx": "", "unit": "Mbps", "loss": "", "delay": "", "direct": "up", "time": now, }
        if "-R" in self.param:
            result["direct"] = "down"
        resBool = False
        while not self.stopBool:
            out = str(self.process.stdout.readline(), encoding="gb2312", errors="ignore")
            # print("out:", out)
            if not out:
                break
            elif "read failed" in out or "connect failed" in out \
                    or "iperf3: error" in out:
                self.close()
                self.signal_result.emit(("connect fail",))
                return
            else:
                lines.append(out)
            self.signal_tb.emit(out)
            self.process.stdout.flush()
        if ' -u ' in self.param and ' -P' in self.param:
            result["proto"] = "udp"
            for line in lines:
                if "[SUM]" in line and "sender" in line and "0.00-"+str(self.tTime)+'.' in line:
                    result["tx"] = re.findall(r'[\d.]* \w*/sec', line)[0].split(' ')[0]
                    resBool = True
                elif "[SUM]" in line and "receiver" in line and "0.00-"+str(self.tTime)+'.' in line:
                    result["rx"] = re.findall(r'[\d.]* \w*/sec', line)[0].split(' ')[0]
                    resBool = True
        elif ' -u ' in self.param:
            result["proto"] = "udp"
            for line in lines:
                if "0.00-"+str(self.tTime)+'.' in line:
                    tmp = re.findall(r'[\d.]* \w*/sec|[\d.]* \w*ms|[\d]*%', line)
                    if len(result) == 3:
                        result["loss"] = tmp[2].split(' ')[0]
                    if len(result) >= 2:
                        result["delay"] = tmp[1].split(' ')[0]
                    if len(result) >= 1:
                        result["throughput"] = tmp[0].split(' ')[0]
                    resBool = True
        elif ' -P' in self.param:
            result["proto"] = "tcp"
            try:
                for line in lines:
                    if "[SUM]" in line and "sender" in line and "0.00-"+str(self.tTime)+'.' in line:
                        result["tx"] = re.findall(r'[\d.]* \w*/sec', line)[0].split(' ')[0]
                        resBool = True
                    elif "[SUM]" in line and "receiver" in line and "0.00-"+str(self.tTime)+'.' in line:
                        result["rx"] = re.findall(r'[\d.]* \w*/sec', line)[0].split(' ')[0]
                        resBool = True
            except Exception as e:
                print(e)
        else:
            result["proto"] = "tcp"
            for line in lines:
                if "sender" in line and "0.00-"+str(self.tTime)+'.' in line:
                    result["tx"] = re.findall(r'[\d.]* \w*/sec', line)[0].split(' ')[0]
                    resBool = True
                elif "receiver" in line and "0.00-"+str(self.tTime)+'.' in line:
                    result["rx"] = re.findall(r'[\d.]* \w*/sec', line)[0].split(' ')[0]
                    resBool = True

        self.signal_result.emit(("result", resBool, result))

class TimeDownThread(QThread):

    signal_Time = pyqtSignal(int)
    signal_TimeOver = pyqtSignal(str)

    def __init__(self, parent=None):
        super(TimeDownThread, self).__init__(parent)
        self.stopBool = False
        self.tTime = 0
        self.intervalTime = 1

    def setTime(self, p0, inTime=1):
        self.tTime = p0
        self.pair = 0
        self.intervalTime = inTime

    def run(self):
        print("倒计时开始")
        self.stopBool = False

        tempTime = self.intervalTime - 0.01
        self.signal_Time.emit(self.tTime)
        while not self.stopBool and self.tTime > 0:
            if tempTime > 0:
                time.sleep(tempTime)
                self.tTime = self.tTime - self.intervalTime
                self.signal_Time.emit(self.tTime)
            else:
                time.sleep(5)
                self.tTime = self.tTime - 5
        self.signal_TimeOver.emit('over')

        time.sleep(10)
        self.signal_TimeOver.emit('stop')

    def stop(self):
        self.stopBool = True

class ScriptThread(QThread):

    signal_sRes = pyqtSignal(tuple)
    signal_index = pyqtSignal(str)
    signal_tb = pyqtSignal(str)

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
        print("script start")
        self.stopBool = False
        i = 0
        while not self.stopBool and i < 3:
            index = 0
            for arg in self.args:
                # print('arg ', arg)
                if arg[0] == self.opp[i]:
                    if "SSH" in arg[1]:
                        s = threading.Thread(target=self.runSSH, args=(self.signal_sRes, self.signal_index, index, arg[0], arg[2], arg[-1]["user"], arg[-1]["passwd"], arg[4], arg[5]))
                        s.start()
                    elif "TELNET" in arg[1]:
                        tl = threading.Thread(target=self.runTelnet, args=(self.signal_sRes, self.signal_index, index, arg[0], arg[2], arg[-1]["user"], arg[-1]["passwd"], arg[3], arg[4]))
                        tl.start()
                    elif "SERIAL" in arg[1]:
                        ser = threading.Thread(target=self.runSerial, args=(self.signal_sRes, self.signal_index, index, arg[0], arg[3], arg[-1]["baudbit"], arg[-1]["user"], arg[-1]["passwd"], arg[4], arg[5]))
                        ser.start()
                    else:
                        pass
                index += 1

            time.sleep(self.c_time/2)
            i += 1

    def stop(self):
        self.stopBool = True

    def runSerial(self, signal_sRes, signal_index, index, opp, com, bitNum, user, passwd, cmd, res_re):
        print("run serial")
        if not cmd:
            self.signal_sRes.emit(("script", {"index": index, "opp": opp, "proto": "Serial", "com": com, "ip": "", "res": ""}))
        else:
            ser = Serial()
            try:
                ser.connect(com, bitNum)
                ser.auth('root', 'nE7jA%5m')
                ser.write(cmd)
                out = ser.read()
                p = re.findall(res_re, out)
                self.signal_sRes.emit(("script", {"index": index, "opp": opp, "proto": "Serial", "com": com, "ip": "", "res": p}))
            except Exception as e:
                self.signal_tb.emit("脚本执行失败：index(" + str(index) + ") 错误：" + str(e))
                logging.error(e)
                self.signal_sRes.emit(("script", {"index": index, "opp": opp, "proto": "Serial", "com": com, "ip": "", "res": ""}))
        if "运行前" == opp:
            self.signal_index.emit(0)
        elif "运行中" == opp:
            self.signal_index.emit(1)
        elif "运行后" == opp:
            self.signal_index.emit(2)

    def runTelnet(self, signal_sRes, signal_index, index, opp, ip, user, passwd, cmd, res_re):
        print("run telnet")
        if not cmd:
            self.signal_sRes.emit(("script", {"index": index, "opp": opp, "proto": "telnet", "com": "", "ip": ip, "res": ""}))
        else:
            try:
                tl = Telnet()
                tl.auth(ip, 23, user, passwd, ('root@OpenWrt:~#', 'Password:'))
                tl.exec_cmd(cmd)
                out = tl.read_very_lazy()
                tl.close('exit')
                p = re.findall(res_re, out)
                self.signal_sRes.emit(("script", {"index": index, "opp": opp, "proto": "telnet", "com": "", "ip": ip, "res": p}))
            except Exception as e:
                self.signal_tb.emit("脚本执行失败：index(" + str(index) + ") 错误：" + str(e))
                logging.error(e)
                self.signal_sRes.emit(("script", {"index": index, "opp": opp, "proto": "telnet", "com": "", "ip": ip, "res": ""}))
        if "运行前" == opp:
            self.signal_index.emit(0)
        elif "运行中" == opp:
            self.signal_index.emit(1)
        elif "运行后" == opp:
            self.signal_index.emit(2)

    def runSSH(self, signal_sRes, signal_index, index, opp, ip, user, passwd, cmd, res_re):
        print("run SSH")
        if not cmd:
            self.signal_sRes.emit(("script", {"index": index, "opp": opp, "proto": "ssh", "com": "", "ip": ip, "res": ""}))
        else:
            ssh = SSH()
            try:
                ssh.authSSH(ip, 22, user, passwd)
                out = ssh.exec_cmd(cmd)
                print("ont", out)
                ssh.close()
                p = re.findall(res_re, out)
                print("p", p)
                self.signal_sRes.emit(("script", {"index": index, "opp": opp, "proto": "ssh", "com": "", "ip": ip, "res": p}))
            except Exception as e:
                self.signal_tb.emit("脚本执行失败：index(" + str(index) + ") 错误：" + str(e))
                logging.error(e)
                self.signal_sRes.emit(("script", {"index": index, "opp": opp, "proto": "ssh", "com": "", "ip": ip, "res": ""}))
        if "运行前" == opp:
            self.signal_index.emit(0)
        elif "运行中" == opp:
            self.signal_index.emit(1)
        elif "运行后" == opp:
            self.signal_index.emit(2)

class ReportThread(QThread):

    signal_result = pyqtSignal(tuple)
    signal_tb = pyqtSignal(str)

    def __init__(self, parent=None):
        super(ReportThread, self).__init__(parent)

    def setParam(self, iperfVer, proto, method, ipPort, uri, dataFormat):
        self.iperfVer = iperfVer
        self.proto = proto
        self.method = method
        self.ipPort = ipPort
        self.uri = uri
        self.headers = {
            'Host': 'jzkjgroup.com',
            'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
            'Content-Type': 'application/json; charset=utf-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE',
        }
        self.dataFormat = dataFormat
        if self.dataFormat == 'JSON':
            self.headers['Conntent-Type'] = 'application/json; charset=utf-8'
        elif self.dataFormat == 'TXT':
            self.headers['Conntent-Type'] = 'text/html; charset=utf-8'
        else:
            pass
        print("参数传递", self.ipPort)

    def setData(self, data):
        self.data = data

    def run(self):
        print("report start")
        if not self.data:
            return

        if self.dataFormat == 'JSON' or self.dataFormat == 'TXT':
            self.data = json.dumps(self.data)

        if self.proto == 'HTTP':
            self.runHttp()
        else:
            pass

        self.data = None

    def runHttp(self):
        url = "http://" + self.ipPort + self.uri + ('/' if self.uri[-1] != '/' else '') + self.iperfVer
        count = 0
        while count < 3:
            try:
                if self.method == 'POST':
                    page = requests.post(url, data=self.data, headers=self.headers)
                elif self.method == 'GET':
                    page = requests.get(url, self.data, headers=self.headers)
                elif self.method == 'PUT':
                    page = requests.put(url, self.data, headers=self.headers)
                else:
                    return
                if page.ok:
                    self.signal_tb.emit("测试结果上报成功")
                    self.signal_result.emit(("report", True))
                    return
                else:
                    raise requests.exceptions.BaseHTTPError
            except requests.exceptions.ChunkedEncodingError as e:
                time.sleep(5)
                count += 1
            except requests.exceptions.BaseHTTPError as e:
                time.sleep(5)
                count += 1
            except requests.exceptions.ConnectionError as e:
                time.sleep(5)
                count += 1
        self.signal_result.emit(("report", False))
        self.signal_tb.emit("测试结果上报失败")

class ExcelThread(QThread):

    def __init__(self, parent=None):
        super(ExcelThread, self).__init__(parent)

    def setParam(self, filePath=None, sheetName=None, *args):
        self.filePath = filePath
        self.sheetName = sheetName
        self.args = args

    def run(self):
        print("excel start")
        if self.filePath and self.sheetName:
            writeExcel(self.filePath, self.sheetName, self.args)
        self.filePath = None
        self.sheetName = None

def reportResult(proto, method, ipPort, uri, iperfVer, dataFormat, data):
    headers = {
        'Host': 'jzkjgroup.com',
        'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
        'Content-Type': 'application/json; charset=utf-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE',
    }
    if dataFormat == 'JSON':
        headers['Conntent-Type'] = 'application/json; charset=utf-8'
    elif dataFormat == 'TXT':
        headers['Conntent-Type'] = 'text/html; charset=utf-8'
    else:
        pass

    def runHttp(method, headers, url, data):
        count = 0
        while count < 3:
            try:
                if method == 'POST':
                    page = requests.post(url, data, headers=headers)
                elif method == 'GET':
                    page = requests.get(url, data, headers=headers)
                elif method == 'PUT':
                    page = requests.put(url, data, headers=headers)
                else:
                    return
                if page.ok:
                    break
                else:
                    raise requests.exceptions.BaseHTTPError
            except requests.exceptions.ChunkedEncodingError as e:
                time.sleep(5)
                count += 1
            except requests.exceptions.BaseHTTPError as e:
                time.sleep(5)
                count += 1

    if not data:
        return
    if dataFormat == 'JSON':
        data = json.dumps(data)
    url = "http://" + ipPort + uri + ('/' if uri[-1] != '/' else '') + 'iperf' + iperfVer
    if proto == 'HTTP':
        runHttp(method, headers, url, data)
    else:
        pass





if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
