from PySide2 import QtCore, QtGui, QtWidgets
from module_view.modules_information_and_error.error_window_ui_class import *

######################
#### WINDOW CLASS ####
######################

class ErrorWindow(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(ErrorWindow, self).__init__()
        self.ui = Ui_ErrorWindow()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowTitle("ERROR")
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.installEventFilter(self)

        def moveWindow(event):
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.error_window_title_bar_frame.mouseMoveEvent = moveWindow

        self.ui.error_window_exit_button.clicked.connect(lambda: self.close())
        self.ui.error_window_ok_pushbutton.clicked.connect(lambda: self.close())

    def eventFilter(self,obj, event):
        if event.type() == QtCore.QEvent.WindowDeactivate:
            self.activateWindow()
            return True

        return False
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
