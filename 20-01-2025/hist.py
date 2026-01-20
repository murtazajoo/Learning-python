import numpy as np
import matplotlib.pyplot as plt


# x = np.random.randint(0,50,100)
y = [7, 10, 33, 9, 22, 45, 0, 39, 10, 28, 31, 31, 32, 23, 7, 25, 9, 5, 18, 8, 39, 31, 48, 0, 9, 8, 39, 25, 5, 17, 25, 21, 25, 31, 35, 35, 38, 14, 6, 23, 38, 30, 12, 25, 24, 42, 41, 45, 6, 30, 27, 31, 38, 1, 25, 39, 37, 33, 22, 44, 4, 48, 35, 0, 45, 4, 34, 22, 22, 29, 15, 9, 32, 1, 23, 34, 37, 6, 49, 24, 30, 46, 12, 49, 5, 2, 44, 40, 32, 21, 25, 27, 5, 25, 19, 9, 19, 41, 25, 16]

# bins : number of bars
# bottom: changes the values of the y axis start
# histype: chages appearance 
# - bar
# - barfilled
# - stepfilled
# - step
# rwidth: used to change the bar width (0-1)
# log: y axis values shows in log

plt.hist(y,label="Deaths",color="orange",edgecolor="black",bins=20,bottom=10,histtype="bar",orientation="vertical",rwidth=1,log=False)
plt.title("Death Histogram")
plt.xlabel("x label")
plt.ylabel("y label")
plt.grid()
plt.legend()
plt.show()