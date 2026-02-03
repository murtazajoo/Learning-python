from PIL import Image
import cv2

import matplotlib.pyplot as plt


# img = Image.open("cat.webp")
# label = "cat"
# plt.imshow(img)
# plt.title(f'Title: {label}') 
# plt.axis("off")

# plt.show()



img = cv2.imread("cat.webp")        
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  

plt.imshow(img)
x = 324
y = 170
plt.gca().add_patch(plt.Rectangle((x,y),800,870,fill=False,linewidth=2,edgecolor="red"))
plt.text(x-20,y-10,"cat",color="red")
plt.axis("off")

plt.show()