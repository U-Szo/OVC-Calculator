from PySide2 import QtCore, QtGui, QtWidgets
import numpy as np
from fractions import Fraction
import itertools as itools

#########################
##WINDOW CLASSES IMPORT##
#########################
from module_view.mainview_ui_class import * 
from module_view.modules_information_and_error.error_window import *
from module_view.modules_information_and_error.info_window import *
from module_view.modules_assigning_values.assign_window import *
from module_view.modules_assigning_values.values_window import *

######################
#### WINDOW CLASS ####
######################
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,admin):
        super(MainWindow, self).__init__()
        self.admin=admin
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self,self.admin)
        self.setWindowTitle("O.V.C.")
        self.assign_values_window = AssignWindow(self,self.admin)
        self.assign_values_window.setWindowTitle("Assign")
        self.assign_values_window.hide()
        self.assign_values_window.is_hidden = True
        self.ui.eq_string_text_edit.installEventFilter(self)
        self.installEventFilter(self)

        def moveWindow(event):
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.title_bar_frame.mouseMoveEvent = moveWindow

        self.ui.minimize_button.clicked.connect(lambda: self.showMinimized())
        self.ui.exit_button.clicked.connect(lambda: self.close())

        self.error_window=ErrorWindow()
        self.info_window=InfoWindow()

    def moveEvent(self, e):
        if not self.assign_values_window.is_hidden:
            assign_x_pos = self.pos().x() - 330
            self.assign_values_window.move(assign_x_pos,self.pos().y())
        super(MainWindow, self).moveEvent(e)
    def closeEvent(self, event):
        self.assign_values_window.close()
        self.assign_values_window.is_hidden = True
        self.assign_values_window.close()
        self.error_window.close()
        self.info_window.close()
        event.accept()

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.WindowStateChange:
            if QtCore.Qt.WindowMinimized:
                self.assign_values_window.hide()
                self.assign_values_window.is_hidden = True
            else:
                pass

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress and obj is self.ui.eq_string_text_edit:
            if event.key() == QtCore.Qt.Key_Return and self.ui.eq_string_text_edit.hasFocus():
                self.ui.equalButtonClicked()
                return True
            if event.key() == QtCore.Qt.Key_Enter and self.ui.eq_string_text_edit.hasFocus():
                self.ui.equalButtonClicked()
                return True
            if event.key() == QtCore.Qt.Key_1 and self.ui.eq_string_text_edit.hasFocus():
                self.ui.eq_string_text_edit.insertPlainText("1")
                return True
            if event.key() == QtCore.Qt.Key_2 and self.ui.eq_string_text_edit.hasFocus():
                self.ui.eq_string_text_edit.insertPlainText("2")
                return True
            if event.key() == QtCore.Qt.Key_3 and self.ui.eq_string_text_edit.hasFocus():
                self.ui.eq_string_text_edit.insertPlainText("3")
                return True
            if event.key() == QtCore.Qt.Key_4 and self.ui.eq_string_text_edit.hasFocus():
                self.ui.eq_string_text_edit.insertPlainText("4")
                return True
            if event.key() == QtCore.Qt.Key_5 and self.ui.eq_string_text_edit.hasFocus():
                self.ui.eq_string_text_edit.insertPlainText("5")
                return True
            if event.key() == QtCore.Qt.Key_6 and self.ui.eq_string_text_edit.hasFocus():
                self.ui.eq_string_text_edit.insertPlainText("6")
                return True
            if event.key() == QtCore.Qt.Key_7 and self.ui.eq_string_text_edit.hasFocus():
                self.ui.eq_string_text_edit.insertPlainText("7")
                return True
            if event.key() == QtCore.Qt.Key_8 and self.ui.eq_string_text_edit.hasFocus():
                self.ui.eq_string_text_edit.insertPlainText("8")
                return True
            if event.key() == QtCore.Qt.Key_9 and self.ui.eq_string_text_edit.hasFocus():
                self.ui.eq_string_text_edit.insertPlainText("9")
                return True
            if event.key() == QtCore.Qt.Key_0 and self.ui.eq_string_text_edit.hasFocus():
                self.ui.eq_string_text_edit.insertPlainText("0")
                return True
            if event.key() == QtCore.Qt.Key_Space and self.ui.eq_string_text_edit.hasFocus():
                self.ui.eq_string_text_edit.insertPlainText(" ")
                return True
            if event.key() == QtCore.Qt.Key_Backspace and self.ui.eq_string_text_edit.hasFocus():
                self.ui.eq_string_text_edit.textCursor().deletePreviousChar()
                return True
            if event.key() == QtCore.Qt.Key_Left and self.ui.eq_string_text_edit.hasFocus():
                self.ui.eq_string_text_edit.moveCursor(QtGui.QTextCursor.Left)
                return True
            if event.key() == QtCore.Qt.Key_Right and self.ui.eq_string_text_edit.hasFocus():
                self.ui.eq_string_text_edit.moveCursor(QtGui.QTextCursor.Right)
                return True
            if event.key() == QtCore.Qt.Key_M and self.ui.eq_string_text_edit.hasFocus():
                self.ui.eq_string_text_edit.insertPlainText("Matrix")
                return True
            if event.key() == QtCore.Qt.Key_V and self.ui.eq_string_text_edit.hasFocus():
                self.ui.eq_string_text_edit.insertPlainText("Vector")
                return True
            if event.key() == QtCore.Qt.Key_A and self.ui.eq_string_text_edit.hasFocus():
                self.ui.eq_string_text_edit.insertPlainText("Ans")
                return True
            if event.key() == QtCore.Qt.Key_ParenLeft and self.ui.eq_string_text_edit.hasFocus():
                self.ui.eq_string_text_edit.insertPlainText("(")
                return True
            if event.key() == QtCore.Qt.Key_ParenRight and self.ui.eq_string_text_edit.hasFocus():
                self.ui.eq_string_text_edit.insertPlainText(")")
                return True
            if event.key() == QtCore.Qt.Key_Period and self.ui.eq_string_text_edit.hasFocus():
                self.ui.eq_string_text_edit.insertPlainText(".")
                return True
            if event.key() == QtCore.Qt.Key_Comma and self.ui.eq_string_text_edit.hasFocus():
                self.ui.eq_string_text_edit.insertPlainText(".")
                return True

        if event.type() == QtCore.QEvent.WindowActivate:
            if  not self.assign_values_window.is_hidden:
                self.assign_values_window.raise_()
            return True
        return super().eventFilter(obj, event)