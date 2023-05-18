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

        self.setWindowTitle("Renamer Tool")
        self.setMinimumHeight(300)
        self.setMaximumHeight(300)
        self.setMinimumWidth(300)
        self.setMaximumWidth(300)

        self.renamerWidget()
        self.renamerLayout()

    def renamerWidget(self):
        self.startRe = QtWidgets.QLabel("Start #:")
        self.paddingRe = QtWidgets.QLabel("Padding #:")
        self.renamer_lineEdit = QtWidgets.QLineEdit()
        self.start_lineEdit = QtWidgets.QLineEdit()
        self.padding_lineEdit = QtWidgets.QLineEdit()
        self.renAndNum_btn = QtWidgets.QPushButton("Rename and Number")




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
        sectionA_layout.addStretch()





        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(sectionA_layout)






if __name__ == "__main__":

    try:
        renamerUI.close()
        renamerUI.deleteLater()
    except:
        pass

    renamerUI = RenamerUI(parent=mayaMainWindow())
    renamerUI.show()
