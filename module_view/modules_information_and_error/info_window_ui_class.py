from PySide2 import QtCore, QtGui, QtWidgets
from module_view.modules_information_and_error.module_bidirectional_iterator.bidirectional_iterator import *
######################
##STYLESHEETS IMPORT##
######################
import module_view.modules_information_and_error.information_and_error_stylesheets.info_window_stylesheet as iwss

class Ui_InfoWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setWindowIcon((QtGui.QIcon("icons/Windowicon.png")))
        MainWindow.setObjectName("Information Window")
        MainWindow.resize(1031, 550)
        MainWindow.setStyleSheet("background-color: rgb(10, 11, 10);")
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.info_window_title_bar_frame = QtWidgets.QFrame(self.central_widget)
        self.info_window_title_bar_frame.setGeometry(QtCore.QRect(7, 0, 1031, 29))
        self.info_window_title_bar_frame.setStyleSheet("background-color: rgb(0, 1, 0);")
        self.info_window_title_bar_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info_window_title_bar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info_window_exit_button = QtWidgets.QPushButton(self.central_widget)
        self.info_window_exit_button.setGeometry(QtCore.QRect(980, 0, 51, 29))
        self.info_window_exit_button.setStyleSheet(iwss.info_window_exit_button_stylesheet)
        self.info_window_exit_button.setText("")
        info_window_exit_button_icon = QtGui.QIcon()
        info_window_exit_button_icon.addPixmap(QtGui.QPixmap("icons/ExitButttonicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.info_window_exit_button.setIcon(info_window_exit_button_icon)
        self.info_window_exit_button.setIconSize(QtCore.QSize(21, 21))
        self.info_window_exit_button.setCheckable(False)
        self.info_main_label = QtWidgets.QLabel(self.central_widget)
        self.info_main_label.setGeometry(QtCore.QRect(70, 40, 896, 500))
        self.info_main_label.setText("")
        self.info_main_label.setPixmap(QtGui.QPixmap("icons/infowindowimages/infoimage01.png"))
        self.info_main_label.setScaledContents(True)
        self.info_right_arrow_pushbutton = QtWidgets.QPushButton(self.central_widget)
        self.info_right_arrow_pushbutton.setGeometry(QtCore.QRect(970, 250, 61, 61))
        self.info_right_arrow_pushbutton.setStyleSheet(iwss.info_right_arrow_pushbutton_stylesheet)
        self.info_right_arrow_pushbutton.setText("")
        info_right_arrow_pushbutton_icon = QtGui.QIcon()
        info_right_arrow_pushbutton_icon.addPixmap(QtGui.QPixmap("icons/infowindowimages/infoarrowright.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.info_right_arrow_pushbutton.setIcon(info_right_arrow_pushbutton_icon)
        self.info_right_arrow_pushbutton.setIconSize(QtCore.QSize(51, 51))
        self.info_right_arrow_pushbutton.clicked.connect(self.right_arrow_clicked)
        self.info_right_arrow_pushbutton.setShortcut("Right")
        self.info_left_arrow_pushbutton = QtWidgets.QPushButton(self.central_widget)
        self.info_left_arrow_pushbutton.setGeometry(QtCore.QRect(0, 250, 61, 61))
        self.info_left_arrow_pushbutton.setStyleSheet(iwss.info_left_arrow_pushbutton_stylesheet)
        self.info_left_arrow_pushbutton.setText("")
        info_left_arrow_pushbutton_icon = QtGui.QIcon()
        info_left_arrow_pushbutton_icon.addPixmap(QtGui.QPixmap("icons/infowindowimages/infoarrowleft.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.info_left_arrow_pushbutton.setIcon(info_left_arrow_pushbutton_icon)
        self.info_left_arrow_pushbutton.setIconSize(QtCore.QSize(51, 51))
        self.info_left_arrow_pushbutton.clicked.connect(self.left_arrow_clicked)
        self.info_left_arrow_pushbutton.setShortcut("Left")
        self.info_images_cycle = BidirectionalIterator([
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
        MainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def right_arrow_clicked(self):
        self.info_main_label.setPixmap(QtGui.QPixmap(self.info_images_cycle.next()))
    def left_arrow_clicked(self):
        self.info_main_label.setPixmap(QtGui.QPixmap(self.info_images_cycle.prev()))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.info_window_exit_button.setToolTip(_translate("MainWindow", "Matrix"))
        self.info_window_exit_button.setStatusTip(_translate("MainWindow", "Matrix"))
        self.info_window_exit_button.setWhatsThis(_translate("MainWindow", "Matrix"))
        self.info_window_exit_button.setAccessibleName(_translate("MainWindow", "Matrix"))
        self.info_window_exit_button.setAccessibleDescription(_translate("MainWindow", "Matrix"))
