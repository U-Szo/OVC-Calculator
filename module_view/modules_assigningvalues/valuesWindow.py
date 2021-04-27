from PySide2 import QtCore, QtGui, QtWidgets


class Ui_ValuesWindow(object):
    def setupUi(self, MainWindow,admin):
        self.admin=admin
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(412, 377)
        MainWindow.setWindowIcon((QtGui.QIcon("icons/Windowicon.png")))
        MainWindow.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowTitleHint)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setStyleSheet("background-color: rgb(27, 28, 27);\n"
            "border: 2px solid rgb(15,16,15);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.selectedvmlabel = QtWidgets.QLabel(self.centralwidget)
        self.selectedvmlabel.setGeometry(QtCore.QRect(2, 20, 251, 21))
        self.selectedvmlabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.46, y1:0, x2:1, y2:0, stop:0 rgba(85, 40, 107, 255), stop:1 rgba(27, 28, 27, 255));\n"
            "border: none;")
        self.selectedvmlabel.setText("")
        self.selectedvmlabel.setObjectName("selectedvmlabel")
        self.applyButton = QtWidgets.QPushButton(self.centralwidget)
        self.applyButton.setGeometry(QtCore.QRect(176, 350, 101, 21))
        self.applyButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(52, 53, 52);\n"
"    border:1px;\n"
"    border-style:outset;\n"
"    border-color:rgb(25, 26, 25);\n"
"    border-radius:5px\n;"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(62, 63, 62);\n"
"    border-color:rgb(35, 36, 35);\n"
"    border-radius:5px\n;"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(57, 58, 57);\n"
"    border-color:rgb(30, 31, 30);\n"
"    border-radius:5px\n;"
"}    ")
        self.applyButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/createwindowicons/Applyicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.applyButton.setIcon(icon)
        self.applyButton.setIconSize(QtCore.QSize(90, 40))
        self.applyButton.setObjectName("applyButton")
        self.applyButton.clicked.connect(self.applyassign)
        self.applyButton.setShortcut("Return")
        self.decorativelabeltoprow = QtWidgets.QLabel(self.centralwidget)
        self.decorativelabeltoprow.setGeometry(QtCore.QRect(0, 0, 411, 21))
        self.decorativelabeltoprow.setStyleSheet("background-color: rgb(52, 53, 52);\n"
"border:2px;\n"
"border-right:1px;\n"
"border-style:solid;\n"
"border-color:rgb(25,26,25);\n"
"")
        self.decorativelabeltoprow.setText("")
        self.decorativelabeltoprow.setObjectName("decorativelabeltoprow")
        self.rowslabel = QtWidgets.QLabel(self.centralwidget)
        self.rowslabel.setGeometry(QtCore.QRect(240, 0, 81, 21))
        self.rowslabel.setStyleSheet("background-color:transparent;\n"
"border: none;\n"
"")
        self.rowslabel.setText("")
        self.rowslabel.setPixmap(QtGui.QPixmap("icons/createwindowicons/Rowsicon.png"))
        self.rowslabel.setScaledContents(True)
        self.rowslabel.setObjectName("rowslabel")
        self.columnslabel = QtWidgets.QLabel(self.centralwidget)
        self.columnslabel.setGeometry(QtCore.QRect(320, 0, 81, 21))
        self.columnslabel.setStyleSheet("background-color:transparent;\n"
"border: none;\n"
"")
        self.columnslabel.setText("")
        self.columnslabel.setPixmap(QtGui.QPixmap("icons/createwindowicons/Columnsicon.png"))
        self.columnslabel.setScaledContents(True)
        self.columnslabel.setObjectName("columnslabel")
        self.selectedlabel = QtWidgets.QLabel(self.centralwidget)
        self.selectedlabel.setGeometry(QtCore.QRect(0, 0, 81, 21))
        self.selectedlabel.setStyleSheet("background-color:transparent;\n"
            "border: none;")
        self.selectedlabel.setText("")
        self.selectedlabel.setPixmap(QtGui.QPixmap("icons/createwindowicons/Selecticon.png"))
        self.selectedlabel.setScaledContents(True)
        self.selectedlabel.setObjectName("selectedlabel")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(300, 350, 101, 21))
        self.cancelButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(52, 53, 52);\n"
"    border:1px;\n"
"    border-style:outset;\n"
"    border-color:rgb(25, 26, 25);\n"
"    border-radius:5px\n;"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(232, 17, 35);\n"
"    border-color: rgb(155, 26, 25);\n"
"    border-radius:5px\n;"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(149, 20, 30);\n"
"    border-color: rgb(95, 26, 25);\n"
"    border-radius:5px\n;"
"}    ")
        self.cancelButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/createwindowicons/Cancelicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelButton.setIcon(icon1)
        self.cancelButton.setIconSize(QtCore.QSize(90, 40))
        self.cancelButton.setObjectName("cancelButton")
        self.cancelButton.clicked.connect(self.cancelassign)

        self.rowscomboBoxframe = QtWidgets.QFrame(self.centralwidget)
        self.rowscomboBoxframe.setGeometry(QtCore.QRect(260, 20, 41, 22))
        self.rowscomboBoxframe.setStyleSheet("QFrame{\n"
"   background-color: rgb(25, 26, 25);\n"
"   color: rgb(236, 236, 236);\n"
"   selection-color: rgb(236, 236, 236);\n"
"   selection-background-color: rgb(52, 53, 52);\n"
"   outline: none;\n"
"   border:none"
"}\n"
"")

        self.rowscomboBox = QtWidgets.QComboBox(self.rowscomboBoxframe)
        self.rowscomboBox.setEnabled(True)
        self.rowscomboBox.setGeometry(QtCore.QRect(0, 0, 41, 22))
        font = QtGui.QFont()
        font.setFamily("Alice")
        font.setPointSize(12)
        self.rowscomboBox.setFont(font)
        self.rowscomboBox.setStyleSheet("background-color: rgb(27, 28, 27);\n"
"color: rgb(236, 236, 236);\n"
"selection-color: rgb(236, 236, 236);\n"
"border: none;\n"
"selection-background-color: rgb(52, 53, 52);\n"
"\n"
"")
        self.rowscomboBox.setObjectName("rowscomboBox")
        for x in range (0,10):
            self.rowscomboBox.addItem("")
        self.rowscomboBox.activated.connect(self.hideandshowrows)

        self.columnscomboBoxframe = QtWidgets.QFrame(self.centralwidget)
        self.columnscomboBoxframe.setGeometry(QtCore.QRect(340, 20, 41, 22))
        self.columnscomboBoxframe.setStyleSheet("QFrame{\n"
"   background-color: rgb(25, 26, 25);\n"
"   color: rgb(236, 236, 236);\n"
"   selection-color: rgb(236, 236, 236);\n"
"   selection-background-color: rgb(52, 53, 52);\n"
"   outline: none;\n"
"   border:none"
"}\n"
"")

        self.columnscomboBox = QtWidgets.QComboBox(self.columnscomboBoxframe)
        self.columnscomboBox.setGeometry(QtCore.QRect(0, 0, 41, 22))
        font = QtGui.QFont()
        font.setFamily("Alice")
        font.setPointSize(12)
        self.columnscomboBox.setFont(font)
        self.columnscomboBox.setStyleSheet("background-color: rgb(27, 28, 27);\n"
"color: rgb(236, 236, 236);\n"
"selection-color: rgb(236, 236, 236);\n"
"border: none;\n"
"selection-background-color: rgb(52, 53, 52);\n"
"\n"
"")
        self.columnscomboBox.setObjectName("columnscomboBox")
        for x in range (0,10):
            self.columnscomboBox.addItem("")
        self.columnscomboBox.activated.connect(self.hideandshowcolumns)

        self.decorativelabeltoprow_2 = QtWidgets.QLabel(self.centralwidget)
        self.decorativelabeltoprow_2.setGeometry(QtCore.QRect(250, 0, 61, 21))
        self.decorativelabeltoprow_2.setStyleSheet("background-color: transparent;\n"
"border-left:2px;\n"
"border-right:2px;\n"
"border-style:solid;\n"
"border-color:rgb(25,26,25);")
        self.decorativelabeltoprow_2.setText("")
        self.decorativelabeltoprow_2.setObjectName("decorativelabeltoprow_2")
        self.selectediconlabel = QtWidgets.QLabel(self.centralwidget)
        self.selectediconlabel.setGeometry(QtCore.QRect(10, 20, 21, 21))
        self.selectediconlabel.setStyleSheet("background-color: transparent;\n"
            "border: none;")
        self.selectediconlabel.setText("")
        self.selectediconlabel.setPixmap(QtGui.QPixmap("icons/individualvectoricon/vector1icon.png"))
        self.selectediconlabel.setScaledContents(True)
        self.selectediconlabel.setObjectName("selectediconlabel")

        ###############################
        ##REGULAR EXPRESION FOR CELLS##
        ###############################

        self.reg_ex_cell = QtCore.QRegExp("(^-?[0-9]+/0*[1-9][0-9]*$|^[-+]?[0-9]+$|^[-+]?[0-9]+\.[0-9]+$)")

        #########
        ##CELLS##
        #########
        celllineeditypos=-30
        celllineeditxpos=20
        self.cellslineedit_dict,self.cellsvalidators={},{}
        for x in range(1,11):
            celllineeditxpos=+30
            for y in range(1,11):
                celllineeditypos+=40
                self.cellslineedit_dict["cell"+str(x)+"_"+str(y)] = QtWidgets.QLineEdit(self.centralwidget)
                self.cellslineedit_dict["cell"+str(x)+"_"+str(y)].setGeometry(QtCore.QRect(celllineeditypos, celllineeditxpos, 31, 21))
                font = QtGui.QFont()
                font.setFamily("Alice")
                font.setPointSize(12)
                self.cellslineedit_dict["cell"+str(x)+"_"+str(y)].setFont(font)
                self.cellslineedit_dict["cell"+str(x)+"_"+str(y)].setStyleSheet("color: rgb(236, 236, 236);"
        "border:1px;"
        "border-style:solid;"
        "border-color: rgb(15, 16, 15);"
        "background-color: rgb(42, 43, 42);"
        "")
                self.cellslineedit_dict["cell"+str(x)+"_"+str(y)].setAlignment(QtCore.Qt.AlignCenter)
                self.cellsvalidators["cell"+str(x)+"_"+str(y)+"_validator"] = QtGui.QRegExpValidator(self.reg_ex_cell, self.cellslineedit_dict["cell"+str(x)+"_"+str(y)])
                self.cellslineedit_dict["cell"+str(x)+"_"+str(y)].setValidator(self.cellsvalidators["cell"+str(x)+"_"+str(y)+"_validator"])
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def hideandshowrows(self):
        y = int(self.rowscomboBox.currentText())
        z = int(self.columnscomboBox.currentText())
        for x in range(0, 10):
            if x <= (y-1):
                for w in range (0,z):
                    self.cellslineedit_dict["cell"+str(x+1)+"_"+str(w+1)].setHidden(False)
                for o in range (z,10):
                    self.cellslineedit_dict["cell"+str(x+1)+"_"+str(o+1)].setHidden(True)
            else:
                for w in range(0,10):
                    self.cellslineedit_dict["cell"+str(x+1)+"_"+str(w+1)].setHidden(True)


        rowwinresize = 377-(30*(10-y))
        self.admin.valueswindow.resize(412, rowwinresize)
        rowbuttonsrepos=350-(30*(10-y))
        self.applyButton.setGeometry(QtCore.QRect(176, rowbuttonsrepos, 101, 21))
        self.cancelButton.setGeometry(QtCore.QRect(300, rowbuttonsrepos, 101, 21))

    def hideandshowcolumns(self):
        z = int(self.rowscomboBox.currentText())
        y = int(self.columnscomboBox.currentText())
        for x in range(0, 10):
            if x <= (y-1):
                for w in range (0,z):
                    self.cellslineedit_dict["cell"+str(w+1)+"_"+str(x+1)].setHidden(False)
                for o in range (z,10):
                    self.cellslineedit_dict["cell"+str(o+1)+"_"+str(x+1)].setHidden(True)
            else:
                for w in range(0,10):
                    self.cellslineedit_dict["cell"+str(w+1)+"_"+str(x+1)].setHidden(True)

        for j in range(0, 10):
            for k in range(0, 10):
                f=10 + (40 * j) + (18*(10-y))
                h=50 + (30 * k)
                self.cellslineedit_dict["cell"+str(k+1)+"_"+str(j+1)].setGeometry(QtCore.QRect(f,h,31,21))

    def cancelassign(self):
        self.admin.valueswindow.hide()
        self.admin.ui.typeofassigntomake = 0

    def applyassign(self):
        if self.admin.ui.typeofassigntomake == "vector":
            getSelected = self.admin.ui.vectortreeWidget.selectedItems()
            selected_vector_item = self.admin.ui.vectortreeWidget.indexOfTopLevelItem(getSelected[0])
            selected_vector_item_rows = int(self.rowscomboBox.currentText())
            selected_vector_item_columns = int(self.columnscomboBox.currentText())

            self.newvector = []

            for x in range(0,selected_vector_item_rows):
                listofrows=[]
                for y in range(0,selected_vector_item_columns):
                    cellvalue = self.cellslineedit_dict["cell"+str(x+1)+"_"+str(y+1)].text()

                    if cellvalue == "":
                        self.admin.admin.admin.window.errorwindow.show()
                        self.admin.admin.admin.window.errorwindow.ui.Errorwindowbodylabel.setText("All cells must be filled")
                        return
                    elif cellvalue == "-":
                        self.admin.admin.admin.window.errorwindow.show()
                        self.admin.admin.admin.window.errorwindow.ui.Errorwindowbodylabel.setText("Invalid cell value: \"-\" ")
                        return
                    else:
                        pass

                    listofrows.append(cellvalue)
                self.newvector.append(listofrows)
            self.admin.admin.admin.modifyvectors(selected_vector_item,selected_vector_item_rows,selected_vector_item_columns,self.newvector)
            self.admin.admin.ui.fillvectorstreeview()

        elif self.admin.ui.typeofassigntomake == "matrix":
            getSelected = self.admin.ui.matrixtreeWidget.selectedItems()
            selected_matrix_item = self.admin.ui.matrixtreeWidget.indexOfTopLevelItem(getSelected[0])
            selected_matrix_item_rows = int(self.rowscomboBox.currentText())
            selected_matrix_item_columns = int(self.columnscomboBox.currentText())

            self.newmatrix = []

            for x in range(0,selected_matrix_item_rows):
                listofrows=[]
                for y in range(0,selected_matrix_item_columns):
                    cellvalue = self.cellslineedit_dict["cell"+str(x+1)+"_"+str(y+1)].text()

                    if cellvalue == "":
                        self.admin.admin.admin.window.errorwindow.show()
                        self.admin.admin.admin.window.errorwindow.ui.Errorwindowbodylabel.setText("All cells must be filled")
                        return
                    elif cellvalue == "-":
                        self.admin.admin.admin.window.errorwindow.show()
                        self.admin.admin.admin.window.errorwindow.ui.Errorwindowbodylabel.setText("Invalid cell value: \"-\" ")
                        return
                    else:
                        pass

                    listofrows.append(cellvalue)
                self.newmatrix.append(listofrows)
            self.admin.admin.admin.modifymatrices(selected_matrix_item,selected_matrix_item_rows,selected_matrix_item_columns,self.newmatrix)
            self.admin.admin.ui.fillmatricestreeview()
        else:
            return
        self.admin.valueswindow.hide()
        self.admin.ui.typeofassigntomake = 0
        self.admin.admin.ui.Anglesvectorxcomboboxvaluechanged()
        self.admin.admin.ui.Anglesvectorycomboboxvaluechanged()
        try:
            self.admin.admin.ui.Eigenvalueschoosematrixlistwidgetitemchanged()
        except:
            pass
        try:
            self.admin.admin.ui.SystemofequationschoosevectorListWidgetitemchanged()
        except:
            pass
        try:
            self.admin.admin.ui.SystemofequationschoosematrixListWidgetitemchanged()
        except:
            pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.rowscomboBox.setItemText(0, _translate("MainWindow", "1"))
        self.rowscomboBox.setItemText(1, _translate("MainWindow", "2"))
        self.rowscomboBox.setItemText(2, _translate("MainWindow", "3"))
        self.rowscomboBox.setItemText(3, _translate("MainWindow", "4"))
        self.rowscomboBox.setItemText(4, _translate("MainWindow", "5"))
        self.rowscomboBox.setItemText(5, _translate("MainWindow", "6"))
        self.rowscomboBox.setItemText(6, _translate("MainWindow", "7"))
        self.rowscomboBox.setItemText(7, _translate("MainWindow", "8"))
        self.rowscomboBox.setItemText(8, _translate("MainWindow", "9"))
        self.rowscomboBox.setItemText(9, _translate("MainWindow", "10"))
        self.columnscomboBox.setItemText(0, _translate("MainWindow", "1"))
        self.columnscomboBox.setItemText(1, _translate("MainWindow", "2"))
        self.columnscomboBox.setItemText(2, _translate("MainWindow", "3"))
        self.columnscomboBox.setItemText(3, _translate("MainWindow", "4"))
        self.columnscomboBox.setItemText(4, _translate("MainWindow", "5"))
        self.columnscomboBox.setItemText(5, _translate("MainWindow", "6"))
        self.columnscomboBox.setItemText(6, _translate("MainWindow", "7"))
        self.columnscomboBox.setItemText(7, _translate("MainWindow", "8"))
        self.columnscomboBox.setItemText(8, _translate("MainWindow", "9"))
        self.columnscomboBox.setItemText(9, _translate("MainWindow", "10"))


############################
#### CLASES DE VENTANAS ####
############################


class ValuesWindow(QtWidgets.QMainWindow):
    def __init__(self,admin,parent=None):
        super(ValuesWindow, self).__init__()
        self.ui = Ui_ValuesWindow()
        self.admin=admin
        self.ui.setupUi(self,self.admin)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

        def moveWindow(event):
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.rowslabel.mouseMoveEvent = moveWindow
        self.ui.columnslabel.mouseMoveEvent = moveWindow
        self.ui.selectedlabel.mouseMoveEvent = moveWindow
        self.ui.decorativelabeltoprow.mouseMoveEvent = moveWindow
        self.ui.decorativelabeltoprow_2.mouseMoveEvent = moveWindow
        self.ui.selectedvmlabel.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
