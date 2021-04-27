from PySide2 import QtCore, QtGui, QtWidgets



class Ui_LoadingScreen(object):
    def setupUi(self, LoadingScreen):
        LoadingScreen.setObjectName("LoadingScreen")
        LoadingScreen.resize(629, 632)
        LoadingScreen.setWindowIcon((QtGui.QIcon("icons/Windowicon.png")))
        self.centralwidget = QtWidgets.QWidget(LoadingScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.loadingmainFrame = QtWidgets.QFrame(self.centralwidget)
        self.loadingmainFrame.setStyleSheet("QFrame {    \n"
"    background-color: transparent;    \n"
"    color: rgb(220, 220, 220);\n"
"    border-radius: 10px;\n"
"}")
        self.loadingmainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loadingmainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.loadingmainFrame.setObjectName("loadingmainFrame")
        self.backgroundLabel = QtWidgets.QLabel(self.loadingmainFrame)
        self.backgroundLabel.setGeometry(QtCore.QRect(0, 0, 609, 612))
        self.backgroundLabel.setStyleSheet("")
        self.backgroundLabel.setText("")
        self.backgroundLabel.setPixmap(QtGui.QPixmap("icons/Loadingscreenbackground.png"))
        self.backgroundLabel.setScaledContents(True)

        
        self.backgroundLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.backgroundLabel.setObjectName("backgroundLabel")
        self.progressBar = QtWidgets.QProgressBar(self.loadingmainFrame)
        self.progressBar.setGeometry(QtCore.QRect(215, 392, 178, 10))
        self.progressBar.setStyleSheet("QProgressBar {\n"
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
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.loadingLabel = QtWidgets.QLabel(self.loadingmainFrame)
        self.loadingLabel.setGeometry(QtCore.QRect(95, 410, 431, 21))
        font = QtGui.QFont()
        font.setFamily("Alice")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.loadingLabel.setFont(font)
        self.loadingLabel.setStyleSheet("font: 10pt \"Alice\";\n"
"color: rgb(196, 196, 196);")
        self.loadingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.loadingLabel.setObjectName("loadingLabel")
        self.loadingprogressLabel = QtWidgets.QLabel(self.loadingmainFrame)
        self.loadingprogressLabel.setGeometry(QtCore.QRect(90, 351, 431, 41))
        self.loadingprogressLabel.setStyleSheet("font: 11pt \"Alice\";\n"
"color: rgb(196, 196, 196);")
        self.loadingprogressLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.loadingprogressLabel.setObjectName("loadingprogressLabel")


        self.verticalLayout.addWidget(self.loadingmainFrame)
        LoadingScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoadingScreen)
        QtCore.QMetaObject.connectSlotsByName(LoadingScreen)

    def retranslateUi(self, LoadingScreen):
        _translate = QtCore.QCoreApplication.translate
        LoadingScreen.setWindowTitle(_translate("LoadingScreen", "MainWindow"))
        self.loadingLabel.setText(_translate("LoadingScreen", "loading..."))
        self.loadingprogressLabel.setText(_translate("LoadingScreen", "<strong>LOADING</strong> ASSETS"))


class LoadingScreen(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_LoadingScreen()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)




