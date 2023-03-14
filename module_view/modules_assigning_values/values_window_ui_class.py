from PySide2 import QtCore, QtGui, QtWidgets

######################
##STYLESHEETS IMPORT##
######################
import module_view.modules_assigning_values.assigning_values_stylesheets.values_window_stylesheet as vwss


class Ui_ValuesWindow(object):
    def setupUi(self, MainWindow,admin):
        self.admin=admin
        MainWindow.resize(412, 377)
        MainWindow.setWindowIcon((QtGui.QIcon("icons/Windowicon.png")))
        MainWindow.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowTitleHint)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setStyleSheet("background-color: rgb(27, 28, 27);\n"
            "border: 2px solid rgb(15,16,15);")
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.selected_vm_label = QtWidgets.QLabel(self.central_widget)
        self.selected_vm_label.setGeometry(QtCore.QRect(2, 20, 251, 21))
        self.selected_vm_label.setStyleSheet(vwss.selected_vm_label_stylesheet)
        self.selected_vm_label.setText("")
        self.apply_button = QtWidgets.QPushButton(self.central_widget)
        self.apply_button.setGeometry(QtCore.QRect(176, 350, 101, 21))
        self.apply_button.setStyleSheet(vwss.apply_button_stylesheet)
        self.apply_button.setText("")
        apply_button_icon = QtGui.QIcon()
        apply_button_icon.addPixmap(QtGui.QPixmap("icons/createwindowicons/Applyicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.apply_button.setIcon(apply_button_icon)
        self.apply_button.setIconSize(QtCore.QSize(90, 40))
        self.apply_button.clicked.connect(self.apply_assign)
        self.apply_button.setShortcut("Return")
        self.decorative_label_top_row = QtWidgets.QLabel(self.central_widget)
        self.decorative_label_top_row.setGeometry(QtCore.QRect(0, 0, 411, 21))
        self.decorative_label_top_row.setStyleSheet(vwss.decorative_label_top_row_stylesheet)
        self.decorative_label_top_row.setText("")
        self.rows_label = QtWidgets.QLabel(self.central_widget)
        self.rows_label.setGeometry(QtCore.QRect(240, 0, 81, 21))
        self.rows_label.setStyleSheet(vwss.rows_label_stylesheet)
        self.rows_label.setText("")
        self.rows_label.setPixmap(QtGui.QPixmap("icons/createwindowicons/Rowsicon.png"))
        self.rows_label.setScaledContents(True)
        self.columns_label = QtWidgets.QLabel(self.central_widget)
        self.columns_label.setGeometry(QtCore.QRect(320, 0, 81, 21))
        self.columns_label.setStyleSheet(vwss.columns_label_stylesheet)
        self.columns_label.setText("")
        self.columns_label.setPixmap(QtGui.QPixmap("icons/createwindowicons/Columnsicon.png"))
        self.columns_label.setScaledContents(True)
        self.selected_label = QtWidgets.QLabel(self.central_widget)
        self.selected_label.setGeometry(QtCore.QRect(0, 0, 81, 21))
        self.selected_label.setStyleSheet(vwss.selected_label_stylesheet)
        self.selected_label.setText("")
        self.selected_label.setPixmap(QtGui.QPixmap("icons/createwindowicons/Selecticon.png"))
        self.selected_label.setScaledContents(True)
        self.cancel_button = QtWidgets.QPushButton(self.central_widget)
        self.cancel_button.setGeometry(QtCore.QRect(300, 350, 101, 21))
        self.cancel_button.setStyleSheet(vwss.cancel_button_stylesheet)
        self.cancel_button.setText("")
        cancel_button_icon = QtGui.QIcon()
        cancel_button_icon.addPixmap(QtGui.QPixmap("icons/createwindowicons/Cancelicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel_button.setIcon(cancel_button_icon)
        self.cancel_button.setIconSize(QtCore.QSize(90, 40))
        self.cancel_button.clicked.connect(self.cancel_assign)

        self.rows_combobox_frame = QtWidgets.QFrame(self.central_widget)
        self.rows_combobox_frame.setGeometry(QtCore.QRect(260, 20, 41, 22))
        self.rows_combobox_frame.setStyleSheet(vwss.rows_combobox_frame_stylesheet)
        self.rows_combobox = QtWidgets.QComboBox(self.rows_combobox_frame)
        self.rows_combobox.setEnabled(True)
        self.rows_combobox.setGeometry(QtCore.QRect(0, 0, 41, 22))
        font = QtGui.QFont()
        font.setFamily("Alice")
        font.setPointSize(12)
        self.rows_combobox.setFont(font)
        self.rows_combobox.setStyleSheet(vwss.rows_combobox_stylesheet)
        for x in range (0,10):
            self.rows_combobox.addItem("")
        self.rows_combobox.activated.connect(self.hide_and_show_rows)

        self.columns_combobox_frame = QtWidgets.QFrame(self.central_widget)
        self.columns_combobox_frame.setGeometry(QtCore.QRect(340, 20, 41, 22))
        self.columns_combobox_frame.setStyleSheet(vwss.columns_combobox_frame_stylesheet)
        self.columns_combobox = QtWidgets.QComboBox(self.columns_combobox_frame)
        self.columns_combobox.setGeometry(QtCore.QRect(0, 0, 41, 22))
        font = QtGui.QFont()
        font.setFamily("Alice")
        font.setPointSize(12)
        self.columns_combobox.setFont(font)
        self.columns_combobox.setStyleSheet(vwss.columns_combobox_stylesheet)
        for x in range (0,10):
            self.columns_combobox.addItem("")
        self.columns_combobox.activated.connect(self.hide_and_show_columns)
        self.decorative_label_top_row_2 = QtWidgets.QLabel(self.central_widget)
        self.decorative_label_top_row_2.setGeometry(QtCore.QRect(250, 0, 61, 21))
        self.decorative_label_top_row_2.setStyleSheet(vwss.decorative_label_top_row_2_stylesheet)
        self.decorative_label_top_row_2.setText("")
        self.selected_icon_label = QtWidgets.QLabel(self.central_widget)
        self.selected_icon_label.setGeometry(QtCore.QRect(10, 20, 21, 21))
        self.selected_icon_label.setStyleSheet(vwss.selected_icon_label_stylesheet)
        self.selected_icon_label.setText("")
        self.selected_icon_label.setPixmap(QtGui.QPixmap("icons/individualvectoricon/vector1icon.png"))
        self.selected_icon_label.setScaledContents(True)

        ###############################
        ##REGULAR EXPRESION FOR CELLS##
        ###############################

        self.reg_ex_cell = QtCore.QRegExp("(^-?[0-9]+/0*[1-9][0-9]*$|^[-+]?[0-9]+$|^[-+]?[0-9]+\.[0-9]+$)")

        #########
        ##CELLS##
        #########
        cell_lineedit_y_pos=-30
        cell_lineedit_x_pos=20
        self.cells_lineedit_dict,self.cells_validators={},{}
        for x in range(1,11):
            cell_lineedit_x_pos=+30
            for y in range(1,11):
                cell_lineedit_y_pos+=40
                self.cells_lineedit_dict["cell"+str(x)+"_"+str(y)] = QtWidgets.QLineEdit(self.central_widget)
                self.cells_lineedit_dict["cell"+str(x)+"_"+str(y)].setGeometry(QtCore.QRect(cell_lineedit_y_pos, cell_lineedit_x_pos, 31, 21))
                font = QtGui.QFont()
                font.setFamily("Alice")
                font.setPointSize(12)
                self.cells_lineedit_dict["cell"+str(x)+"_"+str(y)].setFont(font)
                self.cells_lineedit_dict["cell"+str(x)+"_"+str(y)].setStyleSheet("color: rgb(236, 236, 236);"
        "border:1px;"
        "border-style:solid;"
        "border-color: rgb(15, 16, 15);"
        "background-color: rgb(42, 43, 42);"
        "")
                self.cells_lineedit_dict["cell"+str(x)+"_"+str(y)].setAlignment(QtCore.Qt.AlignCenter)
                self.cells_validators["cell"+str(x)+"_"+str(y)+"_validator"] = QtGui.QRegExpValidator(self.reg_ex_cell, self.cells_lineedit_dict["cell"+str(x)+"_"+str(y)])
                self.cells_lineedit_dict["cell"+str(x)+"_"+str(y)].setValidator(self.cells_validators["cell"+str(x)+"_"+str(y)+"_validator"])
        MainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def hide_and_show_rows(self):
        y = int(self.rows_combobox.currentText())
        z = int(self.columns_combobox.currentText())
        for x in range(0, 10):
            if x <= (y-1):
                for w in range (0,z):
                    self.cells_lineedit_dict["cell"+str(x+1)+"_"+str(w+1)].setHidden(False)
                for o in range (z,10):
                    self.cells_lineedit_dict["cell"+str(x+1)+"_"+str(o+1)].setHidden(True)
            else:
                for w in range(0,10):
                    self.cells_lineedit_dict["cell"+str(x+1)+"_"+str(w+1)].setHidden(True)


        row_win_resize = 377-(30*(10-y))
        self.admin.valueswindow.resize(412, row_win_resize)
        row_buttons_repos=350-(30*(10-y))
        self.apply_button.setGeometry(QtCore.QRect(176, row_buttons_repos, 101, 21))
        self.cancel_button.setGeometry(QtCore.QRect(300, row_buttons_repos, 101, 21))

    def hide_and_show_columns(self):
        z = int(self.rows_combobox.currentText())
        y = int(self.columns_combobox.currentText())
        for x in range(0, 10):
            if x <= (y-1):
                for w in range (0,z):
                    self.cells_lineedit_dict["cell"+str(w+1)+"_"+str(x+1)].setHidden(False)
                for o in range (z,10):
                    self.cells_lineedit_dict["cell"+str(o+1)+"_"+str(x+1)].setHidden(True)
            else:
                for w in range(0,10):
                    self.cells_lineedit_dict["cell"+str(w+1)+"_"+str(x+1)].setHidden(True)

        for j in range(0, 10):
            for k in range(0, 10):
                f=10 + (40 * j) + (18*(10-y))
                h=50 + (30 * k)
                self.cells_lineedit_dict["cell"+str(k+1)+"_"+str(j+1)].setGeometry(QtCore.QRect(f,h,31,21))

    def cancel_assign(self):
        self.admin.valueswindow.hide()
        self.admin.ui.type_of_assign_to_make = 0

    def apply_assign(self):
        if self.admin.ui.type_of_assign_to_make == "vector":
            get_selected = self.admin.ui.vector_tree_widget.selectedItems()
            selected_vector_item = self.admin.ui.vector_tree_widget.indexOfTopLevelItem(get_selected[0])
            selected_vector_item_rows = int(self.rows_combobox.currentText())
            selected_vector_item_columns = int(self.columns_combobox.currentText())

            self.new_vector = []

            for x in range(0,selected_vector_item_rows):
                list_of_rows=[]
                for y in range(0,selected_vector_item_columns):
                    cell_value = self.cells_lineedit_dict["cell"+str(x+1)+"_"+str(y+1)].text()

                    if cell_value == "":
                        self.admin.admin.admin.window.error_window.show()
                        self.admin.admin.admin.window.error_window.ui.error_window_body_label.setText("All cells must be filled")
                        return
                    elif cell_value == "-":
                        self.admin.admin.admin.window.error_window.show()
                        self.admin.admin.admin.window.error_window.ui.error_window_body_label.setText("Invalid cell value: \"-\" ")
                        return
                    else:
                        pass

                    list_of_rows.append(cell_value)
                self.new_vector.append(list_of_rows)
            self.admin.admin.admin.modify_vectors(selected_vector_item,selected_vector_item_rows,selected_vector_item_columns,self.new_vector)
            self.admin.admin.ui.fill_vectors_treeview()

        elif self.admin.ui.type_of_assign_to_make == "matrix":
            get_selected = self.admin.ui.matrix_tree_widget.selectedItems()
            selected_matrix_item = self.admin.ui.matrix_tree_widget.indexOfTopLevelItem(get_selected[0])
            selected_matrix_item_rows = int(self.rows_combobox.currentText())
            selected_matrix_item_columns = int(self.columns_combobox.currentText())

            self.newmatrix = []

            for x in range(0,selected_matrix_item_rows):
                list_of_rows=[]
                for y in range(0,selected_matrix_item_columns):
                    cell_value = self.cells_lineedit_dict["cell"+str(x+1)+"_"+str(y+1)].text()

                    if cell_value == "":
                        self.admin.admin.admin.window.error_window.show()
                        self.admin.admin.admin.window.error_window.ui.error_window_body_label.setText("All cells must be filled")
                        return
                    elif cell_value == "-":
                        self.admin.admin.admin.window.error_window.show()
                        self.admin.admin.admin.window.error_window.ui.error_window_body_label.setText("Invalid cell value: \"-\" ")
                        return
                    else:
                        pass

                    list_of_rows.append(cell_value)
                self.newmatrix.append(list_of_rows)
            self.admin.admin.admin.modify_matrices(selected_matrix_item,selected_matrix_item_rows,selected_matrix_item_columns,self.newmatrix)
            self.admin.admin.ui.fill_matrices_treeview()
        else:
            return
        self.admin.valueswindow.hide()
        self.admin.ui.type_of_assign_to_make = 0
        self.admin.admin.ui.angles_vector_x_combobox_value_changed()
        self.admin.admin.ui.angles_vector_y_combobox_value_changed()
        try:
            self.admin.admin.ui.eigenvalues_choose_matrix_list_widget_item_changed()
        except:
            pass
        try:
            self.admin.admin.ui.system_of_equations_choose_vector_list_widget_item_changed()
        except:
            pass
        try:
            self.admin.admin.ui.system_of_equations_choose_matrix_list_widget_item_changed()
        except:
            pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.rows_combobox.setItemText(0, _translate("MainWindow", "1"))
        self.rows_combobox.setItemText(1, _translate("MainWindow", "2"))
        self.rows_combobox.setItemText(2, _translate("MainWindow", "3"))
        self.rows_combobox.setItemText(3, _translate("MainWindow", "4"))
        self.rows_combobox.setItemText(4, _translate("MainWindow", "5"))
        self.rows_combobox.setItemText(5, _translate("MainWindow", "6"))
        self.rows_combobox.setItemText(6, _translate("MainWindow", "7"))
        self.rows_combobox.setItemText(7, _translate("MainWindow", "8"))
        self.rows_combobox.setItemText(8, _translate("MainWindow", "9"))
        self.rows_combobox.setItemText(9, _translate("MainWindow", "10"))
        self.columns_combobox.setItemText(0, _translate("MainWindow", "1"))
        self.columns_combobox.setItemText(1, _translate("MainWindow", "2"))
        self.columns_combobox.setItemText(2, _translate("MainWindow", "3"))
        self.columns_combobox.setItemText(3, _translate("MainWindow", "4"))
        self.columns_combobox.setItemText(4, _translate("MainWindow", "5"))
        self.columns_combobox.setItemText(5, _translate("MainWindow", "6"))
        self.columns_combobox.setItemText(6, _translate("MainWindow", "7"))
        self.columns_combobox.setItemText(7, _translate("MainWindow", "8"))
        self.columns_combobox.setItemText(8, _translate("MainWindow", "9"))
        self.columns_combobox.setItemText(9, _translate("MainWindow", "10"))

