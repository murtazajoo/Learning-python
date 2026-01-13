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