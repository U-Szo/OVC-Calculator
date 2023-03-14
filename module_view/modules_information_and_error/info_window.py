from PySide2 import QtCore, QtGui, QtWidgets
from module_view.modules_information_and_error.info_window_ui_class import *

######################
#### WINDOW CLASS ####
######################

class InfoWindow(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(InfoWindow, self).__init__()
        self.ui = Ui_InfoWindow()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowTitle("O.V.C. Information")

        def moveWindow(event):
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.info_window_title_bar_frame.mouseMoveEvent = moveWindow

        self.ui.info_window_exit_button.clicked.connect(lambda: self.close())

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()