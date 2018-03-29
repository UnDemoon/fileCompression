# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fileCompression.ui'
#
# Created: Tue Mar 27 21:27:52 2018
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_fileCompression(object):
    def setupUi(self, fileCompression):
        fileCompression.setObjectName(_fromUtf8("fileCompression"))
        fileCompression.resize(566, 207)
        self.centralwidget = QtGui.QWidget(fileCompression)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.fileInput = QtGui.QLineEdit(self.centralwidget)
        self.fileInput.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.fileInput.setObjectName(_fromUtf8("fileInput"))
        self.horizontalLayout.addWidget(self.fileInput)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.fileChoseBtn = QtGui.QPushButton(self.centralwidget)
        self.fileChoseBtn.setObjectName(_fromUtf8("fileChoseBtn"))
        self.verticalLayout_3.addWidget(self.fileChoseBtn)
        self.folderChoseBtn = QtGui.QPushButton(self.centralwidget)
        self.folderChoseBtn.setObjectName(_fromUtf8("folderChoseBtn"))
        self.verticalLayout_3.addWidget(self.folderChoseBtn)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.isCoverCheck = QtGui.QCheckBox(self.centralwidget)
        self.isCoverCheck.setObjectName(_fromUtf8("isCoverCheck"))
        self.horizontalLayout.addWidget(self.isCoverCheck)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.runBtn = QtGui.QPushButton(self.centralwidget)
        self.runBtn.setMinimumSize(QtCore.QSize(0, 0))
        self.runBtn.setObjectName(_fromUtf8("runBtn"))
        self.verticalLayout_2.addWidget(self.runBtn)
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 544, 94))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.dealView = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        self.dealView.setObjectName(_fromUtf8("dealView"))
        self.verticalLayout_4.addWidget(self.dealView)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        fileCompression.setCentralWidget(self.centralwidget)

        self.retranslateUi(fileCompression)
        QtCore.QMetaObject.connectSlotsByName(fileCompression)

    def retranslateUi(self, fileCompression):
        fileCompression.setWindowTitle(_translate("fileCompression", "fileCompression", None))
        self.fileInput.setText(_translate("fileCompression", "请输入文件或文件夹", None))
        self.fileChoseBtn.setText(_translate("fileCompression", "文件", None))
        self.folderChoseBtn.setText(_translate("fileCompression", "目录", None))
        self.isCoverCheck.setText(_translate("fileCompression", "覆盖", None))
        self.runBtn.setText(_translate("fileCompression", "运行", None))

