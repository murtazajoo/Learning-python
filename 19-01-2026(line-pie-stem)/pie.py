import matplotlib.pyplot as plt


x = [5, 9, 4, 3]
x1 = [2,4,6,7]
y = ["C","Python","Java","C++"]
ex = [0,0.1,0,0]
c = ["orange","cyan","teal","purple"]





# labels: used to give labels to different pies
# explode: an array to seperate a part of garph give space in between
# colors: an array of colors
# autopct:  Format string or function to label wedges with percentage.
# shadow : adds a depth effect
# radius : chages the radius og the pie 
# labeldistance :  the distace between the chart and the labels
# startangle: change the start the angle that is rotate the graph  
# wedgeprops: Dict of wedge properties (edgecolor, linewidth, etc.).
# frame: Draw axes frame around pie.
# textprops : Dict of text properties for labels.

plt.figure(figsize=(15,12))
plt.pie(x,counterclock=False,labels=y,explode=ex,colors=c,autopct="%1.2f%%",shadow=True,radius=1.2,labeldistance=None,startangle=90,
    wedgeprops={'linewidth':2, 'edgecolor':'black'},frame=True,textprops={"fontsize":12},pctdistance=0.8
)
plt.pie(x1,labels=y,startangle=90,shadow=True,labeldistance=None,wedgeprops={"edgecolor":"pink",'linewidth':4,"linestyle":"solid","alpha":0.99},radius=0.8,autopct="%0d%%",pctdistance=0.4)


plt.title("Pie Chart of Popular Languages")
plt.tight_layout()
plt.legend(loc="best")
plt.show()

