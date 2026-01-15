import matplotlib.pyplot as plt

#------------------------------------------------------
# Bar Graph 
# used for comparision

x = ["JAVA", "JS", "C", "Python"]
y = [3, 7, 2, 9]
z = [10,9,12,14]
# width parameter: change the width of each bar
# color parameter: change the color the bars also pass an list of colors
# align: aligns the bar label (edge/center)
# edgecolor: changes the color of border of bars (list of colors / color)
# linewidth: changes the width of the border of bars
# linestyle: changes the style of lines (dotted (:) /solid)
# alpha: lightens the color of a graph (0-1)
plt.bar(x, y,width=0.6,color="pink",align="edge",edgecolor="purple",linewidth=3,linestyle=":",alpha=0.9)


c=["teal","purple","red","green"]
ec = ["pink","yellow","purple","teal"]

#here we pass the color as list  
plt.bar(x, z,color=c,edgecolor=ec,linewidth=1.3,width=0.6)

#used to set the title of the graph 
plt.title("Bar Chart")

# used to lable the sides of the graph 
# fontsize parameter used to change the font size of the labels
plt.xlabel("languages", fontsize = 16)
plt.ylabel("Popular", fontsize = 16)

plt.show()

#-----------------------------------------------

# VERTICAL BAR GRAPH ---- barh()
# height: height of the bars 
plt.barh(x, y,color="pink",height=0.6,align="edge",edgecolor="purple",linewidth=3,linestyle=":",alpha=0.9)
plt.barh(x, z,color=c,edgecolor=ec,linewidth=1.3,height=0.4)


plt.show()





















# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 99 , 10]

# plt.plot(x, y)
# plt.title("Line Plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()


# x = [5, 7, 8, 7, 2, 17, 2, 9]
# y = [99, 86, 87, 88, 100, 86, 103, 87]

# plt.scatter(x, y)
# plt.title("Scatter Plot")
# plt.show()


# data = [22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5]
# plt.hist(data, bins=5, color='skyblue', edgecolor='black')
# plt.title("Histogram")
# plt.show()



