# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
import time
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QDialog

from Ui_script_more import Ui_Dialog


class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """

    signal_param = pyqtSignal(tuple)

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Dialog, self).__init__(parent)
        self.setupUi(self)

    def setKey(self, key):
        self.key = key

    @pyqtSlot()
    def on_pushButton_a_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.signal_param.emit((self.key, self.comboBox_baudrate.currentText(), self.lineEdit_user.text(), self.lineEdit_passwd.text()))
        time.sleep(2)
        self.close()
    
    @pyqtSlot()
    def on_pushButton_s_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.close()