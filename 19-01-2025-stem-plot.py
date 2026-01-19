import matplotlib.pyplot as plt


# stem plot used for exact values

x = [0.1,0.2,0.3,0.4,0.5,0.6,]
y = [2,4,6,2,6,4]




# linefmt : dotted or solid line
#  markerfmt : used the shape of the marker at th top of evry line
# basefmt: chage the appearacnce of balse line
#  orientation: change the orientation
#  label: used with legend function
# bottom: baseline distance from y axis
plt.stem(x,y,linefmt="r:",markerfmt="rD",basefmt="red",orientation="horizontal",label="Function",bottom=9)

plt.legend()

plt.show()