# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QLabel, QTableWidgetItem
from PyQt5.QtCore import pyqtSlot, QThread, pyqtSignal, Qt, QCoreApplication
from PyQt5.QtGui import QFont
import subprocess
import win32com.client as wc
import os
import datetime, time
import re, decimal
from rn_common.netTools import getLinkState
from Ui_iperf_client import Ui_MainWindow


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
        self.initWidget()
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

        self.label_count = QLabel()
        font = QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_count.setFont(font)
        self.label_count.setObjectName("label_count")
        self.statusBar.addPermanentWidget(self.label_count)
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
            else:
                self.label_res_th.setText(self.translate("GeneralWindow", p0[1] + ' Mbps'))
                self.addInfo(self.tableWidget, (p0[1] + ' Mbps', '', '编辑', now))

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
        print(fileName, ok)
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
        print(c_param)
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





if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
    
