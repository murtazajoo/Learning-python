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


#sum of elements of array 
print("sum of ele of arr",np.sum(arr))


#mean of elements of array 
print("mean of ele of arr",np.mean(arr))


#median of elements of array 
print("median of ele of arr",np.median(arr))