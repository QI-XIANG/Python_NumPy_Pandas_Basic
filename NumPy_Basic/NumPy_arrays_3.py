# NumPy array: joining 
import numpy as np
array_one = np.array([1,2,3])
array_two = np.array([4,5,6])
array_combine = np.concatenate([array_one,array_two]) # append array_two at the end of array_one
array_add = array_one + array_two
array_2d = np.array([array_one,array_two])

#===========================================================================================

# NumPy array: spliting 切割
array_three = np.concatenate([array_one,array_two])
array_four, array_five,array_six = np.split(array_three,3)

# [x,y] -> [:2] , [2:3] , [3:]
array_four, array_five,array_six = np.split(array_three,[2,3])

#===========================================================================================

# NumPy array: fancy indexing
nameListArray = np.array(['Anna','Tina','Marvin','Cindy'])
selectedArray = np.array(nameListArray[[2,3]]) # same as np.array(nameListArray[2:])

#===========================================================================================

# Numpy array: sorting
originalArray = np.array([2,1,4,3,5])
sortedArray = np.sort(originalArray) # ascending
sortedArray = np.sort(originalArray)[::-1] # descending

# Numpy array: sorting with specific data type
dataTypes = [('name','S10'),('score',int)]
dataValues = [('John',80),('Marry',60),('Ryan',90),('Leon',40)]
originalArray = np.array(dataValues,dtype = dataTypes)
sortedArray = np.sort(originalArray,order='score')[::-1] # descending

#===========================================================================================

# Aggregation
myArray = np.array([1,2,3,4,5])
print(sum(myArray))
print(myArray.max())
print(myArray.min())
print(myArray.sum())

#===========================================================================================