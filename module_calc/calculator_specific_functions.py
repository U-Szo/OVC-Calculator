from .matrix_class import Matrix
import numpy as np
from scipy import linalg
import math

DEG_OR_RAD="RAD"

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
        result.create_array()
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
    if DEG_OR_RAD == "DEG":
        argument = angle * (np.pi / 180)
    if DEG_OR_RAD == "RAD":
        argument = angle
    result = np.sin(argument)
    return result

def cos(angle):
    if DEG_OR_RAD == "DEG":
        argument = angle * (np.pi / 180)
    if DEG_OR_RAD == "RAD":
        argument = angle
    result = np.cos(argument)
    return result

def tan(angle):
    if DEG_OR_RAD == "DEG":
        argument = angle * (np.pi / 180)
    if DEG_OR_RAD == "RAD":
        argument = angle
    result = np.tan(argument)
    return result

def arcsin(angle):
    if DEG_OR_RAD == "DEG":
        argument = angle * (np.pi / 180)
    if DEG_OR_RAD == "RAD":
        argument = angle
    result = np.arcsin(argument)
    return result

def arccos(angle):
    if DEG_OR_RAD == "DEG":
        argument = angle * (np.pi / 180)
    if DEG_OR_RAD == "RAD":
        argument = angle
    result = np.arccos(argument)
    return result

def arctan(angle):
    if DEG_OR_RAD == "DEG":
        argument = angle * (np.pi / 180)
    if DEG_OR_RAD == "RAD":
        argument = angle
    result = np.arctan(argument)
    return result

def sinh(angle):
    if DEG_OR_RAD == "DEG":
        argument = angle * (np.pi / 180)
    if DEG_OR_RAD == "RAD":
        argument = angle
    result = np.sinh(argument)
    return result

def cosh(angle):
    if DEG_OR_RAD == "DEG":
        argument = angle * (np.pi / 180)
    if DEG_OR_RAD == "RAD":
        argument = angle
    result = np.cosh(argument)
    return result

def tanh(angle):
    if DEG_OR_RAD == "DEG":
        argument = angle * (np.pi / 180)
    if DEG_OR_RAD == "RAD":
        argument = angle
    result = np.tanh(argument)
    return result

def arcsinh(angle):
    if DEG_OR_RAD == "DEG":
        argument = angle * (np.pi / 180)
    if DEG_OR_RAD == "RAD":
        argument = angle
    result = np.arcsinh(argument)
    return result

def arccosh(angle):
    if DEG_OR_RAD == "DEG":
        argument = angle * (np.pi / 180)
    if DEG_OR_RAD == "RAD":
        argument = angle
    result = np.arccosh(argument)
    return result

def arctanh(angle):
    if DEG_OR_RAD == "DEG":
        argument = angle * (np.pi / 180)
    if DEG_OR_RAD == "RAD":
        argument = angle
    result = np.arctanh(argument)
    return result

def logarithm_base_ten(argument):
    result = np.log10(argument)
    return result

def logarithm_base_e(argument):
    result = np.log(argument)
    return result

def root(argument):
    result = np.lib.scimath.sqrt(argument)
    return result

def absolute(argument):
    result = np.absolute(argument)
    if result % 1 == 0:
        return int(result)
    else:
        return result

def normalize_vector(vectortonormalize):
    return vectortonormalize / np.linalg.norm(vectortonormalize)

