 #!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-14 21:59:44
# @Author  : Demoon (a_share@sina.com)
# @Link    :
# @Version : $Id$
# @title   : 处理文本文件（去空行）
import os
import sys
def fileDeal(filepath, isClear):
    fileFolder, baseName = os.path.split(filepath)
    fileName, fileType = os.path.splitext(baseName)
    newPath = os.path.join(fileFolder, fileName + '_bak.tmp')
    if copyFile(filepath, newPath):
        f=open(newPath,'a+')
        fnew=open(filepath, 'wb')            #将结果存入新的文本中
        for line in f.readlines():                                  #对每一行先删除空格，\n等无用的字符，再检查此行是否长度为0
            data = line.strip('\n').strip()
            if len(data)!=0:
                fnew.write(line)
        f.close()
        fnew.close()
        if isClear != False:
            os.remove(newPath)
    else:
        raise Exception('Error in copy file!')

def copyFile(filepath, newPath):
    f=open(filepath,'a+')
    fnew=open(newPath, 'wb')            #将结果存入新的文本中
    for line in f.readlines():                                  #对每一行先删除空格，\n等无用的字符，再检查此行是否长度为0
            fnew.write(line)
    f.close()
    fnew.close()
    return True;

class folderTree(object):
    def __init__(self, app, url, isClear, runFuc, successFuc):
        self.isClear = isClear
        self.app = app
        self.workObj = url
        self.runCall = self.callFuc(runFuc)
        self.sucFuc = self.callFuc(successFuc)
        self._traverseFile()

    def _traverseFile(self):
        if os.path.isfile(self.workObj):
            fileDeal(self.workObj, self.isClear)
        else:
            for dirpath, dirnames, filenames in os.walk(self.workObj):
                for filename in filenames:
                    if not filename.endswith('_bak.tmp'):
                        fullpath = os.path.join(dirpath, filename)
                        self.runCall(self.app, fullpath)
                        fileDeal(fullpath, self.isClear)
        self.sucFuc(self.app)

    def callFuc(self, func):
        return func


if __name__ == '__main__':
    try:
        script, url, isClear = sys.argv
    except Exception as e:
        try:
            script, url = sys.argv
            isClear = False
        except Exception as e:
            raise Exception("Must give a file or folder!")
    folderTree(url, isClear)
