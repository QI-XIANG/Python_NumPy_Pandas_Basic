# NumPy arrays use idex to get value
import numpy as np
from numpy.core.fromnumeric import size
np.random.seed(0) # keep random result all the same in execution every time
# np.random.seed(random_state)

a1 = np.random.randint(10,size=6) # generate a array with 6 elements (0~9)
a1[1:4] = 2 # change value to 2 for index 1 to 3
a1[:] = 0 # change value to 0 for all elements

#===========================================================================================

# Numpy array: slicing array
a = np.arange(10) # return numbers from 0 to 9
print(a[4:7])

# Numpy array: reshaping array
originalArray = np.arange(1,10) # return number from 1 to 9
reshapingArray = originalArray.reshape((3,3)) # reshape the array to be a 3*3 array

#===========================================================================================
