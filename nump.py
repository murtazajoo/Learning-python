import numpy as np

arr = np.array([1,2,3,4],ndmin=10)

print(arr.ndim,"d")
print(arr)
print()

arr2 = np.array([[1,2,3,4]])
arr2d = np.array([[1,2,3,4],[5,6,7,8]])
print(arr2.ndim,"d")
print(arr2d.ndim,"d")
print(arr2)
print(arr2d)
print()
print()

arr3 = np.array([[[1,2,3,4]]])
arr3d = np.array([[[1,2,3,4],[4,5,6,8]],[[5,6,7,8],[1,2,3,4]],[[5,6,7,8],[1,2,3,4]]])
print(arr3.ndim,"d")
print(arr3d.ndim,"d")
print(arr3,"single")
print(arr3d)

print()
print()


arrx = np.ones(4)
print(arrx)


print()
print()

arrx = np.ones((4, 3))  
print(arrx)

print()
print()

arrx = np.zeros(4)
print(arrx)

print()
print()

arrx = np.zeros((4, 3))   # shape must be a tuple
print(arrx)


print()
print()

arrx = np.empty(4)
print(arrx)


print()
print()

arrx = np.arange(5)
print(arrx)

print()
print()


arrx = np.eye(5)
print(arrx)

print()
print()


arrx = np.linspace(0,20,num=9)
print(arrx)

print()
print()


arrx = np.random.rand(5)
print(arrx)

print()
print()


arrx = np.random.randn(5)
print(arrx)

print()
print()

arrx = np.random.randn(5,5)
print(arrx)

print()
print()

arrx = np.random.ranf()
print(arrx)

print()
print()


arrx = np.random.randint(-50,10,5)
print(arrx)

print()
print()

arr = np.arange(6)
x = arr + 3
arr+=99

print("X= " ,x)
print()
print("NP.ADD x",np.add(x,3))
print()

print("adding two arrays using +  ",arr+x)
print("using np.add()  ",np.add(x,arr))



x = arr - 1

print("X= " ,x)
print()
print("NP.substract x",np.subtract(x,3))
print()

print("substracting two arrays using +  ",arr-x)
print("using np.subtract()  ",np.subtract(x,arr))



x = arr * 3


print("X= " ,x)
print()
print("NP.multiply x",np.multiply(x,3))
print()

print("multiplying two arrays using +  ",arr*x)
print("using np.multiply()  ",np.multiply(x,arr))


x = arr / 3


print("X= " ,x)
print()
print("NP.divide x",np.divide(x,3))
print()

print("divideing two arrays using +  ",arr/x)
print("using np.divide()  ",np.divide(x,arr))

x = arr % 3
x = np.arange(6)
x+=1

print("X= " ,x)
print()
print("NP.mod x",np.mod(x,3))
print()

print("moding two arrays using +  ",arr%x)
print("using np.mod()  ",np.mod(x,arr))



x = arr ** 3


print("X= " ,x)
print()
print("NP.power x",np.power(x,3))
print()

print("powering two arrays using +  ",arr**x)
print("using np.power()  ",np.power(x,arr))







