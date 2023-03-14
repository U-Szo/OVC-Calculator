from PySide2 import QtCore, QtGui, QtWidgets
from module_view.modules_assigning_values.values_window import *
import module_view.mainview as mainv

from module_view.modules_assigning_values.assign_window_ui_class import *

class AssignWindow(QtWidgets.QMainWindow):
    def __init__(self,admin,parent=None):
        super(AssignWindow, self).__init__()
        self.ui = Ui_AssignWindow()
        self.admin=admin
        self.ui.setupUi(self,self.admin)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.valueswindow = ValuesWindow(self,self.admin)
        self.valueswindow.setWindowTitle("Assign Values")
        self.valueswindow.hide()
        self.is_hidden = True

    def closeEvent(self, event):
        self.is_hidden = True
        event.accept()
    def showEvent(self, e):
        self.is_hidden = False
        self.move(self.admin.admin.window.pos().x() - 330,self.admin.admin.window.pos().y())