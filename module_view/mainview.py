from PySide2 import QtCore, QtGui, QtWidgets
import numpy as np
from fractions import Fraction
import itertools as itools
#########################
##WINDOW CLASSES IMPORT##
#########################
from module_view.modules_informationanderror.errorWindow import *
from module_view.modules_informationanderror.infoWindow import *
from module_view.modules_assigningvalues.assignWindow import *
from module_view.modules_assigningvalues.valuesWindow import *
######################
##STYLESHEETS IMPORT##
######################
import module_view.mainview_stylesheets.mainviewStylesheetsPoststart as mvssps
import module_view.mainview_stylesheets.vectorandmatrixTabStylesheet as vmtss
import module_view.mainview_stylesheets.anglesTabStylesheet as atss
import module_view.mainview_stylesheets.eigenvectorsTabStylesheet as evtss
import module_view.mainview_stylesheets.systemofequationsTabStylesheet as soetss
import module_view.mainview_stylesheets.mainviewsideFramesStylesheet as mvsfss

######################
# VARIABLES GLOBALES #
######################

assignvaluewindowhidden=True
Mainposx=0
Mainposy=0
startupmatrices=True
firsttabchange=True

######################
#### CLASES DE UI ####
######################
class Ui_MainWindow(object):
    def setupUi(self, MainWindow,admin):
        self.admin=admin
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(724, 588)
        MainWindow.setStyleSheet("background-color: rgb(27,28,27);\n")
        MainWindow.setWindowIcon((QtGui.QIcon("icons/Windowicon.png")))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.degorrad="RAD"
        self.ddordms= "DMS"

        ######################
        ##SCREEN SCROLL AREA##
        ######################

        self.screen_scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.screen_scrollArea.setGeometry(QtCore.QRect(112, 119, 481, 159))
        self.screen_scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.screen_scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.screen_scrollArea.setWidgetResizable(True)
        self.screen_scrollArea.setObjectName("screen_scrollArea")

        self.screen_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.screen_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 479, 157))
        self.screen_scrollAreaWidgetContents.setObjectName("screen_scrollAreaWidgetContents")
        self.screen_scrollAreaWidgetContents.setMinimumSize(0, 0)
        self.screen_scrollAreaWidgetContents.setStyleSheet("background-color: rgb(17, 18, 17);\n")
        self.screen_gridLayout = QtWidgets.QHBoxLayout(self.screen_scrollAreaWidgetContents)
        self.screen_gridLayout.setSpacing(0)
        self.screen_gridLayout.setObjectName("screen_gridLayout")

        self.screen_matrixgridLayoutWidget = QtWidgets.QWidget()
        self.screen_matrixgridLayout = QtWidgets.QHBoxLayout(self.screen_matrixgridLayoutWidget)
        self.screen_matrixgridLayout.setSpacing(5)
        ######################
        ##SCREEN VALUES GRID##
        ######################
        self.resultmatrixparentesisopenlabel = QtWidgets.QLabel()
        self.resultmatrixparentesisopenlabel.setPixmap(QtGui.QPixmap("icons/Itemparentesisopen.png"))
        self.resultmatrixparentesisopenlabel.setScaledContents(True)
        self.resultmatrixparentesisopenlabel.setFixedWidth(5)
        self.resultmatrixparentesisclosedlabel = QtWidgets.QLabel()
        self.resultmatrixparentesisclosedlabel.setPixmap(QtGui.QPixmap("icons/Itemparentesisclose.png"))
        self.resultmatrixparentesisclosedlabel.setScaledContents(True)
        self.resultmatrixparentesisclosedlabel.setFixedWidth(5)
        self.screen_valuesgridLayoutWidget = QtWidgets.QWidget()
        self.screen_valuesgridLayout = QtWidgets.QGridLayout(self.screen_valuesgridLayoutWidget)
        self.screen_valuesgridLayout.setContentsMargins(0, 0, 0, 0)
        self.screen_valuesgridLayout.setHorizontalSpacing(20)
        self.screen_valuesgridLayout.setVerticalSpacing(5)
        self.screen_gridLayout.addWidget(self.screen_matrixgridLayoutWidget, 1, alignment=QtCore.Qt.AlignCenter)
        self.screen_matrixgridLayout.addWidget(self.resultmatrixparentesisopenlabel, 0, alignment=QtCore.Qt.AlignLeft)
        self.screen_matrixgridLayout.addWidget(self.screen_valuesgridLayoutWidget, 1, alignment=QtCore.Qt.AlignCenter)
        self.screen_matrixgridLayout.addWidget(self.resultmatrixparentesisclosedlabel, 2, alignment=QtCore.Qt.AlignLeft)
        self.screen_scrollArea.setWidget(self.screen_scrollAreaWidgetContents)
        self.resultmatrixparentesisopenlabel.setHidden(True)
        self.resultmatrixparentesisclosedlabel.setHidden(True)
        ###############################
        ## SCROLL AREA VALUES LABELS ##
        ###############################
        font = QtGui.QFont()
        font.setFamily("Alice")
        font.setPointSize(12)
        intfloatfont = QtGui.QFont()
        intfloatfont.setFamily("Alice")
        intfloatfont.setPointSize(15)
        stringstylesheetresult = "background-color: transparent;\n""color: rgb(236, 236, 236);\n"

        self.result_matrixlabelcelldict={}
        for x, y in itools.product(range(1,11), range(1,11)):
            self.result_matrixlabelcelldict["result_matrixlabelcell"+str(x)+"_"+str(y)] = QtWidgets.QLabel(self.screen_valuesgridLayoutWidget)
            self.result_matrixlabelcelldict["result_matrixlabelcell"+str(x)+"_"+str(y)].setStyleSheet(stringstylesheetresult)
            self.result_matrixlabelcelldict["result_matrixlabelcell"+str(x)+"_"+str(y)].setFont(font)
            self.screen_valuesgridLayout.addWidget(self.result_matrixlabelcelldict["result_matrixlabelcell"+str(x)+"_"+str(y)], (x-1), (y-1), 1, 1, alignment=QtCore.Qt.AlignCenter)
            self.result_matrixlabelcelldict["result_matrixlabelcell"+str(x)+"_"+str(y)].setHidden(True)

        self.resultlabelintorfloat = QtWidgets.QLabel()
        self.resultlabelintorfloat.setStyleSheet("background-color: transparent;\n""color: rgb(236, 236, 236);\n")
        self.resultlabelintorfloat.setFont(intfloatfont)
        self.screen_gridLayout.addWidget(self.resultlabelintorfloat, 103, alignment=QtCore.Qt.AlignCenter)
        self.resultlabelintorfloat.setHidden(True)

        self.resultlabelerror = QtWidgets.QLabel()
        self.resultlabelerror.setStyleSheet("background-color: transparent;\n""color: rgb(232, 17, 35);\n")
        self.resultlabelerror.setFont(intfloatfont)
        self.screen_gridLayout.addWidget(self.resultlabelerror, 4, alignment=QtCore.Qt.AlignLeft)
        self.resultlabelerror.setHidden(True)
 
        self.main_title_label_top = QtWidgets.QLabel(self.centralwidget)
        self.main_title_label_top.setGeometry(QtCore.QRect(2, 9, 611, 91))
        self.main_title_label_top.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:1, y2:0, stop:0 rgba(25, 26, 25, 255), stop:1 rgba(29, 30, 29, 255));\n")
        self.main_title_label_top.setText("")
        self.main_title_label_top.setAlignment(QtCore.Qt.AlignCenter)
        self.main_title_label_top.setObjectName("main_title_label_top")
        self.tab_buttonsframe = QtWidgets.QFrame(self.centralwidget)
        self.tab_buttonsframe.setGeometry(QtCore.QRect(0, 70, 91, 519))
        self.tab_buttonsframe.setStyleSheet(mvsfss.frame_stylesheet)
        self.tab_buttonsframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tab_buttonsframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tab_buttonsframe.setObjectName("frame")
        self.vectorsButton = QtWidgets.QPushButton(self.tab_buttonsframe)
        self.vectorsButton.setGeometry(QtCore.QRect(0, 29, 81, 41))
        self.vectorsButton.setStyleSheet(mvsfss.vectorsButton_stylesheet)
        self.vectorsButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/Vectoresicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.vectorsButton.setIcon(icon)
        self.vectorsButton.setIconSize(QtCore.QSize(24, 24))
        self.vectorsButton.setCheckable(True)
        self.vectorsButton.setObjectName("vectorsButton")
        self.vectorsButton.clicked.connect(self.vectorsButtonstate)
        self.matrixButton = QtWidgets.QPushButton(self.tab_buttonsframe)
        self.matrixButton.setGeometry(QtCore.QRect(0, 69, 81, 41))
        self.matrixButton.setStyleSheet(mvsfss.matrixButton_stylesheet)
        self.matrixButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/Matricesicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.matrixButton.setIcon(icon1)
        self.matrixButton.setIconSize(QtCore.QSize(24, 24))
        self.matrixButton.setCheckable(True)
        self.matrixButton.setObjectName("matrixButton")
        self.matrixButton.clicked.connect(self.matrixButtonstate)
        self.anglesButton = QtWidgets.QPushButton(self.tab_buttonsframe)
        self.anglesButton.setGeometry(QtCore.QRect(0, 109, 81, 41))
        self.anglesButton.setStyleSheet(mvsfss.anglesButton_stylesheet)
        self.anglesButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/Anguloicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.anglesButton.setIcon(icon2)
        self.anglesButton.setIconSize(QtCore.QSize(19, 19))
        self.anglesButton.setCheckable(True)
        self.anglesButton.setObjectName("anglesButton")
        self.anglesButton.clicked.connect(self.anglesButtonstate)
        self.eigenvaluesButton = QtWidgets.QPushButton(self.tab_buttonsframe)
        self.eigenvaluesButton.setGeometry(QtCore.QRect(0, 149, 81, 41))
        self.eigenvaluesButton.setStyleSheet(mvsfss.eigenvaluesButton_sylesheet)
        self.eigenvaluesButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/Eigenvaluesicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.eigenvaluesButton.setIcon(icon4)
        self.eigenvaluesButton.setIconSize(QtCore.QSize(17, 17))
        self.eigenvaluesButton.setCheckable(True)
        self.eigenvaluesButton.setObjectName("eigenvaluesButton")
        self.eigenvaluesButton.clicked.connect(self.eigenvaluesButtonstate)
        self.systemofequationButton = QtWidgets.QPushButton(self.tab_buttonsframe)
        self.systemofequationButton.setGeometry(QtCore.QRect(0, 189, 81, 41))
        self.systemofequationButton.setStyleSheet(mvsfss.systemofequationButton_stylesheet)
        self.systemofequationButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/Systemofequationsicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.systemofequationButton.setIcon(icon5)
        self.systemofequationButton.setIconSize(QtCore.QSize(27, 27))
        self.systemofequationButton.setCheckable(True)
        self.systemofequationButton.setObjectName("systemofequationButton")
        self.systemofequationButton.clicked.connect(self.systemofequationButtonstate)
        self.decorativebottomButton = QtWidgets.QPushButton(self.tab_buttonsframe)
        self.decorativebottomButton.setEnabled(False)
        self.decorativebottomButton.setGeometry(QtCore.QRect(0, 229, 81, 221))
        self.decorativebottomButton.setStyleSheet(mvsfss.decorativebottomButton_stylesheet)
        self.decorativebottomButton.setText("")
        self.decorativebottomButton.setCheckable(True)
        self.Decorativelabelbottom = QtWidgets.QLabel(self.centralwidget)
        self.Decorativelabelbottom.setGeometry(QtCore.QRect(-10, 519, 634, 91))
        self.Decorativelabelbottom.setStyleSheet("background-color: rgb(25, 26, 25);")
        self.Decorativelabelbottom.setText("")
        self.Decorativelabelbottom.setObjectName("Decorativelabelbottom")
        self.infoButton = QtWidgets.QPushButton(self.tab_buttonsframe)
        self.infoButton.setGeometry(QtCore.QRect(28, 369, 26, 26))
        self.infoButton.setStyleSheet(mvsfss.infoButton_stylesheet)
        self.infoButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/Infoicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.infoButton.setIcon(icon3)
        self.infoButton.setIconSize(QtCore.QSize(26, 26))
        self.infoButton.setCheckable(False)
        self.infoButton.setObjectName("infoButton")
        self.infoButton.clicked.connect(self.Infobuttonclicked)
        self.assignButton = QtWidgets.QPushButton(self.centralwidget)
        self.assignButton.setGeometry(QtCore.QRect(0, 519, 96, 41))
        self.assignButton.setStyleSheet(mvsfss.assignButton_stylesheet)
        self.assignButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/Assignicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.assignButton.setIcon(icon4)
        self.assignButton.setIconSize(QtCore.QSize(130, 27))
        self.assignButton.setCheckable(False)
        self.assignButton.setObjectName("assignButton")
        self.assignButton.clicked.connect(self.showassign_window)
        self.Righttopdecorativelabel = QtWidgets.QLabel(self.centralwidget)
        self.Righttopdecorativelabel.setGeometry(QtCore.QRect(0, 29, 82, 71))
        self.Righttopdecorativelabel.setStyleSheet(mvsfss.Righttopdecorativelabel_stylesheet)
        self.Righttopdecorativelabel.setText("")
        self.Righttopdecorativelabel.setScaledContents(True)
        self.Righttopdecorativelabel.setObjectName("Righttopdecorativelabel")
        self.rightallclearFrame = QtWidgets.QFrame(self.centralwidget)
        self.rightallclearFrame.setGeometry(QtCore.QRect(623, -20, 161, 601))
        self.rightallclearFrame.setStyleSheet(mvsfss.rightallclearFrame_stylesheet)
        self.rightallclearFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rightallclearFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightallclearFrame.setObjectName("rightallclearFrame")
        self.Decorativelabelmiddlebottom = QtWidgets.QLabel(self.centralwidget)
        self.Decorativelabelmiddlebottom.setGeometry(QtCore.QRect(282, 419, 141, 101))
        self.Decorativelabelmiddlebottom.setStyleSheet(vmtss.Decorativelabelmiddlebottom_stylesheet)
        self.Decorativelabelmiddlebottom.setText("")
        self.Decorativelabelmiddlebottom.setObjectName("Decorativelabelmiddlebottom")
        self.matrixoperatorsbuttons_names=["additionButton","subtractionButton","matrixproductButton","transposeButton","determinantButton"]
        self.matrixoperatorsbuttons_methods=[self.Additionbuttonclicked,self.Subtractionbuttonclicked,self.Matrixproductbuttonclicked,
        self.Transposebuttonclicked,self.Determinantbuttonclicked]
        self.matrixoperatorsbuttons_icons=["icons/Additionicon.png","icons/Subtractionicon.png","icons/Matrixproducticon.png",
        "icons/transpicon.png","icons/deticon.png"]
        self.vectoroperatorsbuttons_names=["additionButton","subtractionButton","scalarproductButton","vectorproductButton","magnitudeButton"]
        self.vectoroperatorsbuttons_methods=[self.Additionbuttonclicked,self.Subtractionbuttonclicked,self.Scalarbuttonclicked,
        self.Vectorproductbuttonclicked,self.Magnitudebuttonclicked]
        self.vectoroperatorsbuttons_icons=["icons/Additionicon.png","icons/Subtractionicon.png","icons/Scalarproducticon.png",
        "icons/Vectorproducticon.png","icons/Magnitudeicon.png"]
        self.answer_and_equalbuttons_names=["answerButton","equalButton"]
        self.answer_and_equalbuttons_methods=[self.Answerbuttonclicked,self.Equalbuttonclicked]
        self.answer_and_equalbuttons_icons=["icons/Answericon.png","icons/Equalicon.png"]
        self.matrixoperatorsbuttons_dict,self.vectoroperatorsbuttons_dict,self.answer_and_equalbuttons_dict={},{},{}
        self.matrixoperatorsbuttons_position,self.vectoroperatorsbuttons_position,self.answer_and_equalbuttons_position=232,232,369
        self.matrixoperatorbuttonscounter,self.vectoroperatorbuttonscounter,self.answer_and_equalbuttons_counter=-1,-1,-1
        for x in self.matrixoperatorsbuttons_names:
            self.matrixoperatorbuttonscounter+=1
            self.matrixoperatorsbuttons_position+=50
            self.matrixoperatorsbuttons_dict[x] = QtWidgets.QPushButton(self.centralwidget)
            self.matrixoperatorsbuttons_dict[x].setStyleSheet(vmtss.matrix_vector_answer_equal_operators_stylesheet)
            self.matrixoperatorsbuttons_dict[x].setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(self.matrixoperatorsbuttons_icons[self.matrixoperatorbuttonscounter]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.matrixoperatorsbuttons_dict[x].setIcon(icon)
            self.matrixoperatorsbuttons_dict[x].setCheckable(False)
            self.matrixoperatorsbuttons_dict[x].clicked.connect(self.matrixoperatorsbuttons_methods[self.matrixoperatorbuttonscounter])
            if x == "transposeButton":
                self.matrixoperatorsbuttons_dict[x].setIconSize(QtCore.QSize(23, 23))
                self.matrixoperatorsbuttons_dict[x].setGeometry(QtCore.QRect(self.matrixoperatorsbuttons_position-132, 469, 41, 41)) 
            elif x == "determinantButton":
                self.matrixoperatorsbuttons_dict[x].setIconSize(QtCore.QSize(30, 30))
                self.matrixoperatorsbuttons_dict[x].setGeometry(QtCore.QRect(self.matrixoperatorsbuttons_position-132, 469, 41, 41))
            else:
                self.matrixoperatorsbuttons_dict[x].setIconSize(QtCore.QSize(23, 23))
                self.matrixoperatorsbuttons_dict[x].setGeometry(QtCore.QRect(self.matrixoperatorsbuttons_position, 419, 41, 41))
        for x in self.vectoroperatorsbuttons_names:
            self.vectoroperatorbuttonscounter+=1
            self.vectoroperatorsbuttons_position+=50
            self.vectoroperatorsbuttons_dict[x] = QtWidgets.QPushButton(self.centralwidget)
            self.vectoroperatorsbuttons_dict[x].setStyleSheet(vmtss.matrix_vector_answer_equal_operators_stylesheet)
            self.vectoroperatorsbuttons_dict[x].setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(self.vectoroperatorsbuttons_icons[self.vectoroperatorbuttonscounter]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.vectoroperatorsbuttons_dict[x].setIcon(icon)
            self.vectoroperatorsbuttons_dict[x].setCheckable(False)
            self.vectoroperatorsbuttons_dict[x].clicked.connect(self.vectoroperatorsbuttons_methods[self.vectoroperatorbuttonscounter])
            if x == "vectorproductButton":
                self.vectoroperatorsbuttons_dict[x].setIconSize(QtCore.QSize(23, 23))
                self.vectoroperatorsbuttons_dict[x].setGeometry(QtCore.QRect(self.vectoroperatorsbuttons_position-132, 469, 41, 41)) 
            elif x == "magnitudeButton":
                self.vectoroperatorsbuttons_dict[x].setIconSize(QtCore.QSize(27, 27))
                self.vectoroperatorsbuttons_dict[x].setGeometry(QtCore.QRect(self.vectoroperatorsbuttons_position-132, 469, 41, 41))
            else:
                self.vectoroperatorsbuttons_dict[x].setIconSize(QtCore.QSize(23, 23))
                self.vectoroperatorsbuttons_dict[x].setGeometry(QtCore.QRect(self.vectoroperatorsbuttons_position, 419, 41, 41))
        for x in self.answer_and_equalbuttons_names:
            self.answer_and_equalbuttons_counter+=1
            self.answer_and_equalbuttons_position+=50
            self.answer_and_equalbuttons_dict[x] = QtWidgets.QPushButton(self.centralwidget)
            self.answer_and_equalbuttons_dict[x].setStyleSheet(vmtss.matrix_vector_answer_equal_operators_stylesheet)
            self.answer_and_equalbuttons_dict[x].setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(self.answer_and_equalbuttons_icons[self.answer_and_equalbuttons_counter]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.answer_and_equalbuttons_dict[x].setIcon(icon)
            self.answer_and_equalbuttons_dict[x].setCheckable(False)
            self.answer_and_equalbuttons_dict[x].clicked.connect(self.answer_and_equalbuttons_methods[self.answer_and_equalbuttons_counter])
            self.answer_and_equalbuttons_dict[x].setGeometry(QtCore.QRect(473, self.answer_and_equalbuttons_position, 121, 41))
            if x == "answerButton":
                self.answer_and_equalbuttons_dict[x].setIconSize(QtCore.QSize(30, 30))
            if x == "equalButton":
                self.answer_and_equalbuttons_dict[x].setIconSize(QtCore.QSize(23, 23))
                self.answer_and_equalbuttons_dict[x].setShortcut("Return")
        self.allclearButton = QtWidgets.QPushButton(self.rightallclearFrame)
        self.allclearButton.setGeometry(QtCore.QRect(12, 59, 81, 41))
        self.allclearButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(132, 43, 108);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    border-color: rgb(97, 37, 103);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(232, 17, 35);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    border-color: rgb(155, 26, 25);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(149, 20, 30);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    border-color: rgb(95, 26, 25);\n"
"}    ")
        self.allclearButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/Allclearicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.allclearButton.setIcon(icon5)
        self.allclearButton.setIconSize(QtCore.QSize(30, 30))
        self.allclearButton.setCheckable(False)
        self.allclearButton.setObjectName("allclearButton")
        self.allclearButton.clicked.connect(self.Allclearbuttonclicked)
        self.Decographlabel = QtWidgets.QLabel(self.rightallclearFrame)
        self.Decographlabel.setGeometry(QtCore.QRect(22, 100, 59, 492))
        self.Decographlabel.setStyleSheet("background-color: transparent;\n"
"border-top:0px;\n"
"border-style:solid;\n"
"border-top-color: rgb(236, 236, 236);\n"
"border-left:none;\n"
"")
        self.Decographlabel.setText("")
        self.Decographlabel.setPixmap(QtGui.QPixmap("icons/Decorativegraph.png"))
        self.Decographlabel.setScaledContents(True)
        self.Decographlabel.setObjectName("Decographlabel")

        ##########################
        #General operators frame##
        ##########################

        self.generaloperatorsframe = QtWidgets.QFrame(self.centralwidget)
        self.generaloperatorsframe.setGeometry(QtCore.QRect(112, 329, 481, 63))
        self.generaloperatorsframe.setStyleSheet(vmtss.generaloperatorsframestylesheet)
        self.generaloperatorsframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.generaloperatorsframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.generaloperatorsframe.setObjectName("generaloperatorsframe")
        self.generaloperatorsButtonsnamelist_line1=["generaladdButton","generalsubButton","generalmultiplyButton","generaldivisionButton",
        "generalsinButton","generalcosButton","generaltanButton","generalsinhButton","generalcoshButton","generaltanhButton",
        "generallogButton","generalinButton"]
        self.generaloperatorsButtonsnamelist_line2=["generalpowerButton","generalrootButton","generaleButton","generalpiButton",
        "generalsininvButton","generalcosinvButton","generaltaninvButton","generalsinhinvButton","generalcoshinvButton",
        "generaltanhinvButton","generallogchooseButton","generalabsoluteButton"]
        self.generaloperatorsButtonsnamelist_line1icons=["icons/generaloperators/add.png","icons/generaloperators/subtract.png",
        "icons/generaloperators/multiply.png","icons/generaloperators/division.png","icons/generaloperators/sin().png",
        "icons/generaloperators/cos().png","icons/generaloperators/tan().png","icons/generaloperators/sinh().png",
        "icons/generaloperators/cosh().png","icons/generaloperators/tanh().png","icons/generaloperators/log().png",
        "icons/generaloperators/in().png"]
        self.generaloperatorsButtonsnamelist_line2icons=["icons/generaloperators/power.png","icons/generaloperators/root.png",
        "icons/generaloperators/e.png","icons/generaloperators/pi.png","icons/generaloperators/sin-1().png",
        "icons/generaloperators/cos-1().png","icons/generaloperators/tan-1().png","icons/generaloperators/sinh-1().png",
        "icons/generaloperators/cosh-1().png","icons/generaloperators/tanh-1().png","icons/generaloperators/log()().png",
        "icons/generaloperators/absolute.png"]
        self.generaloperatorsButtonsnamelist_line1methods=[self.Generaladdbuttonclicked,self.Generalsubbuttonclicked,
        self.Generalmultiplybuttonclicked,self.Generaldivisionbuttonclicked,self.Generalsinbuttonclicked,
        self.Generalcosbuttonclicked,self.Generaltanbuttonclicked,self.Generalsinhbuttonclicked,self.Generalcoshbuttonclicked,
        self.Generaltanhbuttonclicked,self.Generallogbuttonclicked,self.Generalinbuttonclicked]
        self.generaloperatorsButtonsnamelist_line2methods=[self.Generalpowerbuttonclicked,self.Generalrootbuttonclicked,
        self.Generalebuttonclicked,self.Generalpibuttonclicked,self.Generalsininvbuttonclicked,self.Generalcosinvbuttonclicked,
        self.Generaltaninvbuttonclicked,self.Generalsinhinvbuttonclicked,self.Generalcoshinvbuttonclicked,self.Generaltanhinvbuttonclicked,
        self.Generallogchoosebuttonclicked,self.Generalabsolutebuttonclicked]
        self.generaloperatorsButtonsdict={}
        generaloperatorsButtonsnamelist_line1position,generaloperatorsButtonsnamelist_line1counter=-40,-1
        for x in self.generaloperatorsButtonsnamelist_line1:
            generaloperatorsButtonsnamelist_line1position+=40
            generaloperatorsButtonsnamelist_line1counter+=1
            self.generaloperatorsButtonsdict[x] = QtWidgets.QPushButton(self.generaloperatorsframe)
            self.generaloperatorsButtonsdict[x].setStyleSheet(vmtss.generaloperatorsButtons_stylesheet)
            self.generaloperatorsButtonsdict[x].setText("")
            self.generaloperatorsButtonsdict[x].setGeometry(QtCore.QRect(generaloperatorsButtonsnamelist_line1position, 0, 41, 31))
            icon= QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(self.generaloperatorsButtonsnamelist_line1icons[generaloperatorsButtonsnamelist_line1counter]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.generaloperatorsButtonsdict[x].setIcon(icon)
            self.generaloperatorsButtonsdict[x].setCheckable(False)
            self.generaloperatorsButtonsdict[x].clicked.connect(self.generaloperatorsButtonsnamelist_line1methods[generaloperatorsButtonsnamelist_line1counter])
            if x =="generaladdButton":
                self.generaloperatorsButtonsdict[x].setIconSize(QtCore.QSize(18, 18))
                self.generaloperatorsButtonsdict[x].setShortcut("+")
            elif x == "generalsubButton":
                self.generaloperatorsButtonsdict[x].setIconSize(QtCore.QSize(18, 18))
                self.generaloperatorsButtonsdict[x].setShortcut("-")
            elif x == "generalmultiplyButton":
                self.generaloperatorsButtonsdict[x].setIconSize(QtCore.QSize(18, 18))
                self.generaloperatorsButtonsdict[x].setShortcut("*")
            elif x =="generaldivisionButton":
                self.generaloperatorsButtonsdict[x].setIconSize(QtCore.QSize(18, 18))
                self.generaloperatorsButtonsdict[x].setShortcut("/")
            else:
                self.generaloperatorsButtonsdict[x].setIconSize(QtCore.QSize(35, 35))
        generaloperatorsButtonsnamelist_line2position,generaloperatorsButtonsnamelist_line2counter=-40,-1
        for x in self.generaloperatorsButtonsnamelist_line2:
            generaloperatorsButtonsnamelist_line2position+=40
            generaloperatorsButtonsnamelist_line2counter+=1
            self.generaloperatorsButtonsdict[x] = QtWidgets.QPushButton(self.generaloperatorsframe)
            self.generaloperatorsButtonsdict[x].setStyleSheet(vmtss.generaloperatorsButtons_stylesheet)
            self.generaloperatorsButtonsdict[x].setText("")
            self.generaloperatorsButtonsdict[x].setGeometry(QtCore.QRect(generaloperatorsButtonsnamelist_line2position, 32, 41, 31))
            icon= QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(self.generaloperatorsButtonsnamelist_line2icons[generaloperatorsButtonsnamelist_line2counter]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.generaloperatorsButtonsdict[x].setIcon(icon)
            self.generaloperatorsButtonsdict[x].setCheckable(False)
            self.generaloperatorsButtonsdict[x].clicked.connect(self.generaloperatorsButtonsnamelist_line2methods[generaloperatorsButtonsnamelist_line2counter])
            if x =="generalabsoluteButton":
                self.generaloperatorsButtonsdict[x].setIconSize(QtCore.QSize(18, 18))
            elif x == "generaleButton" or x == "generalpiButton":
                self.generaloperatorsButtonsdict[x].setIconSize(QtCore.QSize(45, 45))
            else:
                self.generaloperatorsButtonsdict[x].setIconSize(QtCore.QSize(35, 35))
        ######################################
        ##Draggable Matrix & Vector elements##
        ######################################

        self.clickndraglabel = QtWidgets.QLabel(self.centralwidget)
        self.clickndraglabel.setGeometry(QtCore.QRect(110, 419, 124, 21))
        self.clickndraglabel.setStyleSheet(vmtss.clickndraglabelstylesheet)
        self.clickndraglabel.setScaledContents(True)
        self.clickndraglabel.setAlignment(QtCore.Qt.AlignCenter)
        self.clickndraglabel.setScaledContents(True)
        self.clickndraglabel.setObjectName("clickndraglabel")
        self.clickndraglabel.setText("CLICK OR DRAG")

        self.draggablematrixListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.draggablematrixListWidget.setGeometry(QtCore.QRect(112, 440, 121, 79))
        self.draggablematrixListWidget.setDragEnabled(True)
        self.draggablematrixListWidget.setDragDropOverwriteMode(True)
        self.draggablematrixListWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.draggablematrixListWidget.setObjectName("draggablematrixListWidget")
        self.draggablematrixListWidget.itemDoubleClicked.connect(self.Vectorandmatrixlistwidgetdoubleclicked)        
        for x in range(0,20):
            item = QtWidgets.QListWidgetItem()
            self.draggablematrixListWidget.addItem(item)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.draggablevectorListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.draggablevectorListWidget.setGeometry(QtCore.QRect(112, 440, 121, 79))
        self.draggablevectorListWidget.setDragEnabled(True)
        self.draggablevectorListWidget.setDragDropOverwriteMode(True)
        self.draggablevectorListWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.draggablevectorListWidget.setObjectName("draggablevectorListWidget")
        self.draggablevectorListWidget.itemDoubleClicked.connect(self.Vectorandmatrixlistwidgetdoubleclicked)
        for x in range(0,20):
            item = QtWidgets.QListWidgetItem()
            self.draggablevectorListWidget.addItem(item)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
        ##########################
        ##Degree and  Rad Slider##
        ##########################

        self.degandradverticalSlider = QtWidgets.QSlider(self.tab_buttonsframe)
        self.degandradverticalSlider.setGeometry(QtCore.QRect(40, 410, 31, 35))
        self.degandradverticalSlider.setStyleSheet(mvsfss.degandradverticalSlider_stylesheet)
        self.degandradverticalSlider.setMaximum(1)
        self.degandradverticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.degandradverticalSlider.setInvertedAppearance(False)
        self.degandradverticalSlider.setObjectName("verticalSlider")
        self.degandradverticalSlider.valueChanged.connect(self.Degandradverticalslidervaluechanged)
        self.degreeLabel = QtWidgets.QLabel(self.tab_buttonsframe)
        self.degreeLabel.setGeometry(QtCore.QRect(20, 410, 31, 16))
        self.degreeLabel.setStyleSheet(mvsfss.degreeLabel_initialstylesheet)
        self.degreeLabel.setObjectName("degreeLabel")
        self.degreeLabel.setText("DEG")
        self.radLabel = QtWidgets.QLabel(self.tab_buttonsframe)
        self.radLabel.setGeometry(QtCore.QRect(20, 430, 31, 16))
        self.radLabel.setStyleSheet(mvsfss.radLabel_initialstylesheet)
        self.radLabel.setObjectName("radLabel")
        self.radLabel.setText("RAD")

        ##################
        ### ANGLES TAB ###
        ##################
        self.bakcgrounddecorativeslideLabel = QtWidgets.QLabel(self.centralwidget)
        self.bakcgrounddecorativeslideLabel.setGeometry(QtCore.QRect(282, 100, 141, 71))
        self.bakcgrounddecorativeslideLabel.setStyleSheet(atss.bakcgrounddecorativeslideLabel_stylesheet)
        self.bakcgrounddecorativeslideLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.bakcgrounddecorativeslideLabel.setObjectName("bakcgrounddecorativeslideLabel")
        self.angleshorizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.angleshorizontalSlider.setGeometry(QtCore.QRect(322, 119, 61, 16))
        self.angleshorizontalSlider.setStyleSheet(atss.angleshorizontalSlider_stylesheet)
        self.angleshorizontalSlider.setMaximum(1)
        self.angleshorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.angleshorizontalSlider.setInvertedAppearance(False)
        self.angleshorizontalSlider.setObjectName("angleshorizontalSlider")
        self.angleshorizontalSlider.valueChanged.connect(self.Angleshorizontalslidervaluechanged)
        self.anglesimportLabel = QtWidgets.QLabel(self.centralwidget)
        self.anglesimportLabel.setGeometry(QtCore.QRect(306, 139, 51, 16))
        self.anglesimportLabel.setStyleSheet(atss.anglesimportLabel_stylesheet)
        self.anglesimportLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.anglesimportLabel.setObjectName("anglesimportLabel")
        self.angleswriteLabel = QtWidgets.QLabel(self.centralwidget)
        self.angleswriteLabel.setGeometry(QtCore.QRect(362, 139, 41, 16))
        self.angleswriteLabel.setStyleSheet(atss.angleswriteLabel_stylesheet)
        self.angleswriteLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.angleswriteLabel.setObjectName("angleswriteLabel")
        self.angleschoosevectorFrame = QtWidgets.QFrame(self.centralwidget)
        self.angleschoosevectorFrame.setGeometry(QtCore.QRect(90, 179, 501, 71))
        self.angleschoosevectorFrame.setStyleSheet(atss.angleschoosevectorFrame_stylesheet)
        self.angleschoosevectorFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.angleschoosevectorFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.angleschoosevectorFrame.setObjectName("angleschoosevectorFrame")
        self.choosevectorcomboBox_x = QtWidgets.QComboBox(self.angleschoosevectorFrame)
        self.choosevectorcomboBox_x.setGeometry(QtCore.QRect(0, 20, 91, 21))
        self.choosevectorcomboBox_x.setStyleSheet(atss.choosevectorcomboBox_x_stylesheet)
        self.choosevectorcomboBox_x.setObjectName("choosevectorcomboBox_x")
        for x in range(0,20):
            self.choosevectorcomboBox_x.addItem("")
        self.choosevectorcomboBox_x.activated.connect(self.Anglesvectorxcomboboxvaluechanged)
        self.choosevectorcomboBox_y = QtWidgets.QComboBox(self.angleschoosevectorFrame)
        self.choosevectorcomboBox_y.setGeometry(QtCore.QRect(0, 50, 91, 21))
        self.choosevectorcomboBox_y.setStyleSheet(atss.choosevectorcomboBox_y_stylesheet)
        self.choosevectorcomboBox_y.setObjectName("choosevectorcomboBox_y")
        for x in range(0,20):
            self.choosevectorcomboBox_y.addItem("")
        self.choosevectorcomboBox_y.activated.connect(self.Anglesvectorycomboboxvaluechanged)
        self.valueschoosexLabel = QtWidgets.QLabel(self.angleschoosevectorFrame)
        self.valueschoosexLabel.setGeometry(QtCore.QRect(90, 20, 412, 21))
        self.valueschoosexLabel.setStyleSheet(atss.valueschoosexLabel_stylesheet)
        self.valueschoosexLabel.setText("")
        self.valueschoosexLabel.setObjectName("valueschoosexLabel")
        self.valueschooseyLabel = QtWidgets.QLabel(self.angleschoosevectorFrame)
        self.valueschooseyLabel.setGeometry(QtCore.QRect(90, 50, 412, 21))
        self.valueschooseyLabel.setStyleSheet(atss.valueschooseyLabel_stylesheet)
        self.valueschooseyLabel.setText("")
        self.valueschooseyLabel.setObjectName("valueschooseyLabel")
        self.valueschooseyLabel.raise_()
        self.valueschoosexLabel.raise_()
        self.choosevectorcomboBox_x.raise_()
        self.choosevectorcomboBox_y.raise_()
        self.angleresultFrame = QtWidgets.QFrame(self.centralwidget)
        self.angleresultFrame.setGeometry(QtCore.QRect(90, 269, 524, 241))
        self.angleresultFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.angleresultFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.angleresultFrame.setObjectName("angleresultFrame")
        self.calculatepushButton = QtWidgets.QPushButton(self.angleresultFrame)
        self.calculatepushButton.setGeometry(QtCore.QRect(82, 40, 361, 31))
        self.calculatepushButton.setStyleSheet(atss.calculatepushButton_stylesheet)
        self.calculatepushButton.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/Calculateicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.calculatepushButton.setIcon(icon9)
        self.calculatepushButton.setIconSize(QtCore.QSize(200, 200))
        self.calculatepushButton.setObjectName("calculatepushButton")
        self.calculatepushButton.clicked.connect(self.AnglescalculatepushButtonclicked)
        self.DeocrativebackgroundLabel = QtWidgets.QLabel(self.angleresultFrame)
        self.DeocrativebackgroundLabel.setGeometry(QtCore.QRect(-10, 0, 534, 21))
        self.DeocrativebackgroundLabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(17, 18, 17, 255), stop:1 rgba(22, 23, 22, 255));")
        self.DeocrativebackgroundLabel.setText("")
        self.DeocrativebackgroundLabel.setObjectName("DeocrativebackgroundLabel")
        self.ddordmshorizontalSlider = QtWidgets.QSlider(self.angleresultFrame)
        self.ddordmshorizontalSlider.setGeometry(QtCore.QRect(233, 2, 41, 16))
        self.ddordmshorizontalSlider.setStyleSheet(atss.ddordmshorizontalSlider_stylesheet)
        self.ddordmshorizontalSlider.setMaximum(1)
        self.ddordmshorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ddordmshorizontalSlider.setInvertedAppearance(False)
        self.ddordmshorizontalSlider.setObjectName("ddordmshorizontalSlider")
        self.ddordmshorizontalSlider.valueChanged.connect(self.Ddordmshorizontalslidervaluechanged)
        self.degreesminutessecondsLabel = QtWidgets.QLabel(self.angleresultFrame)
        self.degreesminutessecondsLabel.setGeometry(QtCore.QRect(208, 3, 22, 16))
        self.degreesminutessecondsLabel.setStyleSheet(atss.degreesminutessecondsLabel_stylesheet)
        self.degreesminutessecondsLabel.setObjectName("degreesminutessecondsLabel")
        self.decimaldegreeLabel = QtWidgets.QLabel(self.angleresultFrame)
        self.decimaldegreeLabel.setGeometry(QtCore.QRect(275, 3, 21, 16))
        self.decimaldegreeLabel.setStyleSheet(atss.decimaldegreeLabel_stylesheet)
        self.decimaldegreeLabel.setObjectName("decimaldegreeLabel")

        self.anglesscreen_scrollArea = QtWidgets.QScrollArea(self.angleresultFrame)
        self.anglesscreen_scrollArea.setGeometry(QtCore.QRect(72, 90, 381, 141))
        self.anglesscreen_scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.anglesscreen_scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.anglesscreen_scrollArea.setWidgetResizable(True)
        self.anglesscreen_scrollArea.setObjectName("anglesscreen_scrollArea")

        self.anglesscreen_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.anglesscreen_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 379, 139))
        self.anglesscreen_scrollAreaWidgetContents.setObjectName("anglesscreen_scrollAreaWidgetContents")
        self.anglesscreen_scrollAreaWidgetContents.setMinimumSize(0, 0)
        self.anglesscreen_scrollAreaWidgetContents.setStyleSheet("background-color: rgb(17, 18, 17);\n")
        self.anglesscreenresulthorizontalgridLayout = QtWidgets.QHBoxLayout(self.anglesscreen_scrollAreaWidgetContents)
        self.anglesscreenresulthorizontalgridLayout.setSpacing(0)
        self.anglesscreenresulthorizontalgridLayout.setObjectName("anglesscreenresulthorizontalgridLayout")
        
        self.anglesscreen_scrollArearesultLabel = QtWidgets.QLabel()
        self.anglesscreen_scrollArearesultLabel.setGeometry(QtCore.QRect(0, 0, 379, 139))
        self.anglesscreen_scrollArearesultLabel.setStyleSheet(atss.anglesscreen_scrollArearesultLabel_stylesheet)
        self.anglesscreen_scrollArearesultLabel.setText("")
        self.anglesscreen_scrollArearesultLabel.setTextFormat(QtCore.Qt.AutoText)
        self.anglesscreen_scrollArearesultLabel.setScaledContents(False)
        self.anglesscreen_scrollArearesultLabel.setWordWrap(False)
        self.anglesscreen_scrollArearesultLabel.setObjectName("anglesscreen_scrollArearesultLabel")

        self.anglesscreenresulthorizontalgridLayout.addWidget(self.anglesscreen_scrollArearesultLabel, 1, alignment=QtCore.Qt.AlignCenter)
        self.anglesscreen_scrollArea.setWidget(self.anglesscreen_scrollAreaWidgetContents)

        self.angleswritevectorFrame = QtWidgets.QFrame(self.centralwidget)
        self.angleswritevectorFrame.setGeometry(QtCore.QRect(90, 179, 501, 71))
        self.angleswritevectorFrame.setStyleSheet(atss.angleswritevectorFrame_stylesheet)
        self.angleswritevectorFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.angleswritevectorFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.angleswritevectorFrame.setObjectName("angleswritevectorFrame")
        self.writevectorLabel_x = QtWidgets.QLabel(self.angleswritevectorFrame)
        self.writevectorLabel_x.setGeometry(QtCore.QRect(0, 20, 91, 21))
        self.writevectorLabel_x.setStyleSheet(atss.writevectorLabel_x_stylesheet)
        self.writevectorLabel_x.setObjectName("writevectorLabel_x")
        self.writevectorLabel_y = QtWidgets.QLabel(self.angleswritevectorFrame)
        self.writevectorLabel_y.setGeometry(QtCore.QRect(0, 50, 91, 21))
        self.writevectorLabel_y.setStyleSheet(atss.writevectorLabel_y_stylesheet)
        self.writevectorLabel_y.setObjectName("writevectorLabel_y")
        self.decorativewritexLabel = QtWidgets.QLabel(self.angleswritevectorFrame)
        self.decorativewritexLabel.setGeometry(QtCore.QRect(90, 20, 412, 21))
        self.decorativewritexLabel.setStyleSheet(atss.decorativewritexLabel_stylesheet)
        self.decorativewriteyLabel = QtWidgets.QLabel(self.angleswritevectorFrame)
        self.decorativewriteyLabel.setGeometry(QtCore.QRect(90, 50, 412, 21))
        self.decorativewriteyLabel.setStyleSheet(atss.decorativewriteyLabel_stylesheet)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.angleswritevectorFrame)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(90, 50, 371, 21))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.writevectorhorizontalLayout_x = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.writevectorhorizontalLayout_x.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.writevectorhorizontalLayout_x.setContentsMargins(0, 0, 0, 0)
        self.writevectorhorizontalLayout_x.setObjectName("writevectorhorizontalLayout_x")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.angleswritevectorFrame)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(90, 20, 371, 22))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.writevectorhorizontalLayout_y = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.writevectorhorizontalLayout_y.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.writevectorhorizontalLayout_y.setContentsMargins(0, 0, 0, 0)
        self.writevectorhorizontalLayout_y.setObjectName("writevectorhorizontalLayout_y")
        self.writevectorcolumncomboBox_x = QtWidgets.QComboBox(self.angleswritevectorFrame)
        self.writevectorcolumncomboBox_x.setGeometry(QtCore.QRect(460, 20, 41, 21))
        self.writevectorcolumncomboBox_x.setStyleSheet(atss.writevectorcolumncomboBox_x_stylesheet)
        self.writevectorcolumncomboBox_x.setObjectName("writevectorcolumncomboBox_x")
        for x in range(0,12):
            self.writevectorcolumncomboBox_x.addItem("")
        self.writevectorcolumncomboBox_x.activated.connect(self.WritevectorcolumncomboBox_xvaluechanged)
        self.writevectorcolumncomboBox_y = QtWidgets.QComboBox(self.angleswritevectorFrame)
        self.writevectorcolumncomboBox_y.setGeometry(QtCore.QRect(460, 50, 41, 21))
        self.writevectorcolumncomboBox_y.setStyleSheet(atss.writevectorcolumncomboBox_y_stylesheet)
        self.writevectorcolumncomboBox_y.setObjectName("writevectorcolumncomboBox_y")
        for x in range(0,12):
            self.writevectorcolumncomboBox_y.addItem("")
        self.writevectorcolumncomboBox_y.activated.connect(self.WritevectorcolumncomboBox_yvaluechanged)
        self.writevectorcolumncomboBox_y.setEnabled(False)
        self.columnsLabel = QtWidgets.QLabel(self.angleswritevectorFrame)
        self.columnsLabel.setGeometry(QtCore.QRect(443, 4, 61, 16))
        self.columnsLabel.setText("")
        self.columnsLabel.setPixmap(QtGui.QPixmap("icons/createwindowicons/Columnsicon.png"))
        self.columnsLabel.setScaledContents(True)
        self.columnsLabel.setObjectName("columnsLabel")

        ######################
        ## ANGLES TAB CELLS ##
        ######################

        self.reg_ex_cell = QtCore.QRegExp("(^-?[0-9]+/0*[1-9][0-9]*$|^[-+]?[0-9]+$|^[-+]?[0-9]+\.[0-9]+$)")
        writefont = QtGui.QFont()
        writefont.setFamily("Alice")
        writefont.setPointSize(12)
        self.writevectorxlineEdit_dict,self.writevectorylineEdit_dict = {},{}
        self.writevectorxlineEdit_validatordict,self.writevectorylineEdit_validatordict = {},{}
        writevectorposition=40
        for x in range(1,13):
            writevectorposition+=30
            self.writevectorxlineEdit_dict["writevectorxlineEdit_"+str(x)] = QtWidgets.QLineEdit(self.angleswritevectorFrame)
            self.writevectorxlineEdit_dict["writevectorxlineEdit_"+str(x)].setGeometry(QtCore.QRect(writevectorposition, 20, 31, 20))
            self.writevectorxlineEdit_dict["writevectorxlineEdit_"+str(x)].setFont(writefont)
            self.writevectorxlineEdit_dict["writevectorxlineEdit_"+str(x)].setStyleSheet("color: rgb(236, 236, 236);"
        "border:1px;"
        "border-style:solid;"
        "border-color: rgb(15, 16, 15);"
        "background-color: rgb(42, 43, 42);"
        "")
            self.writevectorxlineEdit_dict["writevectorxlineEdit_"+str(x)].setAlignment(QtCore.Qt.AlignCenter)
            self.writevectorxlineEdit_validatordict["writevectorxlineEdit_"+str(x)+"_validator"]=QtGui.QRegExpValidator(self.reg_ex_cell, self.writevectorxlineEdit_dict["writevectorxlineEdit_"+str(x)])
            self.writevectorxlineEdit_dict["writevectorxlineEdit_"+str(x)].setValidator(self.writevectorxlineEdit_validatordict["writevectorxlineEdit_"+str(x)+"_validator"])
            self.writevectorylineEdit_dict["writevectorylineEdit_"+str(x)] = QtWidgets.QLineEdit(self.angleswritevectorFrame)
            self.writevectorylineEdit_dict["writevectorylineEdit_"+str(x)].setGeometry(QtCore.QRect(writevectorposition, 50, 31, 20))
            self.writevectorylineEdit_dict["writevectorylineEdit_"+str(x)].setFont(writefont)
            self.writevectorylineEdit_dict["writevectorylineEdit_"+str(x)].setStyleSheet("color: rgb(236, 236, 236);"
        "border:1px;"
        "border-style:solid;"
        "border-color: rgb(15, 16, 15);"
        "background-color: rgb(42, 43, 42);"
        "") 
            self.writevectorylineEdit_dict["writevectorylineEdit_"+str(x)].setAlignment(QtCore.Qt.AlignCenter)
            self.writevectorylineEdit_validatordict["writevectorylineEdit_"+str(x)+"_validator"]=QtGui.QRegExpValidator(self.reg_ex_cell, self.writevectorylineEdit_dict["writevectorylineEdit_"+str(x)])
            self.writevectorylineEdit_dict["writevectorylineEdit_"+str(x)].setValidator(self.writevectorylineEdit_validatordict["writevectorylineEdit_"+str(x)+"_validator"])
        #####################
        ## Eigenvalues Tab ##
        #####################

        self.eigenvaluesframe = QtWidgets.QFrame(self.centralwidget)
        self.eigenvaluesframe.setGeometry(QtCore.QRect(95, 109, 511, 411))
        self.eigenvaluesframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.eigenvaluesframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.eigenvaluesframe.setObjectName("eigenvaluesframe")
        self.eigenvalueschoosematrixListWidget = QtWidgets.QListWidget(self.eigenvaluesframe)
        self.eigenvalueschoosematrixListWidget.setGeometry(QtCore.QRect(20, 10, 469, 31))
        self.eigenvalueschoosematrixListWidget.setDragEnabled(False)
        self.eigenvalueschoosematrixListWidget.setDragDropOverwriteMode(True)
        self.eigenvalueschoosematrixListWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.eigenvalueschoosematrixListWidget.setFlow(QtWidgets.QListView.LeftToRight)
        self.eigenvalueschoosematrixListWidget.setUniformItemSizes(True)
        self.eigenvalueschoosematrixListWidget.setItemAlignment(QtCore.Qt.AlignCenter)
        self.eigenvalueschoosematrixListWidget.setObjectName("eigenvalueschoosematrixListWidget")
        for x in range(0,20):
            item = QtWidgets.QListWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.eigenvalueschoosematrixListWidget.addItem(item)
        self.eigenvalueschoosematrixListWidget.setSpacing(4)
        self.eigenvalueschoosematrixListWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.eigenvalueschoosematrixListWidget.currentItemChanged.connect(self.Eigenvalueschoosematrixlistwidgetitemchanged)
        self.eigenvaluescalculatepushButton = QtWidgets.QPushButton(self.eigenvaluesframe)
        self.eigenvaluescalculatepushButton.setGeometry(QtCore.QRect(80, 214, 361, 31))
        self.eigenvaluescalculatepushButton.setStyleSheet(evtss.eigenvaluescalculatepushButton_stylesheet)
        self.eigenvaluescalculatepushButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/Calculateicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.eigenvaluescalculatepushButton.setIcon(icon8)
        self.eigenvaluescalculatepushButton.setIconSize(QtCore.QSize(200, 200))
        self.eigenvaluescalculatepushButton.setObjectName("eigenvaluescalculatepushButton")
        self.eigenvaluescalculatepushButton.clicked.connect(self.Eigenvaluescalculatepushbuttonclicked)

        #########################################
        ##EIGENVALUES CHOSEN MATRIX SCROLL AREA##
        #########################################

        self.eigenvalueschosenmatrixscreen_scrollArea = QtWidgets.QScrollArea(self.eigenvaluesframe)
        self.eigenvalueschosenmatrixscreen_scrollArea.setGeometry(QtCore.QRect(80, 50, 361, 151))
        self.eigenvalueschosenmatrixscreen_scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.eigenvalueschosenmatrixscreen_scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.eigenvalueschosenmatrixscreen_scrollArea.setWidgetResizable(True)
        self.eigenvalueschosenmatrixscreen_scrollArea.setObjectName("eigenvalueschosenmatrixscreen_scrollArea")

        self.eigenvalueschosenmatrixscreen_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.eigenvalueschosenmatrixscreen_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 359, 149))
        self.eigenvalueschosenmatrixscreen_scrollAreaWidgetContents.setObjectName("eigenvalueschosenmatrixscreen_scrollAreaWidgetContents")
        self.eigenvalueschosenmatrixscreen_scrollAreaWidgetContents.setMinimumSize(0, 0)
        self.eigenvalueschosenmatrixscreen_scrollAreaWidgetContents.setStyleSheet("background-color: rgb(17, 18, 17);\n")
        self.eigenvalueschosenmatrixscreen_gridLayout = QtWidgets.QHBoxLayout(self.eigenvalueschosenmatrixscreen_scrollAreaWidgetContents)
        self.eigenvalueschosenmatrixscreen_gridLayout.setSpacing(0)
        self.eigenvalueschosenmatrixscreen_gridLayout.setObjectName("eigenvalueschosenmatrixscreen_gridLayout")

        self.eigenvalueschosenmatrixscreen_matrixgridLayoutWidget = QtWidgets.QWidget()
        self.eigenvalueschosenmatrixscreen_matrixgridLayout = QtWidgets.QHBoxLayout(self.eigenvalueschosenmatrixscreen_matrixgridLayoutWidget)
        self.eigenvalueschosenmatrixscreen_matrixgridLayout.setSpacing(5)


        #####################################################
        ##EIGENVALUES CHOSEN MATRIX SCROLL AREA VALUES GRID##
        #####################################################

        self.eigenvalueschosenmatrixparentesisopenlabel = QtWidgets.QLabel()
        self.eigenvalueschosenmatrixparentesisopenlabel.setPixmap(QtGui.QPixmap("icons/Itemparentesisopen.png"))
        self.eigenvalueschosenmatrixparentesisopenlabel.setScaledContents(True)
        self.eigenvalueschosenmatrixparentesisopenlabel.setFixedWidth(5)
        self.eigenvalueschosenmatrixparentesisclosedlabel = QtWidgets.QLabel()
        self.eigenvalueschosenmatrixparentesisclosedlabel.setPixmap(QtGui.QPixmap("icons/Itemparentesisclose.png"))
        self.eigenvalueschosenmatrixparentesisclosedlabel.setScaledContents(True)
        self.eigenvalueschosenmatrixparentesisclosedlabel.setFixedWidth(5)

        self.eigenvalueschosenmatrixscreen_valuesgridLayoutWidget = QtWidgets.QWidget()
        self.eigenvalueschosenmatrixscreen_valuesgridLayout = QtWidgets.QGridLayout(self.eigenvalueschosenmatrixscreen_valuesgridLayoutWidget)
        self.eigenvalueschosenmatrixscreen_valuesgridLayout.setContentsMargins(0, 0, 0, 0)
        self.eigenvalueschosenmatrixscreen_valuesgridLayout.setHorizontalSpacing(20)
        self.eigenvalueschosenmatrixscreen_valuesgridLayout.setVerticalSpacing(5)

        self.eigenvalueschosenmatrixscreen_gridLayout.addWidget(self.eigenvalueschosenmatrixscreen_matrixgridLayoutWidget, 1, alignment=QtCore.Qt.AlignCenter)

        self.eigenvalueschosenmatrixscreen_matrixgridLayout.addWidget(self.eigenvalueschosenmatrixparentesisopenlabel, 0, alignment=QtCore.Qt.AlignLeft)
        self.eigenvalueschosenmatrixscreen_matrixgridLayout.addWidget(self.eigenvalueschosenmatrixscreen_valuesgridLayoutWidget, 1, alignment=QtCore.Qt.AlignCenter)
        self.eigenvalueschosenmatrixscreen_matrixgridLayout.addWidget(self.eigenvalueschosenmatrixparentesisclosedlabel, 2, alignment=QtCore.Qt.AlignLeft)

        self.eigenvalueschosenmatrixscreen_scrollArea.setWidget(self.eigenvalueschosenmatrixscreen_scrollAreaWidgetContents)

        self.eigenvalueschosenmatrixparentesisopenlabel.setHidden(True)
        self.eigenvalueschosenmatrixparentesisclosedlabel.setHidden(True)

        #########################################################
        ## EIGENVALUES CHOSEN MATRIX SCROLL AREA VALUES LABELS ##
        #########################################################
        eigenfont = QtGui.QFont()
        eigenfont.setFamily("Alice")
        eigenfont.setPointSize(12)

        stringstylesheeteigenchosen = "background-color: transparent;\n""color: rgb(236, 236, 236);\n"

        self.eigenchosen_matrixlabelcelldict={}
        for x, y in itools.product(range(1,11), range(1,11)):
            self.eigenchosen_matrixlabelcelldict["eigenchosen_matrixlabelcell"+str(x)+"_"+str(y)] = QtWidgets.QLabel(self.eigenvalueschosenmatrixscreen_valuesgridLayoutWidget)
            self.eigenchosen_matrixlabelcelldict["eigenchosen_matrixlabelcell"+str(x)+"_"+str(y)].setStyleSheet(stringstylesheeteigenchosen)
            self.eigenchosen_matrixlabelcelldict["eigenchosen_matrixlabelcell"+str(x)+"_"+str(y)].setFont(eigenfont)
            self.eigenvalueschosenmatrixscreen_valuesgridLayout.addWidget(self.eigenchosen_matrixlabelcelldict["eigenchosen_matrixlabelcell"+str(x)+"_"+str(y)], (x-1), (y-1), 1, 1, alignment=QtCore.Qt.AlignCenter)
            self.eigenchosen_matrixlabelcelldict["eigenchosen_matrixlabelcell"+str(x)+"_"+str(y)].setHidden(True)

        ##################################
        ##EIGENVALUES RESULT SCROLL AREA##
        ##################################
        self.eigenvaluesresultscreen_scrollArea = QtWidgets.QScrollArea(self.eigenvaluesframe)
        self.eigenvaluesresultscreen_scrollArea.setGeometry(QtCore.QRect(80, 257, 361, 151))
        self.eigenvaluesresultscreen_scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.eigenvaluesresultscreen_scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.eigenvaluesresultscreen_scrollArea.setWidgetResizable(True)
        self.eigenvaluesresultscreen_scrollArea.setObjectName("eigenvaluesresultscreen_scrollArea")

        self.eigenvaluesresultscreen_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.eigenvaluesresultscreen_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 359, 149))
        self.eigenvaluesresultscreen_scrollAreaWidgetContents.setObjectName("eigenvaluesresultscreen_scrollAreaWidgetContents")
        self.eigenvaluesresultscreen_scrollAreaWidgetContents.setMinimumSize(0, 0)
        self.eigenvaluesresultscreen_scrollAreaWidgetContents.setStyleSheet("background-color: rgb(17, 18, 17);\n")
        self.eigenvaluesresulthorizontalgridLayout = QtWidgets.QHBoxLayout(self.eigenvaluesresultscreen_scrollAreaWidgetContents)
        self.eigenvaluesresulthorizontalgridLayout.setSpacing(0)
        self.eigenvaluesresulthorizontalgridLayout.setObjectName("eigenvaluesresulthorizontalgridLayout")

        self.gridLayoutWidget = QtWidgets.QWidget()
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 361, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.eigenvaluesresultgridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.eigenvaluesresultgridLayout.setContentsMargins(0, 0, 0, 0)
        self.eigenvaluesresultgridLayout.setSpacing(25)
        self.eigenvaluesresultgridLayout.setObjectName("eigenvaluesresultgridLayout")
        self.eigenvectorsLabel_dict,self.eigenvalueLabel_dict,self.eigenvaluemultiplicityLabel_dict={},{},{}
        for x in range(1,11):
            self.eigenvectorsLabel_dict["eigenvectorsLabel_"+str(x)] = QtWidgets.QLabel(self.gridLayoutWidget)
            self.eigenvectorsLabel_dict["eigenvectorsLabel_"+str(x)].setStyleSheet("")
            self.eigenvectorsLabel_dict["eigenvectorsLabel_"+str(x)].setText("")
            self.eigenvaluesresultgridLayout.addWidget(self.eigenvectorsLabel_dict["eigenvectorsLabel_"+str(x)], 4, (x+9), 1, 1)

            self.eigenvaluemultiplicityLabel_dict["eigenvaluemultiplicityLabel_"+str(x)] = QtWidgets.QLabel(self.gridLayoutWidget)
            self.eigenvaluemultiplicityLabel_dict["eigenvaluemultiplicityLabel_"+str(x)].setStyleSheet("border-bottom:2px dotted rgb(126, 126, 126);")
            self.eigenvaluemultiplicityLabel_dict["eigenvaluemultiplicityLabel_"+str(x)].setText("")
            self.eigenvaluesresultgridLayout.addWidget(self.eigenvaluemultiplicityLabel_dict["eigenvaluemultiplicityLabel_"+str(x)], 3, (x+9), 1, 1)

            self.eigenvalueLabel_dict["eigenvalueLabel_"+str(x)] = QtWidgets.QLabel(self.gridLayoutWidget)
            self.eigenvalueLabel_dict["eigenvalueLabel_"+str(x)].setStyleSheet("border-bottom:2px dotted rgb(126, 126, 126);")
            self.eigenvalueLabel_dict["eigenvalueLabel_"+str(x)].setText("")
            self.eigenvaluesresultgridLayout.addWidget(self.eigenvalueLabel_dict["eigenvalueLabel_"+str(x)], 0, (x+9), 1, 1)

        self.eigenvaluesresulthorizontalgridLayout.addWidget(self.gridLayoutWidget, 1, alignment=QtCore.Qt.AlignCenter)

        self.eigenvaluesresultscreen_scrollArea.setWidget(self.eigenvaluesresultscreen_scrollAreaWidgetContents)

        for x in range(0, 10):
            self.eigenvectorsLabel_dict["eigenvectorsLabel_"+str(x+1)].setHidden(True)
            self.eigenvaluemultiplicityLabel_dict["eigenvaluemultiplicityLabel_"+str(x+1)].setHidden(True)
            self.eigenvalueLabel_dict["eigenvalueLabel_"+str(x+1)].setHidden(True)

            self.eigenvalueLabel_dict["eigenvalueLabel_"+str(x+1)].setAlignment(QtCore.Qt.AlignCenter)
            self.eigenvalueLabel_dict["eigenvalueLabel_"+str(x+1)].setStyleSheet(evtss.eigenvaluelabel_stylesheet)

            self.eigenvaluemultiplicityLabel_dict["eigenvaluemultiplicityLabel_"+str(x+1)].setAlignment(QtCore.Qt.AlignCenter)
            self.eigenvaluemultiplicityLabel_dict["eigenvaluemultiplicityLabel_"+str(x+1)].setStyleSheet(evtss.eigenvaluemultiplicitylabel_stylesheet)

            self.eigenvectorsLabel_dict["eigenvectorsLabel_"+str(x+1)].setAlignment(QtCore.Qt.AlignCenter)
            self.eigenvectorsLabel_dict["eigenvectorsLabel_"+str(x+1)].setStyleSheet(evtss.eigenvectorslabel_stylesheet)


        ##########################
        ###SYSTEMS OF EQUATIONS###
        ##########################

        self.systemofequationsframe = QtWidgets.QFrame(self.centralwidget)
        self.systemofequationsframe.setGeometry(QtCore.QRect(85, 109, 511, 411))
        self.systemofequationsframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.systemofequationsframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.systemofequationsframe.setObjectName("systemofequationsframe")
        self.systemofequationschoosematrixListWidget = QtWidgets.QListWidget(self.systemofequationsframe)
        self.systemofequationschoosematrixListWidget.setGeometry(QtCore.QRect(20, 10, 211, 31))
        
        self.systemofequationschoosematrixListWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.systemofequationschoosematrixListWidget.setDragEnabled(True)
        self.systemofequationschoosematrixListWidget.setDragDropOverwriteMode(True)
        self.systemofequationschoosematrixListWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.systemofequationschoosematrixListWidget.setFlow(QtWidgets.QListView.LeftToRight)
        self.systemofequationschoosematrixListWidget.setUniformItemSizes(True)
        self.systemofequationschoosematrixListWidget.setItemAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop|QtCore.Qt.AlignVCenter)
        self.systemofequationschoosematrixListWidget.setObjectName("systemofequationschoosematrixListWidget")
        for x in range(0,20):
            item = QtWidgets.QListWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.systemofequationschoosematrixListWidget.addItem(item)
        self.systemofequationschoosematrixListWidget.setSpacing(4)
        self.systemofequationschoosematrixListWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.systemofequationschoosematrixListWidget.currentItemChanged.connect(self.SystemofequationschoosematrixListWidgetitemchanged)

        self.systemofequationschoosematrixScrollArea = QtWidgets.QScrollArea(self.systemofequationsframe)
        self.systemofequationschoosematrixScrollArea.setGeometry(QtCore.QRect(20, 50, 211, 151))
        self.systemofequationschoosematrixScrollArea.setStyleSheet(soetss.systemofequationschoosematrixScrollArea_stylesheet)
        self.systemofequationschoosematrixScrollArea.setWidgetResizable(True)
        self.systemofequationschoosematrixScrollArea.setObjectName("systemofequationschoosematrixScrollArea")
        self.systemofequationschoosematrixScrollAreaWidgetContents = QtWidgets.QWidget()
        self.systemofequationschoosematrixScrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 209, 149))
        self.systemofequationschoosematrixScrollAreaWidgetContents.setMinimumSize(0, 0)
        self.systemofequationschoosematrixScrollAreaWidgetContents.setObjectName("systemofequationschoosematrixScrollAreaWidgetContents")
        self.systemofequationschoosematrixScrollAreaWidgetContents.setStyleSheet(soetss.systemofequationschoosematrixScrollAreaWidgetContents_stylesheet)
        self.systemofequationschoosematrixscreen_gridLayout = QtWidgets.QHBoxLayout(self.systemofequationschoosematrixScrollAreaWidgetContents)
        self.systemofequationschoosematrixscreen_gridLayout.setSpacing(0)
        self.systemofequationschoosematrixscreen_gridLayout.setObjectName("systemofequationschoosematrixscreen_gridLayout")

        self.systemofequationschoosematrixscreen_matrixgridLayoutWidget = QtWidgets.QWidget()
        self.systemofequationschoosematrixscreen_matrixgridLayout = QtWidgets.QHBoxLayout(self.systemofequationschoosematrixscreen_matrixgridLayoutWidget)
        self.systemofequationschoosematrixscreen_matrixgridLayout.setSpacing(5)

        ###############################################
        ##SYSTEM OF EQ MATRIX SCROLL AREA VALUES GRID##
        ###############################################

        self.systemofequationschoosematrixparentesisopenlabel = QtWidgets.QLabel()
        self.systemofequationschoosematrixparentesisopenlabel.setPixmap(QtGui.QPixmap("icons/Itemparentesisopen.png"))
        self.systemofequationschoosematrixparentesisopenlabel.setScaledContents(True)
        self.systemofequationschoosematrixparentesisopenlabel.setFixedWidth(5)
        self.systemofequationschoosematrixparentesisclosedlabel = QtWidgets.QLabel()
        self.systemofequationschoosematrixparentesisclosedlabel.setPixmap(QtGui.QPixmap("icons/Itemparentesisclose.png"))
        self.systemofequationschoosematrixparentesisclosedlabel.setScaledContents(True)
        self.systemofequationschoosematrixparentesisclosedlabel.setFixedWidth(5)


        self.systemofequationschoosematrixscreen_valuesgridLayoutWidget = QtWidgets.QWidget()
        self.systemofequationschoosematrixscreen_valuesgridLayout = QtWidgets.QGridLayout(self.systemofequationschoosematrixscreen_valuesgridLayoutWidget)
        self.systemofequationschoosematrixscreen_valuesgridLayout.setContentsMargins(0, 0, 0, 0)
        self.systemofequationschoosematrixscreen_valuesgridLayout.setHorizontalSpacing(20)
        self.systemofequationschoosematrixscreen_valuesgridLayout.setVerticalSpacing(5)

        self.systemofequationschoosematrixscreen_gridLayout.addWidget(self.systemofequationschoosematrixscreen_matrixgridLayoutWidget, 1, alignment=QtCore.Qt.AlignCenter)

        self.systemofequationschoosematrixscreen_matrixgridLayout.addWidget(self.systemofequationschoosematrixparentesisopenlabel, 0, alignment=QtCore.Qt.AlignLeft)
        self.systemofequationschoosematrixscreen_matrixgridLayout.addWidget(self.systemofequationschoosematrixscreen_valuesgridLayoutWidget, 1, alignment=QtCore.Qt.AlignCenter)
        self.systemofequationschoosematrixscreen_matrixgridLayout.addWidget(self.systemofequationschoosematrixparentesisclosedlabel, 2, alignment=QtCore.Qt.AlignLeft)

        self.systemofequationschoosematrixScrollArea.setWidget(self.systemofequationschoosematrixScrollAreaWidgetContents)

        self.systemofequationschoosematrixparentesisopenlabel.setHidden(True)
        self.systemofequationschoosematrixparentesisclosedlabel.setHidden(True)

        #########################################################
        ## EIGENVALUES CHOSEN MATRIX SCROLL AREA VALUES LABELS ##
        #########################################################
        systemfont = QtGui.QFont()
        systemfont.setFamily("Alice")
        systemfont.setPointSize(12)

        stringstylesheetmatrixsystemchosen = "background-color: transparent;\n""color: rgb(236, 236, 236);\n"
        self.systemmatrixchosen_matrixlabelcelldict={}
        for x, y in itools.product(range(1,11), range(1,11)):
            self.systemmatrixchosen_matrixlabelcelldict["systemmatrixchosen_matrixlabelcell"+str(x)+"_"+str(y)] = QtWidgets.QLabel(self.systemofequationschoosematrixscreen_valuesgridLayoutWidget)
            self.systemmatrixchosen_matrixlabelcelldict["systemmatrixchosen_matrixlabelcell"+str(x)+"_"+str(y)].setStyleSheet(stringstylesheetmatrixsystemchosen)
            self.systemmatrixchosen_matrixlabelcelldict["systemmatrixchosen_matrixlabelcell"+str(x)+"_"+str(y)].setFont(systemfont)
            self.systemofequationschoosematrixscreen_valuesgridLayout.addWidget(self.systemmatrixchosen_matrixlabelcelldict["systemmatrixchosen_matrixlabelcell"+str(x)+"_"+str(y)], (x-1), (y-1), 1, 1, alignment=QtCore.Qt.AlignCenter)
            self.systemmatrixchosen_matrixlabelcelldict["systemmatrixchosen_matrixlabelcell"+str(x)+"_"+str(y)].setHidden(True)

        self.systemofequationsresultscrollArea = QtWidgets.QScrollArea(self.systemofequationsframe)
        self.systemofequationsresultscrollArea.setGeometry(QtCore.QRect(80, 250, 361, 151))
        self.systemofequationsresultscrollArea.setStyleSheet(soetss.systemofequationsresultscrollArea_stylesheet)
        self.systemofequationsresultscrollArea.setWidgetResizable(True)
        self.systemofequationsresultscrollArea.setObjectName("systemofequationsresultscrollArea")
        self.systemofequationsresultscrollAreaWidgetContents = QtWidgets.QWidget()
        self.systemofequationsresultscrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 359, 149))
        self.systemofequationsresultscrollAreaWidgetContents.setObjectName("systemofequationsresultscrollAreaWidgetContents")
        self.systemofequationsresultscrollAreaWidgetContents.setStyleSheet(soetss.systemofequationsresultscrollAreaWidgetContents_stylesheet)
        self.systemofequationsresultscrollAreahorizontalgridLayout = QtWidgets.QHBoxLayout(self.systemofequationsresultscrollAreaWidgetContents)
        self.systemofequationsresultscrollAreahorizontalgridLayout.setSpacing(0)
        self.systemofequationsresultscrollAreahorizontalgridLayout.setObjectName("systemofequationsresultscrollAreahorizontalgridLayout")

        self.systemofequationsresultscrollArearesultLabel = QtWidgets.QLabel()
        self.systemofequationsresultscrollArearesultLabel.setGeometry(QtCore.QRect(0, 0, 359, 149))
        self.systemofequationsresultscrollArearesultLabel.setStyleSheet(soetss.systemofequationsresultscrollArearesultLabel_stylesheet)
        self.systemofequationsresultscrollArearesultLabel.setText("")
        self.systemofequationsresultscrollArearesultLabel.setTextFormat(QtCore.Qt.AutoText)
        self.systemofequationsresultscrollArearesultLabel.setScaledContents(False)
        self.systemofequationsresultscrollArearesultLabel.setWordWrap(False)
        self.systemofequationsresultscrollArearesultLabel.setObjectName("systemofequationsresultscrollArearesultLabel")

        self.systemofequationsresultscrollAreahorizontalgridLayout.addWidget(self.systemofequationsresultscrollArearesultLabel, 1, alignment=QtCore.Qt.AlignCenter)
        self.systemofequationsresultscrollArea.setWidget(self.systemofequationsresultscrollAreaWidgetContents)

        self.systemofequationscalculatepushButton = QtWidgets.QPushButton(self.systemofequationsframe)
        self.systemofequationscalculatepushButton.setGeometry(QtCore.QRect(80, 215, 361, 23))
        self.systemofequationscalculatepushButton.setStyleSheet(soetss.systemofequationscalculatepushButton_stylesheet)
        self.systemofequationscalculatepushButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/Calculateicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.systemofequationscalculatepushButton.setIcon(icon8)
        self.systemofequationscalculatepushButton.setIconSize(QtCore.QSize(200, 200))
        self.systemofequationscalculatepushButton.setObjectName("systemofequationscalculatepushButton")
        self.systemofequationscalculatepushButton.clicked.connect(self.Systemofequationscalculatepushbuttonclicked)
        self.systemofequationschoosevectorListWidget = QtWidgets.QListWidget(self.systemofequationsframe)
        self.systemofequationschoosevectorListWidget.setGeometry(QtCore.QRect(430, 10, 81, 31))
        
        self.systemofequationschoosevectorListWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.systemofequationschoosevectorListWidget.setDragEnabled(True)
        self.systemofequationschoosevectorListWidget.setDragDropOverwriteMode(True)
        self.systemofequationschoosevectorListWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.systemofequationschoosevectorListWidget.setFlow(QtWidgets.QListView.LeftToRight)
        self.systemofequationschoosevectorListWidget.setUniformItemSizes(True)
        self.systemofequationschoosevectorListWidget.setItemAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop|QtCore.Qt.AlignVCenter)
        self.systemofequationschoosevectorListWidget.setObjectName("systemofequationschoosevectorListWidget")
        for x in range(0,20):
            item = QtWidgets.QListWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.systemofequationschoosevectorListWidget.addItem(item)
        self.systemofequationschoosevectorListWidget.setSpacing(4)
        self.systemofequationschoosevectorListWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.systemofequationschoosevectorListWidget.currentItemChanged.connect(self.SystemofequationschoosevectorListWidgetitemchanged)

        self.systemofequationschoosevectorScrollArea = QtWidgets.QScrollArea(self.systemofequationsframe)
        self.systemofequationschoosevectorScrollArea.setGeometry(QtCore.QRect(430, 50, 81, 151))
        self.systemofequationschoosevectorScrollArea.setStyleSheet(soetss.systemofequationschoosevectorScrollArea_stylesheet)
        self.systemofequationschoosevectorScrollArea.setWidgetResizable(True)
        self.systemofequationschoosevectorScrollArea.setObjectName("systemofequationschoosevectorScrollArea")
        self.systemofequationschoosevectorScrollAreaWidgetContents = QtWidgets.QWidget()
        self.systemofequationschoosevectorScrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 79, 149))
        self.systemofequationschoosevectorScrollAreaWidgetContents.setObjectName("systemofequationschoosevectorScrollAreaWidgetContents")
        self.systemofequationschoosevectorScrollAreaWidgetContents.setStyleSheet(soetss.systemofequationschoosevectorScrollAreaWidgetContents_stylesheet)

        self.systemofequationschoosevectorscreen_gridLayout = QtWidgets.QHBoxLayout(self.systemofequationschoosevectorScrollAreaWidgetContents)
        self.systemofequationschoosevectorscreen_gridLayout.setSpacing(0)
        self.systemofequationschoosevectorscreen_gridLayout.setObjectName("systemofequationschoosevectorscreen_gridLayout")

        self.systemofequationschoosevectorscreen_vectorgridLayoutWidget = QtWidgets.QWidget()
        self.systemofequationschoosevectorscreen_vectorgridLayout = QtWidgets.QHBoxLayout(self.systemofequationschoosevectorscreen_vectorgridLayoutWidget)
        self.systemofequationschoosevectorscreen_vectorgridLayout.setSpacing(5)

        ###############################################
        ##SYSTEM OF EQ VECTOR SCROLL AREA VALUES GRID##
        ###############################################

        self.systemofequationschoosevectorparentesisopenlabel = QtWidgets.QLabel()
        self.systemofequationschoosevectorparentesisopenlabel.setPixmap(QtGui.QPixmap("icons/Itemparentesisopen.png"))
        self.systemofequationschoosevectorparentesisopenlabel.setScaledContents(True)
        self.systemofequationschoosevectorparentesisopenlabel.setFixedWidth(5)
        self.systemofequationschoosevectorparentesisclosedlabel = QtWidgets.QLabel()
        self.systemofequationschoosevectorparentesisclosedlabel.setPixmap(QtGui.QPixmap("icons/Itemparentesisclose.png"))
        self.systemofequationschoosevectorparentesisclosedlabel.setScaledContents(True)
        self.systemofequationschoosevectorparentesisclosedlabel.setFixedWidth(5)

        self.systemofequationschoosevectorscreen_valuesgridLayoutWidget = QtWidgets.QWidget()
        self.systemofequationschoosevectorscreen_valuesgridLayout = QtWidgets.QGridLayout(self.systemofequationschoosevectorscreen_valuesgridLayoutWidget)
        self.systemofequationschoosevectorscreen_valuesgridLayout.setContentsMargins(0, 0, 0, 0)
        self.systemofequationschoosevectorscreen_valuesgridLayout.setHorizontalSpacing(20)
        self.systemofequationschoosevectorscreen_valuesgridLayout.setVerticalSpacing(5)

        self.systemofequationschoosevectorscreen_gridLayout.addWidget(self.systemofequationschoosevectorscreen_vectorgridLayoutWidget, 1, alignment=QtCore.Qt.AlignCenter)

        self.systemofequationschoosevectorscreen_vectorgridLayout.addWidget(self.systemofequationschoosevectorparentesisopenlabel, 0, alignment=QtCore.Qt.AlignLeft)
        self.systemofequationschoosevectorscreen_vectorgridLayout.addWidget(self.systemofequationschoosevectorscreen_valuesgridLayoutWidget, 1, alignment=QtCore.Qt.AlignCenter)
        self.systemofequationschoosevectorscreen_vectorgridLayout.addWidget(self.systemofequationschoosevectorparentesisclosedlabel, 2, alignment=QtCore.Qt.AlignLeft)

        self.systemofequationschoosevectorScrollArea.setWidget(self.systemofequationschoosevectorScrollAreaWidgetContents)

        self.systemofequationschoosevectorparentesisopenlabel.setHidden(True)
        self.systemofequationschoosevectorparentesisclosedlabel.setHidden(True)

        #########################################################
        ## EIGENVALUES CHOSEN VECTOR SCROLL AREA VALUES LABELS ##
        #########################################################
        systemfont = QtGui.QFont()
        systemfont.setFamily("Alice")
        systemfont.setPointSize(12)

        stringstylesheetvectorsystemchosen = "background-color: transparent;\n""color: rgb(236, 236, 236);\n"
        self.systemvectorchosen_vectorlabelcell_dict={}
        for x in range(1,11):
            self.systemvectorchosen_vectorlabelcell_dict["systemvectorchosen_vectorlabelcell"+str(x)+"_1"] = QtWidgets.QLabel(self.systemofequationschoosevectorscreen_valuesgridLayoutWidget)
            self.systemvectorchosen_vectorlabelcell_dict["systemvectorchosen_vectorlabelcell"+str(x)+"_1"].setStyleSheet(stringstylesheetvectorsystemchosen)
            self.systemvectorchosen_vectorlabelcell_dict["systemvectorchosen_vectorlabelcell"+str(x)+"_1"].setFont(systemfont)
            self.systemofequationschoosevectorscreen_valuesgridLayout.addWidget(self.systemvectorchosen_vectorlabelcell_dict["systemvectorchosen_vectorlabelcell"+str(x)+"_1"], (x-1), 0, 1, 1, alignment=QtCore.Qt.AlignCenter)
            self.systemvectorchosen_vectorlabelcell_dict["systemvectorchosen_vectorlabelcell"+str(x)+"_1"].setHidden(True)
        self.systemofequationdecorativebackgroundLabel = QtWidgets.QLabel(self.systemofequationsframe)
        self.systemofequationdecorativebackgroundLabel.setGeometry(QtCore.QRect(229, 50, 203, 151))
        self.systemofequationdecorativebackgroundLabel.setStyleSheet(soetss.systemofequationdecorativebackgroundLabel_stylesheet)
        self.systemofequationdecorativebackgroundLabel.setText("")
        self.systemofequationdecorativebackgroundLabel.setObjectName("systemofequationdecorativebackgroundLabel")
        self.systemofequationsdecorativeLabel = QtWidgets.QLabel(self.systemofequationsframe)
        self.systemofequationsdecorativeLabel.setGeometry(QtCore.QRect(252, 55, 161, 141))
        self.systemofequationsdecorativeLabel.setStyleSheet("background-color: transparent;")
        self.systemofequationsdecorativeLabel.setText("")
        self.systemofequationsdecorativeLabel.setPixmap(QtGui.QPixmap("icons/Decorativesystemofequationsicon.png"))
        self.systemofequationsdecorativeLabel.setObjectName("systemofequationsdecorativeLabel")
        ###############
        ###Title bar###
        ###############
        self.Titlebarframe = QtWidgets.QFrame(self.centralwidget)
        self.Titlebarframe.setGeometry(QtCore.QRect(0, 0, 618, 29))
        self.Titlebarframe.setStyleSheet("background-color: rgb(17, 18, 17);")
        self.Titlebarframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Titlebarframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Titlebarframe.setObjectName("Titlebarframe")
        self.Exit_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Exit_Button.setGeometry(QtCore.QRect(673, 0, 51, 29))
        self.Exit_Button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(17, 18, 17);\n"
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
        self.Exit_Button.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icons/ExitButttonicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Exit_Button.setIcon(icon13)
        self.Exit_Button.setIconSize(QtCore.QSize(21, 21))
        self.Exit_Button.setCheckable(False)
        self.Exit_Button.setObjectName("Exit_Button")
        self.Minimize_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Minimize_Button.setGeometry(QtCore.QRect(618, 0, 51, 29))
        self.Minimize_Button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(17, 18, 17);\n"
"    border-bottom:2px;\n"
"    border-right:None;\n"
"    border-style:solid;\n"
"    border-color:none;\n"
"    margin:0px;    \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(35, 36, 35);\n"
"    border-style:solid;\n"
"    border-color:none;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(25, 26, 25);\n"
"    border-style:solid;\n"
"    border-color:none;    \n"
"}    \n"
"")
        self.Minimize_Button.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("icons/MinimizeButttonicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Minimize_Button.setIcon(icon14)
        self.Minimize_Button.setIconSize(QtCore.QSize(21, 21))
        self.Minimize_Button.setCheckable(False)
        self.Minimize_Button.setObjectName("Minimize_Button")
        self.Titlebarbuttons_fillerlabel = QtWidgets.QLabel(self.centralwidget)
        self.Titlebarbuttons_fillerlabel.setGeometry(QtCore.QRect(669, 0, 4, 29))
        self.Titlebarbuttons_fillerlabel.setStyleSheet("background-color: rgb(17, 18, 17);\n")
        self.Titlebarbuttons_fillerlabel.setText("")
        self.Titlebarbuttons_fillerlabel.setObjectName("Titlebarbuttons_fillerlabel")
        ######################
        #MAIN ECUATION STRING#
        ######################
        self.layoutforeqstringwidget=QtWidgets.QWidget(self.centralwidget)
        self.layoutforeqstring = QtWidgets.QVBoxLayout(self.layoutforeqstringwidget)
        self.layoutforeqstring.setContentsMargins(0,0,0,0)
        self.layoutforeqstringwidget.setGeometry(QtCore.QRect(112, 289, 481, 29))

        self.eqstringtextEdit = QTextEditdropenabled(self.admin)
        self.eqstringtextEdit.setStyleSheet(vmtss.eqstringtextEdit_stylesheet)
        self.eqstringtextEdit.setObjectName("eqstringtextEdit")
        self.eqstringtextEdit.setPlaceholderText("Type here...")
        self.eqstringtextEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.eqstringtextEdit.setLineWrapColumnOrWidth(0)
        self.eqstringtextEdit.setReadOnly(True)
        self.eqstringtextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.layoutforeqstring.addWidget(self.eqstringtextEdit,0)

        ##################
        #ESCONDER WIDGETS#
        ##################

        self.systemofequationsframe.hide()
        self.Decorativelabelmiddlebottom.hide()
        for x in self.matrixoperatorsbuttons_names:
            self.matrixoperatorsbuttons_dict[x].hide()
        for x in self.vectoroperatorsbuttons_names:
            self.vectoroperatorsbuttons_dict[x].hide() 
        for x in self.answer_and_equalbuttons_names: 
            self.answer_and_equalbuttons_dict[x].hide()
        self.generaloperatorsframe.hide()
        self.draggablevectorListWidget.hide()
        self.draggablematrixListWidget.hide()
        self.clickndraglabel.hide()
        self.screen_scrollArea.hide()
        self.angleswritevectorFrame.hide()
        self.angleschoosevectorFrame.hide()
        self.angleresultFrame.hide()
        self.angleshorizontalSlider.hide()
        self.anglesimportLabel.hide()
        self.angleswriteLabel.hide()
        self.layoutforeqstringwidget.hide()
        self.bakcgrounddecorativeslideLabel.hide()
        self.ddordmshorizontalSlider.hide()
        self.decimaldegreeLabel.hide()
        self.degreesminutessecondsLabel.hide()
        self.eigenvaluesframe.hide()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 29, 711, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setStyleSheet("color: rgb(96, 96, 96);\n"
"font: 10pt \"Alice\";\n"
""
)
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.vectorsButton.setToolTip(_translate("MainWindow", "Vectors"))
        self.vectorsButton.setStatusTip(_translate("MainWindow", "Vectors"))
        self.vectorsButton.setWhatsThis(_translate("MainWindow", "Vectors"))
        self.vectorsButton.setAccessibleName(_translate("MainWindow", "Vectors"))
        self.vectorsButton.setAccessibleDescription(_translate("MainWindow", "Vectors"))
        self.matrixButton.setToolTip(_translate("MainWindow", "Matrix"))
        self.matrixButton.setStatusTip(_translate("MainWindow", "Matrix"))
        self.matrixButton.setWhatsThis(_translate("MainWindow", "Matrix"))
        self.matrixButton.setAccessibleName(_translate("MainWindow", "Matrix"))
        self.matrixButton.setAccessibleDescription(_translate("MainWindow", "Matrix"))
        self.anglesButton.setToolTip(_translate("MainWindow", "Angles"))
        self.anglesButton.setStatusTip(_translate("MainWindow", "Angles"))
        self.anglesButton.setWhatsThis(_translate("MainWindow", "Angles"))
        self.anglesButton.setAccessibleName(_translate("MainWindow", "Angles"))
        self.anglesButton.setAccessibleDescription(_translate("MainWindow", "Angles"))
        self.eigenvaluesButton.setToolTip(_translate("MainWindow", "Eigenvectors"))
        self.eigenvaluesButton.setStatusTip(_translate("MainWindow", "Eigenvectors"))
        self.eigenvaluesButton.setWhatsThis(_translate("MainWindow", "Eigenvectors"))
        self.eigenvaluesButton.setAccessibleName(_translate("MainWindow", "Eigenvectors"))
        self.eigenvaluesButton.setAccessibleDescription(_translate("MainWindow", "Eigenvectors"))
        self.systemofequationButton.setToolTip(_translate("MainWindow", "System of Equations"))
        self.systemofequationButton.setStatusTip(_translate("MainWindow", "System of Equations"))
        self.systemofequationButton.setWhatsThis(_translate("MainWindow", "System of Equations"))
        self.systemofequationButton.setAccessibleName(_translate("MainWindow", "System of Equations"))
        self.systemofequationButton.setAccessibleDescription(_translate("MainWindow", "System of Equations"))
        self.infoButton.setToolTip(_translate("MainWindow", "Info"))
        self.infoButton.setToolTip(_translate("MainWindow", "Info"))
        self.infoButton.setStatusTip(_translate("MainWindow", "Info"))
        self.infoButton.setWhatsThis(_translate("MainWindow", "Info"))
        self.infoButton.setAccessibleName(_translate("MainWindow", "Info"))
        self.assignButton.setToolTip(_translate("MainWindow", "Assign values"))
        self.assignButton.setStatusTip(_translate("MainWindow", "Assign values"))
        self.assignButton.setWhatsThis(_translate("MainWindow", "Assign values"))
        self.assignButton.setAccessibleName(_translate("MainWindow", "Assign values"))
        self.assignButton.setAccessibleDescription(_translate("MainWindow", "Assign values"))
        vectoroperatorsbuttons_tooltipcounter=-1
        vectoroperatorsbuttons_tooltips=["Addition","Subtraction","Scalar Product","Vector Product","Magnitude"]
        for x in self.vectoroperatorsbuttons_names:
            vectoroperatorsbuttons_tooltipcounter+=1
            self.vectoroperatorsbuttons_dict[x].setToolTip(_translate("MainWindow", vectoroperatorsbuttons_tooltips[vectoroperatorsbuttons_tooltipcounter]))
            self.vectoroperatorsbuttons_dict[x].setStatusTip(_translate("MainWindow", vectoroperatorsbuttons_tooltips[vectoroperatorsbuttons_tooltipcounter]))
            self.vectoroperatorsbuttons_dict[x].setWhatsThis(_translate("MainWindow", vectoroperatorsbuttons_tooltips[vectoroperatorsbuttons_tooltipcounter]))
            self.vectoroperatorsbuttons_dict[x].setAccessibleName(_translate("MainWindow", vectoroperatorsbuttons_tooltips[vectoroperatorsbuttons_tooltipcounter]))
        matrixoperatorsbuttons_tooltipcounter=-1
        matrixoperatorsbuttons_tooltips=["Addition","Subtraction","Product","Transpose","Determinant"]
        for x in self.matrixoperatorsbuttons_names:
            matrixoperatorsbuttons_tooltipcounter+=1 
            self.matrixoperatorsbuttons_dict[x].setToolTip(_translate("MainWindow", matrixoperatorsbuttons_tooltips[matrixoperatorsbuttons_tooltipcounter]))
            self.matrixoperatorsbuttons_dict[x].setStatusTip(_translate("MainWindow", matrixoperatorsbuttons_tooltips[matrixoperatorsbuttons_tooltipcounter]))
            self.matrixoperatorsbuttons_dict[x].setWhatsThis(_translate("MainWindow", matrixoperatorsbuttons_tooltips[matrixoperatorsbuttons_tooltipcounter]))
            self.matrixoperatorsbuttons_dict[x].setAccessibleName(_translate("MainWindow", matrixoperatorsbuttons_tooltips[matrixoperatorsbuttons_tooltipcounter]))
        answer_equal_buttons_tooltipcounter=-1
        answer_equal_buttons_tooltips=["Use previous Answer","Solve"]
        for x in self.answer_and_equalbuttons_names: 
            answer_equal_buttons_tooltipcounter+=1 
            self.answer_and_equalbuttons_dict[x].setToolTip(_translate("MainWindow", answer_equal_buttons_tooltips[answer_equal_buttons_tooltipcounter]))
            self.answer_and_equalbuttons_dict[x].setStatusTip(_translate("MainWindow", answer_equal_buttons_tooltips[answer_equal_buttons_tooltipcounter]))
            self.answer_and_equalbuttons_dict[x].setWhatsThis(_translate("MainWindow", answer_equal_buttons_tooltips[answer_equal_buttons_tooltipcounter]))
            self.answer_and_equalbuttons_dict[x].setAccessibleName(_translate("MainWindow", answer_equal_buttons_tooltips[answer_equal_buttons_tooltipcounter]))
        self.allclearButton.setToolTip(_translate("MainWindow", "Clear all"))
        self.allclearButton.setStatusTip(_translate("MainWindow", "Clear all"))
        self.allclearButton.setWhatsThis(_translate("MainWindow", "Clear all"))
        self.allclearButton.setAccessibleName(_translate("MainWindow", "Clear all"))
        self.generaloperatorsButtonsnamelist_line1tooltips=["Add","Subtract","Multiply","Divide","Sine","Cosine","Tangent","Hyperbolic Sine",
        "Hyperbolic Cosine","Hyperbolic Tangent","Logarithm base 10","Natural Logarithm"]
        self.generaloperatorsButtonsnamelist_line2tooltips=["Power","Root","Euler's Number","Pi Number","Inverse Sine","Inverse Cosine",
        "Inverse Tangent","Inverse Hyperbolic Sine","Inverse Hyperbolic Cosine","Inverse Hyperbolic Tangent","Logarithm Without Base",
        "Scalar Absolute"]
        generaloperators_line1_tooltipcounter=-1
        for x in self.generaloperatorsButtonsnamelist_line1:
            generaloperators_line1_tooltipcounter+=1
            self.generaloperatorsButtonsdict[x].setToolTip(_translate("MainWindow", self.generaloperatorsButtonsnamelist_line1tooltips[generaloperators_line1_tooltipcounter]))
            self.generaloperatorsButtonsdict[x].setStatusTip(_translate("MainWindow", self.generaloperatorsButtonsnamelist_line1tooltips[generaloperators_line1_tooltipcounter]))
            self.generaloperatorsButtonsdict[x].setWhatsThis(_translate("MainWindow", self.generaloperatorsButtonsnamelist_line1tooltips[generaloperators_line1_tooltipcounter]))
            self.generaloperatorsButtonsdict[x].setAccessibleName(_translate("MainWindow", self.generaloperatorsButtonsnamelist_line1tooltips[generaloperators_line1_tooltipcounter]))
        generaloperators_line2_tooltipcounter=-1
        for x in self.generaloperatorsButtonsnamelist_line2:
            generaloperators_line2_tooltipcounter+=1
            self.generaloperatorsButtonsdict[x].setToolTip(_translate("MainWindow", self.generaloperatorsButtonsnamelist_line2tooltips[generaloperators_line2_tooltipcounter]))
            self.generaloperatorsButtonsdict[x].setStatusTip(_translate("MainWindow", self.generaloperatorsButtonsnamelist_line2tooltips[generaloperators_line2_tooltipcounter]))
            self.generaloperatorsButtonsdict[x].setWhatsThis(_translate("MainWindow", self.generaloperatorsButtonsnamelist_line2tooltips[generaloperators_line2_tooltipcounter]))
            self.generaloperatorsButtonsdict[x].setAccessibleName(_translate("MainWindow", self.generaloperatorsButtonsnamelist_line2tooltips[generaloperators_line2_tooltipcounter]))
        __sortingEnabled = self.draggablematrixListWidget.isSortingEnabled()
        self.draggablematrixListWidget.setSortingEnabled(False)
        self.draggablematrixListWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.draggablevectorListWidget.isSortingEnabled()
        self.draggablevectorListWidget.setSortingEnabled(False)
        self.draggablevectorListWidget.setSortingEnabled(__sortingEnabled)
        self.anglesimportLabel.setText(_translate("MainWindow", "IMPORT"))
        self.angleswriteLabel.setText(_translate("MainWindow", "WRITE"))
        self.writevectorLabel_x.setText(_translate("MainWindow", " Vector  I"))
        self.writevectorLabel_y.setText(_translate("MainWindow", " Vector II"))
        self.degreesminutessecondsLabel.setText(_translate("MainWindow", "DMS"))
        self.decimaldegreeLabel.setText(_translate("MainWindow", "  DD"))
        __sortingEnabled = self.eigenvalueschoosematrixListWidget.isSortingEnabled()
        self.eigenvalueschoosematrixListWidget.setSortingEnabled(False)
        self.eigenvalueschoosematrixListWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.systemofequationschoosematrixListWidget.isSortingEnabled()
        self.systemofequationschoosematrixListWidget.setSortingEnabled(False)
        self.systemofequationschoosematrixListWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.systemofequationschoosevectorListWidget.isSortingEnabled()
        self.systemofequationschoosevectorListWidget.setSortingEnabled(False)
        self.systemofequationschoosevectorListWidget.setSortingEnabled(__sortingEnabled)
        self.retranslateUi_listofmatrixnames=["Matrix1","Matrix2","Matrix3","Matrix4","Matrix5","Matrix6","Matrix7","Matrix8",
        "Matrix9","Matrix10","Matrix11","Matrix12","Matrix13","Matrix14","Matrix15","Matrix16","Matrix17","Matrix18",
        "Matrix19","Matrix20"]
        self.retranslateUi_listofvectornames=["Vector1","Vector2","Vector3","Vector4","Vector5","Vector6","Vector7","Vector8",
        "Vector9","Vector10","Vector11","Vector12","Vector13","Vector14","Vector15","Vector16","Vector17","Vector18",
        "Vector19","Vector20"]
        for x in range(0,20):
            item = self.draggablematrixListWidget.item(x)
            item.setText(_translate("MainWindow", self.retranslateUi_listofmatrixnames[x]))
            item = self.draggablevectorListWidget.item(x)
            item.setText(_translate("MainWindow", self.retranslateUi_listofvectornames[x]))
            item = self.eigenvalueschoosematrixListWidget.item(x)
            item.setText(_translate("MainWindow", self.retranslateUi_listofmatrixnames[x]))
            item = self.systemofequationschoosematrixListWidget.item(x)
            item.setText(_translate("MainWindow", self.retranslateUi_listofmatrixnames[x]))
            item = self.systemofequationschoosevectorListWidget.item(x)
            item.setText(_translate("MainWindow", self.retranslateUi_listofvectornames[x]))
            self.choosevectorcomboBox_x.setItemText(x, _translate("MainWindow", self.retranslateUi_listofvectornames[x]))
            self.choosevectorcomboBox_y.setItemText(x, _translate("MainWindow", self.retranslateUi_listofvectornames[x]))
            if x<12:
                self.writevectorcolumncomboBox_x.setItemText(x, _translate("MainWindow", str(x+1)))
                self.writevectorcolumncomboBox_y.setItemText(x, _translate("MainWindow", str(x+1)))
    def vectorsButtonstate(self):
        if self.vectorsButton.isChecked():
            self.matrixButton.setChecked(False)
            self.anglesButton.setChecked(False)
            self.eigenvaluesButton.setChecked(False)
            self.systemofequationButton.setChecked(False)
            self.eigenvaluesButtonstate()
            self.systemofequationButtonstate()
            self.anglesButtonstate()
            self.matrixButtonstate()
            self.main_title_label_top.setPixmap(QtGui.QPixmap("icons/Vectorstitle.png"))
            self.Decorativelabelmiddlebottom.show()
            for x in self.vectoroperatorsbuttons_names:
                self.vectoroperatorsbuttons_dict[x].show()
            for x in self.answer_and_equalbuttons_names: 
                self.answer_and_equalbuttons_dict[x].show()
            self.layoutforeqstringwidget.show()
            self.generaloperatorsframe.show()
            self.draggablevectorListWidget.show()
            self.clickndraglabel.show()
            self.screen_scrollArea.show()
        else:
            self.main_title_label_top.clear()
            self.Decorativelabelmiddlebottom.hide()
            for x in self.vectoroperatorsbuttons_names:
                self.vectoroperatorsbuttons_dict[x].hide() 
            for x in self.answer_and_equalbuttons_names: 
                self.answer_and_equalbuttons_dict[x].hide()
            self.layoutforeqstringwidget.hide()
            self.generaloperatorsframe.hide()
            self.draggablevectorListWidget.hide()
            self.clickndraglabel.hide()
            self.screen_scrollArea.hide()
            return
    def matrixButtonstate(self):
        if self.matrixButton.isChecked():
            self.vectorsButton.setChecked(False)
            self.anglesButton.setChecked(False)
            self.eigenvaluesButton.setChecked(False)
            self.systemofequationButton.setChecked(False)
            self.eigenvaluesButtonstate()
            self.systemofequationButtonstate()
            self.vectorsButtonstate()
            self.anglesButtonstate()
            self.main_title_label_top.setPixmap(QtGui.QPixmap("icons/Matrixtitle.png"))
            self.Decorativelabelmiddlebottom.show()
            for x in self.matrixoperatorsbuttons_names:
                self.matrixoperatorsbuttons_dict[x].show()
            for x in self.answer_and_equalbuttons_names: 
                self.answer_and_equalbuttons_dict[x].show()
            self.layoutforeqstringwidget.show()
            self.generaloperatorsframe.show()
            self.draggablematrixListWidget.show()
            self.clickndraglabel.show()
            self.screen_scrollArea.show()
        else:
            self.main_title_label_top.clear()
            self.Decorativelabelmiddlebottom.hide()
            for x in self.matrixoperatorsbuttons_names:
                self.matrixoperatorsbuttons_dict[x].hide()
            for x in self.answer_and_equalbuttons_names: 
                self.answer_and_equalbuttons_dict[x].hide()
            self.layoutforeqstringwidget.hide()
            self.generaloperatorsframe.hide()
            self.draggablematrixListWidget.hide()
            self.clickndraglabel.hide()
            self.screen_scrollArea.hide()
            return
    def anglesButtonstate(self):
        if self.anglesButton.isChecked():
            self.matrixButton.setChecked(False)
            self.vectorsButton.setChecked(False)
            self.eigenvaluesButton.setChecked(False)
            self.systemofequationButton.setChecked(False)
            self.eigenvaluesButtonstate()
            self.systemofequationButtonstate()
            self.vectorsButtonstate()
            self.matrixButtonstate()
            self.main_title_label_top.setPixmap(QtGui.QPixmap("icons/Angletitle.png"))
            self.Angleshorizontalslidervaluechanged()
            self.Anglesvectorxcomboboxvaluechanged()
            self.Anglesvectorycomboboxvaluechanged()
            self.WritevectorcolumncomboBox_yvaluechanged()
            self.WritevectorcolumncomboBox_xvaluechanged()
            self.angleresultFrame.show()
            self.angleshorizontalSlider.show()
            self.anglesimportLabel.show()
            self.angleswriteLabel.show()
            self.bakcgrounddecorativeslideLabel.show()
        else:
            self.main_title_label_top.clear()
            self.generaloperatorsframe.hide()
            self.angleswritevectorFrame.hide()
            self.angleschoosevectorFrame.hide()
            self.angleresultFrame.hide()
            self.angleshorizontalSlider.hide()
            self.anglesimportLabel.hide()
            self.angleswriteLabel.hide()
            self.bakcgrounddecorativeslideLabel.hide()
            return
    def eigenvaluesButtonstate(self):
        if self.eigenvaluesButton.isChecked():
            self.anglesButton.setChecked(False)
            self.matrixButton.setChecked(False)
            self.vectorsButton.setChecked(False)
            self.systemofequationButton.setChecked(False)
            self.systemofequationButtonstate()
            self.anglesButtonstate()
            self.vectorsButtonstate()
            self.matrixButtonstate()
            self.main_title_label_top.setPixmap(QtGui.QPixmap("icons/Eigenvectorstitle.png"))
            self.eigenvaluesframe.show()
        else:
            self.main_title_label_top.clear()
            self.generaloperatorsframe.hide()
            self.eigenvaluesframe.hide()
            return
    def systemofequationButtonstate(self):
        if self.systemofequationButton.isChecked():
            self.anglesButton.setChecked(False)
            self.matrixButton.setChecked(False)
            self.vectorsButton.setChecked(False)
            self.eigenvaluesButton.setChecked(False)
            self.eigenvaluesButtonstate()
            self.anglesButtonstate()
            self.vectorsButtonstate()
            self.matrixButtonstate()
            self.main_title_label_top.setPixmap(QtGui.QPixmap("icons/Systemofequationstitle.png"))
            self.systemofequationsframe.show()
        else:
            self.systemofequationsframe.hide()
            self.main_title_label_top.clear()
            self.generaloperatorsframe.hide()
            return
    def showassign_window(self):
        global assignvaluewindowhidden
        global startupmatrices
        if assignvaluewindowhidden:
            if startupmatrices:
                self.fillvectorstreeview()
                self.fillmatricestreeview()
                self.admin.window.assignvalueswindow.ui.NumberofmatrixcomboBox.setCurrentIndex(19)
                self.admin.window.assignvalueswindow.ui.hideandshowmatrixitems()
                self.admin.window.assignvalueswindow.show()
                startupmatrices=False
            else:
                self.admin.window.assignvalueswindow.show()
            assignvaluewindowhidden=False
        else:
            self.admin.window.assignvalueswindow.hide()
            assignvaluewindowhidden=True
    def updatematrixtreeitemsontabchange(self):
        global firsttabchange
        if firsttabchange:
            self.admin.window.assignvalueswindow.ui.NumberofmatrixcomboBox.setCurrentIndex(19)
            self.admin.window.assignvalueswindow.ui.hideandshowmatrixitems()
            self.fillmatricestreeview()
            self.admin.window.assignvalueswindow.ui.NumberofmatrixcomboBox.setCurrentIndex(0)
            self.admin.window.assignvalueswindow.ui.hideandshowmatrixitems()
            firsttabchange = False
        else:
            pass
    def converttofloat(self,frac_str):
        try:
            return float(frac_str)
        except ValueError:
            num, denom = frac_str.split('/')
            try:
                leading, num = num.split(' ')
                whole = float(leading)
            except ValueError:
                whole = 0
            frac = float(num) / float(denom)
            return whole - frac if whole < 0 else whole + frac
    def fillmatricestreeview(self):
        self.admin.updatematricestree()
        for z in range (0,20):
            numberofmatrix = z
            arrayofselectedmatrix = self.admin.matricesarrays[numberofmatrix]
            spacing="   "

            for x in range(0, self.admin.matricesrows[numberofmatrix]):
                for y in range(0, self.admin.matricescolumns[numberofmatrix]):
                    self.admin.window.assignvalueswindow.ui.matriceslabelcell_dict["matrix"+str(numberofmatrix+1)+"labelcell"+str(x+1)+"_"+str(y+1)].setHidden(False)
                    if y == (self.admin.matricescolumns[numberofmatrix]-1):
                        self.admin.window.assignvalueswindow.ui.matriceslabelcell_dict["matrix"+str(numberofmatrix+1)+"labelcell"+str(x+1)+"_"+str(y+1)].setText(str(arrayofselectedmatrix[x][y]))
                    else:
                        self.admin.window.assignvalueswindow.ui.matriceslabelcell_dict["matrix"+str(numberofmatrix+1)+"labelcell"+str(x+1)+"_"+str(y+1)].setText(str(arrayofselectedmatrix[x][y])+spacing)

            for x in range(0,10):
                for y in range(0,10):
                    if (x+1) > self.admin.matricesrows[numberofmatrix]:
                        self.admin.window.assignvalueswindow.ui.matriceslabelcell_dict["matrix"+str(numberofmatrix+1)+"labelcell"+str(x+1)+"_"+str(y+1)].setHidden(True)
                    elif (y+1) > self.admin.matricescolumns[numberofmatrix]:
                        self.admin.window.assignvalueswindow.ui.matriceslabelcell_dict["matrix"+str(numberofmatrix+1)+"labelcell"+str(x+1)+"_"+str(y+1)].setHidden(True)
                    else:
                        pass

        Comboboxselectionneedeed=self.admin.window.assignvalueswindow.ui.NumberofmatrixcomboBox.currentText()
        self.admin.window.assignvalueswindow.ui.NumberofmatrixcomboBox.setCurrentText(str(int(Comboboxselectionneedeed)-1))
        self.admin.window.assignvalueswindow.ui.hideandshowmatrixitems()
        self.admin.window.assignvalueswindow.ui.NumberofmatrixcomboBox.setCurrentText(Comboboxselectionneedeed)
        self.admin.window.assignvalueswindow.ui.hideandshowmatrixitems()
    def fillvectorstreeview(self):
        self.admin.updatevectorstree()
        for x in range (0,20):
            stringlist=""
            listofthings=[]
            numberofvector = x
            for y in range(0,(self.admin.vectorsrows[numberofvector])):
                listofthings.append(list(self.admin.vectorsarrays[numberofvector][y]))
            for z in range(0, len(listofthings)):
                for w in range(0,self.admin.vectorscolumns[numberofvector]):
                    thing=listofthings[z][w]
                    stringlist = stringlist + str(thing)
                    if w == (self.admin.vectorscolumns[numberofvector]-1):
                        pass
                    else:
                        stringlist = stringlist + "   "
                if z == (len(listofthings)-1):
                    pass
                else:
                    stringlist = stringlist + "\n"

            self.admin.window.assignvalueswindow.ui.vectorslabel_dict["vector"+str(x+1)+"label"].setText(stringlist)
        Comboboxselectionneedeed=self.admin.window.assignvalueswindow.ui.NumberofvectorscomboBox.currentText()
        self.admin.window.assignvalueswindow.ui.NumberofvectorscomboBox.setCurrentText(str(int(Comboboxselectionneedeed)-1))
        self.admin.window.assignvalueswindow.ui.hideandshowvectoritems()
        self.admin.window.assignvalueswindow.ui.NumberofvectorscomboBox.setCurrentText(Comboboxselectionneedeed)
        self.admin.window.assignvalueswindow.ui.hideandshowvectoritems()
    def Allclearbuttonclicked(self):
        if self.vectorsButton.isChecked() or self.matrixButton.isChecked():
            self.eqstringtextEdit.clear()
            for x, y in itools.product(range(1,11), range(1,11)):
                self.result_matrixlabelcelldict["result_matrixlabelcell"+str(x)+"_"+str(y)].setHidden(True)
            self.resultmatrixparentesisopenlabel.setHidden(True)
            self.resultmatrixparentesisclosedlabel.setHidden(True)
            self.resultlabelerror.setHidden(True)
            self.resultlabelintorfloat.setHidden(True)
        if self.anglesButton.isChecked():
            self.anglesscreen_scrollArearesultLabel.clear()
        if self.eigenvaluesButton.isChecked():
            for x in range(0, 10):
                self.eigenvectorsLabel_dict["eigenvectorsLabel_"+str(x+1)].setHidden(True)
                self.eigenvaluemultiplicityLabel_dict["eigenvaluemultiplicityLabel_"+str(x+1)].setHidden(True)
                self.eigenvalueLabel_dict["eigenvalueLabel_"+str(x+1)].setHidden(True)
        if self.systemofequationButton.isChecked():
            self.systemofequationsresultscrollArearesultLabel.clear()
    def formatNumber(self,num):
        if num % 1 == 0:
            return int(num)
        else:
            return num
    def converttofraction(self,num):
        frac = Fraction(num).limit_denominator()
        if frac.denominator > 300:
            return num
        else:
            return frac
    def Equalbuttonclicked(self):
        equation_string = self.eqstringtextEdit.toPlainText()
        if equation_string == "":
            return
        self.admin.calculatestringequation(equation_string,self.degorrad)
        if self.admin.is_equationresult_matrix==True:
            self.resultlabelerror.setHidden(True)
            for j in range(0, (self.admin.equation_final_result.row)):
                for k in range(0,(self.admin.equation_final_result.column)):
                    self.result_matrixlabelcelldict["result_matrixlabelcell"+str(j+1)+"_"+str(k+1)].setText(str(self.converttofraction(self.formatNumber(self.converttofloat(self.admin.equation_final_result.values[j][k])))))
            for x in range(0,10):
                for y in range(0,10):
                    self.result_matrixlabelcelldict["result_matrixlabelcell"+str(x+1)+"_"+str(y+1)].setHidden(True)
            for x in range(0, (self.admin.equation_final_result.row)):
                for y in range(0, (self.admin.equation_final_result.column)):
                    self.result_matrixlabelcelldict["result_matrixlabelcell"+str(x+1)+"_"+str(y+1)].setHidden(False)
            self.resultmatrixparentesisopenlabel.setHidden(False)
            self.resultmatrixparentesisclosedlabel.setHidden(False)
        if self.admin.is_equationresult_matrix==False:
            for x in range(0, 10):
                for y in range(0, 10):
                    self.result_matrixlabelcelldict["result_matrixlabelcell"+str(x+1)+"_"+str(y+1)].setHidden(True)
            self.resultmatrixparentesisopenlabel.setHidden(True)
            self.resultmatrixparentesisclosedlabel.setHidden(True)

        if self.admin.is_equationresult_intorfloat==True or self.admin.is_equationresult_complex==True:
            self.resultlabelerror.setHidden(True)
            self.resultlabelintorfloat.setHidden(False)
            try:
                self.resultlabelintorfloat.setText(str(self.formatNumber(self.admin.equation_final_result)))
            except:
                self.resultlabelintorfloat.setText(str(self.admin.equation_final_result))

        if self.admin.is_equationresult_intorfloat==False and self.admin.is_equationresult_complex==False:
            self.resultlabelintorfloat.setHidden(True)

        if self.admin.is_equationresult_intorfloat==False and self.admin.is_equationresult_matrix==False and self.admin.is_equationresult_complex==False:
            self.resultlabelerror.setHidden(False)
            self.resultlabelerror.setText(str(self.admin.equation_final_result))

    def Answerbuttonclicked(self):
        self.eqstringtextEdit.insertPlainText("Ans")
    def Additionbuttonclicked(self):
        self.eqstringtextEdit.insertPlainText("+")
    def Subtractionbuttonclicked(self):
        self.eqstringtextEdit.insertPlainText("-")
    def Matrixproductbuttonclicked(self):
        self.eqstringtextEdit.insertPlainText("*")
    def Determinantbuttonclicked(self):
        self.eqstringtextEdit.insertPlainText("det()")
    def Transposebuttonclicked(self):
        self.eqstringtextEdit.insertPlainText("tr()")
    def Scalarbuttonclicked(self):
        self.eqstringtextEdit.insertPlainText("@")
    def Vectorproductbuttonclicked(self):
        self.eqstringtextEdit.insertPlainText("&")
    def Magnitudebuttonclicked(self):
        self.eqstringtextEdit.insertPlainText("norm()")
    def Generaladdbuttonclicked(self):
        self.eqstringtextEdit.insertPlainText("+")
    def Generalsubbuttonclicked(self):
        self.eqstringtextEdit.insertPlainText("-")
    def Generalmultiplybuttonclicked(self):
        self.eqstringtextEdit.insertPlainText("*")
    def Generaldivisionbuttonclicked(self):
        self.eqstringtextEdit.insertPlainText("/")
    def Generalpowerbuttonclicked(self):
        self.eqstringtextEdit.insertPlainText("^")
    def Generalrootbuttonclicked(self):
        self.eqstringtextEdit.insertPlainText("√()")
    def Generalebuttonclicked(self):
        self.eqstringtextEdit.insertPlainText("ℇ")
    def Generalpibuttonclicked(self):
        self.eqstringtextEdit.insertPlainText("π")
    def Generalsinbuttonclicked(self):
        self.eqstringtextEdit.insertPlainText("sin()")
    def Generalcosbuttonclicked(self):
        self.eqstringtextEdit.insertPlainText("cos()")
    def Generaltanbuttonclicked(self):
        self.eqstringtextEdit.insertPlainText("tan()")
    def Generalsinhbuttonclicked(self):
        self.eqstringtextEdit.insertPlainText("sinh()")
    def Generalcoshbuttonclicked(self):
        self.eqstringtextEdit.insertPlainText("cosh()")
    def Generaltanhbuttonclicked(self):
        self.eqstringtextEdit.insertPlainText("tanh()")
    def Generalsininvbuttonclicked(self):
        self.eqstringtextEdit.insertPlainText("arcsin()")
    def Generalcosinvbuttonclicked(self):
        self.eqstringtextEdit.insertPlainText("arccos()")
    def Generaltaninvbuttonclicked(self):
        self.eqstringtextEdit.insertPlainText("arctan()")
    def Generalsinhinvbuttonclicked(self):
        self.eqstringtextEdit.insertPlainText("arcsinh()")
    def Generalcoshinvbuttonclicked(self):
        self.eqstringtextEdit.insertPlainText("arccosh()")
    def Generaltanhinvbuttonclicked(self):
        self.eqstringtextEdit.insertPlainText("arctanh()")
    def Generallogbuttonclicked(self):
        self.eqstringtextEdit.insertPlainText("Log()")
    def Generalinbuttonclicked(self):
        self.eqstringtextEdit.insertPlainText("In()")
    def Generallogchoosebuttonclicked(self):
        self.eqstringtextEdit.insertPlainText("Logchoosebase(base,argument)")
    def Generalabsolutebuttonclicked(self):
        self.eqstringtextEdit.insertPlainText("absolute()")
    def Vectorandmatrixlistwidgetdoubleclicked(self):
        texttoadd=""
        if self.admin.window.ui.matrixButton.isChecked():
            texttoadd=str(self.admin.window.ui.draggablematrixListWidget.currentItem().text())
            self.admin.window.ui.eqstringtextEdit.insertPlainText(texttoadd)
        elif self.admin.window.ui.vectorsButton.isChecked():
            texttoadd=str(self.admin.window.ui.draggablevectorListWidget.currentItem().text())
            self.admin.window.ui.eqstringtextEdit.insertPlainText(texttoadd)
        else:
            return

    def Degandradverticalslidervaluechanged(self):
        if self.degandradverticalSlider.value() == 1:
            self.degorrad = "DEG"
            self.radLabel.setStyleSheet("font: 8pt \"Alice\";\n"
"color: rgb(96, 96, 96);\n"
"background-color:transparent;\n"
"border:0px;\n"
"margin:0px;")
            self.degreeLabel.setStyleSheet("font: 8pt \"Alice\";\n"
"color: rgb(126, 126, 126);\n"
"background-color:transparent;\n"
"border:0px;\n"
"margin:0px;")
            self.ddordmshorizontalSlider.show()
            self.decimaldegreeLabel.show()
            self.degreesminutessecondsLabel.show()
        if self.degandradverticalSlider.value() == 0:
            self.degorrad = "RAD"
            self.degreeLabel.setStyleSheet("font: 8pt \"Alice\";\n"
"color: rgb(96, 96, 96);\n"
"background-color:transparent;\n"
"border:0px;\n"
"margin:0px;")
            self.radLabel.setStyleSheet("font: 8pt \"Alice\";\n"
"color: rgb(126, 126, 126);\n"
"background-color:transparent;\n"
"border:0px;\n"
"margin:0px;")
            self.ddordmshorizontalSlider.hide()
            self.decimaldegreeLabel.hide()
            self.degreesminutessecondsLabel.hide()

    def Ddordmshorizontalslidervaluechanged(self):
        if self.ddordmshorizontalSlider.value() == 1:
            self.ddordms = "DD"
            self.decimaldegreeLabel.setStyleSheet("font: 7pt \"Alice\";\n"
"background-color: transparent;\n"
"color: rgb(126, 126, 126);")
            self.degreesminutessecondsLabel.setStyleSheet("font: 7pt \"Alice\";\n"
"background-color: transparent;\n"
"color: rgb(96, 96, 96);")
        if self.ddordmshorizontalSlider.value() == 0:
            self.ddordms = "DMS"
            self.decimaldegreeLabel.setStyleSheet("font: 7pt \"Alice\";\n"
"background-color: transparent;\n"
"color: rgb(96, 96, 96);")
            self.degreesminutessecondsLabel.setStyleSheet("font: 7pt \"Alice\";\n"
"background-color: transparent;\n"
"color: rgb(126, 126, 126);")

    def Angleshorizontalslidervaluechanged(self):
        if self.angleshorizontalSlider.value() == 1:
            self.angleswritevectorFrame.show()
            self.angleschoosevectorFrame.hide()
            self.anglesimportLabel.setStyleSheet("font: 8pt \"Alice\";\n"
"background-color: transparent;\n"
"color: rgb(96, 96, 96);")
            self.angleswriteLabel.setStyleSheet("font: 8pt \"Alice\";\n"
"background-color: transparent;\n"
"color: rgb(126, 126, 126);")
        if self.angleshorizontalSlider.value() == 0:
            self.angleswritevectorFrame.hide()
            self.angleschoosevectorFrame.show()
            self.anglesimportLabel.setStyleSheet("font: 8pt \"Alice\";\n"
"background-color: transparent;\n"
"color: rgb(126, 126, 126);")
            self.angleswriteLabel.setStyleSheet("font: 8pt \"Alice\";\n"
"background-color: transparent;\n"
"color: rgb(96, 96, 96);")

    def Anglesvectorxcomboboxvaluechanged(self):
        chosenvector = self.choosevectorcomboBox_x.currentText()
        chosenvectorvalues = self.admin.getangleschosenvector(chosenvector)
        stringforchosenloop = "(    "
        for x in chosenvectorvalues[0]:
            valueofcell = str(self.converttofraction(self.formatNumber(self.converttofloat(x))))
            stringofchosenvectorvalues = stringforchosenloop + valueofcell + "    "
            stringforchosenloop = stringofchosenvectorvalues
        stringofchosenvectorvalues = stringofchosenvectorvalues + ")"
        self.valueschoosexLabel.setText("        "+stringofchosenvectorvalues)

    def Anglesvectorycomboboxvaluechanged(self):
        chosenvector = self.choosevectorcomboBox_y.currentText()
        chosenvectorvalues = self.admin.getangleschosenvector(chosenvector)
        stringforchosenloop = "(    "
        for x in chosenvectorvalues[0]:
            valueofcell = str(self.converttofraction(self.formatNumber(self.converttofloat(x))))
            stringofchosenvectorvalues = stringforchosenloop + valueofcell + "    "
            stringforchosenloop = stringofchosenvectorvalues
        stringofchosenvectorvalues = stringofchosenvectorvalues + ")"
        self.valueschooseyLabel.setText("        "+stringofchosenvectorvalues)

    def WritevectorcolumncomboBox_xvaluechanged(self):
        numberofcolumnsselected=int(self.writevectorcolumncomboBox_x.currentText())
        self.writevectorcolumncomboBox_y.setItemText(self.writevectorcolumncomboBox_y.currentIndex(),self.writevectorcolumncomboBox_x.currentText())
        self.WritevectorcolumncomboBox_yvaluechanged()
        for x in range (1,numberofcolumnsselected+1):
            self.writevectorxlineEdit_dict["writevectorxlineEdit_"+str(x)].show()
        for x in range (numberofcolumnsselected+1,13):
            self.writevectorxlineEdit_dict["writevectorxlineEdit_"+str(x)].hide()

    def WritevectorcolumncomboBox_yvaluechanged(self):
        numberofcolumnsselected=int(self.writevectorcolumncomboBox_y.currentText())
        for x in range (1,numberofcolumnsselected+1):
            self.writevectorylineEdit_dict["writevectorylineEdit_"+str(x)].show()
        for x in range (numberofcolumnsselected+1,13):
            self.writevectorylineEdit_dict["writevectorylineEdit_"+str(x)].hide()

    def Angleswritevectorscreatearray(self):
        try:
            self.writenvectorsfilled=True
            self.listofvectorxvalues=[[]]
            self.listofvectoryvalues=[[]]
            self.vectorxnumbercolumns=int(self.writevectorcolumncomboBox_x.currentText())
            self.vectorynumbercolumns=int(self.writevectorcolumncomboBox_y.currentText())
            for x in range(1,self.vectorxnumbercolumns+1):
                if self.writevectorxlineEdit_dict["writevectorxlineEdit_"+str(x)].text() == "":
                    self.admin.window.errorwindow.show()
                    self.admin.window.errorwindow.ui.Errorwindowbodylabel.setText("All Vector I cells must be filled.")
                    self.writenvectorsfilled=False
                else:
                    self.listofvectorxvalues[0].append(self.converttofloat(self.writevectorxlineEdit_dict["writevectorxlineEdit_"+str(x)].text()))
            for y in range(1,self.vectorynumbercolumns+1):
                if self.writevectorylineEdit_dict["writevectorylineEdit_"+str(y)].text() == "":
                    self.admin.window.errorwindow.show()
                    self.admin.window.errorwindow.ui.Errorwindowbodylabel.setText("All Vector II cells must be filled.")
                    self.writenvectorsfilled=False
                else:
                    self.listofvectoryvalues[0].append(self.converttofloat(self.writevectorylineEdit_dict["writevectorylineEdit_"+str(y)].text()))
            self.admin.angleswritevectorscreatearray(self.listofvectorxvalues,self.listofvectoryvalues,self.vectorxnumbercolumns,self.vectorynumbercolumns)
        except:
            pass

    def AnglescalculatepushButtonclicked(self):
        if self.angleshorizontalSlider.value() == 0:
            result = self.admin.calculateangles(self.choosevectorcomboBox_x.currentText(),self.choosevectorcomboBox_y.currentText(),self.degorrad,self.ddordms)
            if self.degorrad=="RAD":
                self.anglesscreen_scrollArearesultLabel.setText(result+" rad")
            if self.degorrad=="DEG":
                self.anglesscreen_scrollArearesultLabel.setText(result+" degrees")
        if self.angleshorizontalSlider.value() == 1:
            self.Angleswritevectorscreatearray()
            result = self.admin.calculateangles("VectorI","VectorII",self.degorrad,self.ddordms)
            if self.degorrad=="RAD":
                self.anglesscreen_scrollArearesultLabel.setText(result+" rad")
            if self.degorrad=="DEG":
                self.anglesscreen_scrollArearesultLabel.setText(result+" degrees")
            if self.writenvectorsfilled == False:
                self.anglesscreen_scrollArearesultLabel.clear()
    def Eigenvalueschoosematrixlistwidgetitemchanged(self):
        chosenmatrixtoshow = self.eigenvalueschoosematrixListWidget.currentItem().text()
        self.admin.geteigenchosenmatrix(chosenmatrixtoshow)
        self.emptystring=""

        for j in range(0, 10):
            for k in range(0,10):
                self.eigenchosen_matrixlabelcelldict["eigenchosen_matrixlabelcell"+str(j+1)+"_"+str(k+1)].setText("")

        for j in range(0, (self.admin.eigenchosenmatrixobject.row)):
            for k in range(0,(self.admin.eigenchosenmatrixobject.column)):
                self.eigenchosen_matrixlabelcelldict["eigenchosen_matrixlabelcell"+str(j+1)+"_"+str(k+1)].setText(str(self.converttofraction(self.formatNumber(self.converttofloat(self.admin.eigenchosenmatrixobject.values[j][k])))))

        for x in range(0,10):
            for y in range(0,10):
                self.eigenchosen_matrixlabelcelldict["eigenchosen_matrixlabelcell"+str(x+1)+"_"+str(y+1)].setHidden(True)

        for x in range(0, (self.admin.eigenchosenmatrixobject.row)):
            for y in range(0, (self.admin.eigenchosenmatrixobject.column)):
                self.eigenchosen_matrixlabelcelldict["eigenchosen_matrixlabelcell"+str(x+1)+"_"+str(y+1)].setHidden(False)

        self.eigenvalueschosenmatrixparentesisopenlabel.setHidden(False)
        self.eigenvalueschosenmatrixparentesisclosedlabel.setHidden(False)


    def Eigenvaluescalculatepushbuttonclicked(self):
        try:
            chosenmatrixtoeigen = self.eigenvalueschoosematrixListWidget.currentItem().text()
        except:
            self.admin.window.errorwindow.show()
            self.admin.window.errorwindow.ui.Errorwindowbodylabel.setText("Select a Matrix")
            return

        self.admin.geteigenvectors(chosenmatrixtoeigen)

        if self.admin.eigenvectorsresult == []:
            return
        else:
            for x in range(0,len(self.admin.eigenvectorsresult)):
                self.eigenvalueLabel_dict["eigenvalueLabel_"+str(x+1)].setHidden(False)

            try:
                for x in range(0,len(self.admin.eigenvectorsresult)):
                    self.eigenvalueLabel_dict["eigenvalueLabel_"+str(x+1)].setText("λ = "+str(self.converttofraction(self.formatNumber(self.converttofloat(self.admin.eigenvectorsresult[x][0])))))

            except:
                for x in range(0,len(self.admin.eigenvectorsresult)):
                    self.eigenvalueLabel_dict["eigenvalueLabel_"+str(x+1)].setText("λ = "+str(self.admin.eigenvectorsresult[x][0]))

            for x in range(len(self.admin.eigenvectorsresult),10):
                self.eigenvalueLabel_dict["eigenvalueLabel_"+str(x+1)].setHidden(True)

            for x in range(0,len(self.admin.eigenvectorsresult)):
                self.eigenvaluemultiplicityLabel_dict["eigenvaluemultiplicityLabel_"+str(x+1)].setHidden(False)

            for x in range(0,len(self.admin.eigenvectorsresult)):
                self.eigenvaluemultiplicityLabel_dict["eigenvaluemultiplicityLabel_"+str(x+1)].setText("Algebraic multiplicity: "+str(self.converttofraction(self.formatNumber(self.converttofloat(self.admin.eigenvectorsresult[x][1])))))

            for x in range(len(self.admin.eigenvectorsresult),10):
                self.eigenvaluemultiplicityLabel_dict["eigenvaluemultiplicityLabel_"+str(x+1)].setHidden(True)

            for x in range(0,len(self.admin.eigenvectorsresult)):
                self.eigenvectorsLabel_dict["eigenvectorsLabel_"+str(x+1)].setHidden(False)

            for x in range(0,len(self.admin.eigenvectorsresult)):
                self.eigenvectorsLabel_dict["eigenvectorsLabel_"+str(x+1)].setText(str(self.admin.eigenvectorsresult[x][2]))

            for x in range(len(self.admin.eigenvectorsresult),10):
                self.eigenvectorsLabel_dict["eigenvectorsLabel_"+str(x+1)].setHidden(True)

    def SystemofequationschoosematrixListWidgetitemchanged(self):
        chosenmatrixtoshow = self.systemofequationschoosematrixListWidget.currentItem().text()
        self.admin.geteigenchosenmatrix(chosenmatrixtoshow)
        self.emptystring=""

        for j in range(0, 10):
            for k in range(0,10):
                self.systemmatrixchosen_matrixlabelcelldict["systemmatrixchosen_matrixlabelcell"+str(j+1)+"_"+str(k+1)].setText("")

        for j in range(0, (self.admin.eigenchosenmatrixobject.row)):
            for k in range(0,(self.admin.eigenchosenmatrixobject.column)):
                self.systemmatrixchosen_matrixlabelcelldict["systemmatrixchosen_matrixlabelcell"+str(j+1)+"_"+str(k+1)].setText(str(self.converttofraction(self.formatNumber(self.converttofloat(self.admin.eigenchosenmatrixobject.values[j][k])))))

        for x in range(0,10):
            for y in range(0,10):
                self.systemmatrixchosen_matrixlabelcelldict["systemmatrixchosen_matrixlabelcell"+str(x+1)+"_"+str(y+1)].setHidden(True)

        for x in range(0, (self.admin.eigenchosenmatrixobject.row)):
            for y in range(0, (self.admin.eigenchosenmatrixobject.column)):
                self.systemmatrixchosen_matrixlabelcelldict["systemmatrixchosen_matrixlabelcell"+str(x+1)+"_"+str(y+1)].setHidden(False)

        self.systemofequationschoosematrixparentesisopenlabel.setHidden(False)
        self.systemofequationschoosematrixparentesisclosedlabel.setHidden(False)

    def SystemofequationschoosevectorListWidgetitemchanged(self):
        chosenmatrixtoshow = self.systemofequationschoosevectorListWidget.currentItem().text()
        self.admin.geteigenchosenmatrix(chosenmatrixtoshow)
        self.emptystring=""

        for k in range(0,10):
            self.systemvectorchosen_vectorlabelcell_dict["systemvectorchosen_vectorlabelcell"+str(k+1)+"_1"].setText("")

        for j in range(0, (self.admin.eigenchosenmatrixobject.row)):
            for k in range(0,(self.admin.eigenchosenmatrixobject.column)):
                self.systemvectorchosen_vectorlabelcell_dict["systemvectorchosen_vectorlabelcell"+str(k+1)+"_1"].setText(str(self.converttofraction(self.formatNumber(self.converttofloat(self.admin.eigenchosenmatrixobject.values[j][k])))))

        for x in range(0,10):
            self.systemvectorchosen_vectorlabelcell_dict["systemvectorchosen_vectorlabelcell"+str(x+1)+"_1"].setHidden(True)

        for x in range(0, (self.admin.eigenchosenmatrixobject.column)):
            self.systemvectorchosen_vectorlabelcell_dict["systemvectorchosen_vectorlabelcell"+str(x+1)+"_1"].setHidden(False)

        self.systemofequationschoosevectorparentesisopenlabel.setHidden(False)
        self.systemofequationschoosevectorparentesisclosedlabel.setHidden(False)

    def Systemofequationscalculatepushbuttonclicked(self):
        try:
            systemchosenmatrix,systemchosenvector = self.systemofequationschoosematrixListWidget.currentItem().text(),self.systemofequationschoosevectorListWidget.currentItem().text()
        except:
            self.admin.window.errorwindow.show()
            self.admin.window.errorwindow.ui.Errorwindowbodylabel.setText("Select a matrix and a vector.")
            return
        self.admin.getsystemofequationsresult(systemchosenmatrix,systemchosenvector)
        self.systemofequationsresultscrollArearesultLabel.setText(self.admin.systemsofequationsresult)

    def Infobuttonclicked(self):
        self.admin.window.infowindow.show()
    def Setstylesheetspoststart(self):
        self.systemofequationschoosematrixListWidget.setStyleSheet(mvssps.systemofequationschoosematrixListWidget_stylesheet)
        self.systemofequationschoosevectorListWidget.setStyleSheet(mvssps.systemofequationschoosevectorListWidget_stylesheet)
        self.eigenvaluesresultscreen_scrollArea.setStyleSheet(mvssps.eigenvaluesresultscreen_scrollArea_stylesheet)
        self.systemofequationsresultscrollArea.setStyleSheet(mvssps.systemofequationsresultscrollArea_stylesheet)
        self.systemofequationschoosevectorScrollArea.setStyleSheet(mvssps.systemofequationschoosevectorScrollArea_stylesheet)
        self.systemofequationschoosematrixScrollArea.setStyleSheet(mvssps.systemofequationschoosematrixScrollArea_stylesheet)
        self.eigenvalueschoosematrixListWidget.setStyleSheet(mvssps.eigenvalueschoosematrixListWidget_stylesheet)
        self.eigenvalueschosenmatrixscreen_scrollArea.setStyleSheet(mvssps.eigenvalueschosenmatrixscreen_scrollArea_stylesheet)
        self.screen_scrollArea.setStyleSheet(mvssps.screen_scrollArea_stylesheet)
        self.draggablematrixListWidget.setStyleSheet(mvssps.draggablematrixListWidget_stylesheet)
        self.anglesscreen_scrollArea.setStyleSheet(mvssps.anglesscreen_scrollArea_stylesheet)
        self.draggablevectorListWidget.setStyleSheet(mvssps.draggablevectorListWidget_stylesheet)
        self.eqstringtextEdit.setStyleSheet(mvssps.eqstringtextEdit_stylesheet)
###########################
#### CLASES DE WIDGETS ####
###########################

class QTextEditdropenabled(QtWidgets.QTextEdit):
    def __init__(self,admin):
        self.admin = admin
        super(QTextEditdropenabled, self).__init__()
        self.setAcceptDrops(True)
        self.blinking_colors = itools.cycle([
            QtGui.QColor(50, 50, 50, 255),
            QtGui.QColor(100, 100, 100, 255),
            QtGui.QColor(150, 150, 150, 255),
            QtGui.QColor(180, 180, 180, 255),
            QtGui.QColor(200, 200, 200, 255),
            QtGui.QColor(236, 236, 236, 255),
            QtGui.QColor(236, 236, 236, 255),
            QtGui.QColor(236, 236, 236, 255),
            QtGui.QColor(236, 236, 236, 255),
            QtGui.QColor(236, 236, 236, 255),
            QtGui.QColor(236, 236, 236, 255),
            QtGui.QColor(236, 236, 236, 255),
            QtGui.QColor(236, 236, 236, 255),
            QtGui.QColor(236, 236, 236, 255),
            QtGui.QColor(236, 236, 236, 255),
            QtGui.QColor(236, 236, 236, 255),
            QtGui.QColor(236, 236, 236, 255),
            QtGui.QColor(236, 236, 236, 255),
            QtGui.QColor(200, 200, 200, 255),
            QtGui.QColor(180, 180, 180, 255),
            QtGui.QColor(150, 150, 150, 255),
            QtGui.QColor(100, 100, 100, 255),
            QtGui.QColor(50, 50, 50, 255),
            QtGui.QColor(15, 16, 15, 255)
        ])
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.change_color)
        self.timer.start(32)

    def dragEnterEvent(self, e):
        e.accept()

    def dragMoveEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        texttoadd=""
        if self.admin.window.ui.matrixButton.isChecked():
            texttoadd=str(self.admin.window.ui.draggablematrixListWidget.currentItem().text())
            self.admin.window.ui.eqstringtextEdit.insertPlainText(texttoadd)
        elif self.admin.window.ui.vectorsButton.isChecked():
            texttoadd=str(self.admin.window.ui.draggablevectorListWidget.currentItem().text())
            self.admin.window.ui.eqstringtextEdit.insertPlainText(texttoadd)
        else:
            return
        e.accept()

    def change_color(self):
        self._colorofcursor = next(self.blinking_colors)
        self.update()

    def paintEvent(self, event):
        QtWidgets.QTextEdit.paintEvent(self, event)
        if self.hasFocus():
            rect = self.cursorRect(self.textCursor())
            painter = QtGui.QPainter(self.viewport())
            painter.fillRect(rect, self._colorofcursor)


############################
#### CLASES DE VENTANAS ####
############################
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,admin):
        super(MainWindow, self).__init__()
        self.admin=admin
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self,self.admin)
        self.setWindowTitle("O.V.C.")
        self.assignvalueswindow = AssignWindow(self,self.admin)
        self.assignvalueswindow.setWindowTitle("Assign")
        self.assignvalueswindow.hide()
        global assignvaluewindowhidden
        assignvaluewindowhidden=True
        self.ui.eqstringtextEdit.installEventFilter(self)
        self.installEventFilter(self)

        def moveWindow(event):
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.Titlebarframe.mouseMoveEvent = moveWindow

        self.ui.Minimize_Button.clicked.connect(lambda: self.showMinimized())
        self.ui.Exit_Button.clicked.connect(lambda: self.close())

        self.errorwindow=ErrorWindow()
        self.infowindow=InfoWindow()


    def moveEvent(self, e):
        global Mainposx
        global Mainposy
        Mainposx=self.pos().x()
        Mainposy=self.pos().y()
        global assignvaluewindowhidden
        if not assignvaluewindowhidden:
            x = Mainposx - 330
            y = Mainposy
            self.assignvalueswindow.move(x,y)
        else:
            pass
        super(MainWindow, self).moveEvent(e)
    def closeEvent(self, event):
        self.assignvalueswindow.close()
        global assignvaluewindowhidden
        assignvaluewindowhidden=True
        self.assignvalueswindow.valueswindow.close()
        self.errorwindow.close()
        self.infowindow.close()
        event.accept()

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.WindowStateChange:
            if QtCore.Qt.WindowMinimized:
                self.assignvalueswindow.hide()
                global assignvaluewindowhidden
                assignvaluewindowhidden=True
            else:
                pass

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress and obj is self.ui.eqstringtextEdit:
            if event.key() == QtCore.Qt.Key_Return and self.ui.eqstringtextEdit.hasFocus():
                self.ui.Equalbuttonclicked()
                return True
            if event.key() == QtCore.Qt.Key_Enter and self.ui.eqstringtextEdit.hasFocus():
                self.ui.Equalbuttonclicked()
                return True
            if event.key() == QtCore.Qt.Key_1 and self.ui.eqstringtextEdit.hasFocus():
                self.ui.eqstringtextEdit.insertPlainText("1")
                return True
            if event.key() == QtCore.Qt.Key_2 and self.ui.eqstringtextEdit.hasFocus():
                self.ui.eqstringtextEdit.insertPlainText("2")
                return True
            if event.key() == QtCore.Qt.Key_3 and self.ui.eqstringtextEdit.hasFocus():
                self.ui.eqstringtextEdit.insertPlainText("3")
                return True
            if event.key() == QtCore.Qt.Key_4 and self.ui.eqstringtextEdit.hasFocus():
                self.ui.eqstringtextEdit.insertPlainText("4")
                return True
            if event.key() == QtCore.Qt.Key_5 and self.ui.eqstringtextEdit.hasFocus():
                self.ui.eqstringtextEdit.insertPlainText("5")
                return True
            if event.key() == QtCore.Qt.Key_6 and self.ui.eqstringtextEdit.hasFocus():
                self.ui.eqstringtextEdit.insertPlainText("6")
                return True
            if event.key() == QtCore.Qt.Key_7 and self.ui.eqstringtextEdit.hasFocus():
                self.ui.eqstringtextEdit.insertPlainText("7")
                return True
            if event.key() == QtCore.Qt.Key_8 and self.ui.eqstringtextEdit.hasFocus():
                self.ui.eqstringtextEdit.insertPlainText("8")
                return True
            if event.key() == QtCore.Qt.Key_9 and self.ui.eqstringtextEdit.hasFocus():
                self.ui.eqstringtextEdit.insertPlainText("9")
                return True
            if event.key() == QtCore.Qt.Key_0 and self.ui.eqstringtextEdit.hasFocus():
                self.ui.eqstringtextEdit.insertPlainText("0")
                return True
            if event.key() == QtCore.Qt.Key_Space and self.ui.eqstringtextEdit.hasFocus():
                self.ui.eqstringtextEdit.insertPlainText(" ")
                return True
            if event.key() == QtCore.Qt.Key_Backspace and self.ui.eqstringtextEdit.hasFocus():
                self.ui.eqstringtextEdit.textCursor().deletePreviousChar()
                return True
            if event.key() == QtCore.Qt.Key_Left and self.ui.eqstringtextEdit.hasFocus():
                self.ui.eqstringtextEdit.moveCursor(QtGui.QTextCursor.Left)
                return True
            if event.key() == QtCore.Qt.Key_Right and self.ui.eqstringtextEdit.hasFocus():
                self.ui.eqstringtextEdit.moveCursor(QtGui.QTextCursor.Right)
                return True
            if event.key() == QtCore.Qt.Key_M and self.ui.eqstringtextEdit.hasFocus():
                self.ui.eqstringtextEdit.insertPlainText("Matrix")
                return True
            if event.key() == QtCore.Qt.Key_V and self.ui.eqstringtextEdit.hasFocus():
                self.ui.eqstringtextEdit.insertPlainText("Vector")
                return True
            if event.key() == QtCore.Qt.Key_A and self.ui.eqstringtextEdit.hasFocus():
                self.ui.eqstringtextEdit.insertPlainText("Ans")
                return True
            if event.key() == QtCore.Qt.Key_ParenLeft and self.ui.eqstringtextEdit.hasFocus():
                self.ui.eqstringtextEdit.insertPlainText("(")
                return True
            if event.key() == QtCore.Qt.Key_ParenRight and self.ui.eqstringtextEdit.hasFocus():
                self.ui.eqstringtextEdit.insertPlainText(")")
                return True
            if event.key() == QtCore.Qt.Key_Period and self.ui.eqstringtextEdit.hasFocus():
                self.ui.eqstringtextEdit.insertPlainText(".")
                return True
            if event.key() == QtCore.Qt.Key_Comma and self.ui.eqstringtextEdit.hasFocus():
                self.ui.eqstringtextEdit.insertPlainText(".")
                return True

        if event.type() == QtCore.QEvent.WindowActivate:
            global assignvaluewindowhidden
            if assignvaluewindowhidden == False:
                self.assignvalueswindow.raise_()
            return True
        return super().eventFilter(obj, event)