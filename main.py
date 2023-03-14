import module_view.mainview as mainv

from   module_calc.matrix_class import Matrix
import module_calc.numeric_string_parser_class as nspc
import module_calc.calculator_specific_functions as csf
import module_calc.vectors_angle as va
import module_calc.eigenvalues_and_system_of_equations as easoe

import module_splash.splash_screen as sscreen

import numpy as np
import psutil
import ctypes
import os


class Admin():
    
    def __init__(self):
        self.dict_of_matrices_obj, self.dict_of_vectors_obj, self.dict_of_degree_vectors = {}, {}, {} 

        self.initialize_matrices_vectors_objects()

        self.nsp = nspc.NumericStringParser(self.dict_of_matrices_obj, 
                                            self.dict_of_vectors_obj, 
                                            self.dict_of_degree_vectors)
        self.equation_final_result = None

        self.window = mainv.MainWindow(self)

        self.splash_screen_window=sscreen.SplashScreen(self.window)
        
    def update_matrices_tree(self):
        self.matrices_arrays, self.matrices_rows, self.matrices_columns = [], [], []
        for matrix in self.dict_of_matrices_obj.keys():
            self.matrices_arrays.append(self.dict_of_matrices_obj[matrix].values)
            self.matrices_rows.append(self.dict_of_matrices_obj[matrix].row)
            self.matrices_columns.append(self.dict_of_matrices_obj[matrix].column)

    def update_vectors_tree(self):
        self.vectors_arrays, self.vectors_rows, self.vectors_columns = [], [], []
        for vector in self.dict_of_vectors_obj.keys():
            self.vectors_arrays.append(self.dict_of_vectors_obj[vector].values)
            self.vectors_rows.append(self.dict_of_vectors_obj[vector].row)
            self.vectors_columns.append(self.dict_of_vectors_obj[vector].column)

    def modify_matrices(self, number_of_matrix, new_rows, new_columns, new_values):
        self.dict_of_matrices_obj['Matrix' + str(number_of_matrix + 1)].values = new_values
        self.dict_of_matrices_obj['Matrix' + str(number_of_matrix + 1)].row = new_rows
        self.dict_of_matrices_obj['Matrix' + str(number_of_matrix + 1)].column = new_columns
        self.dict_of_matrices_obj['Matrix' + str(number_of_matrix + 1)].create_array()

    def modify_vectors(self, number_of_vector, new_rows, new_columns, new_values):
        self.dict_of_vectors_obj['Vector' + str(number_of_vector + 1)].values = new_values
        self.dict_of_vectors_obj['Vector' + str(number_of_vector + 1)].row = new_rows
        self.dict_of_vectors_obj['Vector' + str(number_of_vector + 1)].column = new_columns
        self.dict_of_vectors_obj['Vector' + str(number_of_vector + 1)].create_array()

    def calculate_string_equation(self,equation,deg_or_rad):
        (self.is_equation_result_matrix, 
        self.is_equation_result_int_or_float,
        self.is_equation_result_complex) = self.equation_result_type_handling(None)
        csf.DEG_OR_RAD = deg_or_rad
        self.equation_final_result = self.get_equation_result(equation)

    def get_angles_chosen_vector(self,vector):
        return self.nsp.parse(vector, update_previous_answer = False).values

    def calculate_angles(self,vector_x,vector_y,deg_or_rad,dd_or_dms):
        csf.DEG_OR_RAD = deg_or_rad
        va.DD_OR_DMS = dd_or_dms
        return va.angle_between_vectors(self.nsp.parse(vector_x, update_previous_answer = False),self.nsp.parse(vector_y, update_previous_answer = False))

    def angles_write_vectors_create_array(self,vector_I_values,vector_II_values,vector_I_column,vector_II_column):
        self.dict_of_degree_vectors['vectorI'].values = vector_I_values
        self.dict_of_degree_vectors['vectorI'].column = vector_I_column
        self.dict_of_degree_vectors['vectorI'].create_array()
        self.dict_of_degree_vectors['vectorII'].values = vector_II_values
        self.dict_of_degree_vectors['vectorII'].column = vector_II_column
        self.dict_of_degree_vectors['vectorII'].create_array()

    def get_chosen_matrix(self,chosen_matrix):
        self.chosen_matrix_object = self.nsp.parse(chosen_matrix, update_previous_answer = False)

    def get_eigen_vectors(self,matrix_to_eigenize):
        self.eigen_vectors_result = easoe.calculate_eigenvectors(self.nsp.parse(matrix_to_eigenize, update_previous_answer = False))

    def get_system_of_equations_result(self,matrix_of_constants,vector_of_results):
        self.systems_of_equations_result = easoe.calculate_system_of_equations_result(self.nsp.parse(matrix_of_constants, update_previous_answer = False),
                                                                                      self.nsp.parse(vector_of_results, update_previous_answer = False))

    def initialize_matrices_vectors_objects(self):
        for x in range(1,21):
            self.dict_of_vectors_obj['Vector' + str(x)] = Matrix( 'Vector' + str(x), 1, 5, [[1, 0, 0, 0, 0], ])
            self.dict_of_vectors_obj['Vector' + str(x)].create_array()
            self.dict_of_matrices_obj['Matrix' + str(x)] = Matrix('Matrix' + str(x), 3, 3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
            self.dict_of_matrices_obj['Matrix' + str(x)].create_array()
        for x in range(1,3):
            self.dict_of_degree_vectors['Vector' + 'I' * x] = Matrix( 'Vector' + 'I' * x, 1, 5, [[1, 0, 0, 0, 0], ])
            self.dict_of_degree_vectors['Vector' + 'I' * x].create_array()

    def get_equation_result(self,equation):
        try:
            equation_result = self.nsp.parse(equation.replace("√", "root"), update_previous_answer = True)
            (self.is_equation_result_matrix, 
            self.is_equation_result_int_or_float,
            self.is_equation_result_complex) = self.equation_result_type_handling(equation_result)
            return equation_result
        except Exception as e:
            return repr(e)

    def equation_result_type_handling(self, eq_obj):
        if isinstance (eq_obj, Matrix):
            return (True, False, False)
        elif isinstance (eq_obj, (int, float)):
            return (False, True, False)
        elif isinstance (eq_obj, np.complex_):
            return (False, False, True)
        else:
            return (False, False, False)
                


if __name__ == "__main__":
    import sys
    app = mainv.QtWidgets.QApplication(sys.argv)
    my_app_id = 'O.V.C.'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_app_id)
    font_id = mainv.QtGui.QFontDatabase.addApplicationFont("fonts/Alice-Regular.ttf")
    _fontstr = mainv.QtGui.QFontDatabase.applicationFontFamilies(font_id)[0]
    _font = mainv.QtGui.QFont(_fontstr, 10)
    app.setFont(_font)
    admin = Admin()
    sys.exit(app.exec_())