from PySide2 import QtCore, QtGui, QtWidgets

####################
### ERROR WINDOW ###
####################

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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ErrorwindowTitlebarframe = QtWidgets.QFrame(self.centralwidget)
        self.ErrorwindowTitlebarframe.setGeometry(QtCore.QRect(0, 0, 351, 29))
        self.ErrorwindowTitlebarframe.setStyleSheet("background-color: rgb(0, 1, 0);")
        self.ErrorwindowTitlebarframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ErrorwindowTitlebarframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ErrorwindowTitlebarframe.setObjectName("ErrorwindowTitlebarframe")
        self.ErrorwindowExit_Button = QtWidgets.QPushButton(self.centralwidget)
        self.ErrorwindowExit_Button.setGeometry(QtCore.QRect(300, 0, 51, 29))
        self.ErrorwindowExit_Button.setStyleSheet("QPushButton {\n"
"    background-color: none;\n"
"    border-bottom:2px;\n"
"    border-right:None;\n"
"    border-style:solid;\n"
"    border-color:none;\n"
"    margin:0px;    \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(232, 17, 35);\n"
"    border-style:solid;\n"
"    border-color:none;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(149, 20, 30);\n"
"    border-style:solid;\n"
"    border-color:none;    \n"
"}    \n"
"")
        self.ErrorwindowExit_Button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/ExitButttonicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ErrorwindowExit_Button.setIcon(icon)
        self.ErrorwindowExit_Button.setIconSize(QtCore.QSize(21, 21))
        self.ErrorwindowExit_Button.setCheckable(False)
        self.ErrorwindowExit_Button.setObjectName("ErrorwindowExit_Button")
        self.Errorwindowiconlabel = QtWidgets.QLabel(self.centralwidget)
        self.Errorwindowiconlabel.setGeometry(QtCore.QRect(14, 43, 120, 120))
        self.Errorwindowiconlabel.setText("")
        self.Errorwindowiconlabel.setPixmap(QtGui.QPixmap("icons/erroricon.png"))
        self.Errorwindowiconlabel.setScaledContents(True)
        self.Errorwindowiconlabel.setObjectName("Errorwindowiconlabel")
        self.Errorwindowiconlabel.setStyleSheet("border:none")
        self.Errorwindowtitlelabel = QtWidgets.QLabel(self.centralwidget)
        self.Errorwindowtitlelabel.setGeometry(QtCore.QRect(149, 51, 180, 31))
        self.Errorwindowtitlelabel.setStyleSheet("color: rgb(232, 17, 35);\n"
"font: 16pt \"Alice\";\n"
"border-radius:5px;\n"
"border:none;\n"
"")
        self.Errorwindowtitlelabel.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Errorwindowtitlelabel.setObjectName("Errorwindowtitlelabel")
        self.Errorwindowbodylabel = QtWidgets.QLabel(self.centralwidget)
        self.Errorwindowbodylabel.setGeometry(QtCore.QRect(145, 83, 180, 61))
        self.Errorwindowbodylabel.setStyleSheet("border-radius: 5px;\n"
"color: rgb(236, 236, 236);\n"
"font: 10.5pt \"Alice\";"
"border-color:transparent;\n"
"")
        self.Errorwindowbodylabel.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Errorwindowbodylabel.setWordWrap(True)
        self.Errorwindowbodylabel.setObjectName("Errorwindowbodylabel")
        self.ErrorwindowokpushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ErrorwindowokpushButton.setGeometry(QtCore.QRect(195, 150, 121, 31))
        self.ErrorwindowokpushButton.setStyleSheet("QPushButton {\n"
"    color: rgb(236, 236, 236);\n"
"    font: 10.5pt \"Alice\";\n"
"    background-color: rgb(29, 30, 29);\n"
"    border:1px;\n"
"    border-style:outset;\n"
"    border-color:rgb(29, 30, 29);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(42, 43, 42);\n"
"    border-color:rgb(32, 33, 32);\n"
"    border-radius:5px\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(32, 33, 32);\n"
"    border-color:rgb(20, 21, 20);\n"
"    border-radius:5px;\n"
"}    ")
        self.ErrorwindowokpushButton.setObjectName("ErrorwindowokpushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ErrorwindowExit_Button.setToolTip(_translate("MainWindow", "Matrix"))
        self.ErrorwindowExit_Button.setStatusTip(_translate("MainWindow", "Matrix"))
        self.ErrorwindowExit_Button.setWhatsThis(_translate("MainWindow", "Matrix"))
        self.ErrorwindowExit_Button.setAccessibleName(_translate("MainWindow", "Matrix"))
        self.ErrorwindowExit_Button.setAccessibleDescription(_translate("MainWindow", "Matrix"))
        self.Errorwindowtitlelabel.setText(_translate("MainWindow", "ERROR!"))
        self.Errorwindowbodylabel.setText(_translate("MainWindow", "Error text"))
        self.ErrorwindowokpushButton.setText(_translate("MainWindow", "Ok"))


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

        self.ui.ErrorwindowTitlebarframe.mouseMoveEvent = moveWindow

        self.ui.ErrorwindowExit_Button.clicked.connect(lambda: self.close())
        self.ui.ErrorwindowokpushButton.clicked.connect(lambda: self.close())

    def eventFilter(self,obj, event):
        if event.type() == QtCore.QEvent.WindowDeactivate:
            self.activateWindow()
            return True

        return False
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
