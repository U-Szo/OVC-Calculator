from PySide2 import QtCore, QtGui, QtWidgets
from module_view.modules_informationanderror.module_bidirectionaliterator.bidirectional_iterator import *

###################
### INFO WINDOW ###
###################

class Ui_InfoWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setWindowIcon((QtGui.QIcon("icons/Windowicon.png")))
        MainWindow.setObjectName("Information Window")
        MainWindow.resize(1031, 550)
        MainWindow.setStyleSheet("background-color: rgb(10, 11, 10);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.InfowindowTitlebarframe = QtWidgets.QFrame(self.centralwidget)
        self.InfowindowTitlebarframe.setGeometry(QtCore.QRect(7, 0, 1031, 29))
        self.InfowindowTitlebarframe.setStyleSheet("background-color: rgb(0, 1, 0);")
        self.InfowindowTitlebarframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.InfowindowTitlebarframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.InfowindowTitlebarframe.setObjectName("InfowindowTitlebarframe")
        self.InfowindowExit_Button = QtWidgets.QPushButton(self.centralwidget)
        self.InfowindowExit_Button.setGeometry(QtCore.QRect(980, 0, 51, 29))
        self.InfowindowExit_Button.setStyleSheet("QPushButton {\n"
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
        self.InfowindowExit_Button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/ExitButttonicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.InfowindowExit_Button.setIcon(icon)
        self.InfowindowExit_Button.setIconSize(QtCore.QSize(21, 21))
        self.InfowindowExit_Button.setCheckable(False)
        self.InfowindowExit_Button.setObjectName("InfowindowExit_Button")
        self.infomainLabel = QtWidgets.QLabel(self.centralwidget)
        self.infomainLabel.setGeometry(QtCore.QRect(70, 40, 896, 500))
        self.infomainLabel.setText("")
        self.infomainLabel.setPixmap(QtGui.QPixmap("icons/infowindowimages/infoimage01.png"))
        self.infomainLabel.setScaledContents(True)
        self.infomainLabel.setObjectName("infomainLabel")
        self.inforightarrowpushButton = QtWidgets.QPushButton(self.centralwidget)
        self.inforightarrowpushButton.setGeometry(QtCore.QRect(970, 250, 61, 61))
        self.inforightarrowpushButton.setStyleSheet("background-color: transparent;\n"
"border:none;")
        self.inforightarrowpushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/infowindowimages/infoarrowright.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.inforightarrowpushButton.setIcon(icon1)
        self.inforightarrowpushButton.setIconSize(QtCore.QSize(51, 51))
        self.inforightarrowpushButton.setObjectName("inforightarrowpushButton")
        self.inforightarrowpushButton.clicked.connect(self.rightarrowclicked)
        self.inforightarrowpushButton.setShortcut("Right")
        self.infoleftarrowpushButton = QtWidgets.QPushButton(self.centralwidget)
        self.infoleftarrowpushButton.setGeometry(QtCore.QRect(0, 250, 61, 61))
        self.infoleftarrowpushButton.setStyleSheet("background-color: transparent;\n"
"border:none;")
        self.infoleftarrowpushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/infowindowimages/infoarrowleft.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.infoleftarrowpushButton.setIcon(icon2)
        self.infoleftarrowpushButton.setIconSize(QtCore.QSize(51, 51))
        self.infoleftarrowpushButton.setObjectName("infoleftarrowpushButton")
        self.infoleftarrowpushButton.clicked.connect(self.leftarrowclicked)
        self.infoleftarrowpushButton.setShortcut("Left")
        self.infoimagescycle = bidirectional_iterator([
            "icons/infowindowimages/infoimage01.png",
            "icons/infowindowimages/infoimage02.png",
            "icons/infowindowimages/infoimage03.png",
            "icons/infowindowimages/infoimage04.png",
            "icons/infowindowimages/infoimage05.png",
            "icons/infowindowimages/infoimage06.png",
            "icons/infowindowimages/infoimage07.png",
            "icons/infowindowimages/infoimage08.png",
            "icons/infowindowimages/infoimage09.png",
            "icons/infowindowimages/infoimage10.png",
            "icons/infowindowimages/infoimage11.png",
            "icons/infowindowimages/infoimage12.png",
            "icons/infowindowimages/infoimage13.png",
            "icons/infowindowimages/infoimage14.png",
            "icons/infowindowimages/infoimage15.png",
            "icons/infowindowimages/infoimage16.png"
        ])
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def rightarrowclicked(self):
        self.infomainLabel.setPixmap(QtGui.QPixmap(self.infoimagescycle.next()))
    def leftarrowclicked(self):
        self.infomainLabel.setPixmap(QtGui.QPixmap(self.infoimagescycle.prev()))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.InfowindowExit_Button.setToolTip(_translate("MainWindow", "Matrix"))
        self.InfowindowExit_Button.setStatusTip(_translate("MainWindow", "Matrix"))
        self.InfowindowExit_Button.setWhatsThis(_translate("MainWindow", "Matrix"))
        self.InfowindowExit_Button.setAccessibleName(_translate("MainWindow", "Matrix"))
        self.InfowindowExit_Button.setAccessibleDescription(_translate("MainWindow", "Matrix"))

############################
#### CLASES DE VENTANAS ####
############################

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

        self.ui.InfowindowTitlebarframe.mouseMoveEvent = moveWindow

        self.ui.InfowindowExit_Button.clicked.connect(lambda: self.close())

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
