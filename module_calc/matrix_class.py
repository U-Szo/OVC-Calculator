import numpy as np

class Matrix:
    def __init__(self, vmname, rown, columnn, values):
        self.row = rown
        self.column = columnn
        self.values = values
        self.name = vmname

    def create_array(self):
        self.matrix_of_floats = []

        for x in range(0,self.row):
            list_of_rows=[]
            for y in range(0,self.column):
                cell_value=""
                cell_value = str(self.values[x][y])
                cell_value_converted = self.convert_to_float(cell_value)
                list_of_rows.append(cell_value_converted)
            self.matrix_of_floats.append(list_of_rows)

        self.array = np.array(self.matrix_of_floats)

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

    def __add__(self, other):
        result_of_addition=Matrix(self.name,self.row,self.column,self.values)
        if isinstance (other, Matrix):
            if other.array.shape == self.array.shape:
                result_of_addition.values = self.array + other.array
                result_of_addition.create_array()   
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
                result_of_subtraction.create_array()   
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
        result_of_multiplication=None
        if isinstance (other, Matrix):
            result_of_multiplication=Matrix(self.name,self.row,other.column,self.values)
            result_of_multiplication.values = np.matmul(self.array,other.array)
            result_of_multiplication.create_array()   
        elif isinstance (other, (int, float)):
            result_of_multiplication=Matrix(self.name,self.row,self.column,self.values)
            result_of_multiplication.values = self.array * other
            result_of_multiplication.create_array() 
        elif isinstance (other, (np.complex_,complex)):
            raise ValueError("Can't multiply matrix to complex")
        return result_of_multiplication

    def __rmul__(self, other):
        return self.__mul__(other)

    def __pow__(self, other):
        result_of_power=Matrix(self.name,self.row,self.column,self.values)
        result_of_power.create_array()
        other = format_number(other)
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
            result_of_crossproduct.create_array()
        else:
            raise ValueError("Can't use cross product with non-vector")
        return result_of_crossproduct

    def format_number(num):
        if num % 1 == 0:
            return int(num)
        else:
            return num

