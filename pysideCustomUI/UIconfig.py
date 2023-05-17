#This is a UI setup file using pyside2
from PySide2 import QtCore
from PySide2 import QtWidgets
from shiboken2 import wrapInstance

import maya.OpenMayaUI as omui


def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr),QtWidgets.QWidget)

class TestDialog(QtWidgets.QDialog):

    def __int__(self,parent = maya_main_window()):
        super(TestDialog,self).__init__(parent)


if __name__ == "__main__":
    d = TestDialog()
    d.show()