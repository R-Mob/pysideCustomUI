#This is a UI setup file using pyside2

import sys
from PySide2 import QtCore
from PySide2 import QtWidgets
from shiboken2 import wrapInstance

import maya.OpenMayaUI as omui


def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    mainWindow =  wrapInstance(int(main_window_ptr), QtWidgets.QWidget)
    return mainWindow

class TestDialog(QtWidgets.QDialog):
    def __init__(self,parent):
        super(TestDialog, self).__init__(parent)

        self.setWindowTitle('Test_Dialog')
        self.setMinimumWidth(250)
        self.setMinimumHeight(500)


if __name__ == "__main__":

    d = TestDialog(parent=maya_main_window())
    d.show()
