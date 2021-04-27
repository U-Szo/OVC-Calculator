from PySide2 import QtCore, QtGui, QtWidgets
from module_view.modules_assigningvalues.valuesWindow import *
import module_view.mainview as mainv
import itertools as itools

class Ui_AssignWindow(object):
    def setupUi(self, MainWindow,admin):
        self.admin=admin
        MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(330, 588)
        MainWindow.setStyleSheet("background-color: transparent;")
        MainWindow.setWindowIcon((QtGui.QIcon("icons/Windowicon.png")))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 330, 589))
        font = QtGui.QFont()
        font.setFamily("Alice")
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
"    border: 1px solid rgb(15, 16, 15);\n"
"}\n"
"\n"
"QTabWidget::tab-bar:top {\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:bottom {\n"
"    bottom: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:left {\n"
"    right: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:right {\n"
"    left: 1px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border-bottom: 1px;\n"
"    border-top: 0px;\n"
"    border-left: 0px;\n"
"    border-right: 0px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    border-style: solid;\n"
"    border-bottom-color:  rgb(25, 26, 25);\n"
"    color:rgb(0,1,0);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: None;\n"
"    background-color: rgb(32, 33, 32);\n"

"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background-color: rgb(15, 16, 15);\n"

"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    background-color: rgb(42,43,42);\n"

"}\n"
"\n"
"QTabBar::tab:top:!selected {\n"
"    margin-top: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected {\n"
"    margin-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8px;\n"
"    margin-right: -1px;\n"
"    padding: 5px 10px 5px 10px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"    border-bottom-color: qlineargradient(spread:reflect, x1:0.488636, y1:0, x2:0, y2:0.00495455, stop:0 rgba(85, 40, 107, 255), stop:1 rgba(32, 33, 32, 255));\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected {\n"
"    border-top-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected {\n"
"    margin-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected {\n"
"    margin-left: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right {\n"
"    min-height: 8px;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected {\n"
"    border-left-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected {\n"
"    border-right-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {\n"
"    margin-bottom: 0;\n"
"}")
        self.tabWidget.setIconSize(QtCore.QSize(60, 30))
        self.tabWidget.setObjectName("tabWidget")
        self.vectors = QtWidgets.QWidget()
        self.vectors.setObjectName("vectors")
        self.modifyselectedvectorButton = QtWidgets.QPushButton(self.vectors)
        self.modifyselectedvectorButton.setGeometry(QtCore.QRect(0, 511, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Alice")
        font.setPointSize(11)
        self.modifyselectedvectorButton.setFont(font)
        self.modifyselectedvectorButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(25, 26, 25);\n"
"    border:None;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(35, 36, 35);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(29, 30, 29);\n"
"}    ")
        self.modifyselectedvectorButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/Modifyselectedbuttontabicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.modifyselectedvectorButton.setIcon(icon)
        self.modifyselectedvectorButton.setIconSize(QtCore.QSize(180, 40))
        self.modifyselectedvectorButton.setObjectName("modifyselectedvectorButton")
        self.modifyselectedvectorButton.clicked.connect(self.showvalues_windowvector)
        self.modifyselectedvectorButton.setShortcut("F2")
        self.vectortreeWidget = QtWidgets.QTreeWidget(self.vectors)
        self.vectortreeWidget.setGeometry(QtCore.QRect(0, 30, 331, 481))
        font = QtGui.QFont()
        font.setFamily("Alice")
        font.setPointSize(11)
        self.vectortreeWidget.setFont(font)
        self.vectortreeWidget.setStyleSheet("QTreeWidget{\n"
"    border:None;\n"
"    background-color: rgb(25, 26, 25);\n"
"    outline:none;"
"}\n"
"QTreeWidget:item:hover{\n"
"    background-color: rgb(46, 35, 52);\n"
"}\n"
"QTreeWidget:item:selected:active:hover{\n"
"    background-color: rgb(80, 45, 107);\n"
"}\n"
"QTreeWidget:item:selected:hover{\n"
"    background-color: rgb(46, 35, 52);\n"
"}\n"
"QTreeWidget:item:selected:active{\n"
"    background-color: rgb(80, 45, 107);\n"
"}\n"
"QTreeWidget:item:selected{\n"
"    background-color: rgb(41, 30, 47);\n"
"    color: rgb(236, 236, 236);\n"
"    font: 10.5pt \"Alice\";\n"
"}\n"
"QHeaderView::section{\n"
"    border:none;\n"
"    color: rgb(236, 236, 236);\n"
"    background-color: rgb(32, 33, 32);\n"
"    font: 11pt \"Alice\";\n"
"}\n"
"\n"
"/* VERTICAL */\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(5, 6, 5);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: rgb(72, 73, 72);\n"
"    min-height: 30px;\n"
"\n"
"}\n"
"QScrollBar::handle:vertical:hover{    \n"
"    background-color: rgb(102,103, 102);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {    \n"
"    background-color: rgb(85, 86, 85);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(72, 73, 72);\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {    \n"
"    background-color: rgb(102,103, 102);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {    \n"
"    background-color: rgb(85, 86, 85);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(72, 73, 72);\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {    \n"
"    background-color: rgb(102,103, 102);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {    \n"
"    background-color: rgb(85, 86, 85);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"/* HORIZONTAL     */\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(5, 6, 5);\n"
"    height: 11px;\n"
"    margin: 0px 15px 0px 15px ;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR horizontal */\n"
"QScrollBar::handle:horizontal {    \n"
"    background-color: rgb(72, 73, 72);\n"
"    min-width: 30px;\n"
"\n"
"}\n"
"QScrollBar::handle:horizontal:hover{    \n"
"    background-color: rgb(102,103, 102);\n"
"}\n"
"QScrollBar::handle:horizontal:pressed {    \n"
"    background-color: rgb(85, 86, 85);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background-color: rgb(72, 73, 72);\n"
"    width: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {    \n"
"    background-color: rgb(102,103, 102);\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {    \n"
"    background-color: rgb(85, 86, 85);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background-color: rgb(72, 73, 72);\n"
"    width: 15px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:hover {    \n"
"    background-color: rgb(102,103, 102);\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {    \n"
"    background-color: rgb(85, 86, 85);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"")
        self.vectortreeWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.vectortreeWidget.setIconSize(QtCore.QSize(30, 30))
        self.vectortreeWidget.setRootIsDecorated(False)
        self.vectortreeWidget.setItemsExpandable(True)
        self.vectortreeWidget.setAllColumnsShowFocus(False)
        self.vectortreeWidget.setHeaderHidden(False)
        self.vectortreeWidget.setExpandsOnDoubleClick(False)
        self.vectortreeWidget.setObjectName("vectortreeWidget")
        self.vectortreeWidget.headerItem().setBackground(0, QtGui.QColor(236, 236, 236))
        self.vectortreeWidget.header().setDefaultSectionSize(60)
        self.vectortreeWidget.header().setStretchLastSection(False)
        self.vectortreeWidget.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.vectortreeWidget.itemDoubleClicked.connect(self.showvalues_windowvector)
        self.Numberofvectorlabel = QtWidgets.QLabel(self.vectors)
        self.Numberofvectorlabel.setGeometry(QtCore.QRect(0, 0, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Alice")
        font.setPointSize(12)
        self.Numberofvectorlabel.setFont(font)
        self.Numberofvectorlabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.46, y1:0, x2:1, y2:0, stop:0 rgba(32, 33, 32, 255), stop:1 rgba(25, 26, 25, 255));\n"
"color: rgb(236, 236, 236);\n"
"border-bottom:0px;\n"
"border-left:0px;\n"
"border-top:0px;\n"
"border-style:solid;\n"
"border-left-color: rgb(85, 40, 107);\n"
"border-bottom-color: qlineargradient(spread:pad, x1:0.46, y1:0, x2:1, y2:0, stop:0 rgba(15, 16, 15, 255), stop:1 rgba(25, 26, 25, 255));\n"
"border-top-color: qlineargradient(spread:pad, x1:0.46, y1:0, x2:1, y2:0, stop:0 rgba(85, 40, 107, 255), stop:1 rgba(25, 26, 25, 255));\n"
"")
        self.Numberofvectorlabel.setText("")
        self.Numberofvectorlabel.setPixmap(QtGui.QPixmap("icons/Selectamounttoassigntabicon.png"))
        self.Numberofvectorlabel.setScaledContents(False)
        self.Numberofvectorlabel.setObjectName("Numberofvectorlabel")
        self.NumberofvectorscomboBoxframe = QtWidgets.QFrame(self.vectors)
        self.NumberofvectorscomboBoxframe.setGeometry(QtCore.QRect(290, 0, 41, 31))
        self.NumberofvectorscomboBoxframe.setStyleSheet("QFrame{\n"
"   background-color: rgb(25, 26, 25);\n"
"   color: rgb(236, 236, 236);\n"
"   selection-color: rgb(236, 236, 236);\n"
"   selection-background-color: rgb(52, 53, 52);\n"
"   outline: none;\n"
"   border:none"
"}\n"
"")
        self.NumberofvectorscomboBox = QtWidgets.QComboBox(self.NumberofvectorscomboBoxframe)
        self.NumberofvectorscomboBox.setGeometry(QtCore.QRect(0, 0, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Alice")
        font.setPointSize(12)
        self.NumberofvectorscomboBox.setFont(font)
        self.NumberofvectorscomboBox.setStyleSheet("QComboBox{\n"
"   background-color: rgb(25, 26, 25);\n"
"   color: rgb(236, 236, 236);\n"
"   selection-color: rgb(236, 236, 236);\n"
"   selection-background-color: rgb(52, 53, 52);\n"
"   outline: none;\n"
"   border:none"
"}\n"
"\n"
"/* VERTICAL */\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(5, 6, 5);\n"
"    width: 9px;\n"
"    margin: 9px 0 9px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: rgb(72, 73, 72);\n"
"    min-height: 30px;\n"
"\n"
"}\n"
"QScrollBar::handle:vertical:hover{    \n"
"    background-color: rgb(102,103, 102);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {    \n"
"    background-color: rgb(85, 86, 85);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(72, 73, 72);\n"
"    height: 9px;\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {    \n"
"    background-color: rgb(102,103, 102);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {    \n"
"    background-color: rgb(85, 86, 85);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(72, 73, 72);\n"
"    height: 9px;\n"
"    border-bottom-left-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {    \n"
"    background-color: rgb(102,103, 102);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {    \n"
"    background-color: rgb(85, 86, 85);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"/* HORIZONTAL     */\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(5, 6, 5);\n"
"    height: 11px;\n"
"    margin: 0px 15px 0px 15px ;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR horizontal */\n"
"QScrollBar::handle:horizontal {    \n"
"    background-color: rgb(72, 73, 72);\n"
"    min-width: 30px;\n"
"\n"
"}\n"
"QScrollBar::handle:horizontal:hover{    \n"
"    background-color: rgb(102,103, 102);\n"
"}\n"
"QScrollBar::handle:horizontal:pressed {    \n"
"    background-color: rgb(85, 86, 85);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background-color: rgb(72, 73, 72);\n"
"    width: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {    \n"
"    background-color: rgb(102,103, 102);\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {    \n"
"    background-color: rgb(85, 86, 85);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background-color: rgb(72, 73, 72);\n"
"    width: 15px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:hover {    \n"
"    background-color: rgb(102,103, 102);\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {    \n"
"    background-color: rgb(85, 86, 85);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"")
        self.NumberofvectorscomboBox.setObjectName("NumberofvectorscomboBox")
        for x in range(0,20):
            self.NumberofvectorscomboBox.addItem("")

        self.NumberofvectorscomboBox.activated.connect(self.hideandshowvectoritems)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/Vectorsassigntabicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.vectors, icon2, "")

        ########################
        ##VECTORES COMO ITEMS###
        ########################

        self.vectorsparentesis_dict,self.vectorsframe_dict,self.vectorsitem_dict,self.vectorsicon_dict={},{},{},{}
        self.vectorslabel_dict,self.vectorsgrid_dict={},{}
        for x in range(1,21):
            self.vectorsparentesis_dict["vector"+str(x)+"parentesisopenlabel"] = QtWidgets.QLabel()
            self.vectorsparentesis_dict["vector"+str(x)+"parentesisopenlabel"].setPixmap(QtGui.QPixmap("icons/Itemparentesisopen.png"))
            self.vectorsparentesis_dict["vector"+str(x)+"parentesisopenlabel"].setScaledContents(True)
            self.vectorsparentesis_dict["vector"+str(x)+"parentesisopenlabel"].setFixedWidth(5)
            self.vectorsparentesis_dict["vector"+str(x)+"parentesisclosedlabel"] = QtWidgets.QLabel()
            self.vectorsparentesis_dict["vector"+str(x)+"parentesisclosedlabel"].setPixmap(QtGui.QPixmap("icons/Itemparentesisclose.png"))
            self.vectorsparentesis_dict["vector"+str(x)+"parentesisclosedlabel"].setScaledContents(True)
            self.vectorsparentesis_dict["vector"+str(x)+"parentesisclosedlabel"].setFixedWidth(5)
            self.vectorsframe_dict["vector"+str(x)+"frame"] = QtWidgets.QFrame()
            self.vectorsitem_dict["vector"+str(x)+"item"] = QtWidgets.QTreeWidgetItem(self.vectortreeWidget)
            font = QtGui.QFont()
            font.setFamily("Alice")
            font.setPointSize(12)
            self.vectorsitem_dict["vector"+str(x)+"item"].setFont(0, font)
            self.vectorsicon_dict["vector"+str(x)+"item"] = QtGui.QIcon()
            self.vectorsicon_dict["vector"+str(x)+"item"].addPixmap(QtGui.QPixmap("icons/individualvectoricon/vector"+str(x)+"icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.vectorsicon_dict["vector"+str(x)+"item"].addPixmap(QtGui.QPixmap("icons/individualvectoricon/vector"+str(x)+"icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
            self.vectorsicon_dict["vector"+str(x)+"item"].addPixmap(QtGui.QPixmap("icons/individualvectoricon/vector"+str(x)+"icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
            self.vectorsitem_dict["vector"+str(x)+"item"].setIcon(0, self.vectorsicon_dict["vector"+str(x)+"item"])
            self.vectorslabel_dict["vector"+str(x)+"label"] = QtWidgets.QLabel()
            self.vectorslabel_dict["vector"+str(x)+"label"].setStyleSheet("background-color: transparent;\n""color: rgb(236, 236, 236);\n")
            self.vectorslabel_dict["vector"+str(x)+"label"].setFont(font)
            self.vectorsgrid_dict["vector"+str(x)+"grid"] = QtWidgets.QHBoxLayout(self.vectorsframe_dict["vector"+str(x)+"frame"])
            self.vectorsgrid_dict["vector"+str(x)+"grid"].setSpacing(0)
            self.vectorsgrid_dict["vector"+str(x)+"grid"].addWidget(self.vectorsparentesis_dict["vector"+str(x)+"parentesisopenlabel"], 0, alignment=QtCore.Qt.AlignLeft)
            self.vectorsgrid_dict["vector"+str(x)+"grid"].addWidget(self.vectorslabel_dict["vector"+str(x)+"label"], 1, alignment=QtCore.Qt.AlignCenter)
            self.vectorsgrid_dict["vector"+str(x)+"grid"].addWidget(self.vectorsparentesis_dict["vector"+str(x)+"parentesisclosedlabel"], 2, alignment=QtCore.Qt.AlignLeft)
            self.vectortreeWidget.setItemWidget(self.vectorsitem_dict["vector"+str(x)+"item"], 1, self.vectorsframe_dict["vector"+str(x)+"frame"])

        ####################
        ##HIDE VECTORITEMS##
        ####################
        for x in range(1,20):
            self.vectorsitem_dict["vector"+str(x+1)+"item"].setHidden(True)

        self.Matrices = QtWidgets.QWidget()
        self.Matrices.setObjectName("Matrices")
        self.modifyselectedmatrixButton = QtWidgets.QPushButton(self.Matrices)
        self.modifyselectedmatrixButton.setGeometry(QtCore.QRect(0, 511, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Alice")
        font.setPointSize(11)
        self.modifyselectedmatrixButton.setFont(font)
        self.modifyselectedmatrixButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(25, 26, 25);\n"
"    border:None;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(35, 36, 35);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(29, 30, 29);\n"
"}    ")
        self.modifyselectedmatrixButton.setText("")
        self.modifyselectedmatrixButton.setIcon(icon)
        self.modifyselectedmatrixButton.setIconSize(QtCore.QSize(180, 40))
        self.modifyselectedmatrixButton.setObjectName("modifyselectedmatrixButton")
        self.modifyselectedmatrixButton.clicked.connect(self.showvalues_windowmatrix)
        self.modifyselectedmatrixButton.setShortcut("F2")
        self.matrixtreeWidget = QtWidgets.QTreeWidget(self.Matrices)
        self.matrixtreeWidget.setGeometry(QtCore.QRect(0, 30, 331, 481))
        font = QtGui.QFont()
        font.setFamily("Alice")
        font.setPointSize(11)
        self.matrixtreeWidget.setFont(font)
        self.matrixtreeWidget.setStyleSheet("QTreeWidget{\n"
"    border:None;\n"
"    background-color: rgb(25, 26, 25);\n"
"    outline:none;"
"}\n"
"QTreeWidget:item:hover{\n"
"    background-color: rgb(46, 35, 52);\n"
"}\n"
"QTreeWidget:item:selected:active:hover{\n"
"    background-color: rgb(80, 45, 107);\n"
"}\n"
"QTreeWidget:item:selected:hover{\n"
"    background-color: rgb(46, 35, 52);\n"
"}\n"
"QTreeWidget:item:selected:active{\n"
"    background-color: rgb(80, 45, 107);\n"
"}\n"
"QTreeWidget:item:selected{\n"
"    background-color: rgb(41, 30, 47);\n"
"    color: rgb(236, 236, 236);\n"
"    font: 10.5pt \"Alice\";\n"
"}\n"
"QHeaderView::section{\n"
"    border:none;\n"
"    color: rgb(236, 236, 236);\n"
"    background-color: rgb(32, 33, 32);\n"
"    font: 11pt \"Alice\";\n"
"}\n"
"\n"
"/* VERTICAL */\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(5, 6, 5);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: rgb(72, 73, 72);\n"
"    min-height: 30px;\n"
"\n"
"}\n"
"QScrollBar::handle:vertical:hover{    \n"
"    background-color: rgb(102,103, 102);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {    \n"
"    background-color: rgb(85, 86, 85);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(72, 73, 72);\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {    \n"
"    background-color: rgb(102,103, 102);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {    \n"
"    background-color: rgb(85, 86, 85);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(72, 73, 72);\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {    \n"
"    background-color: rgb(102,103, 102);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {    \n"
"    background-color: rgb(85, 86, 85);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"/* HORIZONTAL     */\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(5, 6, 5);\n"
"    height: 11px;\n"
"    margin: 0px 15px 0px 15px ;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR horizontal */\n"
"QScrollBar::handle:horizontal {    \n"
"    background-color: rgb(72, 73, 72);\n"
"    min-width: 30px;\n"
"\n"
"}\n"
"QScrollBar::handle:horizontal:hover{    \n"
"    background-color: rgb(102,103, 102);\n"
"}\n"
"QScrollBar::handle:horizontal:pressed {    \n"
"    background-color: rgb(85, 86, 85);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background-color: rgb(72, 73, 72);\n"
"    width: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {    \n"
"    background-color: rgb(102,103, 102);\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {    \n"
"    background-color: rgb(85, 86, 85);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background-color: rgb(72, 73, 72);\n"
"    width: 15px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:hover {    \n"
"    background-color: rgb(102,103, 102);\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {    \n"
"    background-color: rgb(85, 86, 85);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"")
        self.matrixtreeWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.matrixtreeWidget.setIconSize(QtCore.QSize(30, 30))
        self.matrixtreeWidget.setRootIsDecorated(False)
        self.matrixtreeWidget.setItemsExpandable(True)
        self.matrixtreeWidget.setAllColumnsShowFocus(False)
        self.matrixtreeWidget.setHeaderHidden(False)
        self.matrixtreeWidget.setExpandsOnDoubleClick(False)
        self.matrixtreeWidget.setObjectName("matrixtreeWidget")
        self.matrixtreeWidget.headerItem().setBackground(0, QtGui.QColor(236, 236, 236))
        self.matrixtreeWidget.header().setStretchLastSection(False)
        self.matrixtreeWidget.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.matrixtreeWidget.itemDoubleClicked.connect(self.showvalues_windowmatrix)
        self.Numberofmatrixlabel = QtWidgets.QLabel(self.Matrices)
        self.Numberofmatrixlabel.setGeometry(QtCore.QRect(0, 0, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Alice")
        font.setPointSize(12)
        self.Numberofmatrixlabel.setFont(font)
        self.Numberofmatrixlabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.46, y1:0, x2:1, y2:0, stop:0 rgba(32, 33, 32, 255), stop:1 rgba(25, 26, 25, 255));\n"
"color: rgb(236, 236, 236);\n"
"border-bottom:0px;\n"
"border-left:0px;\n"
"border-top:0px;\n"
"border-style:solid;\n"
"border-left-color: rgb(85, 40, 107);\n"
"border-bottom-color: qlineargradient(spread:pad, x1:0.46, y1:0, x2:1, y2:0, stop:0 rgba(15, 16, 15, 255), stop:1 rgba(25, 26, 25, 255));\n"
"border-top-color: qlineargradient(spread:pad, x1:0.46, y1:0, x2:1, y2:0, stop:0 rgba(85, 40, 107, 255), stop:1 rgba(25, 26, 25, 255));\n"
"")
        self.Numberofmatrixlabel.setText("")
        self.Numberofmatrixlabel.setPixmap(QtGui.QPixmap("icons/Selectamounttoassigntabicon.png"))
        self.Numberofmatrixlabel.setScaledContents(False)
        self.Numberofmatrixlabel.setObjectName("Numberofmatrixlabel")
        self.NumberofmatrixcomboBoxframe = QtWidgets.QFrame(self.Matrices)
        self.NumberofmatrixcomboBoxframe.setGeometry(QtCore.QRect(290, 0, 41, 31))
        self.NumberofmatrixcomboBoxframe.setStyleSheet("QFrame{\n"
"   background-color: rgb(25, 26, 25);\n"
"   color: rgb(236, 236, 236);\n"
"   selection-color: rgb(236, 236, 236);\n"
"   selection-background-color: rgb(52, 53, 52);\n"
"   outline: none;\n"
"   border:none"
"}\n"
"")
        self.NumberofmatrixcomboBox = QtWidgets.QComboBox(self.NumberofmatrixcomboBoxframe)
        self.NumberofmatrixcomboBox.setGeometry(QtCore.QRect(0, 0, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Alice")
        font.setPointSize(12)
        self.NumberofmatrixcomboBox.setFont(font)
        self.NumberofmatrixcomboBox.setStyleSheet("QComboBox{\n"
"   background-color: rgb(25, 26, 25);\n"
"   color: rgb(236, 236, 236);\n"
"   selection-color: rgb(236, 236, 236);\n"
"   selection-background-color: rgb(52, 53, 52);\n"
"   outline: none;\n"
"   border:none"
"}\n"
"\n"
"/* VERTICAL */\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(5, 6, 5);\n"
"    width: 9px;\n"
"    margin: 9px 0 9px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: rgb(72, 73, 72);\n"
"    min-height: 30px;\n"
"\n"
"}\n"
"QScrollBar::handle:vertical:hover{    \n"
"    background-color: rgb(102,103, 102);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {    \n"
"    background-color: rgb(85, 86, 85);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(72, 73, 72);\n"
"    height: 9px;\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {    \n"
"    background-color: rgb(102,103, 102);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {    \n"
"    background-color: rgb(85, 86, 85);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(72, 73, 72);\n"
"    height: 9px;\n"
"    border-bottom-left-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {    \n"
"    background-color: rgb(102,103, 102);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {    \n"
"    background-color: rgb(85, 86, 85);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"/* HORIZONTAL     */\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(5, 6, 5);\n"
"    height: 11px;\n"
"    margin: 0px 15px 0px 15px ;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR horizontal */\n"
"QScrollBar::handle:horizontal {    \n"
"    background-color: rgb(72, 73, 72);\n"
"    min-width: 30px;\n"
"\n"
"}\n"
"QScrollBar::handle:horizontal:hover{    \n"
"    background-color: rgb(102,103, 102);\n"
"}\n"
"QScrollBar::handle:horizontal:pressed {    \n"
"    background-color: rgb(85, 86, 85);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background-color: rgb(72, 73, 72);\n"
"    width: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {    \n"
"    background-color: rgb(102,103, 102);\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {    \n"
"    background-color: rgb(85, 86, 85);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background-color: rgb(72, 73, 72);\n"
"    width: 15px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:hover {    \n"
"    background-color: rgb(102,103, 102);\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {    \n"
"    background-color: rgb(85, 86, 85);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"")
        self.NumberofmatrixcomboBox.setObjectName("NumberofmatrixcomboBox")
        for x in range(0,20):
            self.NumberofmatrixcomboBox.addItem("")

        self.NumberofmatrixcomboBox.activated.connect(self.hideandshowmatrixitems)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/Matrixassigntabicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Matrices, icon3, "")

        #######################
        ##MATRICES COMO ITEMS##
        #######################

        self.matricesparentesis_dict,self.matricesframe_dict,self.matricesitem_dict,self.matricesicon_dict={},{},{},{}
        self.matricesvaluesgridWidget_dict,self.matricesvaluesgrid_dict,self.matricesgrid_dict={},{},{}
        for x in range(1,21):
            self.matricesparentesis_dict["matrix"+str(x)+"parentesisopenlabel"] = QtWidgets.QLabel()
            self.matricesparentesis_dict["matrix"+str(x)+"parentesisopenlabel"].setPixmap(QtGui.QPixmap("icons/Itemparentesisopen.png"))
            self.matricesparentesis_dict["matrix"+str(x)+"parentesisopenlabel"].setScaledContents(True)
            self.matricesparentesis_dict["matrix"+str(x)+"parentesisopenlabel"].setFixedWidth(5)
            self.matricesparentesis_dict["matrix"+str(x)+"parentesisclosedlabel"] = QtWidgets.QLabel()
            self.matricesparentesis_dict["matrix"+str(x)+"parentesisclosedlabel"].setPixmap(QtGui.QPixmap("icons/Itemparentesisclose.png"))
            self.matricesparentesis_dict["matrix"+str(x)+"parentesisclosedlabel"].setScaledContents(True)
            self.matricesparentesis_dict["matrix"+str(x)+"parentesisclosedlabel"].setFixedWidth(5)
            self.matricesframe_dict["matrix"+str(x)+"frame"] = QtWidgets.QFrame()
            self.matricesitem_dict["matrix"+str(x)+"item"] = QtWidgets.QTreeWidgetItem(self.matrixtreeWidget)
            font = QtGui.QFont()
            font.setFamily("Alice")
            font.setPointSize(12)
            self.matricesitem_dict["matrix"+str(x)+"item"].setFont(0, font)
            self.matricesicon_dict["matrix"+str(x)+"item"] = QtGui.QIcon()
            self.matricesicon_dict["matrix"+str(x)+"item"].addPixmap(QtGui.QPixmap("icons/individualmatrixicon/matrix"+str(x)+"icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.matricesicon_dict["matrix"+str(x)+"item"].addPixmap(QtGui.QPixmap("icons/individualmatrixicon/matrix"+str(x)+"icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
            self.matricesicon_dict["matrix"+str(x)+"item"].addPixmap(QtGui.QPixmap("icons/individualmatrixicon/matrix"+str(x)+"icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
            self.matricesitem_dict["matrix"+str(x)+"item"].setIcon(0, self.matricesicon_dict["matrix"+str(x)+"item"])
            self.matricesvaluesgridWidget_dict["matrix"+str(x)+"valuesgridWidget"] = QtWidgets.QWidget()
            self.matricesvaluesgrid_dict["matrix"+str(x)+"valuesgrid"] = QtWidgets.QGridLayout(self.matricesvaluesgridWidget_dict["matrix"+str(x)+"valuesgridWidget"])
            self.matricesvaluesgrid_dict["matrix"+str(x)+"valuesgrid"].setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
            self.matricesvaluesgrid_dict["matrix"+str(x)+"valuesgrid"].setContentsMargins(0, 0, 0, 0)
            self.matricesgrid_dict["matrix"+str(x)+"grid"] = QtWidgets.QHBoxLayout(self.matricesframe_dict["matrix"+str(x)+"frame"])
            self.matricesgrid_dict["matrix"+str(x)+"grid"].setSpacing(0)
            self.matricesgrid_dict["matrix"+str(x)+"grid"].setGeometry(QtCore.QRect(0, 0, 16, 16))
            self.matricesgrid_dict["matrix"+str(x)+"grid"].setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
            self.matricesgrid_dict["matrix"+str(x)+"grid"].addWidget(self.matricesparentesis_dict["matrix"+str(x)+"parentesisopenlabel"], 0, alignment=QtCore.Qt.AlignLeft)
            self.matricesgrid_dict["matrix"+str(x)+"grid"].addWidget(self.matricesvaluesgridWidget_dict["matrix"+str(x)+"valuesgridWidget"], 1, alignment=QtCore.Qt.AlignCenter)
            self.matricesgrid_dict["matrix"+str(x)+"grid"].addWidget(self.matricesparentesis_dict["matrix"+str(x)+"parentesisclosedlabel"], 2, alignment=QtCore.Qt.AlignLeft)
            self.matrixtreeWidget.setItemWidget(self.matricesitem_dict["matrix"+str(x)+"item"], 1, self.matricesframe_dict["matrix"+str(x)+"frame"])
        matriceslabelcell_font = QtGui.QFont()
        matriceslabelcell_font.setFamily("Alice")
        matriceslabelcell_font.setPointSize(12)
        matriceslabelcell_stylesheet = "background-color: transparent;\n""color: rgb(236, 236, 236);\n"
        self.matriceslabelcell_dict={}
        for z in  range(1,21):
            for x, y in itools.product(range(1,11), range(1,11)):
                self.matriceslabelcell_dict["matrix"+str(z)+"labelcell"+str(x)+"_"+str(y)] = QtWidgets.QLabel(self.matricesvaluesgridWidget_dict["matrix"+str(z)+"valuesgridWidget"] )
                self.matriceslabelcell_dict["matrix"+str(z)+"labelcell"+str(x)+"_"+str(y)].setStyleSheet(matriceslabelcell_stylesheet)
                self.matriceslabelcell_dict["matrix"+str(z)+"labelcell"+str(x)+"_"+str(y)].setFont(matriceslabelcell_font)
                self.matricesvaluesgrid_dict["matrix"+str(z)+"valuesgrid"].addWidget(self.matriceslabelcell_dict["matrix"+str(z)+"labelcell"+str(x)+"_"+str(y)], (x-1), (y-1), 1, 1, alignment=QtCore.Qt.AlignCenter)
                self.matriceslabelcell_dict["matrix"+str(z)+"labelcell"+str(x)+"_"+str(y)].setHidden(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 330, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.statusbar.hide()

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.currentChanged.connect(self.admin.ui.updatematrixtreeitemsontabchange)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.typeofassigntomake = 0

    def hideandshowvectoritems(self):
        y = int(self.NumberofvectorscomboBox.currentText())
        for x in range(1, 21):
            if x <= y:
                self.vectorsitem_dict["vector"+str(x)+"item"].setHidden(False)
            else:
                self.vectorsitem_dict["vector"+str(x)+"item"].setHidden(True)


    def hideandshowmatrixitems(self):
        y = int(self.NumberofmatrixcomboBox.currentText())
        for x in range(1, 21):
            if x <= y:
                self.matricesitem_dict["matrix"+str(x)+"item"].setHidden(False)
            else:
                self.matricesitem_dict["matrix"+str(x)+"item"].setHidden(True)

    def showvalues_windowvector(self):
        self.admin.assignvalueswindow.valueswindow.hide()

        self.typeofassigntomake = "vector"

        getSelected = self.vectortreeWidget.selectedItems()
        try:
            selected_vector = self.vectortreeWidget.indexOfTopLevelItem(getSelected[0])
        except:
            self.admin.admin.window.errorwindow.show()
            self.admin.admin.window.errorwindow.ui.Errorwindowbodylabel.setText("Select Vector to modify")
            return
        selected_vector_columns = self.admin.admin.vectorscolumns[int(selected_vector)]
        selected_vector_values = self.admin.admin.vectorsarrays[int(selected_vector)]

        self.admin.assignvalueswindow.valueswindow.show()
        self.admin.assignvalueswindow.valueswindow.ui.rowscomboBox.setCurrentIndex(0)
        self.admin.assignvalueswindow.valueswindow.ui.rowscomboBox.setEnabled(False)
        self.admin.assignvalueswindow.valueswindow.ui.selectediconlabel.setPixmap(QtGui.QPixmap("icons/individualvectoricon/vector"+str(int(selected_vector)+1)+"icon.png"))
        self.admin.assignvalueswindow.valueswindow.ui.columnscomboBox.setCurrentIndex(int(selected_vector_columns)-1)
        self.admin.assignvalueswindow.valueswindow.ui.hideandshowrows()
        self.admin.assignvalueswindow.valueswindow.ui.hideandshowcolumns()

        for x in range(1,11):
            for y in range(1,11):
                self.admin.assignvalueswindow.valueswindow.ui.cellslineedit_dict["cell"+str(x)+"_"+str(y)].setText("")

        for y in range(0,selected_vector_columns):
                valueofcell = str(selected_vector_values[0][y])
                self.admin.assignvalueswindow.valueswindow.ui.cellslineedit_dict["cell"+str(1)+"_"+str(y+1)].setText(valueofcell)

    def showvalues_windowmatrix(self):
        self.admin.assignvalueswindow.valueswindow.hide()

        self.typeofassigntomake = "matrix"

        getSelected = self.matrixtreeWidget.selectedItems()
        try:
            selected_matrix = self.matrixtreeWidget.indexOfTopLevelItem(getSelected[0])
        except:
            self.admin.admin.window.errorwindow.show()
            self.admin.admin.window.errorwindow.ui.Errorwindowbodylabel.setText("Select Matrix to modify")
            return
        selected_matrix_rows = self.admin.admin.matricesrows[int(selected_matrix)]
        selected_matrix_columns = self.admin.admin.matricescolumns[int(selected_matrix)]
        selected_matrix_values = self.admin.admin.matricesarrays[int(selected_matrix)]

        self.admin.assignvalueswindow.valueswindow.show()
        self.admin.assignvalueswindow.valueswindow.ui.rowscomboBox.setEnabled(True)
        self.admin.assignvalueswindow.valueswindow.ui.rowscomboBox.setCurrentIndex(int(selected_matrix_rows)-1)
        self.admin.assignvalueswindow.valueswindow.ui.selectediconlabel.setPixmap(QtGui.QPixmap("icons/individualmatrixicon/matrix"+str(int(selected_matrix)+1)+"icon.png"))
        self.admin.assignvalueswindow.valueswindow.ui.columnscomboBox.setCurrentIndex(int(selected_matrix_columns)-1)
        self.admin.assignvalueswindow.valueswindow.ui.hideandshowrows()
        self.admin.assignvalueswindow.valueswindow.ui.hideandshowcolumns()

        for x in range(1,11):
            for y in range(1,11):
                self.admin.assignvalueswindow.valueswindow.ui.cellslineedit_dict["cell"+str(x)+"_"+str(y)].setText("")

        for x in range(0,selected_matrix_rows):
            for y in range(0,selected_matrix_columns):
                valueofcell = str(selected_matrix_values[x][y])
                self.admin.assignvalueswindow.valueswindow.ui.cellslineedit_dict["cell"+str(x+1)+"_"+str(y+1)].setText(valueofcell)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.vectortreeWidget.headerItem().setText(0, _translate("MainWindow", (" Vector"+" "*15)))
        self.vectortreeWidget.headerItem().setText(1, _translate("MainWindow", ("    Values"+" "*55)))
        __sortingEnabled = self.vectortreeWidget.isSortingEnabled()
        self.vectortreeWidget.setSortingEnabled(False)
        self.vectortreeWidget.setSortingEnabled(__sortingEnabled)
        for x in range(0,20):
            self.NumberofvectorscomboBox.setItemText(x, _translate("MainWindow", str(x+1)))
        self.matrixtreeWidget.headerItem().setText(0, _translate("MainWindow", (" Matrix"+" "*15)))
        self.matrixtreeWidget.headerItem().setText(1, _translate("MainWindow", ("    Values"+" "*55)))
        __sortingEnabled = self.matrixtreeWidget.isSortingEnabled()
        self.matrixtreeWidget.setSortingEnabled(False)
        self.matrixtreeWidget.setSortingEnabled(__sortingEnabled)
        for x in range(0,20):
            self.NumberofmatrixcomboBox.setItemText(x, _translate("MainWindow", str(x+1)))
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

class AssignWindow(QtWidgets.QMainWindow):
    def __init__(self,admin,parent=None):
        super(AssignWindow, self).__init__()
        self.ui = Ui_AssignWindow()
        self.admin=admin
        self.ui.setupUi(self,self.admin)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.valueswindow = ValuesWindow(self,self.admin)
        self.valueswindow.setWindowTitle("Assign Values")
        self.valueswindow.hide()

    def closeEvent(self, event):
        global assignvaluewindowhidden
        assignvaluewindowhidden=True
        event.accept()
    def showEvent(self, e):
        self.Assignposx = mainv.Mainposx - 330
        self.x = self.Assignposx
        self.y = mainv.Mainposy
        self.move(self.x,self.y)