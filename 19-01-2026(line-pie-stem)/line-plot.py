import matplotlib.pyplot as plt



x = [0.1,1.1,1.5,2.4,3.5,4.6]
x1 = [3,4,2,5,3,8]
y = [2.3,3.6,6,2,6,1]



# color: changes tyhe color of the line
# linestyle : changes the style of the line
#  marker: marks the data values
#  markerfacecolor : used co chage the color of the marker
#  markeredgecolor: change edge color of the marker 

plt.plot(x,y,color="black",marker="D",markerfacecolor="pink",markeredgecolor="orange",label="first",linewidth=2)
plt.plot(x,x1,color="black",linestyle=":",marker="^",label="second")


plt.xlabel("THIS IS X")
plt.ylabel("THIS IS Y")
plt.title("Title of the graph")
plt.grid()
plt.legend()
plt.show()


