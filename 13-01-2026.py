import numpy as np

arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[1,2],[3,4]])

print(arr1+arr2)
print(np.add(arr1,arr2))


arr = np.array([1,2,3,4,0])
#find min num in array 
print("min number " ,np.min(arr))

#get postion of the min
print("index of min num ",np.argmin(arr))


#find max num in array 
print("max num in array ",np.max(arr))

#get postion of the max
print("index of max num ",np.argmax(arr))

#finds the square root of all numbers in array 
print("square root  ",np.sqrt(arr))

#gives the sin value of each numebr in the array same for others 
print("sin values",np.sin(arr))
print("cos values",np.cos(arr))
print("tan values",np.tan(arr))

#----------------------------------------------------------------------------------
# STATISTICAL FUNCTIONS


#sum of elements of array 
print("sum of ele of arr",np.sum(arr))
#output: sum of ele of arr 10

#mean of elements of array 
print("mean  of arr",np.mean(arr))
#output:mean  of arr 2.0

#median of elements of array 
print("median of arr",np.median(arr))
#output: median of arr 2.0

#stanndard deviation of elements of array 
print("stanndard deviation of arr",np.std(arr))
#output: stanndard deviation of arr 1.4142135623730951

#----------------------------------------------------------------------------------
# LINEAR ALGEBRA FUNCTIONS

arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[6,7],[5,9]])

#dot product of two matrix
print("dot prduct of arr1 . aar2 = ",np.dot(arr1,arr2))
# output
# [[16 25]
#  [38 57]]


#inverse of a matrix
print("inverse of arr1 " , np.linalg.inv(arr1))
#output 
# [[-2.   1. ]
#  [ 1.5 -0.5]]


#determinant of a matrix
print("determinant of arr2 = ",np.linalg.det(arr2))
#output 
#18.999999999999996




#----------------------------------------------------------------------------------

arr = np.array([[1,2],[3,4]])

#covert to 1D

print(arr.flatten())
#ouput: [1 2 3 4]

#LOG
print(np.log(arr))
# output: 
# [[0.         0.69314718]
#  [1.09861229 1.38629436]]



#---------------------------------------------------------------------------------

arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[6,7],[5,9]])
#combine two arrays
print(np.concatenate((arr1,arr2)))
#output: [[1 2]
#  [3 4]
#  [6 7]
#  [5 9]]


#---------------------------------------------------------------------------------


# INDEXING In Array 

a = np.array([1,2,3,4])

print(a[1]) #ouput: 2
print(a[-2]) #output: 3

a2d = np.array([[1,2],[3,4]])

print(a2d[0,1]) #ouput: 2
print(a2d[-2,-2]) #output: 1


#---------------------------------------------------------------------------------


sin = np.sin(a)
print(sin)
#output: [ 0.84147098  0.90929743  0.14112001 -0.7568025 ]

#cos
cos = 1/sin
print(cos)
#output: [ 1.18839511  1.09975017  7.0861674  -1.32134871]

#tan
tan = sin/cos
print(tan)
#output: [0.70807342 0.82682181 0.01991486 0.57275002]


#cot
cot = cos/sin
print(cot)
#output: [ 1.41228293  1.20945044 50.21376836  1.74596241]

#cosec
cosec = 1/sin
print(cosec)
#output: [ 1.18839511  1.09975017  7.0861674  -1.32134871]

#sec
sec = 1/cos
print(sec)
#output: [ 0.84147098  0.90929743  0.14112001 -0.7568025 ]

