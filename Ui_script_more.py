# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\git\iperf_gui\script_more.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(239, 190)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        Dialog.setFont(font)
        Dialog.setSizeGripEnabled(True)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox_baudrate = QtWidgets.QComboBox(self.widget)
        self.comboBox_baudrate.setObjectName("comboBox_baudrate")
        self.comboBox_baudrate.addItem("")
        self.comboBox_baudrate.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_baudrate)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_user = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_user.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.verticalLayout_2.addWidget(self.lineEdit_user)
        self.lineEdit_passwd = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_passwd.setObjectName("lineEdit_passwd")
        self.verticalLayout_2.addWidget(self.lineEdit_passwd)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.widget_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_a = QtWidgets.QPushButton(Dialog)
        self.pushButton_a.setObjectName("pushButton_a")
        self.horizontalLayout_3.addWidget(self.pushButton_a)
        self.pushButton_s = QtWidgets.QPushButton(Dialog)
        self.pushButton_s.setObjectName("pushButton_s")
        self.horizontalLayout_3.addWidget(self.pushButton_s)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Script More Setting"))
        self.label.setText(_translate("Dialog", "Baudrate:"))
        self.comboBox_baudrate.setItemText(0, _translate("Dialog", "115200"))
        self.comboBox_baudrate.setItemText(1, _translate("Dialog", "9600"))
        self.label_2.setText(_translate("Dialog", "User:"))
        self.label_3.setText(_translate("Dialog", "Password:"))
        self.lineEdit_user.setText(_translate("Dialog", "root"))
        self.lineEdit_passwd.setText(_translate("Dialog", "nE7jA%5m"))
        self.pushButton_a.setText(_translate("Dialog", "确定"))
        self.pushButton_s.setText(_translate("Dialog", "取消"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
