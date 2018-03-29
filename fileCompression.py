#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-3-27 12:00:44
# @Author  : Demoon (a_share@sina.com)
# @Link    :
# @Version : $Id$
# @title   : 文件压缩

import sys
import os
import json
#引入ui文件
import ui_fileCompression
#引入文本处理模板
import fileHanding
#引入文件选择模块
import fileOpener
from PyQt4 import  QtCore, QtGui, uic

#处理编码问题
reload(sys)
sys.setdefaultencoding('utf-8')

#ui文件运用方法
#qtCreatorFile = os.path.join(os.getcwd(), os.path.splitext(os.path.basename(__file__))[0] +".ui")  # Enter file here.
#Ui_fileCompression, QtBaseClass = uic.loadUiType(qtCreatorFile)
#ui转为py运用方法

Ui_fileCompression = ui_fileCompression.Ui_fileCompression



def runCallBack(app, string):
    app.dealView.setText(app.dealView.toPlainText() + '\n' + string)

def successCallBack(app):
    msg_box = QtGui.QMessageBox.about(app, u"提示", u"处理完成！")

class MyApp(QtGui.QMainWindow, Ui_fileCompression):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_fileCompression.__init__(self)
        self.setupUi(self)
        #设置路径缓存
        self.cache = None;

        self.runBtn.clicked.connect(self.dealFile)
        self.fileChoseBtn.clicked.connect(self.fileChose)
        self.folderChoseBtn.clicked.connect(self.folderChose)

    #处理函数
    def dealFile(self):
        #路径或文件
        filePath = self.fileInput.text()
        #是否覆盖
        isCover = self.isCoverCheck.isChecked()

        #清空显示区域
        self.dealView.setText("")

        fileHanding.folderTree(self, str(filePath), isCover, runCallBack, successCallBack,)

    def setCache(self, key, value):
        if self.cache:
            self.cache[key] = value
        else:
            self.cache = {key:value}

    def getCache(self, key):
        if self.cache and key in self.cache:
            return self.cache[key]
        else:
            return None

    #文件选择器
    def fileChose(self):
        apk_file = self.getCache('filepath') if self.getCache('filepath') else __file__
        filename = QtGui.QFileDialog.getOpenFileName(self,apk_file);
        self.setCache('filepath', filename)
        #self.cacheUtils.setCacheString('apk_file', filename)
        self.fileInput.setText(filename)
        print self.cache
    #路径选择器
    def folderChose(self):
        path = self.getCache('folderpath') if self.getCache('folderpath') else 'C:'
        folder = QtGui.QFileDialog.getExistingDirectory(self,directory=path);
        if folder:
            self.setCache('folderpath', folder)
        self.fileInput.setText(folder)
        print self.cache


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
