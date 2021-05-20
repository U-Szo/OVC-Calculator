from PySide2 import QtCore, QtGui, QtWidgets
from module_view.modules_assigningvalues.ValuesWindow import *
import module_view.Mainview as mainv
import itertools as itools
######################
##STYLESHEETS IMPORT##
######################
import module_view.modules_assigningvalues.assigningvalues_stylesheets.AssignWindowStylesheet as awss

class Ui_AssignWindow(object):
    def setupUi(self, MainWindow,admin):
        self.admin=admin
        MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.resize(330, 588)
        MainWindow.setStyleSheet("background-color: transparent;")
        MainWindow.setWindowIcon((QtGui.QIcon("icons/Windowicon.png")))
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.tab_widget = QtWidgets.QTabWidget(self.central_widget)
        self.tab_widget.setGeometry(QtCore.QRect(0, 0, 330, 589))
        font = QtGui.QFont()
        font.setFamily("Alice")
        font.setPointSize(11)
        self.tab_widget.setFont(font)
        self.tab_widget.setAutoFillBackground(False)
        self.tab_widget.setStyleSheet(awss.tab_widget_stylesheet)
        self.tab_widget.setIconSize(QtCore.QSize(60, 30))
        self.vectors = QtWidgets.QWidget()
        self.modify_selected_vector_button = QtWidgets.QPushButton(self.vectors)
        self.modify_selected_vector_button.setGeometry(QtCore.QRect(0, 511, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Alice")
        font.setPointSize(11)
        self.modify_selected_vector_button.setFont(font)
        self.modify_selected_vector_button.setStyleSheet(awss.modify_selected_vector_button_stylesheet)
        self.modify_selected_vector_button.setText("")
        modify_selected_vector_button_icon = QtGui.QIcon()
        modify_selected_vector_button_icon.addPixmap(QtGui.QPixmap("icons/Modifyselectedbuttontabicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.modify_selected_vector_button.setIcon(modify_selected_vector_button_icon)
        self.modify_selected_vector_button.setIconSize(QtCore.QSize(180, 40))
        self.modify_selected_vector_button.clicked.connect(self.showValuesWindowVector)
        self.modify_selected_vector_button.setShortcut("F2")
        self.vector_tree_widget = QtWidgets.QTreeWidget(self.vectors)
        self.vector_tree_widget.setGeometry(QtCore.QRect(0, 30, 331, 481))
        font = QtGui.QFont()
        font.setFamily("Alice")
        font.setPointSize(11)
        self.vector_tree_widget.setFont(font)
        self.vector_tree_widget.setStyleSheet(awss.vector_tree_widget_stylesheet)
        self.vector_tree_widget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.vector_tree_widget.setIconSize(QtCore.QSize(30, 30))
        self.vector_tree_widget.setRootIsDecorated(False)
        self.vector_tree_widget.setItemsExpandable(True)
        self.vector_tree_widget.setAllColumnsShowFocus(False)
        self.vector_tree_widget.setHeaderHidden(False)
        self.vector_tree_widget.setExpandsOnDoubleClick(False)
        self.vector_tree_widget.headerItem().setBackground(0, QtGui.QColor(236, 236, 236))
        self.vector_tree_widget.header().setDefaultSectionSize(60)
        self.vector_tree_widget.header().setStretchLastSection(False)
        self.vector_tree_widget.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.vector_tree_widget.itemDoubleClicked.connect(self.showValuesWindowVector)
        self.number_of_vector_label = QtWidgets.QLabel(self.vectors)
        self.number_of_vector_label.setGeometry(QtCore.QRect(0, 0, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Alice")
        font.setPointSize(12)
        self.number_of_vector_label.setFont(font)
        self.number_of_vector_label.setStyleSheet(awss.number_of_vector_label_stylesheet)
        self.number_of_vector_label.setText("")
        self.number_of_vector_label.setPixmap(QtGui.QPixmap("icons/Selectamounttoassigntabicon.png"))
        self.number_of_vector_label.setScaledContents(False)
        self.number_of_vectors_combobox_frame = QtWidgets.QFrame(self.vectors)
        self.number_of_vectors_combobox_frame.setGeometry(QtCore.QRect(290, 0, 41, 31))
        self.number_of_vectors_combobox_frame.setStyleSheet(awss.number_of_vectors_combobox_frame_stylesheet)
        self.number_of_vectors_combobox = QtWidgets.QComboBox(self.number_of_vectors_combobox_frame)
        self.number_of_vectors_combobox.setGeometry(QtCore.QRect(0, 0, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Alice")
        font.setPointSize(12)
        self.number_of_vectors_combobox.setFont(font)
        self.number_of_vectors_combobox.setStyleSheet(awss.number_of_vectors_combobox_stylesheet)
        for x in range(0,20):
            self.number_of_vectors_combobox.addItem("")

        self.number_of_vectors_combobox.activated.connect(self.hideAndShowVectorItems)
        selected_vector_icon = QtGui.QIcon()
        selected_vector_icon.addPixmap(QtGui.QPixmap("icons/Vectorsassigntabicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_widget.addTab(self.vectors, selected_vector_icon, "")

        ########################
        ##VECTORES COMO ITEMS###
        ########################

        self.vectors_parentesis_dict,self.vectors_frame_dict,self.vectors_item_dict,self.vectors_icon_dict={},{},{},{}
        self.vectors_label_dict,self.vectors_grid_dict={},{}
        for x in range(1,21):
            self.vectors_parentesis_dict["vector"+str(x)+"parentesisopenlabel"] = QtWidgets.QLabel()
            self.vectors_parentesis_dict["vector"+str(x)+"parentesisopenlabel"].setPixmap(QtGui.QPixmap("icons/Itemparentesisopen.png"))
            self.vectors_parentesis_dict["vector"+str(x)+"parentesisopenlabel"].setScaledContents(True)
            self.vectors_parentesis_dict["vector"+str(x)+"parentesisopenlabel"].setFixedWidth(5)
            self.vectors_parentesis_dict["vector"+str(x)+"parentesisclosedlabel"] = QtWidgets.QLabel()
            self.vectors_parentesis_dict["vector"+str(x)+"parentesisclosedlabel"].setPixmap(QtGui.QPixmap("icons/Itemparentesisclose.png"))
            self.vectors_parentesis_dict["vector"+str(x)+"parentesisclosedlabel"].setScaledContents(True)
            self.vectors_parentesis_dict["vector"+str(x)+"parentesisclosedlabel"].setFixedWidth(5)
            self.vectors_frame_dict["vector"+str(x)+"frame"] = QtWidgets.QFrame()
            self.vectors_item_dict["vector"+str(x)+"item"] = QtWidgets.QTreeWidgetItem(self.vector_tree_widget)
            font = QtGui.QFont()
            font.setFamily("Alice")
            font.setPointSize(12)
            self.vectors_item_dict["vector"+str(x)+"item"].setFont(0, font)
            self.vectors_icon_dict["vector"+str(x)+"item"] = QtGui.QIcon()
            self.vectors_icon_dict["vector"+str(x)+"item"].addPixmap(QtGui.QPixmap("icons/individualvectoricon/vector"+str(x)+"icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.vectors_icon_dict["vector"+str(x)+"item"].addPixmap(QtGui.QPixmap("icons/individualvectoricon/vector"+str(x)+"icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
            self.vectors_icon_dict["vector"+str(x)+"item"].addPixmap(QtGui.QPixmap("icons/individualvectoricon/vector"+str(x)+"icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
            self.vectors_item_dict["vector"+str(x)+"item"].setIcon(0, self.vectors_icon_dict["vector"+str(x)+"item"])
            self.vectors_label_dict["vector"+str(x)+"label"] = QtWidgets.QLabel()
            self.vectors_label_dict["vector"+str(x)+"label"].setStyleSheet("background-color: transparent;\n""color: rgb(236, 236, 236);\n")
            self.vectors_label_dict["vector"+str(x)+"label"].setFont(font)
            self.vectors_grid_dict["vector"+str(x)+"grid"] = QtWidgets.QHBoxLayout(self.vectors_frame_dict["vector"+str(x)+"frame"])
            self.vectors_grid_dict["vector"+str(x)+"grid"].setSpacing(0)
            self.vectors_grid_dict["vector"+str(x)+"grid"].addWidget(self.vectors_parentesis_dict["vector"+str(x)+"parentesisopenlabel"], 0, alignment=QtCore.Qt.AlignLeft)
            self.vectors_grid_dict["vector"+str(x)+"grid"].addWidget(self.vectors_label_dict["vector"+str(x)+"label"], 1, alignment=QtCore.Qt.AlignCenter)
            self.vectors_grid_dict["vector"+str(x)+"grid"].addWidget(self.vectors_parentesis_dict["vector"+str(x)+"parentesisclosedlabel"], 2, alignment=QtCore.Qt.AlignLeft)
            self.vector_tree_widget.setItemWidget(self.vectors_item_dict["vector"+str(x)+"item"], 1, self.vectors_frame_dict["vector"+str(x)+"frame"])

        ####################
        ##HIDE VECTORITEMS##
        ####################
        for x in range(1,20):
            self.vectors_item_dict["vector"+str(x+1)+"item"].setHidden(True)

        self.matrices = QtWidgets.QWidget()
        self.modify_selected_matrix_button = QtWidgets.QPushButton(self.matrices)
        self.modify_selected_matrix_button.setGeometry(QtCore.QRect(0, 511, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Alice")
        font.setPointSize(11)
        self.modify_selected_matrix_button.setFont(font)
        self.modify_selected_matrix_button.setStyleSheet(awss.modify_selected_matrix_button_stylesheet)
        self.modify_selected_matrix_button.setText("")
        self.modify_selected_matrix_button.setIcon(modify_selected_vector_button_icon)
        self.modify_selected_matrix_button.setIconSize(QtCore.QSize(180, 40))
        self.modify_selected_matrix_button.clicked.connect(self.showValuesWindowMatrix)
        self.modify_selected_matrix_button.setShortcut("F2")
        self.matrix_tree_widget = QtWidgets.QTreeWidget(self.matrices)
        self.matrix_tree_widget.setGeometry(QtCore.QRect(0, 30, 331, 481))
        font = QtGui.QFont()
        font.setFamily("Alice")
        font.setPointSize(11)
        self.matrix_tree_widget.setFont(font)
        self.matrix_tree_widget.setStyleSheet(awss.matrix_tree_widget_stylesheet)
        self.matrix_tree_widget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.matrix_tree_widget.setIconSize(QtCore.QSize(30, 30))
        self.matrix_tree_widget.setRootIsDecorated(False)
        self.matrix_tree_widget.setItemsExpandable(True)
        self.matrix_tree_widget.setAllColumnsShowFocus(False)
        self.matrix_tree_widget.setHeaderHidden(False)
        self.matrix_tree_widget.setExpandsOnDoubleClick(False)
        self.matrix_tree_widget.headerItem().setBackground(0, QtGui.QColor(236, 236, 236))
        self.matrix_tree_widget.header().setStretchLastSection(False)
        self.matrix_tree_widget.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.matrix_tree_widget.itemDoubleClicked.connect(self.showValuesWindowMatrix)
        self.number_of_matrix_label = QtWidgets.QLabel(self.matrices)
        self.number_of_matrix_label.setGeometry(QtCore.QRect(0, 0, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Alice")
        font.setPointSize(12)
        self.number_of_matrix_label.setFont(font)
        self.number_of_matrix_label.setStyleSheet(awss.number_of_matrix_label_stylesheet)
        self.number_of_matrix_label.setText("")
        self.number_of_matrix_label.setPixmap(QtGui.QPixmap("icons/Selectamounttoassigntabicon.png"))
        self.number_of_matrix_label.setScaledContents(False)
        self.number_of_matrix_combobox_frame = QtWidgets.QFrame(self.matrices)
        self.number_of_matrix_combobox_frame.setGeometry(QtCore.QRect(290, 0, 41, 31))
        self.number_of_matrix_combobox_frame.setStyleSheet(awss.number_of_matrix_combobox_frame_stylesheet)
        self.number_of_matrix_combobox = QtWidgets.QComboBox(self.number_of_matrix_combobox_frame)
        self.number_of_matrix_combobox.setGeometry(QtCore.QRect(0, 0, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Alice")
        font.setPointSize(12)
        self.number_of_matrix_combobox.setFont(font)
        self.number_of_matrix_combobox.setStyleSheet(awss.number_of_matrix_combobox_stylesheet)
        for x in range(0,20):
            self.number_of_matrix_combobox.addItem("")

        self.number_of_matrix_combobox.activated.connect(self.hideAndShowMatrixItems)
        selected_matrix_icon = QtGui.QIcon()
        selected_matrix_icon.addPixmap(QtGui.QPixmap("icons/Matrixassigntabicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_widget.addTab(self.matrices, selected_matrix_icon, "")

        #######################
        ##mATRICES COMO ITEMS##
        #######################

        self.matrices_parentesis_dict,self.matrices_frame_dict,self.matrices_item_dict,self.matrices_icon_dict={},{},{},{}
        self.matrices_values_grid_widget_dict,self.matrices_values_grid_dict,self.matrices_grid_dict={},{},{}
        for x in range(1,21):
            self.matrices_parentesis_dict["matrix"+str(x)+"parentesisopenlabel"] = QtWidgets.QLabel()
            self.matrices_parentesis_dict["matrix"+str(x)+"parentesisopenlabel"].setPixmap(QtGui.QPixmap("icons/Itemparentesisopen.png"))
            self.matrices_parentesis_dict["matrix"+str(x)+"parentesisopenlabel"].setScaledContents(True)
            self.matrices_parentesis_dict["matrix"+str(x)+"parentesisopenlabel"].setFixedWidth(5)
            self.matrices_parentesis_dict["matrix"+str(x)+"parentesisclosedlabel"] = QtWidgets.QLabel()
            self.matrices_parentesis_dict["matrix"+str(x)+"parentesisclosedlabel"].setPixmap(QtGui.QPixmap("icons/Itemparentesisclose.png"))
            self.matrices_parentesis_dict["matrix"+str(x)+"parentesisclosedlabel"].setScaledContents(True)
            self.matrices_parentesis_dict["matrix"+str(x)+"parentesisclosedlabel"].setFixedWidth(5)
            self.matrices_frame_dict["matrix"+str(x)+"frame"] = QtWidgets.QFrame()
            self.matrices_item_dict["matrix"+str(x)+"item"] = QtWidgets.QTreeWidgetItem(self.matrix_tree_widget)
            font = QtGui.QFont()
            font.setFamily("Alice")
            font.setPointSize(12)
            self.matrices_item_dict["matrix"+str(x)+"item"].setFont(0, font)
            self.matrices_icon_dict["matrix"+str(x)+"item"] = QtGui.QIcon()
            self.matrices_icon_dict["matrix"+str(x)+"item"].addPixmap(QtGui.QPixmap("icons/individualmatrixicon/matrix"+str(x)+"icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.matrices_icon_dict["matrix"+str(x)+"item"].addPixmap(QtGui.QPixmap("icons/individualmatrixicon/matrix"+str(x)+"icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
            self.matrices_icon_dict["matrix"+str(x)+"item"].addPixmap(QtGui.QPixmap("icons/individualmatrixicon/matrix"+str(x)+"icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
            self.matrices_item_dict["matrix"+str(x)+"item"].setIcon(0, self.matrices_icon_dict["matrix"+str(x)+"item"])
            self.matrices_values_grid_widget_dict["matrix"+str(x)+"valuesgridWidget"] = QtWidgets.QWidget()
            self.matrices_values_grid_dict["matrix"+str(x)+"valuesgrid"] = QtWidgets.QGridLayout(self.matrices_values_grid_widget_dict["matrix"+str(x)+"valuesgridWidget"])
            self.matrices_values_grid_dict["matrix"+str(x)+"valuesgrid"].setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
            self.matrices_values_grid_dict["matrix"+str(x)+"valuesgrid"].setContentsMargins(0, 0, 0, 0)
            self.matrices_grid_dict["matrix"+str(x)+"grid"] = QtWidgets.QHBoxLayout(self.matrices_frame_dict["matrix"+str(x)+"frame"])
            self.matrices_grid_dict["matrix"+str(x)+"grid"].setSpacing(0)
            self.matrices_grid_dict["matrix"+str(x)+"grid"].setGeometry(QtCore.QRect(0, 0, 16, 16))
            self.matrices_grid_dict["matrix"+str(x)+"grid"].setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
            self.matrices_grid_dict["matrix"+str(x)+"grid"].addWidget(self.matrices_parentesis_dict["matrix"+str(x)+"parentesisopenlabel"], 0, alignment=QtCore.Qt.AlignLeft)
            self.matrices_grid_dict["matrix"+str(x)+"grid"].addWidget(self.matrices_values_grid_widget_dict["matrix"+str(x)+"valuesgridWidget"], 1, alignment=QtCore.Qt.AlignCenter)
            self.matrices_grid_dict["matrix"+str(x)+"grid"].addWidget(self.matrices_parentesis_dict["matrix"+str(x)+"parentesisclosedlabel"], 2, alignment=QtCore.Qt.AlignLeft)
            self.matrix_tree_widget.setItemWidget(self.matrices_item_dict["matrix"+str(x)+"item"], 1, self.matrices_frame_dict["matrix"+str(x)+"frame"])
        matrices_label_cell_font = QtGui.QFont()
        matrices_label_cell_font.setFamily("Alice")
        matrices_label_cell_font.setPointSize(12)
        matrices_label_cell_stylesheet = "background-color: transparent;\n""color: rgb(236, 236, 236);\n"
        self.matrices_label_cell_dict={}
        for z in  range(1,21):
            for x, y in itools.product(range(1,11), range(1,11)):
                self.matrices_label_cell_dict["matrix"+str(z)+"labelcell"+str(x)+"_"+str(y)] = QtWidgets.QLabel(self.matrices_values_grid_widget_dict["matrix"+str(z)+"valuesgridWidget"] )
                self.matrices_label_cell_dict["matrix"+str(z)+"labelcell"+str(x)+"_"+str(y)].setStyleSheet(matrices_label_cell_stylesheet)
                self.matrices_label_cell_dict["matrix"+str(z)+"labelcell"+str(x)+"_"+str(y)].setFont(matrices_label_cell_font)
                self.matrices_values_grid_dict["matrix"+str(z)+"valuesgrid"].addWidget(self.matrices_label_cell_dict["matrix"+str(z)+"labelcell"+str(x)+"_"+str(y)], (x-1), (y-1), 1, 1, alignment=QtCore.Qt.AlignCenter)
                self.matrices_label_cell_dict["matrix"+str(z)+"labelcell"+str(x)+"_"+str(y)].setHidden(True)
        MainWindow.setCentralWidget(self.central_widget)
        self.menu_bar = QtWidgets.QMenuBar(MainWindow)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 330, 21))
        MainWindow.setMenuBar(self.menu_bar)
        self.status_bar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.status_bar)
        self.status_bar.hide()
        self.retranslateUi(MainWindow)
        self.tab_widget.setCurrentIndex(0)
        self.tab_widget.currentChanged.connect(self.admin.ui.updateMatrixTreeItemsOnTabChange)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.type_of_assign_to_make = 0

    def hideAndShowVectorItems(self):
        y = int(self.number_of_vectors_combobox.currentText())
        for x in range(1, 21):
            if x <= y:
                self.vectors_item_dict["vector"+str(x)+"item"].setHidden(False)
            else:
                self.vectors_item_dict["vector"+str(x)+"item"].setHidden(True)


    def hideAndShowMatrixItems(self):
        y = int(self.number_of_matrix_combobox.currentText())
        for x in range(1, 21):
            if x <= y:
                self.matrices_item_dict["matrix"+str(x)+"item"].setHidden(False)
            else:
                self.matrices_item_dict["matrix"+str(x)+"item"].setHidden(True)

    def showValuesWindowVector(self):
        self.admin.assign_values_window.valueswindow.hide()

        self.type_of_assign_to_make = "vector"

        get_selected = self.vector_tree_widget.selectedItems()
        try:
            selected_vector = self.vector_tree_widget.indexOfTopLevelItem(get_selected[0])
        except:
            self.admin.admin.window.error_window.show()
            self.admin.admin.window.error_window.ui.error_window_body_label.setText("Select Vector to modify")
            return
        selected_vector_columns = self.admin.admin.vectors_columns[int(selected_vector)]
        selected_vector_values = self.admin.admin.vectors_arrays[int(selected_vector)]

        self.admin.assign_values_window.valueswindow.show()
        self.admin.assign_values_window.valueswindow.ui.rows_combobox.setCurrentIndex(0)
        self.admin.assign_values_window.valueswindow.ui.rows_combobox.setEnabled(False)
        self.admin.assign_values_window.valueswindow.ui.selected_icon_label.setPixmap(QtGui.QPixmap("icons/individualvectoricon/vector"+str(int(selected_vector)+1)+"icon.png"))
        self.admin.assign_values_window.valueswindow.ui.columns_combobox.setCurrentIndex(int(selected_vector_columns)-1)
        self.admin.assign_values_window.valueswindow.ui.hideAndShowRows()
        self.admin.assign_values_window.valueswindow.ui.hideAndShowColumns()

        for x in range(1,11):
            for y in range(1,11):
                self.admin.assign_values_window.valueswindow.ui.cells_lineedit_dict["cell"+str(x)+"_"+str(y)].setText("")

        for y in range(0,selected_vector_columns):
                valueofcell = str(selected_vector_values[0][y])
                self.admin.assign_values_window.valueswindow.ui.cells_lineedit_dict["cell"+str(1)+"_"+str(y+1)].setText(valueofcell)

    def showValuesWindowMatrix(self):
        self.admin.assign_values_window.valueswindow.hide()

        self.type_of_assign_to_make = "matrix"

        get_selected = self.matrix_tree_widget.selectedItems()
        try:
            selected_matrix = self.matrix_tree_widget.indexOfTopLevelItem(get_selected[0])
        except:
            self.admin.admin.window.error_window.show()
            self.admin.admin.window.error_window.ui.error_window_body_label.setText("Select Matrix to modify")
            return
        selected_matrix_rows = self.admin.admin.matrices_rows[int(selected_matrix)]
        selected_matrix_columns = self.admin.admin.matrices_columns[int(selected_matrix)]
        selected_matrix_values = self.admin.admin.matrices_arrays[int(selected_matrix)]

        self.admin.assign_values_window.valueswindow.show()
        self.admin.assign_values_window.valueswindow.ui.rows_combobox.setEnabled(True)
        self.admin.assign_values_window.valueswindow.ui.rows_combobox.setCurrentIndex(int(selected_matrix_rows)-1)
        self.admin.assign_values_window.valueswindow.ui.selected_icon_label.setPixmap(QtGui.QPixmap("icons/individualmatrixicon/matrix"+str(int(selected_matrix)+1)+"icon.png"))
        self.admin.assign_values_window.valueswindow.ui.columns_combobox.setCurrentIndex(int(selected_matrix_columns)-1)
        self.admin.assign_values_window.valueswindow.ui.hideAndShowRows()
        self.admin.assign_values_window.valueswindow.ui.hideAndShowColumns()

        for x in range(1,11):
            for y in range(1,11):
                self.admin.assign_values_window.valueswindow.ui.cells_lineedit_dict["cell"+str(x)+"_"+str(y)].setText("")

        for x in range(0,selected_matrix_rows):
            for y in range(0,selected_matrix_columns):
                valueofcell = str(selected_matrix_values[x][y])
                self.admin.assign_values_window.valueswindow.ui.cells_lineedit_dict["cell"+str(x+1)+"_"+str(y+1)].setText(valueofcell)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.vector_tree_widget.headerItem().setText(0, _translate("MainWindow", (" Vector"+" "*15)))
        self.vector_tree_widget.headerItem().setText(1, _translate("MainWindow", ("    Values"+" "*55)))
        __sortingEnabled = self.vector_tree_widget.isSortingEnabled()
        self.vector_tree_widget.setSortingEnabled(False)
        self.vector_tree_widget.setSortingEnabled(__sortingEnabled)
        for x in range(0,20):
            self.number_of_vectors_combobox.setItemText(x, _translate("MainWindow", str(x+1)))
        self.matrix_tree_widget.headerItem().setText(0, _translate("MainWindow", (" Matrix"+" "*15)))
        self.matrix_tree_widget.headerItem().setText(1, _translate("MainWindow", ("    Values"+" "*55)))
        __sortingEnabled = self.matrix_tree_widget.isSortingEnabled()
        self.matrix_tree_widget.setSortingEnabled(False)
        self.matrix_tree_widget.setSortingEnabled(__sortingEnabled)
        for x in range(0,20):
            self.number_of_matrix_combobox.setItemText(x, _translate("MainWindow", str(x+1)))
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
        self.assign_pos_x = mainv.MAINWINDOWPOSITIONXAXIS - 330
        self.x = self.assign_pos_x
        self.y = mainv.MAINWINDOWPOSITIONYAXIS
        self.move(self.x,self.y)