# NumPy arrays vs. Python List
import numpy as np
from numpy.core.fromnumeric import size
myList = [True,"Bob",3.0,4]
myListTypeList = [type(item) for item in myList] # data type in python list can be various

myArray = np.array([True,"Bob",3.0,4]) # data type in numpy array would be all the same
myArrayTypeList = [type(item) for item in myArray]

#===========================================================================================

# Execution time
my_list = list(range(1000000))
%time my_list2 = [x*2 for x in my_list]

my_arr = np.array(my_list)
%time my_arr = my_arr*2 # double each element in array

# Execution time: NumPy array win !

#===========================================================================================

# Arithmetic operations with NumPy Array (without for-loop)
arr = np.array([[1,2,3],[4,5,6]])
arr.dtype # show data type of element
print(1/arr)
print(arr*0.5)
print(arr*arr)

# Generate boolean array for comparing two arrays directly
arr2 = np.array([[0,4,1],[7,2,12]])
print(arr > arr2)

#===========================================================================================

# Create array and some common attributes
a3 = np.random.randint(10,size=(3,4,5)) # Create a random array (3*4*5) with 0~9
print(a3.ndim) # ndim
print(a3.shape) # elememts in each ndim 
print(a3.size) # number of elements

# Create array with all zero
zero_array = np.zeros(10) # fill ten 0 elements
zero_2d_array = np.zeros((3,6)) # fill the 2d array (3*6) with all 0

#===========================================================================================

# Observation for NumPy array's data type

float_array = np.array([1.0,2.0,3.0,4.0,5.0])
float_array.dtype # show element's data type

int_array = float_array.astype(np.int32) # change data type
int_array.dtype

#===========================================================================================