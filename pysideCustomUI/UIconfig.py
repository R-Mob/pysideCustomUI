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
        #self.setMinimumHeight(500)

        self.createWidgets()
        self.createLayouts()

    def createWidgets(self):
        self.lineedit = QtWidgets.QLineEdit()
        self.checkbox1 = QtWidgets.QCheckBox("checkbox1")
        self.checkbox2 = QtWidgets.QCheckBox("checkbox2")
        self.ok_btn = QtWidgets.QPushButton("OK")
        self.cncl_btn = QtWidgets.QPushButton("Cancel")

    def createLayouts(self):
        btn_layout = QtWidgets.QHBoxLayout()
        btn_layout.addWidget(self.ok_btn)
        btn_layout.addWidget(self.cncl_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.lineedit)
        main_layout.addWidget(self.checkbox1)
        main_layout.addWidget(self.checkbox2)


        main_layout.addLayout(btn_layout)




if __name__ == "__main__":

    d = TestDialog(parent=maya_main_window())
    d.show()
