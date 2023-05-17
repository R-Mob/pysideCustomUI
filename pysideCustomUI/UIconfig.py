#This is a UI setup file using pyside2



from PySide2 import QtCore
from PySide2 import QtWidgets
from shiboken2 import wrapInstance

import maya.OpenMayaUI as omui


def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    mainWindow =  wrapInstance(int(main_window_ptr), QtWidgets.QWidget)
    return mainWindow

class TestDialog(QtWidgets.QDialog):
    def __int__(self,parent= None):
        super(TestDialog, self).__init__(parent=parent)
        l = QtWidgets.QVBoxLayout(self)
        l.addWidget(QtWidgets.QPushButton())


if __name__ == "__main__":

    d = TestDialog(parent=maya_main_window())
    d.show()



