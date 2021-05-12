# Exercise for getting specific value from NumPy array 1
import numpy as np 
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[:2,1:])
print(arr[2,:])
print(arr[:,:2])
print(arr[1,:2])
print(np.array([arr[0,:2],arr[2,:2]]))

#===========================================================================

# Exercise for getting specific value from NumPy array 2
name = np.array(["Tony","Lura","Wangwu","Zack","Mimi"])
gender = np.array(["male","female","male","male","female"])
height = np.array([172,155,183,153,168])
weight = np.array([75.2,45.6,84.3,72.1,51.0])
score_math = np.array([45,74,62,89,32])
score_english = np.array([92,85,28,61,78])
score_chinese = np.array([88,55,70,61,98])

print(name[gender=='female'])
print(name[np.logical_and(gender=='female',height>160)])
print(score_chinese[gender!='female'].mean())
print(name[score_english<60])



