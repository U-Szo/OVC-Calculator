from PySide2 import QtCore, QtGui, QtWidgets



class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.resize(629, 632)
        SplashScreen.setWindowIcon((QtGui.QIcon("icons/Windowicon.png")))
        self.central_widget = QtWidgets.QWidget(SplashScreen)
        self.vertical_layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.vertical_layout.setContentsMargins(10, 10, 10, 10)
        self.vertical_layout.setSpacing(0)
        self.loading_main_frame = QtWidgets.QFrame(self.central_widget)
        self.loading_main_frame.setStyleSheet("QFrame {    \n"
"    background-color: transparent;    \n"
"    color: rgb(220, 220, 220);\n"
"    border-radius: 10px;\n"
"}")
        self.loading_main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loading_main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background_label = QtWidgets.QLabel(self.loading_main_frame)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 609, 612))
        self.background_label.setStyleSheet("")
        self.background_label.setText("")
        self.background_label.setPixmap(QtGui.QPixmap("icons/splashScreenbackground.png"))
        self.background_label.setScaledContents(True)

        
        self.background_label.setAlignment(QtCore.Qt.AlignCenter)
        self.progress_bar = QtWidgets.QProgressBar(self.loading_main_frame)
        self.progress_bar.setGeometry(QtCore.QRect(215, 392, 178, 10))
        self.progress_bar.setStyleSheet("QProgressBar {\n"
"    background-color: rgb(0, 1, 0);\n"
"    color: transparent;\n"
"    border-style: none;\n"
"    font: 12pt \"Alice\";\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"    border-radius: 5px;\n"
"    background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(32, 33, 32, 255), stop:1 rgba(25, 26, 25, 255));\n"
"}")
        self.progress_bar.setProperty("value", 24)
        self.loading_label = QtWidgets.QLabel(self.loading_main_frame)
        self.loading_label.setGeometry(QtCore.QRect(95, 410, 431, 21))
        font = QtGui.QFont()
        font.setFamily("Alice")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.loading_label.setFont(font)
        self.loading_label.setStyleSheet("font: 10pt \"Alice\";\n"
"color: rgb(196, 196, 196);")
        self.loading_label.setAlignment(QtCore.Qt.AlignCenter)
        self.loading_progress_label = QtWidgets.QLabel(self.loading_main_frame)
        self.loading_progress_label.setGeometry(QtCore.QRect(90, 351, 431, 41))
        self.loading_progress_label.setStyleSheet("font: 11pt \"Alice\";\n"
"color: rgb(196, 196, 196);")
        self.loading_progress_label.setAlignment(QtCore.Qt.AlignCenter)

        self.vertical_layout.addWidget(self.loading_main_frame)
        SplashScreen.setCentralWidget(self.central_widget)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "MainWindow"))
        self.loading_label.setText(_translate("SplashScreen", "loading..."))
        self.loading_progress_label.setText(_translate("SplashScreen", "<strong>LOADING</strong> ASSETS"))


class SplashScreen(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)




