from PySide2 import QtCore, QtGui, QtWidgets
from module_view.modules_assigning_values.values_window_ui_class import *

############################
#### CLASES DE VENTANAS ####
############################

class ValuesWindow(QtWidgets.QMainWindow):
    def __init__(self,admin,parent=None):
        super(ValuesWindow, self).__init__()
        self.ui = Ui_ValuesWindow()
        self.admin=admin
        self.ui.setupUi(self,self.admin)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

        def moveWindow(event):
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.rows_label.mouseMoveEvent = moveWindow
        self.ui.columns_label.mouseMoveEvent = moveWindow
        self.ui.selected_label.mouseMoveEvent = moveWindow
        self.ui.decorative_label_top_row.mouseMoveEvent = moveWindow
        self.ui.decorative_label_top_row_2.mouseMoveEvent = moveWindow
        self.ui.selected_vm_label.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()