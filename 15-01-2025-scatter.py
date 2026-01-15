import matplotlib.pyplot as plt


x = [5, 7, 8, 7, 2, 17, 2, 9]
y = [99, 86, 71, 78, 100, 81, 103, 87]
z=[108,65,88,100,60,70,80,90]

c = ["r","g","b","yellow","pink","purple","teal","red"]
s = [150,300,300,400,500,100,200,400]

# color: for colors of marks
# marker: change the shape of marker 
# - "o" → Circle
# - "s" → Square
# - "^" → Triangle up
# - "v" → Triangle down
# - "D" → Diamond
# - "*" → Star
# - "+" → Plus
# - "x" → Cross
# - "." → Point

# sizes/s : changes the sizes of marks
# edgecolor: chages the border color of marks 
# edgecolors : takes an array of arrays
# linewidth: chages the border width of marks
# linewidths: takes array of widths

plt.scatter(x, y,color=c,marker=".",sizes=s,edgecolor="teal",linewidth=2)
plt.scatter(x,z,color="orange",sizes=s,edgecolors="black",marker="+")
plt.title("Scatter Plot")
plt.grid()
plt.show()


# data = [22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5]
# plt.hist(data, bins=5, color='skyblue', edgecolor='black')
# plt.title("Histogram")
# plt.show()



