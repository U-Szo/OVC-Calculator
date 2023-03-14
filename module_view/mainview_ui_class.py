from PySide2 import QtCore, QtGui, QtWidgets
import numpy as np
from fractions import Fraction
import itertools as itools
from module_view.widgets.text_drop_class import QTextEditDropEnabled

######################
##STYLESHEETS IMPORT##
######################
import module_view.mainview_stylesheets.mainview_stylesheets_poststart as mvssps
import module_view.mainview_stylesheets.vector_and_matrix_tab_stylesheet as vmtss
import module_view.mainview_stylesheets.angles_tab_stylesheet as atss
import module_view.mainview_stylesheets.eigenvectors_tab_stylesheet as evtss
import module_view.mainview_stylesheets.system_of_equations_tab_stylesheet as soetss
import module_view.mainview_stylesheets.mainview_side_frames_stylesheet as mvsfss

####################
# GLOBAL VARIABLES #
####################
_FIRST_TIME_LOADING_MATRICES = True
_FIRST_TAB_CHANGE = True

####################
##### UI CLASS #####
####################
class Ui_MainWindow(object):
    def setupUi(self, MainWindow,admin):
        self.admin=admin
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setFixedSize(704, 588)
        MainWindow.setStyleSheet("background-color: rgb(25,26,25);\n")
        MainWindow.setWindowIcon((QtGui.QIcon("icons/Windowicon.png")))
        self.mainwindow_central_widget = QtWidgets.QWidget(MainWindow)

        self.deg_or_rad="RAD"
        self.dd_or_dms= "DMS"
        #############################################
        ##MAIN VECTOR AND MATRIX SCREEN SCROLL AREA##
        #############################################
        self.main_vector_matrix_screen_scrollarea = QtWidgets.QScrollArea(self.mainwindow_central_widget)
        self.main_vector_matrix_screen_scrollarea.setGeometry(QtCore.QRect(112, 119, 481, 159))
        self.main_vector_matrix_screen_scrollarea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.main_vector_matrix_screen_scrollarea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.main_vector_matrix_screen_scrollarea.setWidgetResizable(True)

        self.main_vector_matrix_screen_scrollarea_widget_contents = QtWidgets.QWidget()
        self.main_vector_matrix_screen_scrollarea_widget_contents.setGeometry(QtCore.QRect(0, 0, 479, 157))
        self.main_vector_matrix_screen_scrollarea_widget_contents.setMinimumSize(0, 0)
        self.main_vector_matrix_screen_scrollarea_widget_contents.setStyleSheet("background-color: rgb(17, 18, 17);\n")
        self.main_vector_matrix_screen_gridlayout = QtWidgets.QHBoxLayout(self.main_vector_matrix_screen_scrollarea_widget_contents)
        self.main_vector_matrix_screen_gridlayout.setSpacing(0)

        self.main_vector_matrix_screen_matrix_gridlayout_widget = QtWidgets.QWidget()
        self.main_vector_matrix_screen_matrix_gridlayout = QtWidgets.QHBoxLayout(self.main_vector_matrix_screen_matrix_gridlayout_widget)
        self.main_vector_matrix_screen_matrix_gridlayout.setSpacing(5)
        #############################################
        ##MAIN VECTOR AND MATRIX SCREEN VALUES GRID##
        #############################################
        self.result_matrix_parentesis_open_label = QtWidgets.QLabel()
        self.result_matrix_parentesis_open_label.setPixmap(QtGui.QPixmap("icons/Itemparentesisopen.png"))
        self.result_matrix_parentesis_open_label.setScaledContents(True)
        self.result_matrix_parentesis_open_label.setFixedWidth(5)
        self.result_matrix_parentesis_closed_label = QtWidgets.QLabel()
        self.result_matrix_parentesis_closed_label.setPixmap(QtGui.QPixmap("icons/Itemparentesisclose.png"))
        self.result_matrix_parentesis_closed_label.setScaledContents(True)
        self.result_matrix_parentesis_closed_label.setFixedWidth(5)
        self.main_vector_matrix_screen_values_gridlayout_widget = QtWidgets.QWidget()
        self.main_vector_matrix_screen_values_gridlayout = QtWidgets.QGridLayout(self.main_vector_matrix_screen_values_gridlayout_widget)
        self.main_vector_matrix_screen_values_gridlayout.setContentsMargins(0, 0, 0, 0)
        self.main_vector_matrix_screen_values_gridlayout.setHorizontalSpacing(20)
        self.main_vector_matrix_screen_values_gridlayout.setVerticalSpacing(5)
        self.main_vector_matrix_screen_gridlayout.addWidget(self.main_vector_matrix_screen_matrix_gridlayout_widget, 1, alignment=QtCore.Qt.AlignCenter)
        self.main_vector_matrix_screen_matrix_gridlayout.addWidget(self.result_matrix_parentesis_open_label, 0, alignment=QtCore.Qt.AlignLeft)
        self.main_vector_matrix_screen_matrix_gridlayout.addWidget(self.main_vector_matrix_screen_values_gridlayout_widget, 1, alignment=QtCore.Qt.AlignCenter)
        self.main_vector_matrix_screen_matrix_gridlayout.addWidget(self.result_matrix_parentesis_closed_label, 2, alignment=QtCore.Qt.AlignLeft)
        self.main_vector_matrix_screen_scrollarea.setWidget(self.main_vector_matrix_screen_scrollarea_widget_contents)
        self.result_matrix_parentesis_open_label.setHidden(True)
        self.result_matrix_parentesis_closed_label.setHidden(True)
        ######################################################
        ## MAIN VECTOR AND MATRIX SCROLL AREA VALUES LABELS ##
        ######################################################
        font = QtGui.QFont()
        font.setFamily("Alice")
        font.setPointSize(12)
        int_float_font = QtGui.QFont()
        int_float_font.setFamily("Alice")
        int_float_font.setPointSize(15)
        result_matrix_stylesheet = "background-color: transparent;\n""color: rgb(236, 236, 236);\n"

        self.result_matrix_label_cell_dict={}
        for x, y in itools.product(range(1,11), range(1,11)):
            self.result_matrix_label_cell_dict["result_matrixlabelcell"+str(x)+"_"+str(y)] = QtWidgets.QLabel(self.main_vector_matrix_screen_values_gridlayout_widget)
            self.result_matrix_label_cell_dict["result_matrixlabelcell"+str(x)+"_"+str(y)].setStyleSheet(result_matrix_stylesheet)
            self.result_matrix_label_cell_dict["result_matrixlabelcell"+str(x)+"_"+str(y)].setFont(font)
            self.main_vector_matrix_screen_values_gridlayout.addWidget(self.result_matrix_label_cell_dict["result_matrixlabelcell"+str(x)+"_"+str(y)], (x-1), (y-1), 1, 1, alignment=QtCore.Qt.AlignCenter)
            self.result_matrix_label_cell_dict["result_matrixlabelcell"+str(x)+"_"+str(y)].setHidden(True)

        self.result_label_int_or_float = QtWidgets.QLabel()
        self.result_label_int_or_float.setStyleSheet("background-color: transparent;\n""color: rgb(236, 236, 236);\n")
        self.result_label_int_or_float.setFont(int_float_font)
        self.main_vector_matrix_screen_gridlayout.addWidget(self.result_label_int_or_float, 103, alignment=QtCore.Qt.AlignCenter)
        self.result_label_int_or_float.setHidden(True)

        self.result_label_error = QtWidgets.QLabel()
        self.result_label_error.setStyleSheet("background-color: transparent;\n""color: rgb(232, 17, 35);\n")
        self.result_label_error.setFont(int_float_font)
        self.main_vector_matrix_screen_gridlayout.addWidget(self.result_label_error, 4, alignment=QtCore.Qt.AlignLeft)
        self.result_label_error.setHidden(True)
 
        self.main_title_label_top = QtWidgets.QLabel(self.mainwindow_central_widget)
        self.main_title_label_top.setGeometry(QtCore.QRect(-15, 9, 638, 91))
        self.main_title_label_top.setStyleSheet("background-color: rgb(25,26,25);\n")
        self.main_title_label_top.setText("")
        self.main_title_label_top.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_buttons_frame = QtWidgets.QFrame(self.mainwindow_central_widget)
        self.tab_buttons_frame.setGeometry(QtCore.QRect(0, 70, 91, 519))
        self.tab_buttons_frame.setStyleSheet(mvsfss.tab_buttons_frame_stylesheet)
        self.tab_buttons_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tab_buttons_frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.tab_buttons_dict={}
        self.tab_buttons_name_list=["vector_tab_button","matrix_tab_button","angles_tab_button",
        "eigenvalues_tab_button","system_of_equations_tab_button"]
        self.tab_buttons_stylesheet_list=[mvsfss.vector_tab_button_stylesheet,
        mvsfss.matrix_tab_button_stylesheet,mvsfss.angles_tab_button_stylesheet,
        mvsfss.eigenvalues_tab_button_sylesheet,mvsfss.system_of_equations_tab_button_stylesheet]
        self.tab_buttons_icon_list=["icons/Vectoresicon.png","icons/Matricesicon.png",
        "icons/Anguloicon.png","icons/Eigenvaluesicon.png","icons/Systemofequationsicon.png"]
        self.tab_buttons_method_list=[self.vectors_button_state,self.matrix_button_state,
        self.angles_button_state,self.eigenvalues_button_state,self.system_of_equation_button_state]
        self.tab_buttons_position=-11
        for x in range(0,5):
            self.tab_buttons_position+=40
            self.tab_buttons_dict[self.tab_buttons_name_list[x]] = QtWidgets.QPushButton(self.tab_buttons_frame)
            self.tab_buttons_dict[self.tab_buttons_name_list[x]].setGeometry(QtCore.QRect(0, self.tab_buttons_position, 81, 41))
            self.tab_buttons_dict[self.tab_buttons_name_list[x]].setStyleSheet(self.tab_buttons_stylesheet_list[x])
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(self.tab_buttons_icon_list[x]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.tab_buttons_dict[self.tab_buttons_name_list[x]].setIcon(icon)
            if self.tab_buttons_name_list[x] == "vector_tab_button":
                self.tab_buttons_dict[self.tab_buttons_name_list[x]].setIconSize(QtCore.QSize(24, 24))
            elif self.tab_buttons_name_list[x] == "matrix_tab_button":
                self.tab_buttons_dict[self.tab_buttons_name_list[x]].setIconSize(QtCore.QSize(24, 24))
            elif self.tab_buttons_name_list[x] == "angles_tab_button":
                self.tab_buttons_dict[self.tab_buttons_name_list[x]].setIconSize(QtCore.QSize(19, 19))
            elif self.tab_buttons_name_list[x] == "eigenvalues_tab_button":
                self.tab_buttons_dict[self.tab_buttons_name_list[x]].setIconSize(QtCore.QSize(17, 17))
            elif self.tab_buttons_name_list[x] == "system_of_equations_tab_button":
                self.tab_buttons_dict[self.tab_buttons_name_list[x]].setIconSize(QtCore.QSize(27, 27))
            self.tab_buttons_dict[self.tab_buttons_name_list[x]].setCheckable(True)
            self.tab_buttons_dict[self.tab_buttons_name_list[x]].clicked.connect(self.tab_buttons_method_list[x])

        self.filler_bottom_left_frame_button = QtWidgets.QPushButton(self.tab_buttons_frame)
        self.filler_bottom_left_frame_button.setEnabled(False)
        self.filler_bottom_left_frame_button.setGeometry(QtCore.QRect(0, 229, 81, 221))
        self.filler_bottom_left_frame_button.setStyleSheet(mvsfss.filler_bottom_left_frame_button_stylesheet)
        self.filler_bottom_left_frame_button.setText("")
        self.filler_bottom_left_frame_button.setCheckable(True)
        self.bottom_assign_button_background_label = QtWidgets.QLabel(self.mainwindow_central_widget)
        self.bottom_assign_button_background_label.setGeometry(QtCore.QRect(-10, 519, 714, 91))
        self.bottom_assign_button_background_label.setStyleSheet("background-color: rgb(25, 26, 25);")
        self.bottom_assign_button_background_label.setPixmap(QtGui.QPixmap("icons/Bottomassignbuttonbackground.png"))
        self.bottom_assign_button_background_label.setText("")
        self.info_button = QtWidgets.QPushButton(self.tab_buttons_frame)
        self.info_button.setGeometry(QtCore.QRect(28, 369, 26, 26))
        self.info_button.setStyleSheet(mvsfss.infoButton_stylesheet)
        self.info_button.setText("")
        info_button_icon = QtGui.QIcon()
        info_button_icon.addPixmap(QtGui.QPixmap("icons/Infoicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.info_button.setIcon(info_button_icon)
        self.info_button.setIconSize(QtCore.QSize(26, 26))
        self.info_button.setCheckable(False)
        self.info_button.clicked.connect(self.info_button_clicked)
        self.assign_button = QtWidgets.QPushButton(self.mainwindow_central_widget)
        self.assign_button.setGeometry(QtCore.QRect(0, 519, 96, 41))
        self.assign_button.setStyleSheet(mvsfss.assign_button_stylesheet)
        self.assign_button.setText("")
        assign_button_icon = QtGui.QIcon()
        assign_button_icon.addPixmap(QtGui.QPixmap("icons/Assignicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.assign_button.setIcon(assign_button_icon)
        self.assign_button.setIconSize(QtCore.QSize(130, 27))
        self.assign_button.setCheckable(False)
        self.assign_button.clicked.connect(self.show_assign_window)
        self.filler_top_left_frame_label = QtWidgets.QLabel(self.mainwindow_central_widget)
        self.filler_top_left_frame_label.setGeometry(QtCore.QRect(0, 29, 82, 71))
        self.filler_top_left_frame_label.setStyleSheet(mvsfss.filler_top_left_frame_label_stylesheet)
        self.filler_top_left_frame_label.setText("")
        self.filler_top_left_frame_label.setScaledContents(True)
        self.right_all_clear_frame = QtWidgets.QFrame(self.mainwindow_central_widget)
        self.right_all_clear_frame.setGeometry(QtCore.QRect(623, -20, 81, 539))
        self.right_all_clear_frame.setStyleSheet(mvsfss.right_all_clear_frame_stylesheet)
        self.right_all_clear_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right_all_clear_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background_vectors_and_matrices_operators_label = QtWidgets.QLabel(self.mainwindow_central_widget)
        self.background_vectors_and_matrices_operators_label.setGeometry(QtCore.QRect(283, 460, 140, 59))
        self.background_vectors_and_matrices_operators_label.setStyleSheet(vmtss.background_vectors_and_matrices_operators_label_stylesheet)
        self.background_vectors_and_matrices_operators_label.setText("")
        self.matrix_operators_buttons_names=["additionButton","subtractionButton","matrixproductButton","transposeButton","determinantButton"]
        self.matrixoperatorsbuttons_methods=[self.addition_button_clicked,self.subtraction_button_clicked,self.matrix_product_button_clicked,
        self.transpose_button_clicked,self.determinant_button_clicked]
        self.matrixoperatorsbuttons_icons=["icons/Additionicon.png","icons/Subtractionicon.png","icons/Matrixproducticon.png",
        "icons/transpicon.png","icons/deticon.png"]
        self.vector_operators_buttons_names=["additionButton","subtractionButton","scalarproductButton","vectorproductButton","magnitudeButton"]
        self.vectoroperatorsbuttons_methods=[self.addition_button_clicked,self.subtraction_button_clicked,self.scalar_button_clicked,
        self.vector_product_button_clicked,self.magnitude_button_clicked]
        self.vectoroperatorsbuttons_icons=["icons/Additionicon.png","icons/Subtractionicon.png","icons/Scalarproducticon.png",
        "icons/Vectorproducticon.png","icons/Magnitudeicon.png"]
        self.answer_and_equal_buttons_names=["answerButton","equalButton"]
        self.answer_and_equalbuttons_methods=[self.answer_button_clicked,self.equal_button_clicked]
        self.answer_and_equalbuttons_icons=["icons/Answericon.png","icons/Equalicon.png"]
        self.matrix_operators_buttons_dict,self.vector_operators_buttons_dict,self.answer_and_equal_buttons_dict={},{},{}
        self.matrixoperatorsbuttons_position,self.vectoroperatorsbuttons_position,self.answer_and_equalbuttons_position=232,232,369
        self.matrixoperatorbuttonscounter,self.vectoroperatorbuttonscounter,self.answer_and_equalbuttons_counter=-1,-1,-1
        for x in self.matrix_operators_buttons_names:
            self.matrixoperatorbuttonscounter+=1
            self.matrixoperatorsbuttons_position+=50
            self.matrix_operators_buttons_dict[x] = QtWidgets.QPushButton(self.mainwindow_central_widget)
            self.matrix_operators_buttons_dict[x].setStyleSheet(vmtss.matrix_vector_answer_equal_operators_stylesheet)
            self.matrix_operators_buttons_dict[x].setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(self.matrixoperatorsbuttons_icons[self.matrixoperatorbuttonscounter]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.matrix_operators_buttons_dict[x].setIcon(icon)
            self.matrix_operators_buttons_dict[x].setCheckable(False)
            self.matrix_operators_buttons_dict[x].clicked.connect(self.matrixoperatorsbuttons_methods[self.matrixoperatorbuttonscounter])
            if x == "transposeButton":
                self.matrix_operators_buttons_dict[x].setIconSize(QtCore.QSize(23, 23))
                self.matrix_operators_buttons_dict[x].setGeometry(QtCore.QRect(self.matrixoperatorsbuttons_position-132, 469, 41, 41)) 
            elif x == "determinantButton":
                self.matrix_operators_buttons_dict[x].setIconSize(QtCore.QSize(30, 30))
                self.matrix_operators_buttons_dict[x].setGeometry(QtCore.QRect(self.matrixoperatorsbuttons_position-132, 469, 41, 41))
            else:
                self.matrix_operators_buttons_dict[x].setIconSize(QtCore.QSize(23, 23))
                self.matrix_operators_buttons_dict[x].setGeometry(QtCore.QRect(self.matrixoperatorsbuttons_position, 419, 41, 41))
        for x in self.vector_operators_buttons_names:
            self.vectoroperatorbuttonscounter+=1
            self.vectoroperatorsbuttons_position+=50
            self.vector_operators_buttons_dict[x] = QtWidgets.QPushButton(self.mainwindow_central_widget)
            self.vector_operators_buttons_dict[x].setStyleSheet(vmtss.matrix_vector_answer_equal_operators_stylesheet)
            self.vector_operators_buttons_dict[x].setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(self.vectoroperatorsbuttons_icons[self.vectoroperatorbuttonscounter]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.vector_operators_buttons_dict[x].setIcon(icon)
            self.vector_operators_buttons_dict[x].setCheckable(False)
            self.vector_operators_buttons_dict[x].clicked.connect(self.vectoroperatorsbuttons_methods[self.vectoroperatorbuttonscounter])
            if x == "vectorproductButton":
                self.vector_operators_buttons_dict[x].setIconSize(QtCore.QSize(23, 23))
                self.vector_operators_buttons_dict[x].setGeometry(QtCore.QRect(self.vectoroperatorsbuttons_position-132, 469, 41, 41)) 
            elif x == "magnitudeButton":
                self.vector_operators_buttons_dict[x].setIconSize(QtCore.QSize(27, 27))
                self.vector_operators_buttons_dict[x].setGeometry(QtCore.QRect(self.vectoroperatorsbuttons_position-132, 469, 41, 41))
            else:
                self.vector_operators_buttons_dict[x].setIconSize(QtCore.QSize(23, 23))
                self.vector_operators_buttons_dict[x].setGeometry(QtCore.QRect(self.vectoroperatorsbuttons_position, 419, 41, 41))
        for x in self.answer_and_equal_buttons_names:
            self.answer_and_equalbuttons_counter+=1
            self.answer_and_equalbuttons_position+=50
            self.answer_and_equal_buttons_dict[x] = QtWidgets.QPushButton(self.mainwindow_central_widget)
            self.answer_and_equal_buttons_dict[x].setStyleSheet(vmtss.matrix_vector_answer_equal_operators_stylesheet)
            self.answer_and_equal_buttons_dict[x].setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(self.answer_and_equalbuttons_icons[self.answer_and_equalbuttons_counter]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.answer_and_equal_buttons_dict[x].setIcon(icon)
            self.answer_and_equal_buttons_dict[x].setCheckable(False)
            self.answer_and_equal_buttons_dict[x].clicked.connect(self.answer_and_equalbuttons_methods[self.answer_and_equalbuttons_counter])
            self.answer_and_equal_buttons_dict[x].setGeometry(QtCore.QRect(473, self.answer_and_equalbuttons_position, 121, 41))
            if x == "answerButton":
                self.answer_and_equal_buttons_dict[x].setIconSize(QtCore.QSize(30, 30))
            if x == "equalButton":
                self.answer_and_equal_buttons_dict[x].setIconSize(QtCore.QSize(23, 23))
                self.answer_and_equal_buttons_dict[x].setShortcut("Return")
        self.all_clear_button = QtWidgets.QPushButton(self.right_all_clear_frame)
        self.all_clear_button.setGeometry(QtCore.QRect(0, 119, 81, 41))
        self.all_clear_button.setStyleSheet(mvsfss.all_clear_button_stylesheet)
        self.all_clear_button.setText("")
        all_clear_button_icon = QtGui.QIcon()
        all_clear_button_icon.addPixmap(QtGui.QPixmap("icons/Allclearicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.all_clear_button.setIcon(all_clear_button_icon)
        self.all_clear_button.setIconSize(QtCore.QSize(30, 30))
        self.all_clear_button.setCheckable(False)
        self.all_clear_button.clicked.connect(self.all_clear_button_clicked)
        self.decorative_graph_label = QtWidgets.QLabel(self.right_all_clear_frame)
        self.decorative_graph_label.setGeometry(QtCore.QRect(11, 163, 59, 492))
        self.decorative_graph_label.setStyleSheet(
                                                 "background-color: transparent;\n"
                                                 "border-top:0px;\n"
                                                 "border-style:solid;\n"
                                                 "border-top-color: rgb(236, 236, 236);\n"
                                                 "border-left:none;\n"
                                                 )
        self.decorative_graph_label.setText("")
        self.decorative_graph_label.setPixmap(QtGui.QPixmap("icons/Decorativegraph.png"))
        self.decorative_graph_label.setScaledContents(True)

        ###########################
        ##GENERAL OPERATORS FRAME##
        ###########################

        self.general_operators_frame = QtWidgets.QFrame(self.mainwindow_central_widget)
        self.general_operators_frame.setGeometry(QtCore.QRect(112, 329, 481, 63))
        self.general_operators_frame.setStyleSheet(vmtss.general_operators_framestylesheet)
        self.general_operators_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.general_operators_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.general_operators_buttons_name_list_line1=["generaladdButton","generalsubButton","generalmultiplyButton","generaldivisionButton",
        "generalsinButton","generalcosButton","generaltanButton","generalsinhButton","generalcoshButton","generaltanhButton",
        "generallogButton","generalinButton"]
        self.general_operators_buttons_name_list_line2=["generalpowerButton","generalrootButton","generaleButton","generalpiButton",
        "generalsininvButton","generalcosinvButton","generaltaninvButton","generalsinhinvButton","generalcoshinvButton",
        "generaltanhinvButton","generallogchooseButton","generalabsoluteButton"]
        self.general_operators_buttons_name_list_line1_icons=["icons/generaloperators/add.png","icons/generaloperators/subtract.png",
        "icons/generaloperators/multiply.png","icons/generaloperators/division.png","icons/generaloperators/sin().png",
        "icons/generaloperators/cos().png","icons/generaloperators/tan().png","icons/generaloperators/sinh().png",
        "icons/generaloperators/cosh().png","icons/generaloperators/tanh().png","icons/generaloperators/log().png",
        "icons/generaloperators/in().png"]
        self.general_operators_buttons_name_list_line2_icons=["icons/generaloperators/power.png","icons/generaloperators/root.png",
        "icons/generaloperators/e.png","icons/generaloperators/pi.png","icons/generaloperators/sin-1().png",
        "icons/generaloperators/cos-1().png","icons/generaloperators/tan-1().png","icons/generaloperators/sinh-1().png",
        "icons/generaloperators/cosh-1().png","icons/generaloperators/tanh-1().png","icons/generaloperators/log()().png",
        "icons/generaloperators/absolute.png"]
        self.general_operators_buttons_name_list_line1_methods=[self.general_add_button_clicked,self.general_sub_button_clicked,
        self.general_multiply_button_clicked,self.general_division_button_clicked,self.general_sin_button_clicked,
        self.general_cos_button_clicked,self.general_tan_button_clicked,self.general_sinh_button_clicked,self.general_cosh_button_clicked,
        self.general_tanh_button_clicked,self.general_log_button_clicked,self.general_in_button_clicked]
        self.general_operators_buttons_name_list_line2_methods=[self.general_power_button_clicked,self.general_root_button_clicked,
        self.general_e_button_clicked,self.general_pi_button_clicked,self.general_sin_inv_button_clicked,self.general_cos_inv_button_clicked,
        self.general_tan_inv_button_clicked,self.general_sinh_inv_button_clicked,self.general_cosh_inv_button_clicked,self.general_tanh_inv_button_clicked,
        self.general_log_choose_button_clicked,self.general_absolute_button_clicked]
        self.general_operators_buttons_dict={}
        general_operators_buttons_name_list_line1_position,general_operators_buttons_name_list_line1_counter=-40,-1
        for x in self.general_operators_buttons_name_list_line1:
            general_operators_buttons_name_list_line1_position+=40
            general_operators_buttons_name_list_line1_counter+=1
            self.general_operators_buttons_dict[x] = QtWidgets.QPushButton(self.general_operators_frame)
            self.general_operators_buttons_dict[x].setStyleSheet(vmtss.generaloperatorsButtons_stylesheet)
            self.general_operators_buttons_dict[x].setText("")
            self.general_operators_buttons_dict[x].setGeometry(QtCore.QRect(general_operators_buttons_name_list_line1_position, 0, 41, 31))
            icon= QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(self.general_operators_buttons_name_list_line1_icons[general_operators_buttons_name_list_line1_counter]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.general_operators_buttons_dict[x].setIcon(icon)
            self.general_operators_buttons_dict[x].setCheckable(False)
            self.general_operators_buttons_dict[x].clicked.connect(self.general_operators_buttons_name_list_line1_methods[general_operators_buttons_name_list_line1_counter])
            if x =="generaladdButton":
                self.general_operators_buttons_dict[x].setIconSize(QtCore.QSize(18, 18))
                self.general_operators_buttons_dict[x].setShortcut("+")
            elif x == "generalsubButton":
                self.general_operators_buttons_dict[x].setIconSize(QtCore.QSize(18, 18))
                self.general_operators_buttons_dict[x].setShortcut("-")
            elif x == "generalmultiplyButton":
                self.general_operators_buttons_dict[x].setIconSize(QtCore.QSize(18, 18))
                self.general_operators_buttons_dict[x].setShortcut("*")
            elif x =="generaldivisionButton":
                self.general_operators_buttons_dict[x].setIconSize(QtCore.QSize(18, 18))
                self.general_operators_buttons_dict[x].setShortcut("/")
            else:
                self.general_operators_buttons_dict[x].setIconSize(QtCore.QSize(35, 35))
        general_operators_buttons_name_list_line2_position,general_operators_buttons_name_list_line2_counter=-40,-1
        for x in self.general_operators_buttons_name_list_line2:
            general_operators_buttons_name_list_line2_position+=40
            general_operators_buttons_name_list_line2_counter+=1
            self.general_operators_buttons_dict[x] = QtWidgets.QPushButton(self.general_operators_frame)
            self.general_operators_buttons_dict[x].setStyleSheet(vmtss.generaloperatorsButtons_stylesheet)
            self.general_operators_buttons_dict[x].setText("")
            self.general_operators_buttons_dict[x].setGeometry(QtCore.QRect(general_operators_buttons_name_list_line2_position, 32, 41, 31))
            icon= QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(self.general_operators_buttons_name_list_line2_icons[general_operators_buttons_name_list_line2_counter]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.general_operators_buttons_dict[x].setIcon(icon)
            self.general_operators_buttons_dict[x].setCheckable(False)
            self.general_operators_buttons_dict[x].clicked.connect(self.general_operators_buttons_name_list_line2_methods[general_operators_buttons_name_list_line2_counter])
            if x =="generalabsoluteButton":
                self.general_operators_buttons_dict[x].setIconSize(QtCore.QSize(18, 18))
            elif x == "generaleButton" or x == "generalpiButton":
                self.general_operators_buttons_dict[x].setIconSize(QtCore.QSize(45, 45))
            else:
                self.general_operators_buttons_dict[x].setIconSize(QtCore.QSize(35, 35))
        ########################################
        ##DRAGGABLE VECTORS AND MATRICES LISTS##
        ########################################
        self.click_and_drag_label = QtWidgets.QLabel(self.mainwindow_central_widget)
        self.click_and_drag_label.setGeometry(QtCore.QRect(110, 419, 124, 21))
        self.click_and_drag_label.setStyleSheet(vmtss.click_and_drag_labelstylesheet)
        self.click_and_drag_label.setScaledContents(True)
        self.click_and_drag_label.setAlignment(QtCore.Qt.AlignCenter)
        self.click_and_drag_label.setScaledContents(True)
        self.click_and_drag_label.setText("CLICK OR DRAG")

        self.draggable_matrix_list_widget = QtWidgets.QListWidget(self.mainwindow_central_widget)
        self.draggable_matrix_list_widget.setGeometry(QtCore.QRect(110, 440, 123, 79))
        self.draggable_matrix_list_widget.setDragEnabled(True)
        self.draggable_matrix_list_widget.setDragDropOverwriteMode(True)
        self.draggable_matrix_list_widget.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.draggable_matrix_list_widget.itemDoubleClicked.connect(self.vector_and_matrix_list_widget_double_clicked)        
        for x in range(0,20):
            item = QtWidgets.QListWidgetItem()
            self.draggable_matrix_list_widget.addItem(item)
            item.setTextAlignment(QtCore.Qt.AlignCenter)

        self.draggable_vector_list_widget = QtWidgets.QListWidget(self.mainwindow_central_widget)
        self.draggable_vector_list_widget.setGeometry(QtCore.QRect(110, 440, 123, 79))
        self.draggable_vector_list_widget.setDragEnabled(True)
        self.draggable_vector_list_widget.setDragDropOverwriteMode(True)
        self.draggable_vector_list_widget.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.draggable_vector_list_widget.itemDoubleClicked.connect(self.vector_and_matrix_list_widget_double_clicked)
        for x in range(0,20):
            item = QtWidgets.QListWidgetItem()
            self.draggable_vector_list_widget.addItem(item)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
        ######################
        ##DEG AND RAD SLIDER##
        ######################
        self.deg_and_rad_vertical_slider = QtWidgets.QSlider(self.tab_buttons_frame)
        self.deg_and_rad_vertical_slider.setGeometry(QtCore.QRect(40, 410, 31, 35))
        self.deg_and_rad_vertical_slider.setStyleSheet(mvsfss.deg_and_rad_vertical_slider_stylesheet)
        self.deg_and_rad_vertical_slider.setMaximum(1)
        self.deg_and_rad_vertical_slider.setOrientation(QtCore.Qt.Vertical)
        self.deg_and_rad_vertical_slider.setInvertedAppearance(False)
        self.deg_and_rad_vertical_slider.valueChanged.connect(self.deg_and_rad_vertical_slider_value_changed)
        self.degree_label = QtWidgets.QLabel(self.tab_buttons_frame)
        self.degree_label.setGeometry(QtCore.QRect(20, 410, 31, 16))
        self.degree_label.setStyleSheet(mvsfss.degree_label_initial_stylesheet)
        self.degree_label.setText("DEG")
        self.rad_label = QtWidgets.QLabel(self.tab_buttons_frame)
        self.rad_label.setGeometry(QtCore.QRect(20, 430, 31, 16))
        self.rad_label.setStyleSheet(mvsfss.rad_label_initial_stylesheet)
        self.rad_label.setText("RAD")
        ##################
        ### ANGLES TAB ###
        ##################
        self.background_decorative_slide_label = QtWidgets.QLabel(self.mainwindow_central_widget)
        self.background_decorative_slide_label.setGeometry(QtCore.QRect(282, 100, 141, 71))
        self.background_decorative_slide_label.setStyleSheet(atss.background_decorative_slide_label_stylesheet)
        self.background_decorative_slide_label.setAlignment(QtCore.Qt.AlignCenter)
        self.choose_type_horizontal_slider = QtWidgets.QSlider(self.mainwindow_central_widget)
        self.choose_type_horizontal_slider.setGeometry(QtCore.QRect(322, 119, 61, 16))
        self.choose_type_horizontal_slider.setStyleSheet(atss.choose_type_horizontal_slider_stylesheet)
        self.choose_type_horizontal_slider.setMaximum(1)
        self.choose_type_horizontal_slider.setOrientation(QtCore.Qt.Horizontal)
        self.choose_type_horizontal_slider.setInvertedAppearance(False)
        self.choose_type_horizontal_slider.valueChanged.connect(self.choose_type_horizontal_slider_value_changed)
        self.vector_import_label = QtWidgets.QLabel(self.mainwindow_central_widget)
        self.vector_import_label.setGeometry(QtCore.QRect(306, 139, 51, 16))
        self.vector_import_label.setStyleSheet(atss.vector_import_label_stylesheet)
        self.vector_import_label.setAlignment(QtCore.Qt.AlignCenter)
        self.vector_write_label = QtWidgets.QLabel(self.mainwindow_central_widget)
        self.vector_write_label.setGeometry(QtCore.QRect(362, 139, 41, 16))
        self.vector_write_label.setStyleSheet(atss.vector_write_label_stylesheet)
        self.vector_write_label.setAlignment(QtCore.Qt.AlignCenter)
        self.choose_vector_frame = QtWidgets.QFrame(self.mainwindow_central_widget)
        self.choose_vector_frame.setGeometry(QtCore.QRect(90, 179, 501, 71))
        self.choose_vector_frame.setStyleSheet(atss.choose_vector_frame_stylesheet)
        self.choose_vector_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.choose_vector_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.choose_vector_combobox_x = QtWidgets.QComboBox(self.choose_vector_frame)
        self.choose_vector_combobox_x.setGeometry(QtCore.QRect(0, 20, 91, 21))
        self.choose_vector_combobox_x.setStyleSheet(atss.choose_vector_combobox_x_stylesheet)
        for x in range(0,20):
            self.choose_vector_combobox_x.addItem("")
        self.choose_vector_combobox_x.activated.connect(self.angles_vector_x_combobox_value_changed)
        self.choose_vector_combobox_y = QtWidgets.QComboBox(self.choose_vector_frame)
        self.choose_vector_combobox_y.setGeometry(QtCore.QRect(0, 50, 91, 21))
        self.choose_vector_combobox_y.setStyleSheet(atss.choose_vector_combobox_y_stylesheet)
        for x in range(0,20):
            self.choose_vector_combobox_y.addItem("")
        self.choose_vector_combobox_y.activated.connect(self.angles_vector_y_combobox_value_changed)
        self.values_chosen_x_label = QtWidgets.QLabel(self.choose_vector_frame)
        self.values_chosen_x_label.setGeometry(QtCore.QRect(90, 20, 412, 21))
        self.values_chosen_x_label.setStyleSheet(atss.values_chosen_x_label_stylesheet)
        self.values_chosen_x_label.setText("")
        self.values_chosen_y_label = QtWidgets.QLabel(self.choose_vector_frame)
        self.values_chosen_y_label.setGeometry(QtCore.QRect(90, 50, 412, 21))
        self.values_chosen_y_label.setStyleSheet(atss.values_chosen_y_label_stylesheet)
        self.values_chosen_y_label.setText("")
        self.values_chosen_y_label.raise_()
        self.values_chosen_x_label.raise_()
        self.choose_vector_combobox_x.raise_()
        self.choose_vector_combobox_y.raise_()
        self.angle_result_frame = QtWidgets.QFrame(self.mainwindow_central_widget)
        self.angle_result_frame.setGeometry(QtCore.QRect(90, 269, 524, 241))
        self.angle_result_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.angle_result_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.angle_calculate_button = QtWidgets.QPushButton(self.angle_result_frame)
        self.angle_calculate_button.setGeometry(QtCore.QRect(82, 40, 361, 31))
        self.angle_calculate_button.setStyleSheet(atss.angle_calculate_button_stylesheet)
        self.angle_calculate_button.setText("")
        angle_calculate_button_icon = QtGui.QIcon()
        angle_calculate_button_icon.addPixmap(QtGui.QPixmap("icons/Calculateicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.angle_calculate_button.setIcon(angle_calculate_button_icon)
        self.angle_calculate_button.setIconSize(QtCore.QSize(200, 200))
        self.angle_calculate_button.clicked.connect(self.angles_calculate_pushbutton_clicked)
        self.dd_or_dms_background_decorative_label = QtWidgets.QLabel(self.angle_result_frame)
        self.dd_or_dms_background_decorative_label.setGeometry(QtCore.QRect(-10, 0, 534, 21))
        self.dd_or_dms_background_decorative_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(17, 18, 17, 255), stop:1 rgba(22, 23, 22, 255));")
        self.dd_or_dms_background_decorative_label.setText("")
        self.dd_or_dms_horizontal_slider = QtWidgets.QSlider(self.angle_result_frame)
        self.dd_or_dms_horizontal_slider.setGeometry(QtCore.QRect(233, 2, 41, 16))
        self.dd_or_dms_horizontal_slider.setStyleSheet(atss.dd_or_dms_horizontal_slider_stylesheet)
        self.dd_or_dms_horizontal_slider.setMaximum(1)
        self.dd_or_dms_horizontal_slider.setOrientation(QtCore.Qt.Horizontal)
        self.dd_or_dms_horizontal_slider.setInvertedAppearance(False)
        self.dd_or_dms_horizontal_slider.valueChanged.connect(self.dd_or_dms_horizontal_slider_value_changed)
        self.degrees_minutes_seconds_label = QtWidgets.QLabel(self.angle_result_frame)
        self.degrees_minutes_seconds_label.setGeometry(QtCore.QRect(208, 3, 22, 16))
        self.degrees_minutes_seconds_label.setStyleSheet(atss.degrees_minutes_seconds_label_stylesheet)
        self.decimal_degree_label = QtWidgets.QLabel(self.angle_result_frame)
        self.decimal_degree_label.setGeometry(QtCore.QRect(275, 3, 21, 16))
        self.decimal_degree_label.setStyleSheet(atss.decimal_degree_label_stylesheet)

        self.angle_result_screen_scrollarea = QtWidgets.QScrollArea(self.angle_result_frame)
        self.angle_result_screen_scrollarea.setGeometry(QtCore.QRect(72, 90, 381, 141))
        self.angle_result_screen_scrollarea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.angle_result_screen_scrollarea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.angle_result_screen_scrollarea.setWidgetResizable(True)
        self.angle_result_screen_scroll_area_widgetcontents = QtWidgets.QWidget()
        self.angle_result_screen_scroll_area_widgetcontents.setGeometry(QtCore.QRect(0, 0, 379, 139))
        self.angle_result_screen_scroll_area_widgetcontents.setMinimumSize(0, 0)
        self.angle_result_screen_scroll_area_widgetcontents.setStyleSheet("background-color: rgb(17, 18, 17);\n")
        self.angle_result_screen_horizontal_gridlayout = QtWidgets.QHBoxLayout(self.angle_result_screen_scroll_area_widgetcontents)
        self.angle_result_screen_horizontal_gridlayout.setSpacing(0)
        self.angle_result_screen_scrollarea_label = QtWidgets.QLabel()
        self.angle_result_screen_scrollarea_label.setGeometry(QtCore.QRect(0, 0, 379, 139))
        self.angle_result_screen_scrollarea_label.setStyleSheet(atss.angle_result_screen_scrollarea_label_stylesheet)
        self.angle_result_screen_scrollarea_label.setText("")
        self.angle_result_screen_scrollarea_label.setTextFormat(QtCore.Qt.AutoText)
        self.angle_result_screen_scrollarea_label.setScaledContents(False)
        self.angle_result_screen_scrollarea_label.setWordWrap(False)

        self.angle_result_screen_horizontal_gridlayout.addWidget(self.angle_result_screen_scrollarea_label, 1, alignment=QtCore.Qt.AlignCenter)
        self.angle_result_screen_scrollarea.setWidget(self.angle_result_screen_scroll_area_widgetcontents)

        self.write_vector_frame = QtWidgets.QFrame(self.mainwindow_central_widget)
        self.write_vector_frame.setGeometry(QtCore.QRect(90, 179, 501, 71))
        self.write_vector_frame.setStyleSheet(atss.write_vector_frame_stylesheet)
        self.write_vector_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.write_vector_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.write_vector_label_x = QtWidgets.QLabel(self.write_vector_frame)
        self.write_vector_label_x.setGeometry(QtCore.QRect(0, 20, 91, 21))
        self.write_vector_label_x.setStyleSheet(atss.write_vector_label_x_stylesheet)
        self.write_vector_label_y = QtWidgets.QLabel(self.write_vector_frame)
        self.write_vector_label_y.setGeometry(QtCore.QRect(0, 50, 91, 21))
        self.write_vector_label_y.setStyleSheet(atss.write_vector_label_y_stylesheet)
        self.decorative_write_x_label = QtWidgets.QLabel(self.write_vector_frame)
        self.decorative_write_x_label.setGeometry(QtCore.QRect(90, 20, 412, 21))
        self.decorative_write_x_label.setStyleSheet(atss.decorative_write_x_label_stylesheet)
        self.decorative_write_y_label = QtWidgets.QLabel(self.write_vector_frame)
        self.decorative_write_y_label.setGeometry(QtCore.QRect(90, 50, 412, 21))
        self.decorative_write_y_label.setStyleSheet(atss.decorative_write_y_label_stylesheet)
        self.write_vector_horizontal_layout_widget_x = QtWidgets.QWidget(self.write_vector_frame)
        self.write_vector_horizontal_layout_widget_x.setGeometry(QtCore.QRect(90, 50, 371, 21))
        self.write_vector_horizontal_layout_x = QtWidgets.QHBoxLayout(self.write_vector_horizontal_layout_widget_x)
        self.write_vector_horizontal_layout_x.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.write_vector_horizontal_layout_x.setContentsMargins(0, 0, 0, 0)
        self.write_vector_horizontal_layout_widget_y = QtWidgets.QWidget(self.write_vector_frame)
        self.write_vector_horizontal_layout_widget_y.setGeometry(QtCore.QRect(90, 20, 371, 22))
        self.write_vector_horizontal_layout_y = QtWidgets.QHBoxLayout(self.write_vector_horizontal_layout_widget_y)
        self.write_vector_horizontal_layout_y.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.write_vector_horizontal_layout_y.setContentsMargins(0, 0, 0, 0)
        self.write_vector_column_combobox_x = QtWidgets.QComboBox(self.write_vector_frame)
        self.write_vector_column_combobox_x.setGeometry(QtCore.QRect(460, 20, 41, 21))
        self.write_vector_column_combobox_x.setStyleSheet(atss.write_vector_column_combobox_x_stylesheet)
        for x in range(0,12):
            self.write_vector_column_combobox_x.addItem("")
        self.write_vector_column_combobox_x.activated.connect(self.write_vector_column_combobox_x_value_changed)
        self.write_vector_column_combobox_y = QtWidgets.QComboBox(self.write_vector_frame)
        self.write_vector_column_combobox_y.setGeometry(QtCore.QRect(460, 50, 41, 21))
        self.write_vector_column_combobox_y.setStyleSheet(atss.write_vector_column_combobox_y_stylesheet)
        for x in range(0,12):
            self.write_vector_column_combobox_y.addItem("")
        self.write_vector_column_combobox_y.activated.connect(self.write_vector_column_combobox_y_value_changed)
        self.write_vector_column_combobox_y.setEnabled(False)
        self.write_vector_columns_label = QtWidgets.QLabel(self.write_vector_frame)
        self.write_vector_columns_label.setGeometry(QtCore.QRect(443, 4, 61, 16))
        self.write_vector_columns_label.setText("")
        self.write_vector_columns_label.setPixmap(QtGui.QPixmap("icons/createwindowicons/Columnsicon.png"))
        self.write_vector_columns_label.setScaledContents(True)

        ######################
        ## ANGLES TAB CELLS ##
        ######################

        self.reg_ex_cell = QtCore.QRegExp("(^-?[0-9]+/0*[1-9][0-9]*$|^[-+]?[0-9]+$|^[-+]?[0-9]+\.[0-9]+$)")
        write_vector_font = QtGui.QFont()
        write_vector_font.setFamily("Alice")
        write_vector_font.setPointSize(12)
        self.write_vector_x_lineedit_dict,self.write_vector_y_lineedit_dict = {},{}
        self.write_vector_x_lineedit_validator_dict,self.write_vector_y_lineedit_validatordict = {},{}
        write_vector_position=40
        for x in range(1,13):
            write_vector_position+=30
            self.write_vector_x_lineedit_dict["writevectorxlineEdit_"+str(x)] = QtWidgets.QLineEdit(self.write_vector_frame)
            self.write_vector_x_lineedit_dict["writevectorxlineEdit_"+str(x)].setGeometry(QtCore.QRect(write_vector_position, 20, 31, 20))
            self.write_vector_x_lineedit_dict["writevectorxlineEdit_"+str(x)].setFont(write_vector_font)
            self.write_vector_x_lineedit_dict["writevectorxlineEdit_"+str(x)].setStyleSheet(
                                                                                           "color: rgb(236, 236, 236);"
                                                                                           "border:1px;"
                                                                                           "border-style:solid;"
                                                                                           "border-color: rgb(15, 16, 15);"
                                                                                           "background-color: rgb(42, 43, 42);"
                                                                                           )
            self.write_vector_x_lineedit_dict["writevectorxlineEdit_"+str(x)].setAlignment(QtCore.Qt.AlignCenter)
            self.write_vector_x_lineedit_validator_dict["writevectorxlineEdit_"+str(x)+"_validator"]=QtGui.QRegExpValidator(self.reg_ex_cell, self.write_vector_x_lineedit_dict["writevectorxlineEdit_"+str(x)])
            self.write_vector_x_lineedit_dict["writevectorxlineEdit_"+str(x)].setValidator(self.write_vector_x_lineedit_validator_dict["writevectorxlineEdit_"+str(x)+"_validator"])
            self.write_vector_y_lineedit_dict["writevectorylineEdit_"+str(x)] = QtWidgets.QLineEdit(self.write_vector_frame)
            self.write_vector_y_lineedit_dict["writevectorylineEdit_"+str(x)].setGeometry(QtCore.QRect(write_vector_position, 50, 31, 20))
            self.write_vector_y_lineedit_dict["writevectorylineEdit_"+str(x)].setFont(write_vector_font)
            self.write_vector_y_lineedit_dict["writevectorylineEdit_"+str(x)].setStyleSheet(
                                                                                           "color: rgb(236, 236, 236);"
                                                                                           "border:1px;"
                                                                                           "border-style:solid;"
                                                                                           "border-color: rgb(15, 16, 15);"
                                                                                           "background-color: rgb(42, 43, 42);"
                                                                                           ) 
            self.write_vector_y_lineedit_dict["writevectorylineEdit_"+str(x)].setAlignment(QtCore.Qt.AlignCenter)
            self.write_vector_y_lineedit_validatordict["writevectorylineEdit_"+str(x)+"_validator"]=QtGui.QRegExpValidator(self.reg_ex_cell, self.write_vector_y_lineedit_dict["writevectorylineEdit_"+str(x)])
            self.write_vector_y_lineedit_dict["writevectorylineEdit_"+str(x)].setValidator(self.write_vector_y_lineedit_validatordict["writevectorylineEdit_"+str(x)+"_validator"])
        
        #####################
        ## EIGENVALUES TAB ##
        #####################

        self.eigenvalues_frame = QtWidgets.QFrame(self.mainwindow_central_widget)
        self.eigenvalues_frame.setGeometry(QtCore.QRect(95, 109, 511, 411))
        self.eigenvalues_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.eigenvalues_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.eigenvalues_choose_matrix_list_widget = QtWidgets.QListWidget(self.eigenvalues_frame)
        self.eigenvalues_choose_matrix_list_widget.setGeometry(QtCore.QRect(20, 10, 469, 31))
        self.eigenvalues_choose_matrix_list_widget.setDragEnabled(False)
        self.eigenvalues_choose_matrix_list_widget.setDragDropOverwriteMode(True)
        self.eigenvalues_choose_matrix_list_widget.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.eigenvalues_choose_matrix_list_widget.setFlow(QtWidgets.QListView.LeftToRight)
        self.eigenvalues_choose_matrix_list_widget.setUniformItemSizes(True)
        self.eigenvalues_choose_matrix_list_widget.setItemAlignment(QtCore.Qt.AlignCenter)
        for x in range(0,20):
            item = QtWidgets.QListWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.eigenvalues_choose_matrix_list_widget.addItem(item)
        self.eigenvalues_choose_matrix_list_widget.setSpacing(4)
        self.eigenvalues_choose_matrix_list_widget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.eigenvalues_choose_matrix_list_widget.currentItemChanged.connect(self.eigenvalues_choose_matrix_list_widget_item_changed)
        self.eigenvalues_calculate_pushbutton = QtWidgets.QPushButton(self.eigenvalues_frame)
        self.eigenvalues_calculate_pushbutton.setGeometry(QtCore.QRect(80, 214, 361, 31))
        self.eigenvalues_calculate_pushbutton.setStyleSheet(evtss.eigenvalues_calculate_pushbutton_stylesheet)
        self.eigenvalues_calculate_pushbutton.setText("")
        eigenvalues_calculate_pushbutton_icon = QtGui.QIcon()
        eigenvalues_calculate_pushbutton_icon.addPixmap(QtGui.QPixmap("icons/Calculateicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.eigenvalues_calculate_pushbutton.setIcon(eigenvalues_calculate_pushbutton_icon)
        self.eigenvalues_calculate_pushbutton.setIconSize(QtCore.QSize(200, 200))
        self.eigenvalues_calculate_pushbutton.clicked.connect(self.eigenvalues_calculate_pushbutton_clicked)

        #########################################
        ##EIGENVALUES CHOSEN MATRIX SCROLL AREA##
        #########################################

        self.eigenvalues_chosen_matrix_screen_scrollarea = QtWidgets.QScrollArea(self.eigenvalues_frame)
        self.eigenvalues_chosen_matrix_screen_scrollarea.setGeometry(QtCore.QRect(80, 50, 361, 151))
        self.eigenvalues_chosen_matrix_screen_scrollarea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.eigenvalues_chosen_matrix_screen_scrollarea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.eigenvalues_chosen_matrix_screen_scrollarea.setWidgetResizable(True)

        self.eigenvalues_chosen_matrixscreen_scrollarea_widget_contents = QtWidgets.QWidget()
        self.eigenvalues_chosen_matrixscreen_scrollarea_widget_contents.setGeometry(QtCore.QRect(0, 0, 359, 149))
        self.eigenvalues_chosen_matrixscreen_scrollarea_widget_contents.setMinimumSize(0, 0)
        self.eigenvalues_chosen_matrixscreen_scrollarea_widget_contents.setStyleSheet("background-color: rgb(17, 18, 17);\n")
        self.eigenvalues_chosen_matrix_screen_gridlayout = QtWidgets.QHBoxLayout(self.eigenvalues_chosen_matrixscreen_scrollarea_widget_contents)
        self.eigenvalues_chosen_matrix_screen_gridlayout.setSpacing(0)

        self.eigenvalues_chosen_matrix_screen_matrix_gridlayout_widget = QtWidgets.QWidget()
        self.eigenvalues_chosen_matrix_screen_matrix_gridlayout = QtWidgets.QHBoxLayout(self.eigenvalues_chosen_matrix_screen_matrix_gridlayout_widget)
        self.eigenvalues_chosen_matrix_screen_matrix_gridlayout.setSpacing(5)

        #####################################################
        ##EIGENVALUES CHOSEN MATRIX SCROLL AREA VALUES GRID##
        #####################################################

        self.eigenvalues_chosen_matrix_parentesis_open_label = QtWidgets.QLabel()
        self.eigenvalues_chosen_matrix_parentesis_open_label.setPixmap(QtGui.QPixmap("icons/Itemparentesisopen.png"))
        self.eigenvalues_chosen_matrix_parentesis_open_label.setScaledContents(True)
        self.eigenvalues_chosen_matrix_parentesis_open_label.setFixedWidth(5)
        self.eigenvalues_chosen_matrix_parentesis_closed_label = QtWidgets.QLabel()
        self.eigenvalues_chosen_matrix_parentesis_closed_label.setPixmap(QtGui.QPixmap("icons/Itemparentesisclose.png"))
        self.eigenvalues_chosen_matrix_parentesis_closed_label.setScaledContents(True)
        self.eigenvalues_chosen_matrix_parentesis_closed_label.setFixedWidth(5)

        self.eigenvalues_chosen_matrix_screen_values_gridlayout_widget = QtWidgets.QWidget()
        self.eigenvalues_chosen_matrix_screen_values_gridlayout = QtWidgets.QGridLayout(self.eigenvalues_chosen_matrix_screen_values_gridlayout_widget)
        self.eigenvalues_chosen_matrix_screen_values_gridlayout.setContentsMargins(0, 0, 0, 0)
        self.eigenvalues_chosen_matrix_screen_values_gridlayout.setHorizontalSpacing(20)
        self.eigenvalues_chosen_matrix_screen_values_gridlayout.setVerticalSpacing(5)

        self.eigenvalues_chosen_matrix_screen_gridlayout.addWidget(self.eigenvalues_chosen_matrix_screen_matrix_gridlayout_widget, 1, alignment=QtCore.Qt.AlignCenter)

        self.eigenvalues_chosen_matrix_screen_matrix_gridlayout.addWidget(self.eigenvalues_chosen_matrix_parentesis_open_label, 0, alignment=QtCore.Qt.AlignLeft)
        self.eigenvalues_chosen_matrix_screen_matrix_gridlayout.addWidget(self.eigenvalues_chosen_matrix_screen_values_gridlayout_widget, 1, alignment=QtCore.Qt.AlignCenter)
        self.eigenvalues_chosen_matrix_screen_matrix_gridlayout.addWidget(self.eigenvalues_chosen_matrix_parentesis_closed_label, 2, alignment=QtCore.Qt.AlignLeft)

        self.eigenvalues_chosen_matrix_screen_scrollarea.setWidget(self.eigenvalues_chosen_matrixscreen_scrollarea_widget_contents)

        self.eigenvalues_chosen_matrix_parentesis_open_label.setHidden(True)
        self.eigenvalues_chosen_matrix_parentesis_closed_label.setHidden(True)

        #########################################################
        ## EIGENVALUES CHOSEN MATRIX SCROLL AREA VALUES LABELS ##
        #########################################################
        eigen_font = QtGui.QFont()
        eigen_font.setFamily("Alice")
        eigen_font.setPointSize(12)
        eigen_chosen_stylesheet = "background-color: transparent;\n""color: rgb(236, 236, 236);\n"

        self.eigenchosen_matrix_label_cell_dict={}
        for x, y in itools.product(range(1,11), range(1,11)):
            self.eigenchosen_matrix_label_cell_dict["eigenchosen_matrixlabelcell"+str(x)+"_"+str(y)] = QtWidgets.QLabel(self.eigenvalues_chosen_matrix_screen_values_gridlayout_widget)
            self.eigenchosen_matrix_label_cell_dict["eigenchosen_matrixlabelcell"+str(x)+"_"+str(y)].setStyleSheet(eigen_chosen_stylesheet)
            self.eigenchosen_matrix_label_cell_dict["eigenchosen_matrixlabelcell"+str(x)+"_"+str(y)].setFont(eigen_font)
            self.eigenvalues_chosen_matrix_screen_values_gridlayout.addWidget(self.eigenchosen_matrix_label_cell_dict["eigenchosen_matrixlabelcell"+str(x)+"_"+str(y)], (x-1), (y-1), 1, 1, alignment=QtCore.Qt.AlignCenter)
            self.eigenchosen_matrix_label_cell_dict["eigenchosen_matrixlabelcell"+str(x)+"_"+str(y)].setHidden(True)

        ##################################
        ##EIGENVALUES RESULT SCROLL AREA##
        ##################################
        self.eigenvalues_result_screen_scrollarea = QtWidgets.QScrollArea(self.eigenvalues_frame)
        self.eigenvalues_result_screen_scrollarea.setGeometry(QtCore.QRect(80, 257, 361, 151))
        self.eigenvalues_result_screen_scrollarea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.eigenvalues_result_screen_scrollarea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.eigenvalues_result_screen_scrollarea.setWidgetResizable(True)

        self.eigenvalues_result_screen_scrollarea_widget_contents = QtWidgets.QWidget()
        self.eigenvalues_result_screen_scrollarea_widget_contents.setGeometry(QtCore.QRect(0, 0, 359, 149))
        self.eigenvalues_result_screen_scrollarea_widget_contents.setMinimumSize(0, 0)
        self.eigenvalues_result_screen_scrollarea_widget_contents.setStyleSheet("background-color: rgb(17, 18, 17);\n")
        self.eigenvalues_result_horizontal_gridlayout = QtWidgets.QHBoxLayout(self.eigenvalues_result_screen_scrollarea_widget_contents)
        self.eigenvalues_result_horizontal_gridlayout.setSpacing(0)

        self.eigenvalues_result_gridlayout_widget = QtWidgets.QWidget()
        self.eigenvalues_result_gridlayout_widget.setGeometry(QtCore.QRect(-1, -1, 361, 151))

        self.eigenvalues_result_gridlayout = QtWidgets.QGridLayout(self.eigenvalues_result_gridlayout_widget)
        self.eigenvalues_result_gridlayout.setContentsMargins(0, 0, 0, 0)
        self.eigenvalues_result_gridlayout.setSpacing(25)
        self.eigenvectors_label_dict,self.eigenvalue_label_dict,self.eigenvalue_multiplicity_label_dict={},{},{}
        for x in range(1,11):
            self.eigenvectors_label_dict["eigenvectorsLabel_"+str(x)] = QtWidgets.QLabel(self.eigenvalues_result_gridlayout_widget)
            self.eigenvectors_label_dict["eigenvectorsLabel_"+str(x)].setStyleSheet("")
            self.eigenvectors_label_dict["eigenvectorsLabel_"+str(x)].setText("")
            self.eigenvalues_result_gridlayout.addWidget(self.eigenvectors_label_dict["eigenvectorsLabel_"+str(x)], 4, (x+9), 1, 1)

            self.eigenvalue_multiplicity_label_dict["eigenvaluemultiplicityLabel_"+str(x)] = QtWidgets.QLabel(self.eigenvalues_result_gridlayout_widget)
            self.eigenvalue_multiplicity_label_dict["eigenvaluemultiplicityLabel_"+str(x)].setStyleSheet("border-bottom:2px dotted rgb(126, 126, 126);")
            self.eigenvalue_multiplicity_label_dict["eigenvaluemultiplicityLabel_"+str(x)].setText("")
            self.eigenvalues_result_gridlayout.addWidget(self.eigenvalue_multiplicity_label_dict["eigenvaluemultiplicityLabel_"+str(x)], 3, (x+9), 1, 1)

            self.eigenvalue_label_dict["eigenvalueLabel_"+str(x)] = QtWidgets.QLabel(self.eigenvalues_result_gridlayout_widget)
            self.eigenvalue_label_dict["eigenvalueLabel_"+str(x)].setStyleSheet("border-bottom:2px dotted rgb(126, 126, 126);")
            self.eigenvalue_label_dict["eigenvalueLabel_"+str(x)].setText("")
            self.eigenvalues_result_gridlayout.addWidget(self.eigenvalue_label_dict["eigenvalueLabel_"+str(x)], 0, (x+9), 1, 1)

        self.eigenvalues_result_horizontal_gridlayout.addWidget(self.eigenvalues_result_gridlayout_widget, 1, alignment=QtCore.Qt.AlignCenter)

        self.eigenvalues_result_screen_scrollarea.setWidget(self.eigenvalues_result_screen_scrollarea_widget_contents)

        for x in range(0, 10):
            self.eigenvectors_label_dict["eigenvectorsLabel_"+str(x+1)].setHidden(True)
            self.eigenvalue_multiplicity_label_dict["eigenvaluemultiplicityLabel_"+str(x+1)].setHidden(True)
            self.eigenvalue_label_dict["eigenvalueLabel_"+str(x+1)].setHidden(True)

            self.eigenvalue_label_dict["eigenvalueLabel_"+str(x+1)].setAlignment(QtCore.Qt.AlignCenter)
            self.eigenvalue_label_dict["eigenvalueLabel_"+str(x+1)].setStyleSheet(evtss.eigenvaluelabel_stylesheet)

            self.eigenvalue_multiplicity_label_dict["eigenvaluemultiplicityLabel_"+str(x+1)].setAlignment(QtCore.Qt.AlignCenter)
            self.eigenvalue_multiplicity_label_dict["eigenvaluemultiplicityLabel_"+str(x+1)].setStyleSheet(evtss.eigenvaluemultiplicitylabel_stylesheet)

            self.eigenvectors_label_dict["eigenvectorsLabel_"+str(x+1)].setAlignment(QtCore.Qt.AlignCenter)
            self.eigenvectors_label_dict["eigenvectorsLabel_"+str(x+1)].setStyleSheet(evtss.eigenvectorslabel_stylesheet)


        ##########################
        ###SYSTEMS OF EQUATIONS###
        ##########################

        self.system_of_equations_frame = QtWidgets.QFrame(self.mainwindow_central_widget)
        self.system_of_equations_frame.setGeometry(QtCore.QRect(85, 109, 511, 411))
        self.system_of_equations_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.system_of_equations_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.system_of_equations_choose_matrix_listwidget = QtWidgets.QListWidget(self.system_of_equations_frame)
        self.system_of_equations_choose_matrix_listwidget.setGeometry(QtCore.QRect(20, 10, 211, 31))
        
        self.system_of_equations_choose_matrix_listwidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.system_of_equations_choose_matrix_listwidget.setDragEnabled(True)
        self.system_of_equations_choose_matrix_listwidget.setDragDropOverwriteMode(True)
        self.system_of_equations_choose_matrix_listwidget.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.system_of_equations_choose_matrix_listwidget.setFlow(QtWidgets.QListView.LeftToRight)
        self.system_of_equations_choose_matrix_listwidget.setUniformItemSizes(True)
        self.system_of_equations_choose_matrix_listwidget.setItemAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop|QtCore.Qt.AlignVCenter)
        for x in range(0,20):
            item = QtWidgets.QListWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.system_of_equations_choose_matrix_listwidget.addItem(item)
        self.system_of_equations_choose_matrix_listwidget.setSpacing(4)
        self.system_of_equations_choose_matrix_listwidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.system_of_equations_choose_matrix_listwidget.currentItemChanged.connect(self.system_of_equations_choose_matrix_list_widget_item_changed)
        self.system_of_equations_choose_matrix_scrollarea = QtWidgets.QScrollArea(self.system_of_equations_frame)
        self.system_of_equations_choose_matrix_scrollarea.setGeometry(QtCore.QRect(20, 50, 211, 151))
        self.system_of_equations_choose_matrix_scrollarea.setStyleSheet(soetss.system_of_equations_choose_matrix_scrollarea_stylesheet)
        self.system_of_equations_choose_matrix_scrollarea.setWidgetResizable(True)
        self.system_of_equations_choose_matrix_scrollarea_widget_contents = QtWidgets.QWidget()
        self.system_of_equations_choose_matrix_scrollarea_widget_contents.setGeometry(QtCore.QRect(0, 0, 209, 149))
        self.system_of_equations_choose_matrix_scrollarea_widget_contents.setMinimumSize(0, 0)
        self.system_of_equations_choose_matrix_scrollarea_widget_contents.setStyleSheet(soetss.system_of_equations_choose_matrix_scrollarea_widget_contents_stylesheet)
        self.system_of_equations_choose_matrix_screen_gridlayout = QtWidgets.QHBoxLayout(self.system_of_equations_choose_matrix_scrollarea_widget_contents)
        self.system_of_equations_choose_matrix_screen_gridlayout.setSpacing(0)

        self.system_of_equations_choose_matrix_screen_matrix_gridlayout_widget = QtWidgets.QWidget()
        self.system_of_equations_choose_matrix_screen_matrix_gridlayout = QtWidgets.QHBoxLayout(self.system_of_equations_choose_matrix_screen_matrix_gridlayout_widget)
        self.system_of_equations_choose_matrix_screen_matrix_gridlayout.setSpacing(5)

        ###############################################
        ##SYSTEM OF EQ MATRIX SCROLL AREA VALUES GRID##
        ###############################################

        self.system_of_equations_choose_matrix_parentesis_open_label = QtWidgets.QLabel()
        self.system_of_equations_choose_matrix_parentesis_open_label.setPixmap(QtGui.QPixmap("icons/Itemparentesisopen.png"))
        self.system_of_equations_choose_matrix_parentesis_open_label.setScaledContents(True)
        self.system_of_equations_choose_matrix_parentesis_open_label.setFixedWidth(5)
        self.system_of_equations_choose_matrix_parentesis_closed_label = QtWidgets.QLabel()
        self.system_of_equations_choose_matrix_parentesis_closed_label.setPixmap(QtGui.QPixmap("icons/Itemparentesisclose.png"))
        self.system_of_equations_choose_matrix_parentesis_closed_label.setScaledContents(True)
        self.system_of_equations_choose_matrix_parentesis_closed_label.setFixedWidth(5)

        self.system_of_equations_choose_matrix_screen_values_gridlayout_widget = QtWidgets.QWidget()
        self.system_of_equations_choose_matrix_screen_values_gridlayout = QtWidgets.QGridLayout(self.system_of_equations_choose_matrix_screen_values_gridlayout_widget)
        self.system_of_equations_choose_matrix_screen_values_gridlayout.setContentsMargins(0, 0, 0, 0)
        self.system_of_equations_choose_matrix_screen_values_gridlayout.setHorizontalSpacing(20)
        self.system_of_equations_choose_matrix_screen_values_gridlayout.setVerticalSpacing(5)

        self.system_of_equations_choose_matrix_screen_gridlayout.addWidget(self.system_of_equations_choose_matrix_screen_matrix_gridlayout_widget, 1, alignment=QtCore.Qt.AlignCenter)

        self.system_of_equations_choose_matrix_screen_matrix_gridlayout.addWidget(self.system_of_equations_choose_matrix_parentesis_open_label, 0, alignment=QtCore.Qt.AlignLeft)
        self.system_of_equations_choose_matrix_screen_matrix_gridlayout.addWidget(self.system_of_equations_choose_matrix_screen_values_gridlayout_widget, 1, alignment=QtCore.Qt.AlignCenter)
        self.system_of_equations_choose_matrix_screen_matrix_gridlayout.addWidget(self.system_of_equations_choose_matrix_parentesis_closed_label, 2, alignment=QtCore.Qt.AlignLeft)

        self.system_of_equations_choose_matrix_scrollarea.setWidget(self.system_of_equations_choose_matrix_scrollarea_widget_contents)

        self.system_of_equations_choose_matrix_parentesis_open_label.setHidden(True)
        self.system_of_equations_choose_matrix_parentesis_closed_label.setHidden(True)

        #########################################################
        ## EIGENVALUES CHOSEN MATRIX SCROLL AREA VALUES LABELS ##
        #########################################################
        system_font = QtGui.QFont()
        system_font.setFamily("Alice")
        system_font.setPointSize(12)

        system_matrix_chosen_stylesheet = "background-color: transparent;\n""color: rgb(236, 236, 236);\n"
        self.system_matrix_chosen_matrix_label_cell_dict={}
        for x, y in itools.product(range(1,11), range(1,11)):
            self.system_matrix_chosen_matrix_label_cell_dict["systemmatrixchosen_matrixlabelcell"+str(x)+"_"+str(y)] = QtWidgets.QLabel(self.system_of_equations_choose_matrix_screen_values_gridlayout_widget)
            self.system_matrix_chosen_matrix_label_cell_dict["systemmatrixchosen_matrixlabelcell"+str(x)+"_"+str(y)].setStyleSheet(system_matrix_chosen_stylesheet)
            self.system_matrix_chosen_matrix_label_cell_dict["systemmatrixchosen_matrixlabelcell"+str(x)+"_"+str(y)].setFont(system_font)
            self.system_of_equations_choose_matrix_screen_values_gridlayout.addWidget(self.system_matrix_chosen_matrix_label_cell_dict["systemmatrixchosen_matrixlabelcell"+str(x)+"_"+str(y)], (x-1), (y-1), 1, 1, alignment=QtCore.Qt.AlignCenter)
            self.system_matrix_chosen_matrix_label_cell_dict["systemmatrixchosen_matrixlabelcell"+str(x)+"_"+str(y)].setHidden(True)

        self.system_of_equations_result_scrollarea = QtWidgets.QScrollArea(self.system_of_equations_frame)
        self.system_of_equations_result_scrollarea.setGeometry(QtCore.QRect(80, 250, 361, 151))
        self.system_of_equations_result_scrollarea.setStyleSheet(soetss.system_of_equations_result_scrollarea_stylesheet)
        self.system_of_equations_result_scrollarea.setWidgetResizable(True)
        self.system_of_equations_result_scrollarea_widget_contents = QtWidgets.QWidget()
        self.system_of_equations_result_scrollarea_widget_contents.setGeometry(QtCore.QRect(0, 0, 359, 149))
        self.system_of_equations_result_scrollarea_widget_contents.setStyleSheet(soetss.system_of_equations_result_scrollarea_widget_contents_stylesheet)
        self.system_of_equations_result_scrollarea_horizontal_gridlayout = QtWidgets.QHBoxLayout(self.system_of_equations_result_scrollarea_widget_contents)
        self.system_of_equations_result_scrollarea_horizontal_gridlayout.setSpacing(0)

        self.system_of_equations_result_scrollarea_result_label = QtWidgets.QLabel()
        self.system_of_equations_result_scrollarea_result_label.setGeometry(QtCore.QRect(0, 0, 359, 149))
        self.system_of_equations_result_scrollarea_result_label.setStyleSheet(soetss.system_of_equations_result_scrollarea_result_label_stylesheet)
        self.system_of_equations_result_scrollarea_result_label.setText("")
        self.system_of_equations_result_scrollarea_result_label.setTextFormat(QtCore.Qt.AutoText)
        self.system_of_equations_result_scrollarea_result_label.setScaledContents(False)
        self.system_of_equations_result_scrollarea_result_label.setWordWrap(False)

        self.system_of_equations_result_scrollarea_horizontal_gridlayout.addWidget(self.system_of_equations_result_scrollarea_result_label, 1, alignment=QtCore.Qt.AlignCenter)
        self.system_of_equations_result_scrollarea.setWidget(self.system_of_equations_result_scrollarea_widget_contents)

        self.system_of_equations_calculate_pushbutton = QtWidgets.QPushButton(self.system_of_equations_frame)
        self.system_of_equations_calculate_pushbutton.setGeometry(QtCore.QRect(80, 215, 361, 23))
        self.system_of_equations_calculate_pushbutton.setStyleSheet(soetss.system_of_equations_calculate_pushbutton_stylesheet)
        self.system_of_equations_calculate_pushbutton.setText("")
        system_of_equations_calculate_pushbutton_icon = QtGui.QIcon()
        system_of_equations_calculate_pushbutton_icon.addPixmap(QtGui.QPixmap("icons/Calculateicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.system_of_equations_calculate_pushbutton.setIcon(system_of_equations_calculate_pushbutton_icon)
        self.system_of_equations_calculate_pushbutton.setIconSize(QtCore.QSize(200, 200))
        self.system_of_equations_calculate_pushbutton.clicked.connect(self.system_of_equations_calculate_pushbutton_clicked)
        self.system_of_equations_choosevector_list_widget = QtWidgets.QListWidget(self.system_of_equations_frame)
        self.system_of_equations_choosevector_list_widget.setGeometry(QtCore.QRect(430, 10, 81, 31))
        
        self.system_of_equations_choosevector_list_widget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.system_of_equations_choosevector_list_widget.setDragEnabled(True)
        self.system_of_equations_choosevector_list_widget.setDragDropOverwriteMode(True)
        self.system_of_equations_choosevector_list_widget.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.system_of_equations_choosevector_list_widget.setFlow(QtWidgets.QListView.LeftToRight)
        self.system_of_equations_choosevector_list_widget.setUniformItemSizes(True)
        self.system_of_equations_choosevector_list_widget.setItemAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop|QtCore.Qt.AlignVCenter)
        for x in range(0,20):
            item = QtWidgets.QListWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.system_of_equations_choosevector_list_widget.addItem(item)
        self.system_of_equations_choosevector_list_widget.setSpacing(4)
        self.system_of_equations_choosevector_list_widget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.system_of_equations_choosevector_list_widget.currentItemChanged.connect(self.system_of_equations_choose_vector_list_widget_item_changed)

        self.system_of_equations_choose_vector_scrollarea = QtWidgets.QScrollArea(self.system_of_equations_frame)
        self.system_of_equations_choose_vector_scrollarea.setGeometry(QtCore.QRect(430, 50, 81, 151))
        self.system_of_equations_choose_vector_scrollarea.setStyleSheet(soetss.system_of_equations_choose_vector_scrollarea_stylesheet)
        self.system_of_equations_choose_vector_scrollarea.setWidgetResizable(True)
        self.system_of_equations_choose_vector_scrollarea_widget_contents = QtWidgets.QWidget()
        self.system_of_equations_choose_vector_scrollarea_widget_contents.setGeometry(QtCore.QRect(0, 0, 79, 149))
        self.system_of_equations_choose_vector_scrollarea_widget_contents.setStyleSheet(soetss.system_of_equations_choose_vector_scrollarea_widget_contents_stylesheet)

        self.system_of_equations_choose_vector_screen_gridlayout = QtWidgets.QHBoxLayout(self.system_of_equations_choose_vector_scrollarea_widget_contents)
        self.system_of_equations_choose_vector_screen_gridlayout.setSpacing(0)

        self.system_of_equations_choose_vector_screen_vector_gridlayout_widget = QtWidgets.QWidget()
        self.system_of_equations_choose_vector_screen_vector_gridlayout = QtWidgets.QHBoxLayout(self.system_of_equations_choose_vector_screen_vector_gridlayout_widget)
        self.system_of_equations_choose_vector_screen_vector_gridlayout.setSpacing(5)

        ###############################################
        ##SYSTEM OF EQ VECTOR SCROLL AREA VALUES GRID##
        ###############################################

        self.system_of_equations_choose_vector_parentesis_open_label = QtWidgets.QLabel()
        self.system_of_equations_choose_vector_parentesis_open_label.setPixmap(QtGui.QPixmap("icons/Itemparentesisopen.png"))
        self.system_of_equations_choose_vector_parentesis_open_label.setScaledContents(True)
        self.system_of_equations_choose_vector_parentesis_open_label.setFixedWidth(5)
        self.system_of_equations_choose_vector_parentesis_closed_label = QtWidgets.QLabel()
        self.system_of_equations_choose_vector_parentesis_closed_label.setPixmap(QtGui.QPixmap("icons/Itemparentesisclose.png"))
        self.system_of_equations_choose_vector_parentesis_closed_label.setScaledContents(True)
        self.system_of_equations_choose_vector_parentesis_closed_label.setFixedWidth(5)

        self.system_of_equations_choose_vector_screen_values_gridlayout_widget = QtWidgets.QWidget()
        self.system_of_equations_choose_vector_screen_values_gridlayout = QtWidgets.QGridLayout(self.system_of_equations_choose_vector_screen_values_gridlayout_widget)
        self.system_of_equations_choose_vector_screen_values_gridlayout.setContentsMargins(0, 0, 0, 0)
        self.system_of_equations_choose_vector_screen_values_gridlayout.setHorizontalSpacing(20)
        self.system_of_equations_choose_vector_screen_values_gridlayout.setVerticalSpacing(5)

        self.system_of_equations_choose_vector_screen_gridlayout.addWidget(self.system_of_equations_choose_vector_screen_vector_gridlayout_widget, 1, alignment=QtCore.Qt.AlignCenter)

        self.system_of_equations_choose_vector_screen_vector_gridlayout.addWidget(self.system_of_equations_choose_vector_parentesis_open_label, 0, alignment=QtCore.Qt.AlignLeft)
        self.system_of_equations_choose_vector_screen_vector_gridlayout.addWidget(self.system_of_equations_choose_vector_screen_values_gridlayout_widget, 1, alignment=QtCore.Qt.AlignCenter)
        self.system_of_equations_choose_vector_screen_vector_gridlayout.addWidget(self.system_of_equations_choose_vector_parentesis_closed_label, 2, alignment=QtCore.Qt.AlignLeft)

        self.system_of_equations_choose_vector_scrollarea.setWidget(self.system_of_equations_choose_vector_scrollarea_widget_contents)

        self.system_of_equations_choose_vector_parentesis_open_label.setHidden(True)
        self.system_of_equations_choose_vector_parentesis_closed_label.setHidden(True)

        #########################################################
        ## EIGENVALUES CHOSEN VECTOR SCROLL AREA VALUES LABELS ##
        #########################################################
        system_font = QtGui.QFont()
        system_font.setFamily("Alice")
        system_font.setPointSize(12)

        system_vector_chosen_stylesheet = "background-color: transparent;\n""color: rgb(236, 236, 236);\n"
        self.system_vector_chosen_vector_label_cell_dict={}
        for x in range(1,11):
            self.system_vector_chosen_vector_label_cell_dict["systemvectorchosen_vectorlabelcell"+str(x)+"_1"] = QtWidgets.QLabel(self.system_of_equations_choose_vector_screen_values_gridlayout_widget)
            self.system_vector_chosen_vector_label_cell_dict["systemvectorchosen_vectorlabelcell"+str(x)+"_1"].setStyleSheet(system_vector_chosen_stylesheet)
            self.system_vector_chosen_vector_label_cell_dict["systemvectorchosen_vectorlabelcell"+str(x)+"_1"].setFont(system_font)
            self.system_of_equations_choose_vector_screen_values_gridlayout.addWidget(self.system_vector_chosen_vector_label_cell_dict["systemvectorchosen_vectorlabelcell"+str(x)+"_1"], (x-1), 0, 1, 1, alignment=QtCore.Qt.AlignCenter)
            self.system_vector_chosen_vector_label_cell_dict["systemvectorchosen_vectorlabelcell"+str(x)+"_1"].setHidden(True)
        self.system_of_equations_decorative_background_label = QtWidgets.QLabel(self.system_of_equations_frame)
        self.system_of_equations_decorative_background_label.setGeometry(QtCore.QRect(229, 50, 203, 151))
        self.system_of_equations_decorative_background_label.setStyleSheet(soetss.system_of_equations_decorative_background_label_stylesheet)
        self.system_of_equations_decorative_background_label.setText("")
        self.system_of_equations_decorative_label = QtWidgets.QLabel(self.system_of_equations_frame)
        self.system_of_equations_decorative_label.setGeometry(QtCore.QRect(252, 55, 161, 141))
        self.system_of_equations_decorative_label.setStyleSheet("background-color: transparent;")
        self.system_of_equations_decorative_label.setText("")
        self.system_of_equations_decorative_label.setPixmap(QtGui.QPixmap("icons/Decorativesystemofequationsicon.png"))
        ###############
        ###Title bar###
        ###############
        self.title_bar_frame = QtWidgets.QFrame(self.mainwindow_central_widget)
        self.title_bar_frame.setGeometry(QtCore.QRect(0, 0, 704, 29))
        self.title_bar_frame.setStyleSheet("background-color: rgb(17, 18, 17);")
        self.title_bar_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_bar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.exit_button = QtWidgets.QPushButton(self.mainwindow_central_widget)
        self.exit_button.setGeometry(QtCore.QRect(653, 0, 51, 29))
        self.exit_button.setStyleSheet(
                                      "QPushButton {\n"
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
                                      )
        self.exit_button.setText("")
        exit_button_icon = QtGui.QIcon()
        exit_button_icon.addPixmap(QtGui.QPixmap("icons/ExitButttonicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_button.setIcon(exit_button_icon)
        self.exit_button.setIconSize(QtCore.QSize(21, 21))
        self.exit_button.setCheckable(False)
        self.minimize_button = QtWidgets.QPushButton(self.mainwindow_central_widget)
        self.minimize_button.setGeometry(QtCore.QRect(598, 0, 51, 29))
        self.minimize_button.setStyleSheet(
                                          "QPushButton {\n"
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
                                          )
        self.minimize_button.setText("")
        minimize_button_icon = QtGui.QIcon()
        minimize_button_icon.addPixmap(QtGui.QPixmap("icons/MinimizeButttonicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimize_button.setIcon(minimize_button_icon)
        self.minimize_button.setIconSize(QtCore.QSize(21, 21))
        self.minimize_button.setCheckable(False)
        self.title_bar_buttons_filler_label = QtWidgets.QLabel(self.mainwindow_central_widget)
        self.title_bar_buttons_filler_label.setGeometry(QtCore.QRect(649, 0, 4, 29))
        self.title_bar_buttons_filler_label.setStyleSheet("background-color: rgb(17, 18, 17);\n")
        self.title_bar_buttons_filler_label.setText("")
        ######################
        #MAIN ECUATION STRING#
        ######################

        self.eq_string_layout_widget=QtWidgets.QWidget(self.mainwindow_central_widget)
        self.eq_string_layout = QtWidgets.QVBoxLayout(self.eq_string_layout_widget)
        self.eq_string_layout.setContentsMargins(0,0,0,0)
        self.eq_string_layout_widget.setGeometry(QtCore.QRect(112, 289, 481, 29))

        self.eq_string_text_edit = QTextEditDropEnabled(self.admin)
        self.eq_string_text_edit.setStyleSheet(vmtss.eq_string_text_edit_stylesheet)
        self.eq_string_text_edit.setPlaceholderText("Type here...")
        self.eq_string_text_edit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.eq_string_text_edit.setLineWrapColumnOrWidth(0)
        self.eq_string_text_edit.setReadOnly(True)
        self.eq_string_text_edit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.eq_string_layout.addWidget(self.eq_string_text_edit,0)

        ################
        ##HIDE WIDGETS##
        ################

        self.system_of_equations_frame.hide()
        self.background_vectors_and_matrices_operators_label.hide()
        for x in self.matrix_operators_buttons_names:
            self.matrix_operators_buttons_dict[x].hide()
        for x in self.vector_operators_buttons_names:
            self.vector_operators_buttons_dict[x].hide() 
        for x in self.answer_and_equal_buttons_names: 
            self.answer_and_equal_buttons_dict[x].hide()
        self.general_operators_frame.hide()
        self.draggable_vector_list_widget.hide()
        self.draggable_matrix_list_widget.hide()
        self.click_and_drag_label.hide()
        self.main_vector_matrix_screen_scrollarea.hide()
        self.write_vector_frame.hide()
        self.choose_vector_frame.hide()
        self.angle_result_frame.hide()
        self.choose_type_horizontal_slider.hide()
        self.vector_import_label.hide()
        self.vector_write_label.hide()
        self.eq_string_layout_widget.hide()
        self.background_decorative_slide_label.hide()
        self.dd_or_dms_horizontal_slider.hide()
        self.decimal_degree_label.hide()
        self.degrees_minutes_seconds_label.hide()
        self.eigenvalues_frame.hide()

        MainWindow.setCentralWidget(self.mainwindow_central_widget)
        self.menu_bar = QtWidgets.QMenuBar(MainWindow)
        self.menu_bar.setGeometry(QtCore.QRect(0, 29, 711, 21))
        MainWindow.setMenuBar(self.menu_bar)
        self.status_bar = QtWidgets.QStatusBar(MainWindow)
        self.status_bar.setStyleSheet(mvsfss.status_bar_stylesheet)
        MainWindow.setStatusBar(self.status_bar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tab_buttons_tooltips_list=["Vectors","Matrix","Angles","Eigenvectors",
        "System of Equations"]
        for x in range(0,5):
            self.tab_buttons_dict[self.tab_buttons_name_list[x]].setToolTip(_translate("MainWindow", self.tab_buttons_tooltips_list[x]))
            self.tab_buttons_dict[self.tab_buttons_name_list[x]].setStatusTip(_translate("MainWindow", self.tab_buttons_tooltips_list[x]))
            self.tab_buttons_dict[self.tab_buttons_name_list[x]].setWhatsThis(_translate("MainWindow", self.tab_buttons_tooltips_list[x]))
            self.tab_buttons_dict[self.tab_buttons_name_list[x]].setAccessibleName(_translate("MainWindow", self.tab_buttons_tooltips_list[x]))
            self.tab_buttons_dict[self.tab_buttons_name_list[x]].setAccessibleDescription(_translate("MainWindow", self.tab_buttons_tooltips_list[x]))
        self.info_button.setToolTip(_translate("MainWindow", "Info"))
        self.info_button.setToolTip(_translate("MainWindow", "Info"))
        self.info_button.setStatusTip(_translate("MainWindow", "Info"))
        self.info_button.setWhatsThis(_translate("MainWindow", "Info"))
        self.info_button.setAccessibleName(_translate("MainWindow", "Info"))
        self.assign_button.setToolTip(_translate("MainWindow", "Assign values"))
        self.assign_button.setStatusTip(_translate("MainWindow", "Assign values"))
        self.assign_button.setWhatsThis(_translate("MainWindow", "Assign values"))
        self.assign_button.setAccessibleName(_translate("MainWindow", "Assign values"))
        self.assign_button.setAccessibleDescription(_translate("MainWindow", "Assign values"))
        vector_operators_buttons_tooltip_counter=-1
        vector_operators_buttons_tooltips=["Addition","Subtraction","Scalar Product","Vector Product","Magnitude"]
        for x in self.vector_operators_buttons_names:
            vector_operators_buttons_tooltip_counter+=1
            self.vector_operators_buttons_dict[x].setToolTip(_translate("MainWindow", vector_operators_buttons_tooltips[vector_operators_buttons_tooltip_counter]))
            self.vector_operators_buttons_dict[x].setStatusTip(_translate("MainWindow", vector_operators_buttons_tooltips[vector_operators_buttons_tooltip_counter]))
            self.vector_operators_buttons_dict[x].setWhatsThis(_translate("MainWindow", vector_operators_buttons_tooltips[vector_operators_buttons_tooltip_counter]))
            self.vector_operators_buttons_dict[x].setAccessibleName(_translate("MainWindow", vector_operators_buttons_tooltips[vector_operators_buttons_tooltip_counter]))
        matrix_operators_buttons_tooltip_counter=-1
        matrix_operators_buttons_tooltips=["Addition","Subtraction","Product","Transpose","Determinant"]
        for x in self.matrix_operators_buttons_names:
            matrix_operators_buttons_tooltip_counter+=1 
            self.matrix_operators_buttons_dict[x].setToolTip(_translate("MainWindow", matrix_operators_buttons_tooltips[matrix_operators_buttons_tooltip_counter]))
            self.matrix_operators_buttons_dict[x].setStatusTip(_translate("MainWindow", matrix_operators_buttons_tooltips[matrix_operators_buttons_tooltip_counter]))
            self.matrix_operators_buttons_dict[x].setWhatsThis(_translate("MainWindow", matrix_operators_buttons_tooltips[matrix_operators_buttons_tooltip_counter]))
            self.matrix_operators_buttons_dict[x].setAccessibleName(_translate("MainWindow", matrix_operators_buttons_tooltips[matrix_operators_buttons_tooltip_counter]))
        answer_equal_buttons_tooltip_counter=-1
        answer_equal_buttons_tooltips=["Use previous Answer","Solve"]
        for x in self.answer_and_equal_buttons_names: 
            answer_equal_buttons_tooltip_counter+=1 
            self.answer_and_equal_buttons_dict[x].setToolTip(_translate("MainWindow", answer_equal_buttons_tooltips[answer_equal_buttons_tooltip_counter]))
            self.answer_and_equal_buttons_dict[x].setStatusTip(_translate("MainWindow", answer_equal_buttons_tooltips[answer_equal_buttons_tooltip_counter]))
            self.answer_and_equal_buttons_dict[x].setWhatsThis(_translate("MainWindow", answer_equal_buttons_tooltips[answer_equal_buttons_tooltip_counter]))
            self.answer_and_equal_buttons_dict[x].setAccessibleName(_translate("MainWindow", answer_equal_buttons_tooltips[answer_equal_buttons_tooltip_counter]))
        self.all_clear_button.setToolTip(_translate("MainWindow", "Clear all"))
        self.all_clear_button.setStatusTip(_translate("MainWindow", "Clear all"))
        self.all_clear_button.setWhatsThis(_translate("MainWindow", "Clear all"))
        self.all_clear_button.setAccessibleName(_translate("MainWindow", "Clear all"))
        self.general_operators_buttons_name_list_line1tooltips=["Add","Subtract","Multiply","Divide","Sine","Cosine","Tangent","Hyperbolic Sine",
        "Hyperbolic Cosine","Hyperbolic Tangent","Logarithm base 10","Natural Logarithm"]
        self.general_operators_buttons_name_list_line2tooltips=["Power","Root","Euler's Number","Pi Number","Inverse Sine","Inverse Cosine",
        "Inverse Tangent","Inverse Hyperbolic Sine","Inverse Hyperbolic Cosine","Inverse Hyperbolic Tangent","Logarithm Without Base",
        "Scalar Absolute"]
        general_operators_line1_tooltip_counter=-1
        for x in self.general_operators_buttons_name_list_line1:
            general_operators_line1_tooltip_counter+=1
            self.general_operators_buttons_dict[x].setToolTip(_translate("MainWindow", self.general_operators_buttons_name_list_line1tooltips[general_operators_line1_tooltip_counter]))
            self.general_operators_buttons_dict[x].setStatusTip(_translate("MainWindow", self.general_operators_buttons_name_list_line1tooltips[general_operators_line1_tooltip_counter]))
            self.general_operators_buttons_dict[x].setWhatsThis(_translate("MainWindow", self.general_operators_buttons_name_list_line1tooltips[general_operators_line1_tooltip_counter]))
            self.general_operators_buttons_dict[x].setAccessibleName(_translate("MainWindow", self.general_operators_buttons_name_list_line1tooltips[general_operators_line1_tooltip_counter]))
        general_operators_line2_tooltip_counter=-1
        for x in self.general_operators_buttons_name_list_line2:
            general_operators_line2_tooltip_counter+=1
            self.general_operators_buttons_dict[x].setToolTip(_translate("MainWindow", self.general_operators_buttons_name_list_line2tooltips[general_operators_line2_tooltip_counter]))
            self.general_operators_buttons_dict[x].setStatusTip(_translate("MainWindow", self.general_operators_buttons_name_list_line2tooltips[general_operators_line2_tooltip_counter]))
            self.general_operators_buttons_dict[x].setWhatsThis(_translate("MainWindow", self.general_operators_buttons_name_list_line2tooltips[general_operators_line2_tooltip_counter]))
            self.general_operators_buttons_dict[x].setAccessibleName(_translate("MainWindow", self.general_operators_buttons_name_list_line2tooltips[general_operators_line2_tooltip_counter]))
        __sortingEnabled = self.draggable_matrix_list_widget.isSortingEnabled()
        self.draggable_matrix_list_widget.setSortingEnabled(False)
        self.draggable_matrix_list_widget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.draggable_vector_list_widget.isSortingEnabled()
        self.draggable_vector_list_widget.setSortingEnabled(False)
        self.draggable_vector_list_widget.setSortingEnabled(__sortingEnabled)
        self.vector_import_label.setText(_translate("MainWindow", "IMPORT"))
        self.vector_write_label.setText(_translate("MainWindow", "WRITE"))
        self.write_vector_label_x.setText(_translate("MainWindow", " Vector  I"))
        self.write_vector_label_y.setText(_translate("MainWindow", " Vector II"))
        self.degrees_minutes_seconds_label.setText(_translate("MainWindow", "DMS"))
        self.decimal_degree_label.setText(_translate("MainWindow", "  DD"))
        __sortingEnabled = self.eigenvalues_choose_matrix_list_widget.isSortingEnabled()
        self.eigenvalues_choose_matrix_list_widget.setSortingEnabled(False)
        self.eigenvalues_choose_matrix_list_widget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.system_of_equations_choose_matrix_listwidget.isSortingEnabled()
        self.system_of_equations_choose_matrix_listwidget.setSortingEnabled(False)
        self.system_of_equations_choose_matrix_listwidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.system_of_equations_choosevector_list_widget.isSortingEnabled()
        self.system_of_equations_choosevector_list_widget.setSortingEnabled(False)
        self.system_of_equations_choosevector_list_widget.setSortingEnabled(__sortingEnabled)
        for x in range(0,20):
            item = self.draggable_matrix_list_widget.item(x)
            item.setText(_translate("MainWindow", "Matrix"+str(x+1)))
            item = self.draggable_vector_list_widget.item(x)
            item.setText(_translate("MainWindow", "Vector"+str(x+1)))
            item = self.eigenvalues_choose_matrix_list_widget.item(x)
            item.setText(_translate("MainWindow", "Matrix"+str(x+1)))
            item = self.system_of_equations_choose_matrix_listwidget.item(x)
            item.setText(_translate("MainWindow", "Matrix"+str(x+1)))
            item = self.system_of_equations_choosevector_list_widget.item(x)
            item.setText(_translate("MainWindow", "Vector"+str(x+1)))
            self.choose_vector_combobox_x.setItemText(x, _translate("MainWindow", "Vector"+str(x+1)))
            self.choose_vector_combobox_y.setItemText(x, _translate("MainWindow", "Vector"+str(x+1)))
            if x<12:
                self.write_vector_column_combobox_x.setItemText(x, _translate("MainWindow", str(x+1)))
                self.write_vector_column_combobox_y.setItemText(x, _translate("MainWindow", str(x+1)))
    def vectors_button_state(self):
        if self.tab_buttons_dict["vector_tab_button"].isChecked():
            for x in range(0,5):
                if self.tab_buttons_name_list[x] == "vector_tab_button":
                    pass
                else:
                    self.tab_buttons_dict[self.tab_buttons_name_list[x]].setChecked(False)
            self.eigenvalues_button_state()
            self.system_of_equation_button_state()
            self.angles_button_state()
            self.matrix_button_state()
            self.main_title_label_top.setPixmap(QtGui.QPixmap("icons/Vectorstitle.png"))
            self.background_vectors_and_matrices_operators_label.show()
            for x in self.vector_operators_buttons_names:
                self.vector_operators_buttons_dict[x].show()
            for x in self.answer_and_equal_buttons_names: 
                self.answer_and_equal_buttons_dict[x].show()
            self.eq_string_layout_widget.show()
            self.general_operators_frame.show()
            self.draggable_vector_list_widget.show()
            self.click_and_drag_label.show()
            self.main_vector_matrix_screen_scrollarea.show()
        else:
            self.main_title_label_top.clear()
            self.background_vectors_and_matrices_operators_label.hide()
            for x in self.vector_operators_buttons_names:
                self.vector_operators_buttons_dict[x].hide() 
            for x in self.answer_and_equal_buttons_names: 
                self.answer_and_equal_buttons_dict[x].hide()
            self.eq_string_layout_widget.hide()
            self.general_operators_frame.hide()
            self.draggable_vector_list_widget.hide()
            self.click_and_drag_label.hide()
            self.main_vector_matrix_screen_scrollarea.hide()
            return
    def matrix_button_state(self):
        if self.tab_buttons_dict["matrix_tab_button"].isChecked():
            for x in range(0,5):
                if self.tab_buttons_name_list[x] == "matrix_tab_button":
                    pass
                else:
                    self.tab_buttons_dict[self.tab_buttons_name_list[x]].setChecked(False)
            self.eigenvalues_button_state()
            self.system_of_equation_button_state()
            self.vectors_button_state()
            self.angles_button_state()
            self.main_title_label_top.setPixmap(QtGui.QPixmap("icons/Matrixtitle.png"))
            self.background_vectors_and_matrices_operators_label.show()
            for x in self.matrix_operators_buttons_names:
                self.matrix_operators_buttons_dict[x].show()
            for x in self.answer_and_equal_buttons_names: 
                self.answer_and_equal_buttons_dict[x].show()
            self.eq_string_layout_widget.show()
            self.general_operators_frame.show()
            self.draggable_matrix_list_widget.show()
            self.click_and_drag_label.show()
            self.main_vector_matrix_screen_scrollarea.show()
        else:
            self.main_title_label_top.clear()
            self.background_vectors_and_matrices_operators_label.hide()
            for x in self.matrix_operators_buttons_names:
                self.matrix_operators_buttons_dict[x].hide()
            for x in self.answer_and_equal_buttons_names: 
                self.answer_and_equal_buttons_dict[x].hide()
            self.eq_string_layout_widget.hide()
            self.general_operators_frame.hide()
            self.draggable_matrix_list_widget.hide()
            self.click_and_drag_label.hide()
            self.main_vector_matrix_screen_scrollarea.hide()
            return
    def angles_button_state(self):
        if self.tab_buttons_dict["angles_tab_button"].isChecked():
            for x in range(0,5):
                if self.tab_buttons_name_list[x] == "angles_tab_button":
                    pass
                else:
                    self.tab_buttons_dict[self.tab_buttons_name_list[x]].setChecked(False)
            self.eigenvalues_button_state()
            self.system_of_equation_button_state()
            self.vectors_button_state()
            self.matrix_button_state()
            self.main_title_label_top.setPixmap(QtGui.QPixmap("icons/Angletitle.png"))
            self.choose_type_horizontal_slider_value_changed()
            self.angles_vector_x_combobox_value_changed()
            self.angles_vector_y_combobox_value_changed()
            self.write_vector_column_combobox_y_value_changed()
            self.write_vector_column_combobox_x_value_changed()
            self.angle_result_frame.show()
            self.choose_type_horizontal_slider.show()
            self.vector_import_label.show()
            self.vector_write_label.show()
            self.background_decorative_slide_label.show()
        else:
            self.main_title_label_top.clear()
            self.general_operators_frame.hide()
            self.write_vector_frame.hide()
            self.choose_vector_frame.hide()
            self.angle_result_frame.hide()
            self.choose_type_horizontal_slider.hide()
            self.vector_import_label.hide()
            self.vector_write_label.hide()
            self.background_decorative_slide_label.hide()
            return
    def eigenvalues_button_state(self):
        if self.tab_buttons_dict["eigenvalues_tab_button"].isChecked():
            for x in range(0,5):
                if self.tab_buttons_name_list[x] == "eigenvalues_tab_button":
                    pass
                else:
                    self.tab_buttons_dict[self.tab_buttons_name_list[x]].setChecked(False)
            self.system_of_equation_button_state()
            self.angles_button_state()
            self.vectors_button_state()
            self.matrix_button_state()
            self.main_title_label_top.setPixmap(QtGui.QPixmap("icons/Eigenvectorstitle.png"))
            self.eigenvalues_frame.show()
        else:
            self.main_title_label_top.clear()
            self.general_operators_frame.hide()
            self.eigenvalues_frame.hide()
            return
    def system_of_equation_button_state(self):
        if self.tab_buttons_dict["system_of_equations_tab_button"].isChecked():
            for x in range(0,5):
                if self.tab_buttons_name_list[x] == "system_of_equations_tab_button":
                    pass
                else:
                    self.tab_buttons_dict[self.tab_buttons_name_list[x]].setChecked(False)
            self.eigenvalues_button_state()
            self.angles_button_state()
            self.vectors_button_state()
            self.matrix_button_state()
            self.main_title_label_top.setPixmap(QtGui.QPixmap("icons/Systemofequationstitle.png"))
            self.system_of_equations_frame.show()
        else:
            self.system_of_equations_frame.hide()
            self.main_title_label_top.clear()
            self.general_operators_frame.hide()
            return
    def show_assign_window(self):
        global _FIRST_TIME_LOADING_MATRICES
        if self.admin.window.assign_values_window.is_hidden:
            if _FIRST_TIME_LOADING_MATRICES:
                self.fill_vectors_treeview()
                self.fill_matrices_treeview()
                self.admin.window.assign_values_window.ui.number_of_matrix_combobox.setCurrentIndex(19)
                self.admin.window.assign_values_window.ui.hide_and_show_matrix_items()
                self.admin.window.assign_values_window.show()
                _FIRST_TIME_LOADING_MATRICES=False
            else:
                self.admin.window.assign_values_window.show()
            self.admin.window.assign_values_window.is_hidden = False
        else:
            self.admin.window.assign_values_window.hide()
            self.admin.window.assign_values_window.is_hidden = True
    def update_matrix_tree_items_on_tab_change(self):
        global _FIRST_TAB_CHANGE
        if _FIRST_TAB_CHANGE:
            self.admin.window.assign_values_window.ui.number_of_matrix_combobox.setCurrentIndex(19)
            self.admin.window.assign_values_window.ui.hide_and_show_matrix_items()
            self.fill_matrices_treeview()
            self.admin.window.assign_values_window.ui.number_of_matrix_combobox.setCurrentIndex(0)
            self.admin.window.assign_values_window.ui.hide_and_show_matrix_items()
            _FIRST_TAB_CHANGE = False
        else:
            pass
    def convert_to_float(self,frac_str):
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
    def fill_matrices_treeview(self):
        self.admin.update_matrices_tree()
        for z in range (0,20):
            number_of_matrix = z
            array_of_selected_matrix = self.admin.matrices_arrays[number_of_matrix]
            spacing="   "

            for x in range(0, self.admin.matrices_rows[number_of_matrix]):
                for y in range(0, self.admin.matrices_columns[number_of_matrix]):
                    self.admin.window.assign_values_window.ui.matrices_label_cell_dict["matrix"+str(number_of_matrix+1)+"labelcell"+str(x+1)+"_"+str(y+1)].setHidden(False)
                    if y == (self.admin.matrices_columns[number_of_matrix]-1):
                        self.admin.window.assign_values_window.ui.matrices_label_cell_dict["matrix"+str(number_of_matrix+1)+"labelcell"+str(x+1)+"_"+str(y+1)].setText(str(array_of_selected_matrix[x][y]))
                    else:
                        self.admin.window.assign_values_window.ui.matrices_label_cell_dict["matrix"+str(number_of_matrix+1)+"labelcell"+str(x+1)+"_"+str(y+1)].setText(str(array_of_selected_matrix[x][y])+spacing)

            for x in range(0,10):
                for y in range(0,10):
                    if (x+1) > self.admin.matrices_rows[number_of_matrix]:
                        self.admin.window.assign_values_window.ui.matrices_label_cell_dict["matrix"+str(number_of_matrix+1)+"labelcell"+str(x+1)+"_"+str(y+1)].setHidden(True)
                    elif (y+1) > self.admin.matrices_columns[number_of_matrix]:
                        self.admin.window.assign_values_window.ui.matrices_label_cell_dict["matrix"+str(number_of_matrix+1)+"labelcell"+str(x+1)+"_"+str(y+1)].setHidden(True)
                    else:
                        pass

        combobox_selection_needeed=self.admin.window.assign_values_window.ui.number_of_matrix_combobox.currentText()
        self.admin.window.assign_values_window.ui.number_of_matrix_combobox.setCurrentText(str(int(combobox_selection_needeed)-1))
        self.admin.window.assign_values_window.ui.hide_and_show_matrix_items()
        self.admin.window.assign_values_window.ui.number_of_matrix_combobox.setCurrentText(combobox_selection_needeed)
        self.admin.window.assign_values_window.ui.hide_and_show_matrix_items()
    def fill_vectors_treeview(self):
        self.admin.update_vectors_tree()
        for x in range (0,20):
            vector_values_string=""
            vector_values_list=[]
            number_of_vector = x
            for y in range(0,(self.admin.vectors_rows[number_of_vector])):
                vector_values_list.append(list(self.admin.vectors_arrays[number_of_vector][y]))
            for z in range(0, len(vector_values_list)):
                for w in range(0,self.admin.vectors_columns[number_of_vector]):
                    individual_vector_value=vector_values_list[z][w]
                    vector_values_string = vector_values_string + str(individual_vector_value)
                    if w == (self.admin.vectors_columns[number_of_vector]-1):
                        pass
                    else:
                        vector_values_string = vector_values_string + "   "
                if z == (len(vector_values_list)-1):
                    pass
                else:
                    vector_values_string = vector_values_string + "\n"

            self.admin.window.assign_values_window.ui.vectors_label_dict["vector"+str(x+1)+"label"].setText(vector_values_string)
        combobox_selection_needeed=self.admin.window.assign_values_window.ui.number_of_vectors_combobox.currentText()
        self.admin.window.assign_values_window.ui.number_of_vectors_combobox.setCurrentText(str(int(combobox_selection_needeed)-1))
        self.admin.window.assign_values_window.ui.hide_and_show_vector_items()
        self.admin.window.assign_values_window.ui.number_of_vectors_combobox.setCurrentText(combobox_selection_needeed)
        self.admin.window.assign_values_window.ui.hide_and_show_vector_items()
    def all_clear_button_clicked(self):
        if self.tab_buttons_dict["vector_tab_button"].isChecked() or self.tab_buttons_dict["matrix_tab_button"].isChecked():
            self.eq_string_text_edit.clear()
            for x, y in itools.product(range(1,11), range(1,11)):
                self.result_matrix_label_cell_dict["result_matrixlabelcell"+str(x)+"_"+str(y)].setHidden(True)
            self.result_matrix_parentesis_open_label.setHidden(True)
            self.result_matrix_parentesis_closed_label.setHidden(True)
            self.result_label_error.setHidden(True)
            self.result_label_int_or_float.setHidden(True)
        if self.tab_buttons_dict["angles_tab_button"].isChecked():
            self.angle_result_screen_scrollarea_label.clear()
        if self.tab_buttons_dict["eigenvalues_tab_button"].isChecked():
            for x in range(0, 10):
                self.eigenvectors_label_dict["eigenvectorsLabel_"+str(x+1)].setHidden(True)
                self.eigenvalue_multiplicity_label_dict["eigenvaluemultiplicityLabel_"+str(x+1)].setHidden(True)
                self.eigenvalue_label_dict["eigenvalueLabel_"+str(x+1)].setHidden(True)
        if self.tab_buttons_dict["system_of_equations_tab_button"].isChecked():
            self.system_of_equations_result_scrollarea_result_label.clear()
    def format_number(self,num):
        if num % 1 == 0:
            return int(num)
        else:
            return num
    def convert_to_fraction(self,num):
        frac = Fraction(num).limit_denominator()
        if frac.denominator > 300:
            return num
        else:
            return frac
    def equal_button_clicked(self):
        equation_string = self.eq_string_text_edit.toPlainText()
        if equation_string == "":
            return
        self.admin.calculate_string_equation(equation_string,self.deg_or_rad)
        if self.admin.is_equation_result_matrix==True:
            self.result_label_error.setHidden(True)
            for j in range(0, (self.admin.equation_final_result.row)):
                for k in range(0,(self.admin.equation_final_result.column)):
                    self.result_matrix_label_cell_dict["result_matrixlabelcell"+str(j+1)+"_"+str(k+1)].setText(str(self.convert_to_fraction(self.format_number(self.convert_to_float(self.admin.equation_final_result.values[j][k])))))
            for x in range(0,10):
                for y in range(0,10):
                    self.result_matrix_label_cell_dict["result_matrixlabelcell"+str(x+1)+"_"+str(y+1)].setHidden(True)
            for x in range(0, (self.admin.equation_final_result.row)):
                for y in range(0, (self.admin.equation_final_result.column)):
                    self.result_matrix_label_cell_dict["result_matrixlabelcell"+str(x+1)+"_"+str(y+1)].setHidden(False)
            self.result_matrix_parentesis_open_label.setHidden(False)
            self.result_matrix_parentesis_closed_label.setHidden(False)
        if self.admin.is_equation_result_matrix==False:
            for x in range(0, 10):
                for y in range(0, 10):
                    self.result_matrix_label_cell_dict["result_matrixlabelcell"+str(x+1)+"_"+str(y+1)].setHidden(True)
            self.result_matrix_parentesis_open_label.setHidden(True)
            self.result_matrix_parentesis_closed_label.setHidden(True)

        if self.admin.is_equation_result_int_or_float==True or self.admin.is_equation_result_complex==True:
            self.result_label_error.setHidden(True)
            self.result_label_int_or_float.setHidden(False)
            try:
                self.result_label_int_or_float.setText(str(self.format_number(self.admin.equation_final_result)))
            except:
                self.result_label_int_or_float.setText(str(self.admin.equation_final_result))

        if self.admin.is_equation_result_int_or_float==False and self.admin.is_equation_result_complex==False:
            self.result_label_int_or_float.setHidden(True)

        if self.admin.is_equation_result_int_or_float==False and self.admin.is_equation_result_matrix==False and self.admin.is_equation_result_complex==False:
            self.result_label_error.setHidden(False)
            self.result_label_error.setText(str(self.admin.equation_final_result))

    def answer_button_clicked(self):
        self.eq_string_text_edit.insertPlainText("Ans")
    def addition_button_clicked(self):
        self.eq_string_text_edit.insertPlainText("+")
    def subtraction_button_clicked(self):
        self.eq_string_text_edit.insertPlainText("-")
    def matrix_product_button_clicked(self):
        self.eq_string_text_edit.insertPlainText("*")
    def determinant_button_clicked(self):
        self.eq_string_text_edit.insertPlainText("det()")
    def transpose_button_clicked(self):
        self.eq_string_text_edit.insertPlainText("tr()")
    def scalar_button_clicked(self):
        self.eq_string_text_edit.insertPlainText("@")
    def vector_product_button_clicked(self):
        self.eq_string_text_edit.insertPlainText("&")
    def magnitude_button_clicked(self):
        self.eq_string_text_edit.insertPlainText("norm()")
    def general_add_button_clicked(self):
        self.eq_string_text_edit.insertPlainText("+")
    def general_sub_button_clicked(self):
        self.eq_string_text_edit.insertPlainText("-")
    def general_multiply_button_clicked(self):
        self.eq_string_text_edit.insertPlainText("*")
    def general_division_button_clicked(self):
        self.eq_string_text_edit.insertPlainText("/")
    def general_power_button_clicked(self):
        self.eq_string_text_edit.insertPlainText("^")
    def general_root_button_clicked(self):
        self.eq_string_text_edit.insertPlainText("√()")
    def general_e_button_clicked(self):
        self.eq_string_text_edit.insertPlainText("ℇ")
    def general_pi_button_clicked(self):
        self.eq_string_text_edit.insertPlainText("π")
    def general_sin_button_clicked(self):
        self.eq_string_text_edit.insertPlainText("sin()")
    def general_cos_button_clicked(self):
        self.eq_string_text_edit.insertPlainText("cos()")
    def general_tan_button_clicked(self):
        self.eq_string_text_edit.insertPlainText("tan()")
    def general_sinh_button_clicked(self):
        self.eq_string_text_edit.insertPlainText("sinh()")
    def general_cosh_button_clicked(self):
        self.eq_string_text_edit.insertPlainText("cosh()")
    def general_tanh_button_clicked(self):
        self.eq_string_text_edit.insertPlainText("tanh()")
    def general_sin_inv_button_clicked(self):
        self.eq_string_text_edit.insertPlainText("arcsin()")
    def general_cos_inv_button_clicked(self):
        self.eq_string_text_edit.insertPlainText("arccos()")
    def general_tan_inv_button_clicked(self):
        self.eq_string_text_edit.insertPlainText("arctan()")
    def general_sinh_inv_button_clicked(self):
        self.eq_string_text_edit.insertPlainText("arcsinh()")
    def general_cosh_inv_button_clicked(self):
        self.eq_string_text_edit.insertPlainText("arccosh()")
    def general_tanh_inv_button_clicked(self):
        self.eq_string_text_edit.insertPlainText("arctanh()")
    def general_log_button_clicked(self):
        self.eq_string_text_edit.insertPlainText("Log()")
    def general_in_button_clicked(self):
        self.eq_string_text_edit.insertPlainText("In()")
    def general_log_choose_button_clicked(self):
        self.eq_string_text_edit.insertPlainText("Log(argument)/Log(base)")
    def general_absolute_button_clicked(self):
        self.eq_string_text_edit.insertPlainText("absolute()")

    def vector_and_matrix_list_widget_double_clicked(self):
        text_to_add=""
        if self.admin.window.ui.tab_buttons_dict["matrix_tab_button"].isChecked():
            text_to_add=str(self.admin.window.ui.draggable_matrix_list_widget.currentItem().text())
            self.admin.window.ui.eq_string_text_edit.insertPlainText(text_to_add)
        elif self.admin.window.ui.tab_buttons_dict["vector_tab_button"].isChecked():
            text_to_add=str(self.admin.window.ui.draggable_vector_list_widget.currentItem().text())
            self.admin.window.ui.eq_string_text_edit.insertPlainText(text_to_add)
        else:
            return
    def deg_and_rad_vertical_slider_value_changed(self):
        if self.deg_and_rad_vertical_slider.value() == 1:
            self.deg_or_rad = "DEG"
            self.rad_label.setStyleSheet(   
                                        "font: 8pt \"Alice\";\n"
                                        "color: rgb(96, 96, 96);\n"
                                        "background-color:transparent;\n"
                                        "border:0px;\n"
                                        "margin:0px;"
                                        )
            self.degree_label.setStyleSheet(
                                           "font: 8pt \"Alice\";\n"
                                           "color: rgb(126, 126, 126);\n"
                                           "background-color:transparent;\n"
                                           "border:0px;\n"
                                           "margin:0px;"
                                           )
            self.dd_or_dms_horizontal_slider.show()
            self.decimal_degree_label.show()
            self.degrees_minutes_seconds_label.show()
        if self.deg_and_rad_vertical_slider.value() == 0:
            self.deg_or_rad = "RAD"
            self.degree_label.setStyleSheet(
                                           "font: 8pt \"Alice\";\n"
                                           "color: rgb(96, 96, 96);\n"
                                           "background-color:transparent;\n"
                                           "border:0px;\n"
                                           "margin:0px;"
                                           )
            self.rad_label.setStyleSheet(
                                        "font: 8pt \"Alice\";\n"
                                        "color: rgb(126, 126, 126);\n"
                                        "background-color:transparent;\n"
                                        "border:0px;\n"
                                        "margin:0px;"
                                        )
            self.dd_or_dms_horizontal_slider.hide()
            self.decimal_degree_label.hide()
            self.degrees_minutes_seconds_label.hide()

    def dd_or_dms_horizontal_slider_value_changed(self):
        if self.dd_or_dms_horizontal_slider.value() == 1:
            self.dd_or_dms = "DD"
            self.decimal_degree_label.setStyleSheet(
                                                   "font: 7pt \"Alice\";\n"
                                                   "background-color: transparent;\n"
                                                   "color: rgb(126, 126, 126);"
                                                   )
            self.degrees_minutes_seconds_label.setStyleSheet(
                                                            "font: 7pt \"Alice\";\n"
                                                            "background-color: transparent;\n"
                                                            "color: rgb(96, 96, 96);"
                                                            )
        if self.dd_or_dms_horizontal_slider.value() == 0:
            self.dd_or_dms = "DMS"
            self.decimal_degree_label.setStyleSheet(
                                                   "font: 7pt \"Alice\";\n"
                                                   "background-color: transparent;\n"
                                                   "color: rgb(96, 96, 96);"
                                                   )
            self.degrees_minutes_seconds_label.setStyleSheet(
                                                            "font: 7pt \"Alice\";\n"
                                                            "background-color: transparent;\n"
                                                            "color: rgb(126, 126, 126);"
                                                            )

    def choose_type_horizontal_slider_value_changed(self):
        if self.choose_type_horizontal_slider.value() == 1:
            self.write_vector_frame.show()
            self.choose_vector_frame.hide()
            self.vector_import_label.setStyleSheet(
                                                  "font: 8pt \"Alice\";\n"
                                                  "background-color: transparent;\n"
                                                  "color: rgb(96, 96, 96);"
                                                  )
            self.vector_write_label.setStyleSheet(
                                                 "font: 8pt \"Alice\";\n"
                                                 "background-color: transparent;\n"
                                                 "color: rgb(126, 126, 126);"
                                                 )
        if self.choose_type_horizontal_slider.value() == 0:
            self.write_vector_frame.hide()
            self.choose_vector_frame.show()
            self.vector_import_label.setStyleSheet(
                                                  "font: 8pt \"Alice\";\n"
                                                  "background-color: transparent;\n"
                                                  "color: rgb(126, 126, 126);"
                                                  )
            self.vector_write_label.setStyleSheet(
                                                 "font: 8pt \"Alice\";\n"
                                                 "background-color: transparent;\n"
                                                 "color: rgb(96, 96, 96);"
                                                 )

    def angles_vector_x_combobox_value_changed(self):
        chosen_vector = self.choose_vector_combobox_x.currentText()
        chosen_vector_values = self.admin.get_angles_chosen_vector(chosen_vector)
        string_for_chosen_loop = "(    "
        for x in chosen_vector_values[0]:
            valueofcell = str(self.convert_to_fraction(self.format_number(self.convert_to_float(x))))
            stringofchosen_vector_values = string_for_chosen_loop + valueofcell + "    "
            string_for_chosen_loop = stringofchosen_vector_values
        stringofchosen_vector_values = stringofchosen_vector_values + ")"
        self.values_chosen_x_label.setText("        "+stringofchosen_vector_values)

    def angles_vector_y_combobox_value_changed(self):
        chosen_vector = self.choose_vector_combobox_y.currentText()
        chosen_vector_values = self.admin.get_angles_chosen_vector(chosen_vector)
        string_for_chosen_loop = "(    "
        for x in chosen_vector_values[0]:
            valueofcell = str(self.convert_to_fraction(self.format_number(self.convert_to_float(x))))
            stringofchosen_vector_values = string_for_chosen_loop + valueofcell + "    "
            string_for_chosen_loop = stringofchosen_vector_values
        stringofchosen_vector_values = stringofchosen_vector_values + ")"
        self.values_chosen_y_label.setText("        "+stringofchosen_vector_values)

    def write_vector_column_combobox_x_value_changed(self):
        number_of_columns_selected=int(self.write_vector_column_combobox_x.currentText())
        self.write_vector_column_combobox_y.setItemText(self.write_vector_column_combobox_y.currentIndex(),self.write_vector_column_combobox_x.currentText())
        self.write_vector_column_combobox_y_value_changed()
        for x in range (1,number_of_columns_selected+1):
            self.write_vector_x_lineedit_dict["writevectorxlineEdit_"+str(x)].show()
        for x in range (number_of_columns_selected+1,13):
            self.write_vector_x_lineedit_dict["writevectorxlineEdit_"+str(x)].hide()

    def write_vector_column_combobox_y_value_changed(self):
        number_of_columns_selected=int(self.write_vector_column_combobox_y.currentText())
        for x in range (1,number_of_columns_selected+1):
            self.write_vector_y_lineedit_dict["writevectorylineEdit_"+str(x)].show()
        for x in range (number_of_columns_selected+1,13):
            self.write_vector_y_lineedit_dict["writevectorylineEdit_"+str(x)].hide()

    def angles_write_vectors_create_array(self):
        try:
            self.writen_vectors_filled=True
            self.list_of_vector_x_values=[[]]
            self.list_of_vector_y_values=[[]]
            self.vector_x_number_columns=int(self.write_vector_column_combobox_x.currentText())
            self.vector_y_number_columns=int(self.write_vector_column_combobox_y.currentText())
            for x in range(1,self.vector_x_number_columns+1):
                if self.write_vector_x_lineedit_dict["writevectorxlineEdit_"+str(x)].text() == "":
                    self.admin.window.error_window.show()
                    self.admin.window.error_window.ui.error_window_body_label.setText("All Vector I cells must be filled.")
                    self.writen_vectors_filled=False
                else:
                    self.list_of_vector_x_values[0].append(self.convert_to_float(self.write_vector_x_lineedit_dict["writevectorxlineEdit_"+str(x)].text()))
            for y in range(1,self.vector_y_number_columns+1):
                if self.write_vector_y_lineedit_dict["writevectorylineEdit_"+str(y)].text() == "":
                    self.admin.window.error_window.show()
                    self.admin.window.error_window.ui.error_window_body_label.setText("All Vector II cells must be filled.")
                    self.writen_vectors_filled=False
                else:
                    self.list_of_vector_y_values[0].append(self.convert_to_float(self.write_vector_y_lineedit_dict["writevectorylineEdit_"+str(y)].text()))
            self.admin.angles_write_vectors_create_array(self.list_of_vector_x_values,self.list_of_vector_y_values,self.vector_x_number_columns,self.vector_y_number_columns)
        except:
            pass

    def angles_calculate_pushbutton_clicked(self):
        if self.choose_type_horizontal_slider.value() == 0:
            result = self.admin.calculate_angles(self.choose_vector_combobox_x.currentText(),self.choose_vector_combobox_y.currentText(),self.deg_or_rad,self.dd_or_dms)
            if self.deg_or_rad=="RAD":
                self.angle_result_screen_scrollarea_label.setText(result+" rad")
            if self.deg_or_rad=="DEG":
                self.angle_result_screen_scrollarea_label.setText(result+" degrees")
        if self.choose_type_horizontal_slider.value() == 1:
            self.calculate_angles()
            result = self.admin.calculate_angles("VectorI","VectorII",self.deg_or_rad,self.dd_or_dms)
            if self.deg_or_rad=="RAD":
                self.angle_result_screen_scrollarea_label.setText(result+" rad")
            if self.deg_or_rad=="DEG":
                self.angle_result_screen_scrollarea_label.setText(result+" degrees")
            if self.writen_vectors_filled == False:
                self.angle_result_screen_scrollarea_label.clear()
    def eigenvalues_choose_matrix_list_widget_item_changed(self):
        chosen_matrix_to_show = self.eigenvalues_choose_matrix_list_widget.currentItem().text()
        self.admin.get_chosen_matrix(chosen_matrix_to_show)
        self.empty_string=""

        for j in range(0, 10):
            for k in range(0,10):
                self.eigenchosen_matrix_label_cell_dict["eigenchosen_matrixlabelcell"+str(j+1)+"_"+str(k+1)].setText("")

        for j in range(0, (self.admin.chosen_matrix_object.row)):
            for k in range(0,(self.admin.chosen_matrix_object.column)):
                self.eigenchosen_matrix_label_cell_dict["eigenchosen_matrixlabelcell"+str(j+1)+"_"+str(k+1)].setText(str(self.convert_to_fraction(self.format_number(self.convert_to_float(self.admin.chosen_matrix_object.values[j][k])))))

        for x in range(0,10):
            for y in range(0,10):
                self.eigenchosen_matrix_label_cell_dict["eigenchosen_matrixlabelcell"+str(x+1)+"_"+str(y+1)].setHidden(True)

        for x in range(0, (self.admin.chosen_matrix_object.row)):
            for y in range(0, (self.admin.chosen_matrix_object.column)):
                self.eigenchosen_matrix_label_cell_dict["eigenchosen_matrixlabelcell"+str(x+1)+"_"+str(y+1)].setHidden(False)

        self.eigenvalues_chosen_matrix_parentesis_open_label.setHidden(False)
        self.eigenvalues_chosen_matrix_parentesis_closed_label.setHidden(False)


    def eigenvalues_calculate_pushbutton_clicked(self):
        try:
            chosen_matrix_to_eigen = self.eigenvalues_choose_matrix_list_widget.currentItem().text()
        except:
            self.admin.window.error_window.show()
            self.admin.window.error_window.ui.error_window_body_label.setText("Select a Matrix")
            return

        self.admin.get_eigen_vectors(chosen_matrix_to_eigen)

        if self.admin.eigen_vectors_result == []:
            return
        else:
            for x in range(0,len(self.admin.eigen_vectors_result)):
                self.eigenvalue_label_dict["eigenvalueLabel_"+str(x+1)].setHidden(False)

            try:
                for x in range(0,len(self.admin.eigen_vectors_result)):
                    self.eigenvalue_label_dict["eigenvalueLabel_"+str(x+1)].setText("λ = "+str(self.convert_to_fraction(self.format_number(self.convert_to_float(self.admin.eigen_vectors_result[x][0])))))

            except:
                for x in range(0,len(self.admin.eigen_vectors_result)):
                    self.eigenvalue_label_dict["eigenvalueLabel_"+str(x+1)].setText("λ = "+str(self.admin.eigen_vectors_result[x][0]))

            for x in range(len(self.admin.eigen_vectors_result),10):
                self.eigenvalue_label_dict["eigenvalueLabel_"+str(x+1)].setHidden(True)

            for x in range(0,len(self.admin.eigen_vectors_result)):
                self.eigenvalue_multiplicity_label_dict["eigenvaluemultiplicityLabel_"+str(x+1)].setHidden(False)

            for x in range(0,len(self.admin.eigen_vectors_result)):
                self.eigenvalue_multiplicity_label_dict["eigenvaluemultiplicityLabel_"+str(x+1)].setText("Algebraic multiplicity: "+str(self.convert_to_fraction(self.format_number(self.convert_to_float(self.admin.eigen_vectors_result[x][1])))))

            for x in range(len(self.admin.eigen_vectors_result),10):
                self.eigenvalue_multiplicity_label_dict["eigenvaluemultiplicityLabel_"+str(x+1)].setHidden(True)

            for x in range(0,len(self.admin.eigen_vectors_result)):
                self.eigenvectors_label_dict["eigenvectorsLabel_"+str(x+1)].setHidden(False)

            for x in range(0,len(self.admin.eigen_vectors_result)):
                self.eigenvectors_label_dict["eigenvectorsLabel_"+str(x+1)].setText(str(self.admin.eigen_vectors_result[x][2]))

            for x in range(len(self.admin.eigen_vectors_result),10):
                self.eigenvectors_label_dict["eigenvectorsLabel_"+str(x+1)].setHidden(True)

    def system_of_equations_choose_matrix_list_widget_item_changed(self):
        chosen_matrix_to_show = self.system_of_equations_choose_matrix_listwidget.currentItem().text()
        self.admin.get_chosen_matrix(chosen_matrix_to_show)
        self.empty_string=""

        for j in range(0, 10):
            for k in range(0,10):
                self.system_matrix_chosen_matrix_label_cell_dict["systemmatrixchosen_matrixlabelcell"+str(j+1)+"_"+str(k+1)].setText("")

        for j in range(0, (self.admin.chosen_matrix_object.row)):
            for k in range(0,(self.admin.chosen_matrix_object.column)):
                self.system_matrix_chosen_matrix_label_cell_dict["systemmatrixchosen_matrixlabelcell"+str(j+1)+"_"+str(k+1)].setText(str(self.convert_to_fraction(self.format_number(self.convert_to_float(self.admin.chosen_matrix_object.values[j][k])))))

        for x in range(0,10):
            for y in range(0,10):
                self.system_matrix_chosen_matrix_label_cell_dict["systemmatrixchosen_matrixlabelcell"+str(x+1)+"_"+str(y+1)].setHidden(True)

        for x in range(0, (self.admin.chosen_matrix_object.row)):
            for y in range(0, (self.admin.chosen_matrix_object.column)):
                self.system_matrix_chosen_matrix_label_cell_dict["systemmatrixchosen_matrixlabelcell"+str(x+1)+"_"+str(y+1)].setHidden(False)

        self.system_of_equations_choose_matrix_parentesis_open_label.setHidden(False)
        self.system_of_equations_choose_matrix_parentesis_closed_label.setHidden(False)

    def system_of_equations_choose_vector_list_widget_item_changed(self):
        chosen_matrix_to_show = self.system_of_equations_choosevector_list_widget.currentItem().text()
        self.admin.get_chosen_matrix(chosen_matrix_to_show)
        self.empty_string=""

        for k in range(0,10):
            self.system_vector_chosen_vector_label_cell_dict["systemvectorchosen_vectorlabelcell"+str(k+1)+"_1"].setText("")

        for j in range(0, (self.admin.chosen_matrix_object.row)):
            for k in range(0,(self.admin.chosen_matrix_object.column)):
                self.system_vector_chosen_vector_label_cell_dict["systemvectorchosen_vectorlabelcell"+str(k+1)+"_1"].setText(str(self.convert_to_fraction(self.format_number(self.convert_to_float(self.admin.chosen_matrix_object.values[j][k])))))

        for x in range(0,10):
            self.system_vector_chosen_vector_label_cell_dict["systemvectorchosen_vectorlabelcell"+str(x+1)+"_1"].setHidden(True)

        for x in range(0, (self.admin.chosen_matrix_object.column)):
            self.system_vector_chosen_vector_label_cell_dict["systemvectorchosen_vectorlabelcell"+str(x+1)+"_1"].setHidden(False)

        self.system_of_equations_choose_vector_parentesis_open_label.setHidden(False)
        self.system_of_equations_choose_vector_parentesis_closed_label.setHidden(False)

    def system_of_equations_calculate_pushbutton_clicked(self):
        try:
            system_chosen_matrix,system_chosen_vector = self.system_of_equations_choose_matrix_listwidget.currentItem().text(),self.system_of_equations_choosevector_list_widget.currentItem().text()
        except:
            self.admin.window.error_window.show()
            self.admin.window.error_window.ui.error_window_body_label.setText("Select a matrix and a vector.")
            return
        print(system_chosen_matrix)
        self.admin.get_system_of_equations_result(system_chosen_matrix,system_chosen_vector)
        self.system_of_equations_result_scrollarea_result_label.setText(self.admin.systems_of_equations_result)
    def info_button_clicked(self):
        self.admin.window.info_window.show()
    def set_stylesheets_poststart(self):
        self.system_of_equations_choose_matrix_listwidget.setStyleSheet(mvssps.system_of_equations_choose_matrix_listwidget_stylesheet)
        self.system_of_equations_choosevector_list_widget.setStyleSheet(mvssps.system_of_equations_choosevector_list_widget_stylesheet)
        self.eigenvalues_result_screen_scrollarea.setStyleSheet(mvssps.eigenvalues_result_screen_scrollarea_stylesheet)
        self.system_of_equations_result_scrollarea.setStyleSheet(mvssps.system_of_equations_result_scrollarea_stylesheet)
        self.system_of_equations_choose_vector_scrollarea.setStyleSheet(mvssps.system_of_equations_choose_vector_scrollarea_stylesheet)
        self.system_of_equations_choose_matrix_scrollarea.setStyleSheet(mvssps.system_of_equations_choose_matrix_scrollarea_stylesheet)
        self.eigenvalues_choose_matrix_list_widget.setStyleSheet(mvssps.eigenvalues_choose_matrix_list_widget_stylesheet)
        self.eigenvalues_chosen_matrix_screen_scrollarea.setStyleSheet(mvssps.eigenvalues_chosen_matrix_screen_scrollarea_stylesheet)
        self.main_vector_matrix_screen_scrollarea.setStyleSheet(mvssps.main_vector_matrix_screen_scrollarea_stylesheet)
        self.draggable_matrix_list_widget.setStyleSheet(mvssps.draggable_matrix_list_widget_stylesheet)
        self.angle_result_screen_scrollarea.setStyleSheet(mvssps.angle_result_screen_scrollarea_stylesheet)
        self.draggable_vector_list_widget.setStyleSheet(mvssps.draggable_vector_list_widget_stylesheet)
        self.eq_string_text_edit.setStyleSheet(mvssps.eq_string_text_edit_stylesheet)