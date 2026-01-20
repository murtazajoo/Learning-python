import numpy as np

arr1 = np.array([[2,3],[4,5]])
arr2 = np.array([[5,6],[7,8]])

print(arr1 + arr2)
print(np.add(arr1, arr2))

arr = np.array([10, 20, 5, 15, 25])

print("min number", np.min(arr))
print("index of min num", np.argmin(arr))

print("max num in array", np.max(arr))
print("index of max num", np.argmax(arr))

print("square root", np.sqrt(arr))
print("sin values", np.sin(arr))
print("cos values", np.cos(arr))
print("tan values", np.tan(arr))

print("sum of arr", np.sum(arr))
print("mean of arr", np.mean(arr))
print("median of arr", np.median(arr))
print("standard deviation of arr", np.std(arr))

arr3 = np.array([[2,1],[1,3]])
arr4 = np.array([[4,2],[3,1]])

print("dot product", np.dot(arr3, arr4))
print("inverse of arr3", np.linalg.inv(arr3))
print("determinant of arr4", np.linalg.det(arr4))


a = np.array([1,2,3,4])

print(a[1]) 
print(a[-2]) 

a2d = np.array([[1,2],[3,4]])

print(a2d[0,1]) 
print(a2d[-2,-2]) 


a3d = np.array([[[1,2],[2,3]],[[3,4],[4,5]],[[1,2],[2,3]]])

print(a3d[0,1,1]) 
print(a3d[-2,-2,-2]) 


sin = np.sin(a)
print(sin)

#cos
cos = 1/sin
print(cos)

#tan
tan = sin/cos
print(tan)

#cot
cot = cos/sin
print(cot)
#cosec
cosec = 1/sin
print(cosec)

#sec
sec = 1/cos
print(sec)

#================================================================================

#OUTPUTS

# $ python 13-01-2026-extra-examples.py
# [[ 7  9]
#  [11 13]]
# [[ 7  9]
#  [11 13]]
# min number 5
# index of min num 2
# max num in array 25
# index of max num 4
# square root [3.16227766 4.47213595 2.23606798 3.87298335 5.        ]
# sin values [-0.54402111  0.91294525 -0.95892427  0.65028784 -0.13235175]
# cos values [-0.83907153  0.40808206  0.28366219 -0.75968791  0.99120281]
# tan values [ 0.64836083  2.23716094 -3.38051501 -0.8559934  -0.13352641]
# sum of arr 75
# mean of arr 15.0
# median of arr 15.0
# standard deviation of arr 7.0710678118654755
# dot product [[11  5]
#  [13  5]]
# inverse of arr3 [[ 0.6 -0.2]
#  [-0.2  0.4]]
# determinant of arr4 -2.0
# 2
# 3
# 2
# 1
# 3
# 3
# [ 0.84147098  0.90929743  0.14112001 -0.7568025 ]
# [ 1.18839511  1.09975017  7.0861674  -1.32134871]
# [0.70807342 0.82682181 0.01991486 0.57275002]
# [ 1.41228293  1.20945044 50.21376836  1.74596241]
# [ 1.18839511  1.09975017  7.0861674  -1.32134871]
# [ 0.84147098  0.90929743  0.14112001 -0.7568025 ]