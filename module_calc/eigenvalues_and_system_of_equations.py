import numpy as np
from scipy import linalg
import sympy as sp
sp.init_printing(use_unicode=True)


def check_eigenvalues_type(listofeigenvalues):
    if all(isinstance(x, (sp.core.numbers.Integer,sp.core.numbers.One,sp.core.numbers.Float,sp.core.numbers.Zero,
                        sp.core.numbers.NegativeOne)) for x in list(listofeigenvalues.keys())): 
        return "Go for Sympy"
    else:
        return "Go for Numpy"

def calculate_eigenvectors(matrix_to_eigenize_parsed):
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
        eigen_choose_module = check_eigenvalues_type(matrix_to_eigenize_symp.eigenvals())
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
       
    return result


def calculate_system_of_equations_result(matrix_of_constants_parsed,vector_of_results_parsed):
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
                
        return final_result
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
            
            return final_result
        except Exception as e:

            return repr(e)

