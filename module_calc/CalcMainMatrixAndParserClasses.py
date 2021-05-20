from __future__ import division
import functools
import numpy as np
from scipy import linalg
import sympy as sp
sp.init_printing(use_unicode=True)
from pyparsing import (Literal, CaselessLiteral, Word, Combine, Group, Optional,
                       ZeroOrMore, Forward, nums, alphas, oneOf)
import math
import operator

DEG_OR_RAD="RAD"
DD_OR_DMS= "DMS"


class Matrix:
    def __init__(self, vmname, rown, columnn, values):
        self.row = rown
        self.column = columnn
        self.values = values
        self.name = vmname

    def createArray(self):
        self.matrix_of_floats = []

        for x in range(0,self.row):
            list_of_rows=[]
            for y in range(0,self.column):
                cell_value=""
                cell_value = str(self.values[x][y])
                cell_value_converted = self.convertToFloat(cell_value)
                list_of_rows.append(cell_value_converted)
            self.matrix_of_floats.append(list_of_rows)

        self.array = np.array(self.matrix_of_floats)

    def convertToFloat(self,frac_str):
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

    def __add__(self, other):
        result_of_addition=Matrix(self.name,self.row,self.column,self.values)
        if isinstance (other, Matrix):
            if other.array.shape == self.array.shape:
                result_of_addition.values = self.array + other.array
                result_of_addition.createArray()   
            else:
                raise ValueError('Tried to add diferent sizes matrices')
        elif isinstance (other, (int, float)):
            raise ValueError("Can't add matrix to scalar")
        elif isinstance (other, (np.complex_,complex)):
            raise ValueError("Can't add matrix to complex")
        return result_of_addition

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self,other):
        result_of_subtraction=Matrix(self.name,self.row,self.column,self.values)
        if isinstance (other, Matrix):
            if other.array.shape == self.array.shape:
                result_of_subtraction.values = self.array - other.array
                result_of_subtraction.createArray()   
            else:
                raise ValueError('Tried to subtract diferent sizes matrices')
        elif isinstance (other, (int, float)):
            raise ValueError("Can't subtract matrix to scalar")
        elif isinstance (other, (np.complex_,complex)):
            raise ValueError("Can't subtract matrix to complex")
        return result_of_subtraction

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self,other):
        result_of_multiplication=Matrix(self.name,self.row,self.column,self.values)
        if isinstance (other, Matrix):
            result_of_multiplication.values = np.matmul(self.array,other.array)
            result_of_multiplication.createArray()   
        elif isinstance (other, (int, float)):
            result_of_multiplication.values = self.array * other
            result_of_multiplication.createArray() 
        elif isinstance (other, (np.complex_,complex)):
            raise ValueError("Can't multiply matrix to complex")
        return result_of_multiplication

    def __rmul__(self, other):
        return self.__mul__(other)

    def __pow__(self, other):
        result_of_power=Matrix(self.name,self.row,self.column,self.values)
        result_of_power.createArray()
        other = formatNumber(other)
        if isinstance (other, int):
            if self.row == self.column:
                if other>0:
                    for x in range(0,(other-1)):
                        result_of_power=result_of_power*self
                    return result_of_power
                if other<0:
                    result_of_power.array=np.linalg.inv(self.array)
                    for x in range(0,(abs(other)-1)):
                        result_of_power.array= result_of_power.array@np.linalg.inv(self.array)
                    result_of_power.values=result_of_power.array.tolist()
                    return result_of_power
                if other==0:
                    result_of_power.array=np.identity(self.row)
                    result_of_power.values=result_of_power.array.tolist()
                    return result_of_power

            else:
                raise ValueError("Can´t calculate power of non-square matrix")
        else:
            raise ValueError("Invalid power for matrix")


    def __matmul__(self, other):
        if isinstance (other, Matrix) and self.row==1 and other.row==1:
           result_of_dotproduct = np.dot(self.array[0],other.array[0])
           return result_of_dotproduct
        else:
            raise ValueError("Can't use dot product with non-vector")

    def __rmatmul__(self, other):
        return self.__matmul__(other)

    def __and__(self, other):
        result_cross_values=[]
        result_of_crossproduct=Matrix(self.name,self.row,self.column,self.values)
        if isinstance (other, Matrix) and self.row==1 and other.row==1:
            result_cross_values.append(np.cross(self.array[0],other.array[0]))
            result_of_crossproduct.values = result_cross_values
            result_of_crossproduct.createArray()
        else:
            raise ValueError("Can't use cross product with non-vector")
        return result_of_crossproduct

def formatNumber(num):
        if num % 1 == 0:
            return int(num)
        else:
            return num


####################
##### MATRICES #####
####################


matrix1 = Matrix('matrix1', 3, 3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
matrix1.createArray()

matrix2 = Matrix('matrix2', 3, 3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
matrix2.createArray()

matrix3 = Matrix('matrix3', 3, 3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
matrix3.createArray()

matrix4 = Matrix('matrix4', 3, 3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
matrix4.createArray()

matrix5 = Matrix('matrix5', 3, 3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
matrix5.createArray()

matrix6 = Matrix('matrix6', 3, 3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
matrix6.createArray()

matrix7 = Matrix('matrix7', 3, 3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
matrix7.createArray()

matrix8 = Matrix('matrix8', 3, 3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
matrix8.createArray()

matrix9 = Matrix('matrix9', 3, 3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
matrix9.createArray()

matrix10 = Matrix('matrix10', 3, 3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
matrix10.createArray()

matrix11 = Matrix('matrix11', 3, 3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
matrix11.createArray()

matrix12 = Matrix('matrix12', 3, 3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
matrix12.createArray()

matrix13 = Matrix('matrix13', 3, 3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
matrix13.createArray()

matrix14 = Matrix('matrix14', 3, 3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
matrix14.createArray()

matrix15 = Matrix('matrix15', 3, 3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
matrix15.createArray()

matrix16 = Matrix('matrix16', 3, 3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
matrix16.createArray()

matrix17 = Matrix('matrix17', 3, 3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
matrix17.createArray()

matrix18 = Matrix('matrix18', 3, 3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
matrix18.createArray()

matrix19 = Matrix('matrix19', 3, 3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
matrix19.createArray()

matrix20 = Matrix('matrix20', 3, 3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
matrix20.createArray()

#################
#### VECTORS ####
#################

vector1 = Matrix('vector1', 1, 5, [[1, 0, 0, 0, 0], ])
vector1.createArray()

vector2 = Matrix('vector2', 1, 5, [[1, 0, 0, 0, 0], ])
vector2.createArray()

vector3 = Matrix('vector3', 1, 5, [[1, 0, 0, 0, 0], ])
vector3.createArray()

vector4 = Matrix('vector4', 1, 5, [[1, 0, 0, 0, 0], ])
vector4.createArray()

vector5 = Matrix('vector5', 1, 5, [[1, 0, 0, 0, 0], ])
vector5.createArray()

vector6 = Matrix('vector6', 1, 5, [[1, 0, 0, 0, 0], ])
vector6.createArray()

vector7 = Matrix('vector7', 1, 5, [[1, 0, 0, 0, 0], ])
vector7.createArray()

vector8 = Matrix('vector8', 1, 5, [[1, 0, 0, 0, 0], ])
vector8.createArray()

vector9 = Matrix('vector9', 1, 5, [[1, 0, 0, 0, 0], ])
vector9.createArray()

vector10 = Matrix('vector10', 1, 5, [[1, 0, 0, 0, 0], ])
vector10.createArray()

vector11 = Matrix('vector11', 1, 5, [[1, 0, 0, 0, 0], ])
vector11.createArray()

vector12 = Matrix('vector12', 1, 5, [[1, 0, 0, 0, 0], ])
vector12.createArray()

vector13 = Matrix('vector13', 1, 5, [[1, 0, 0, 0, 0], ])
vector13.createArray()

vector14 = Matrix('vector14', 1, 5, [[1, 0, 0, 0, 0], ])
vector14.createArray()

vector15 = Matrix('vector15', 1, 5, [[1, 0, 0, 0, 0], ])
vector15.createArray()

vector16 = Matrix('vector16', 1, 5, [[1, 0, 0, 0, 0], ])
vector16.createArray()

vector17 = Matrix('vector17', 1, 5, [[1, 0, 0, 0, 0], ])
vector17.createArray()

vector18 = Matrix('vector18', 1, 5, [[1, 0, 0, 0, 0], ])
vector18.createArray()

vector19 = Matrix('vector19', 1, 5, [[1, 0, 0, 0, 0], ])
vector19.createArray()

vector20 = Matrix('vector20', 1, 5, [[1, 0, 0, 0, 0], ])
vector20.createArray()

vectorI = Matrix('vector20', 1, 5, [[1, 0, 0, 0, 0], ])
vectorI.createArray()

vectorII = Matrix('vector20', 1, 5, [[1, 0, 0, 0, 0], ])
vectorII.createArray()

#####################
## PREVIOUS ANSWER ##
#####################

previous_answer = []

def vectorsValues(admin):
    list_of_vectors=[vector1.values, vector2.values, vector3.values, vector4.values, vector5.values, vector6.values, vector7.values, vector8.values, vector9.values, vector10.values, vector11.values, vector12.values, vector13.values, vector14.values, vector15.values, vector16.values, vector17.values, vector18.values, vector19.values, vector20.values]
    list_of_vectors_rows=[vector1.row, vector2.row, vector3.row, vector4.row, vector5.row, vector6.row, vector7.row, vector8.row, vector9.row, vector10.row, vector11.row, vector12.row, vector13.row, vector14.row, vector15.row, vector16.row, vector17.row, vector18.row, vector19.row, vector20.row]
    list_of_vectors_columns=[vector1.column, vector2.column, vector3.column, vector4.column, vector5.column, vector6.column, vector7.column, vector8.column, vector9.column, vector10.column, vector11.column, vector12.column, vector13.column, vector14.column, vector15.column, vector16.column, vector17.column, vector18.column, vector19.column, vector20.column]
    admin.vectors_arrays = list_of_vectors
    admin.vectors_rows = list_of_vectors_rows
    admin.vectors_columns = list_of_vectors_columns

def matricesValues(admin):
    list_of_matrices=[matrix1.values, matrix2.values, matrix3.values, matrix4.values, matrix5.values, matrix6.values, matrix7.values, matrix8.values, matrix9.values, matrix10.values, matrix11.values, matrix12.values, matrix13.values, matrix14.values, matrix15.values, matrix16.values, matrix17.values, matrix18.values, matrix19.values, matrix20.values]
    list_of_matrices_rows=[matrix1.row, matrix2.row, matrix3.row, matrix4.row, matrix5.row, matrix6.row, matrix7.row, matrix8.row, matrix9.row, matrix10.row, matrix11.row, matrix12.row, matrix13.row, matrix14.row, matrix15.row, matrix16.row, matrix17.row, matrix18.row, matrix19.row, matrix20.row]
    list_of_matrices_columns=[matrix1.column, matrix2.column, matrix3.column, matrix4.column, matrix5.column, matrix6.column, matrix7.column, matrix8.column, matrix9.column, matrix10.column, matrix11.column, matrix12.column, matrix13.column, matrix14.column, matrix15.column, matrix16.column, matrix17.column, matrix18.column, matrix19.column, matrix20.column]
    admin.matrices_arrays = list_of_matrices
    admin.matrices_rows = list_of_matrices_rows
    admin.matrices_columns = list_of_matrices_columns

def modifyMatricesArrays(admin,numberofmatrix,rows,columns,values):
    list_of_matrices_objects = [matrix1, matrix2, matrix3, matrix4, matrix5, matrix6, matrix7, matrix8, matrix9, matrix10, matrix11, matrix12, matrix13, matrix14, matrix15, matrix16, matrix17, matrix18, matrix19, matrix20]
    list_of_matrices_objects[numberofmatrix].row = rows
    list_of_matrices_objects[numberofmatrix].column = columns
    list_of_matrices_objects[numberofmatrix].values = values
    list_of_matrices_objects[numberofmatrix].createArray()

def modifyVectorsArrays(admin,numberofvector,rows,columns,values):
    list_of_vectors_objects = [vector1, vector2, vector3, vector4, vector5, vector6, vector7, vector8, vector9, vector10, vector11, vector12, vector13, vector14, vector15, vector16, vector17, vector18, vector19, vector20]
    list_of_vectors_objects[numberofvector].row = rows
    list_of_vectors_objects[numberofvector].column = columns
    list_of_vectors_objects[numberofvector].values = values
    list_of_vectors_objects[numberofvector].createArray()

def det(matrixtocalculatedeterminant):
    if isinstance (matrixtocalculatedeterminant, Matrix):
        result = linalg.det(matrixtocalculatedeterminant.array)
        return result
    else:
        raise ValueError("Can't calculate determinant of non-matrix")

def tr(matrixtotranspose):
    if isinstance (matrixtotranspose, Matrix):
        result_matrix_values=[]
        result = Matrix('result', matrixtotranspose.row, matrixtotranspose.column, [[1,0,0],])
        for x in range(0,matrixtotranspose.column):
            result_matrix_values.append(matrixtotranspose.array.transpose()[x])
        result.row=matrixtotranspose.column
        result.column=matrixtotranspose.row
        result.values = result_matrix_values
        result.createArray()
        return result
    else:
        raise ValueError("Can't transpose non-matrix")

def norm(vectortocalculatemagnitude):
    if isinstance (vectortocalculatemagnitude, Matrix):
        if vectortocalculatemagnitude.row == 1:
            result = np.linalg.norm(vectortocalculatemagnitude.array)
            return result
        else:
            raise ValueError("Number of rows must be 1")
    else:
        raise ValueError("Can't calculate magnitude of non-vector")

def sin(angle):
    try:
        if DEG_OR_RAD == "DEG":
            argument = angle * (np.pi / 180)
        if DEG_OR_RAD == "RAD":
            argument = angle
        result = np.sin(argument)
        return result
    except Exception as e:
        admin.equation_final_result = repr(e)

def cos(angle):
    try:
        if DEG_OR_RAD == "DEG":
            argument = angle * (np.pi / 180)
        if DEG_OR_RAD == "RAD":
            argument = angle
        result = np.cos(argument)
        return result
    except Exception as e:
        admin.equation_final_result = repr(e)

def tan(angle):
    try:
        if DEG_OR_RAD == "DEG":
            argument = angle * (np.pi / 180)
        if DEG_OR_RAD == "RAD":
            argument = angle
        result = np.tan(argument)
        return result
    except Exception as e:
        admin.equation_final_result = repr(e)

def arcsin(angle):
    try:
        if DEG_OR_RAD == "DEG":
            argument = angle * (np.pi / 180)
        if DEG_OR_RAD == "RAD":
            argument = angle
        result = np.arcsin(argument)
        return result
    except Exception as e:
        admin.equation_final_result = repr(e)

def arccos(angle):
    try:
        if DEG_OR_RAD == "DEG":
            argument = angle * (np.pi / 180)
        if DEG_OR_RAD == "RAD":
            argument = angle
        result = np.arccos(argument)
        return result
    except Exception as e:
        admin.equation_final_result = repr(e)

def arctan(angle):
    try:
        if DEG_OR_RAD == "DEG":
            argument = angle * (np.pi / 180)
        if DEG_OR_RAD == "RAD":
            argument = angle
        result = np.arctan(argument)
        return result
    except Exception as e:
        admin.equation_final_result = repr(e)

def sinh(angle):
    try:
        if DEG_OR_RAD == "DEG":
            argument = angle * (np.pi / 180)
        if DEG_OR_RAD == "RAD":
            argument = angle
        result = np.sinh(argument)
        return result
    except Exception as e:
        admin.equation_final_result = repr(e)

def cosh(angle):
    try:
        if DEG_OR_RAD == "DEG":
            argument = angle * (np.pi / 180)
        if DEG_OR_RAD == "RAD":
            argument = angle
        result = np.cosh(argument)
        return result
    except Exception as e:
        admin.equation_final_result = repr(e)

def tanh(angle):
    try:
        if DEG_OR_RAD == "DEG":
            argument = angle * (np.pi / 180)
        if DEG_OR_RAD == "RAD":
            argument = angle
        result = np.tanh(argument)
        return result
    except Exception as e:
        admin.equation_final_result = repr(e)

def arcsinh(angle):
    try:
        if DEG_OR_RAD == "DEG":
            argument = angle * (np.pi / 180)
        if DEG_OR_RAD == "RAD":
            argument = angle
        result = np.arcsinh(argument)
        return result
    except Exception as e:
        admin.equation_final_result = repr(e)

def arccosh(angle):
    try:
        if DEG_OR_RAD == "DEG":
            argument = angle * (np.pi / 180)
        if DEG_OR_RAD == "RAD":
            argument = angle
        result = np.arccosh(argument)
        return result
    except Exception as e:
        admin.equation_final_result = repr(e)

def arctanh(angle):
    try:
        if DEG_OR_RAD == "DEG":
            argument = angle * (np.pi / 180)
        if DEG_OR_RAD == "RAD":
            argument = angle
        result = np.arctanh(argument)
        return result
    except Exception as e:
        admin.equation_final_result = repr(e)

def Log(argument):
    try:
        result = np.log10(argument)
        return result
    except Exception as e:
        admin.equation_final_result = repr(e)

def In(argument):
    try:
        result = np.log(argument)
        return result
    except Exception as e:
        admin.equation_final_result = repr(e)

def Logchoosebase(base,argument):
    try:
        result = (np.log(argument))/(np.log(base))
        return result
    except Exception as e:
        admin.equation_final_result = repr(e)

def root(argument):
    try:
        result = np.lib.scimath.sqrt(argument)
        return result
    except Exception as e:
        admin.equation_final_result = repr(e)

def absolute(argument):
    try:
        result = np.absolute(argument)
        if result % 1 == 0:
            return int(result)
        else:
            return result
    except Exception as e:
        admin.equation_final_result = repr(e)

def loadChosenVectorValues(admin,chosenvector):
    chosenvector= chosenvector.replace("Vector", "vector")
    final_chosen_vector = nsp.parse(chosenvector)
    admin.chosen_vector_values = final_chosen_vector.array


def normalizeVector(vectortonormalize):
    return vectortonormalize / np.linalg.norm(vectortonormalize)

def ddToDms(dd):
   is_positive = dd >= 0
   dd = abs(dd)
   minutes,seconds = divmod(dd*3600,60)
   degrees,minutes = divmod(minutes,60)
   degrees = degrees if is_positive else -degrees
   return [degrees,minutes,seconds]

def angleOfVectors(vectorx, vectory):
    try:
        vectorx=vectorx.replace("Vector", "vector")
        vectory=vectory.replace("Vector", "vector")
        vector_x_parsed = nsp.parse(vectorx)
        vector_y_parsed = nsp.parse(vectory)
        vector_x_normalized = normalizeVector(vector_x_parsed.array)
        vector_y_normalized = normalizeVector(vector_y_parsed.array)
        result = np.arccos(np.clip(np.dot(vector_x_normalized[0], vector_y_normalized[0]), -1.0, 1.0))
        if DEG_OR_RAD == "DEG":
            if DD_OR_DMS == "DD":
                final_result = result * (180 / np.pi)
            if DD_OR_DMS == "DMS":
                dmsresult = ddToDms(result* (180 / np.pi))
                final_result = str(dmsresult[0])+"° "+str(dmsresult[1])+"\' "+str(dmsresult[2])+"\'\'"
        if DEG_OR_RAD == "RAD":
            final_result = result
        return ("The angle between the vectors is "+str(final_result))
    except Exception as e:
        return repr(e)

def createArrayForVectorsIAndII(vectorxvalues,vectoryvalues,vectorxcolumn,vectorycolumn):
    vectorI.values=vectorxvalues
    vectorI.column=vectorxcolumn
    vectorI.createArray()
    vectorII.values=vectoryvalues
    vectorII.column=vectorycolumn
    vectorII.createArray()


def getChosenMatrixValues(admin,chosenmatrix):
    chosenmatrix = chosenmatrix.replace("Matrix", "matrix")
    admin.chosen_matrix_object = nsp.parse(chosenmatrix)

def checkEigenvaluesType(listofeigenvalues):
    if all(isinstance(x, (sp.core.numbers.Integer,sp.core.numbers.One,sp.core.numbers.Float,sp.core.numbers.Zero,sp.core.numbers.NegativeOne)) for x in list(listofeigenvalues.keys())): 
        return "Go for Sympy"
    else:
        return "Go for Numpy"

def calculateEigenvectors(admin,matrixtoeigenize):
    matrixtoeigenize = matrixtoeigenize.replace("Matrix", "matrix")
    matrix_to_eigenize_parsed = nsp.parse(matrixtoeigenize)
    matrix_eigen_array = matrix_to_eigenize_parsed.array

    num_rows, num_cols = matrix_eigen_array.shape

    longest_decimal=1

    for x in range(0,num_rows):
        for y in range(0,num_cols):
            try:
                after_dot_places = str(matrix_eigen_array[x][y]).split(".",1)[1]
                if len(after_dot_places) > longest_decimal:
                    longest_decimal = len(after_dot_places)
                else:
                    pass
            except:
                pass

    matrix_eigen_array = matrix_eigen_array*(10**longest_decimal)
    matrix_eigen_array = matrix_eigen_array.astype(int)

    matrix_to_eigenize_symp = sp.Matrix(matrix_eigen_array)
    try:
        eigen_choose_module = checkEigenvaluesType(matrix_to_eigenize_symp.eigenvals())
    except:
        eigen_choose_module = "Go for Numpy"
    if eigen_choose_module == "Go for Sympy":
        eigenvectors_of_matrix = matrix_to_eigenize_symp.eigenvects()
        result = eigenvectors_of_matrix
        final_eigenvectors = []
        for x in range(0,len(result)):
            vectors_in_matrix_form = np.array(result[x][2]).tolist()
            vectors_for_value_list=[]
            for y in range(0,len(vectors_in_matrix_form)):
                individual_string_vector_list="(  "
                for z in range(0,len(vectors_in_matrix_form[y])):
                    individual_string_vector_list = individual_string_vector_list + str(vectors_in_matrix_form[y][z][0])+"  "
                individual_string_vector_list = individual_string_vector_list + ")"
                vectors_for_value_list.append(individual_string_vector_list)
            final_eigenvectors.append(vectors_for_value_list)
        for x in range(0,len(result)):
            result[x] = list(result[x])
        for x in range(0,len(result)):
            result[x][2] = final_eigenvectors[x]
        for x in range(0,len(result)):
            result[x][0] = result[x][0]/(10**longest_decimal)
    if eigen_choose_module == "Go for Numpy":
        result_eigenvalues, result_eigenvectors = np.linalg.eig(matrix_eigen_array)
        final_result=[]
        length_of_eigenvals=list(range(0,len(result_eigenvalues)))
        for x in result_eigenvalues:
            individualeigenvaluelist = [str(next(iter(result_eigenvalues))),"1",list(result_eigenvectors[:,next(iter(length_of_eigenvals))])]
            final_result.append(individualeigenvaluelist)
        result = final_result
       
    admin.eigen_vectors_result=result


def calculateSystemOfEquationsResult(admin,matrixofconstants,vectorofresults):
    matrixofconstants = matrixofconstants.replace("Matrix", "matrix")
    vectorofresults = vectorofresults.replace("Vector", "vector")
    matrix_of_constants_parsed = nsp.parse(matrixofconstants)
    vector_of_results_parsed = nsp.parse(vectorofresults)
    try:
        result = np.linalg.solve(matrix_of_constants_parsed.array,vector_of_results_parsed.array[0])
        list_of_ints = list(range(1,len(result)+1))
        for x in range(0,len(list_of_ints)):
                list_of_ints[x] = str(list_of_ints[x])

        list_of_ints = iter(list_of_ints)
        final_result=""

        for x in result:
                string_of_result = "X"+next(list_of_ints)+" = "+str(x)+"        "
                final_result = final_result +string_of_result
                
        admin.systems_of_equations_result = final_result
    except:
        try:
            result, residuals, rank, sing= np.linalg.lstsq(matrix_of_constants_parsed.array,vector_of_results_parsed.array[0],rcond=None)
            list_of_ints = list(range(1,len(result)+1))
            for x in range(0,len(list_of_ints)):
                    list_of_ints[x] = str(list_of_ints[x])

            list_of_ints = iter(list_of_ints)
            final_result="Couldn't calculate exact result, one result using the least squares method is:\n "

            for x in result:
                    string_of_result = "X"+next(list_of_ints)+" = "+str(x)+" "
                    final_result = final_result +string_of_result
                    
            final_result = final_result + "\n\nthe residuals are: \n {} \n\nthe rank of the coefficient matrix is: \n {} \n\nthe singular values of the coefficient matrix are: \n {} \n".format(residuals, rank, sing)
            admin.systems_of_equations_result = final_result
        except Exception as e:
            admin.systems_of_equations_result = repr(e)


################################
################################
#### ECUATION PARSER OBJECT ####
################################
################################


class NumericStringParser(object):
    '''
    This parser is based on the parser created by:

    author= Paul McGuire
    version = $Revision: 0.0 $
    date = $Date: 2009-03-20 $
    source= http://pyparsing.wikispaces.com/file/view/fourFn.py
    http://pyparsing.wikispaces.com/message/view/home/15549426

    Most of this code comes from the fourFn.py pyparsing example

    It's been modified to be used with the classes and functions in this module

    '''

    def pushFirst(self, strg, loc, toks):
        self.exprStack.append(toks[0])

    def pushUMinus(self, strg, loc, toks):
        if toks and toks[0] == '-':
            self.exprStack.append('unary -')

    def __init__(self):
        """
        expop   :: '^'
        multop  :: '*' | '/'
        addop   :: '+' | '-'
        integer :: ['+' | '-'] '0'..'9'+
        atom    :: π | ℇ | real | fn '(' expr ')' | '(' expr ')'
        factor  :: atom [ expop factor ]*
        term    :: factor [ multop factor ]*
        expr    :: term [ addop term ]*
        """
        point = Literal(".")
        e = CaselessLiteral("ℇ")
        fnumber = Combine(Word("+-" + nums, nums) +
                          Optional(point + Optional(Word(nums))) +
                          Optional(e + Word("+-" + nums, nums)))
        ident = Word(alphas, alphas + nums + "_$")
        plus = Literal("+")
        minus = Literal("-")
        mult = Literal("*")
        div = Literal("/")
        dotprod=Literal("@")
        crossprod=Literal("&")
        lpar = Literal("(").suppress()
        rpar = Literal(")").suppress()
        addop = plus | minus
        multop = mult | div | dotprod | crossprod
        expop = Literal("^")
        pi = CaselessLiteral("π")
        matrix20 = CaselessLiteral("matrix20")
        matrix19 = CaselessLiteral("matrix19")
        matrix18 = CaselessLiteral("matrix18")
        matrix17 = CaselessLiteral("matrix17")
        matrix16 = CaselessLiteral("matrix16")
        matrix15 = CaselessLiteral("matrix15")
        matrix14 = CaselessLiteral("matrix14")
        matrix13 = CaselessLiteral("matrix13")
        matrix12 = CaselessLiteral("matrix12")
        matrix11 = CaselessLiteral("matrix11")
        matrix10 = CaselessLiteral("matrix10")
        matrix9 = CaselessLiteral("matrix9")
        matrix8 = CaselessLiteral("matrix8")
        matrix7 = CaselessLiteral("matrix7")
        matrix6 = CaselessLiteral("matrix6")
        matrix5 = CaselessLiteral("matrix5")
        matrix4 = CaselessLiteral("matrix4")
        matrix3 = CaselessLiteral("matrix3")
        matrix2 = CaselessLiteral("matrix2")
        matrix1 = CaselessLiteral("matrix1")
        vector20 = CaselessLiteral("vector20")
        vector19 = CaselessLiteral("vector19")
        vector18 = CaselessLiteral("vector18")
        vector17 = CaselessLiteral("vector17")
        vector16 = CaselessLiteral("vector16")
        vector15 = CaselessLiteral("vector15")
        vector14 = CaselessLiteral("vector14")
        vector13 = CaselessLiteral("vector13")
        vector12 = CaselessLiteral("vector12")
        vector11 = CaselessLiteral("vector11")
        vector10 = CaselessLiteral("vector10")
        vector9 = CaselessLiteral("vector9")
        vector8 = CaselessLiteral("vector8")
        vector7 = CaselessLiteral("vector7")
        vector6 = CaselessLiteral("vector6")
        vector5 = CaselessLiteral("vector5")
        vector4 = CaselessLiteral("vector4")
        vector3 = CaselessLiteral("vector3")
        vector2 = CaselessLiteral("vector2")
        vector1 = CaselessLiteral("vector1")
        vectorII = CaselessLiteral("vectorII")
        vectorI = CaselessLiteral("vectorI")
        previous_answer = CaselessLiteral("previous_answer")
        expr = Forward()
        atom = ((Optional(oneOf("- +")) +
                 (ident + lpar + expr + rpar | pi | e | fnumber | matrix20 | matrix19 | matrix18 | matrix17 | matrix16 | matrix15 | matrix14 | matrix13 | matrix12 | matrix11 | matrix10 | matrix9 | matrix8 | matrix7 | matrix6 | matrix5 | matrix4 | matrix3 | matrix2 | matrix1 | vector20 | vector19 | vector18 | vector17 | vector16 | vector15 | vector14 | vector13 | vector12 | vector11 | vector10 | vector9 | vector8 | vector7 | vector6 | vector5 | vector4 | vector3 | vector2 | vector1 | previous_answer | vectorII | vectorI ).setParseAction(self.pushFirst))
                | Optional(oneOf("- +")) + Group(lpar + expr + rpar)
                ).setParseAction(self.pushUMinus)
        # by defining exponentiation as "atom [ ^ factor ]..." instead of
        # "atom [ ^ atom ]...", we get right-to-left exponents, instead of left-to-right
        # that is, 2^3^2 = 2^(3^2), not (2^3)^2.
        factor = Forward()
        factor << atom + \
            ZeroOrMore((expop + factor).setParseAction(self.pushFirst))
        term = factor + \
            ZeroOrMore((multop + factor).setParseAction(self.pushFirst))
        expr << term + \
            ZeroOrMore((addop + term).setParseAction(self.pushFirst))
        # addop_term = ( addop + term ).setParseAction( self.pushFirst )
        # general_term = term + ZeroOrMore( addop_term ) | OneOrMore( addop_term)
        # expr <<  general_term
        self.bnf = expr
        # map operator symbols to corresponding arithmetic operations
        epsilon = 1e-12
        self.opn = {"+": operator.add,
                    "-": operator.sub,
                    "*": operator.mul,
                    "/": operator.truediv,
                    "^": operator.pow,
                    "@": operator.matmul,
                    "&": operator.and_}
        self.fn = {"sin": sin,
                   "arcsin": arcsin,
                   "cos": cos,
                   "arccos": arccos,
                   "tan": tan,
                   "arctan": arctan,
                   "sinh": sinh,
                   "arcsinh": arcsinh,
                   "cosh": cosh,
                   "arccosh": arccosh,
                   "tanh": tanh,
                   "arctanh": arctanh,
                   "Log": Log,
                   "Logchoosebase": Logchoosebase,
                   "absolute": absolute,
                   "In": In,
                   "norm": norm,
                   "det": det,
                   "tr": tr,
                   "root": root,
                   "exp": math.exp,
                   "abs": abs,
                   "trunc": lambda a: int(a),
                   "round": round,
                   "sgn": lambda a: abs(a) > epsilon and cmp(a, 0) or 0}

    def evaluateStack(self, s):
        op = s.pop()
        if op == 'unary -':
            return -self.evaluateStack(s)
        if op in "+-*/^@&":
            op2 = self.evaluateStack(s)
            op1 = self.evaluateStack(s)
            return self.opn[op](op1, op2)
        elif op == "π":
            return np.pi 
        elif op == "ℇ":
            return np.e  
        elif op == "matrix20":
            return matrix20
        elif op == "matrix19":
            return matrix19
        elif op == "matrix18":
            return matrix18
        elif op == "matrix17":
            return matrix17
        elif op == "matrix16":
            return matrix16
        elif op == "matrix15":
            return matrix15
        elif op == "matrix14":
            return matrix14
        elif op == "matrix13":
            return matrix13
        elif op == "matrix12":
            return matrix12
        elif op == "matrix11":
            return matrix11
        elif op == "matrix10":
            return matrix10
        elif op == "matrix9":
            return matrix9
        elif op == "matrix8":
            return matrix8
        elif op == "matrix7":
            return matrix7
        elif op == "matrix6":
            return matrix6
        elif op == "matrix5":
            return matrix5
        elif op == "matrix4":
            return matrix4
        elif op == "matrix3":
            return matrix3
        elif op == "matrix2":
            return matrix2
        elif op == "matrix1":
            return matrix1
        elif op == "vector20":
            return vector20
        elif op == "vector19":
            return vector19
        elif op == "vector18":
            return vector18
        elif op == "vector17":
            return vector17
        elif op == "vector16":
            return vector16
        elif op == "vector15":
            return vector15
        elif op == "vector14":
            return vector14
        elif op == "vector13":
            return vector13
        elif op == "vector12":
            return vector12
        elif op == "vector11":
            return vector11
        elif op == "vector10":
            return vector10
        elif op == "vector9":
            return vector9
        elif op == "vector8":
            return vector8
        elif op == "vector7":
            return vector7
        elif op == "vector6":
            return vector6
        elif op == "vector5":
            return vector5
        elif op == "vector4":
            return vector4
        elif op == "vector3":
            return vector3
        elif op == "vector2":
            return vector2
        elif op == "vector1":
            return vector1
        elif op == "vectorII":
            return vectorII
        elif op == "vectorI":
            return vectorI
        elif op == "previous_answer":
            return previous_answer
        elif op in self.fn:
            return self.fn[op](self.evaluateStack(s))
        elif op[0].isalpha():
            return 0
        else:
            return float(op)

    def parse(self, num_string, parseAll=True):
        self.exprStack = []
        results = self.bnf.parseString(num_string, parseAll)
        val = self.evaluateStack(self.exprStack[:])
        return val

nsp = NumericStringParser()

##############################
##############################
#### FUNCTION TO PARSE EQ ####
##############################
##############################

def getEquationResult(admin,equation):
    global previous_answer
    equation = equation.replace("√", "root")
    equation = equation.replace("Vector", "vector")
    equation = equation.replace("Matrix", "matrix")
    equation = equation.replace("ans", "previous_answer")
    equation = equation.replace("Ans", "previous_answer")
    equation = equation.replace("print", " ")
    equation = equation.replace("__", " ")
    equation = equation.replace("import", " ")
    equation = equation.replace("from", " ")
    equation = equation.replace("os.", " ")
    equation = equation.replace("eval", " ")
    equation = equation.replace("exec", " ")
    equation = equation.replace("init", " ")
    equation = equation.replace("delete", " ")
    equation = equation.replace("run", " ")
    equation = equation.replace("exe", " ")
    equation = equation.replace("return", " ")
    try:
        equation_result = nsp.parse(equation)
        if isinstance (equation_result, Matrix):
            admin.is_equation_result_matrix = True
            admin.is_equation_result_int_or_float = False
            admin.is_equation_result_complex = False
            previous_answer = equation_result
        elif isinstance (equation_result, (int, float)):
            admin.is_equation_result_int_or_float = True
            admin.is_equation_result_matrix = False
            admin.is_equation_result_complex = False
            previous_answer = equation_result
        elif isinstance (equation_result, np.complex_):
            admin.is_equation_result_int_or_float = False
            admin.is_equation_result_matrix = False
            admin.is_equation_result_complex = True
            previous_answer = equation_result
        else:
            admin.is_equation_result_int_or_float = False
            admin.is_equation_result_matrix = False
            admin.is_equation_result_complex = False
        admin.equation_final_result = equation_result
    except Exception as e:
        admin.equation_final_result = repr(e)