from PySide2 import QtCore, QtGui, QtWidgets
######################
##STYLESHEETS IMPORT##
######################
import module_view.modules_informationanderror.informationanderror_stylesheets.ErrorWindowStylesheet as ewss

class Ui_ErrorWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setWindowIcon((QtGui.QIcon("icons/Windowicon.png")))
        MainWindow.setObjectName("ERROR")
        MainWindow.resize(351, 196)
        MainWindow.setStyleSheet("background-color: rgb(25, 26, 25);\n"
"border: 2px solid rgb(15,16,15);"
            )
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.error_window_title_bar_frame = QtWidgets.QFrame(self.central_widget)
        self.error_window_title_bar_frame.setGeometry(QtCore.QRect(0, 0, 351, 29))
        self.error_window_title_bar_frame.setStyleSheet("background-color: rgb(0, 1, 0);")
        self.error_window_title_bar_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.error_window_title_bar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.error_window_exit_button = QtWidgets.QPushButton(self.central_widget)
        self.error_window_exit_button.setGeometry(QtCore.QRect(300, 0, 51, 29))
        self.error_window_exit_button.setStyleSheet(ewss.error_window_exit_button_stylesheet)
        self.error_window_exit_button.setText("")
        error_window_exit_button_icon = QtGui.QIcon()
        error_window_exit_button_icon.addPixmap(QtGui.QPixmap("icons/ExitButttonicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.error_window_exit_button.setIcon(error_window_exit_button_icon)
        self.error_window_exit_button.setIconSize(QtCore.QSize(21, 21))
        self.error_window_exit_button.setCheckable(False)
        self.error_window_icon_label = QtWidgets.QLabel(self.central_widget)
        self.error_window_icon_label.setGeometry(QtCore.QRect(14, 43, 120, 120))
        self.error_window_icon_label.setText("")
        self.error_window_icon_label.setPixmap(QtGui.QPixmap("icons/erroricon.png"))
        self.error_window_icon_label.setScaledContents(True)
        self.error_window_icon_label.setStyleSheet("border:none")
        self.error_window_title_label = QtWidgets.QLabel(self.central_widget)
        self.error_window_title_label.setGeometry(QtCore.QRect(149, 51, 180, 31))
        self.error_window_title_label.setStyleSheet(ewss.error_window_title_label_stylesheet)
        self.error_window_title_label.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.error_window_body_label = QtWidgets.QLabel(self.central_widget)
        self.error_window_body_label.setGeometry(QtCore.QRect(145, 83, 180, 61))
        self.error_window_body_label.setStyleSheet(ewss.error_window_body_label_stylesheet)
        self.error_window_body_label.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.error_window_body_label.setWordWrap(True)
        self.error_window_ok_pushbutton = QtWidgets.QPushButton(self.central_widget)
        self.error_window_ok_pushbutton.setGeometry(QtCore.QRect(195, 150, 121, 31))
        self.error_window_ok_pushbutton.setStyleSheet(ewss.error_window_ok_pushbutton_stylesheet)
        MainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.error_window_exit_button.setToolTip(_translate("MainWindow", "Matrix"))
        self.error_window_exit_button.setStatusTip(_translate("MainWindow", "Matrix"))
        self.error_window_exit_button.setWhatsThis(_translate("MainWindow", "Matrix"))
        self.error_window_exit_button.setAccessibleName(_translate("MainWindow", "Matrix"))
        self.error_window_exit_button.setAccessibleDescription(_translate("MainWindow", "Matrix"))
        self.error_window_title_label.setText(_translate("MainWindow", "ERROR!"))
        self.error_window_body_label.setText(_translate("MainWindow", "Error text"))
        self.error_window_ok_pushbutton.setText(_translate("MainWindow", "Ok"))


############################
#### CLASES DE VENTANAS ####
############################

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
