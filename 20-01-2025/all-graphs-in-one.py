import matplotlib.pyplot as plt
plt.title("Graphs")
plt.grid()

x = [3, 7, 2, 9]
x2 = [31, 17, 12, 19]
plt.subplot(2,2,1)
plt.plot(x,x2)


y =["a","b","c","d"]
y1= [10,20,30,40]
plt.subplot(2,2,2)

plt.bar(y,y1)


z = [10,20,30,40]
z1 =["a","b","c","d"]
plt.subplot(2,2,3)

plt.pie(z,labels=z1)

plt.show()