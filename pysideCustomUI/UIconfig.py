#This is a UI setup file using pyside2

from PySide2 import QtCore
from PySide2 import QtWidgets
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui

def mayaMainWindow():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)

class RenamerUI(QtWidgets.QDialog):
    def __init__(self, parent = mayaMainWindow()):
        super(RenamerUI,self).__init__(parent)

        self.setWindowTitle("[Mobius] Renamer Tool v0.1")
        self.setMinimumHeight(400)
        self.setMaximumHeight(400)
        self.setMinimumWidth(360)
        self.setMaximumWidth(360)

        self.renamerWidget()
        self.renamerLayout()

    def renamerWidget(self):
        self.startRe = QtWidgets.QLabel("Start #:")
        self.paddingRe = QtWidgets.QLabel("Padding #:")
        self.renamer_lineEdit = QtWidgets.QLineEdit()
        self.start_lineEdit = QtWidgets.QLineEdit()
        self.padding_lineEdit = QtWidgets.QLineEdit()
        self.renAndNum_btn = QtWidgets.QPushButton("Rename and Number")

        self.removeLavel = QtWidgets.QLabel("Remove...  ")
        self.firstCharBtn = QtWidgets.QPushButton("First Character-->")
        self.lastCharBtn = QtWidgets.QPushButton("<--Last Character")

        self.intersection = QtWidgets.QLabel("-----------------------------------------------------------------------------------")
        self.intersection1 = QtWidgets.QLabel(
            "-----------------------------------------------------------------------------------")

        self.hashLabel = QtWidgets.QLabel("Hash Rename   ")
        self.namesuffLineEdit = QtWidgets.QLineEdit("")
        self.renBtn = QtWidgets.QPushButton("Rename")

        self.beforeLabel = QtWidgets.QLabel("(Before)            ")
        self.afterLabel = QtWidgets.QLabel("(After)              ")
        self.prefLineEdit = QtWidgets.QLineEdit()
        self.sufLineEdit= QtWidgets.QLineEdit()
        self.addBtn=QtWidgets.QPushButton("Add")
        self.addBtn1 = QtWidgets.QPushButton("Add")

        self.grpBtn = QtWidgets.QPushButton("_grp")
        self.geoBtn = QtWidgets.QPushButton("_geo")
        self.ctrlBtn = QtWidgets.QPushButton("_ctrl")
        self.jntBtn = QtWidgets.QPushButton("_jnt")
        self.drvBtn = QtWidgets.QPushButton("_drv")


    def renamerLayout(self):
        grid_layout = QtWidgets.QGridLayout()

        grid_layout.addWidget(self.startRe, 1, 0)
        grid_layout.addWidget((self.start_lineEdit), 1, 1)
        grid_layout.addWidget(self.paddingRe, 1, 2)
        grid_layout.addWidget((self.padding_lineEdit), 1, 3)

        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow("Rename :" , self.renamer_lineEdit)

        sectionA_layout = QtWidgets.QVBoxLayout()
        sectionA_layout.addLayout(form_layout)
        sectionA_layout.addLayout(grid_layout)
        sectionA_layout.addWidget(self.renAndNum_btn)

        sectionB_layout = QtWidgets.QHBoxLayout()
        sectionB_layout.addWidget(self.removeLavel)
        sectionB_layout.addWidget(self.firstCharBtn)
        sectionB_layout.addWidget(self.lastCharBtn)

        sectionB_A_layout = QtWidgets.QHBoxLayout()
        sectionB_A_layout.addWidget(self.hashLabel)
        sectionB_A_layout.addWidget(self.namesuffLineEdit)
        sectionB_A_layout.addWidget(self.renBtn)

        sectionB_FLayout = QtWidgets.QVBoxLayout()
        sectionB_FLayout.addWidget(self.intersection)
        sectionB_FLayout.addLayout(sectionB_layout)
        sectionB_FLayout.addLayout(sectionB_A_layout)

        sectionC_ALayout = QtWidgets.QHBoxLayout()
        sectionC_ALayout.addWidget(self.beforeLabel)
        sectionC_ALayout.addWidget(self.prefLineEdit)
        sectionC_ALayout.addWidget(self.addBtn)

        sectionC_BLayout = QtWidgets.QHBoxLayout()
        sectionC_BLayout.addWidget(self.afterLabel)
        sectionC_BLayout.addWidget(self.sufLineEdit)
        sectionC_BLayout.addWidget(self.addBtn1)

        sectionD_layout = QtWidgets.QHBoxLayout()
        sectionD_layout.addWidget(self.grpBtn)
        sectionD_layout.addWidget(self.geoBtn)
        sectionD_layout.addWidget(self.ctrlBtn)
        sectionD_layout.addWidget(self.jntBtn)
        sectionD_layout.addWidget(self.drvBtn)



        sectionC_Flayout = QtWidgets.QVBoxLayout()
        sectionC_Flayout.addWidget(self.intersection1)
        sectionC_Flayout.addLayout(sectionC_ALayout)
        sectionC_Flayout.addLayout(sectionC_BLayout)
        sectionC_Flayout.addLayout(sectionD_layout)
        sectionC_Flayout.addStretch()

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(sectionA_layout)
        main_layout.addLayout(sectionB_FLayout)
        main_layout.addLayout(sectionC_Flayout)



if __name__ == "__main__":

    try:
        renamerUI.close()
        renamerUI.deleteLater()
    except:
        pass

    renamerUI = RenamerUI(parent=mayaMainWindow())
    renamerUI.show()
