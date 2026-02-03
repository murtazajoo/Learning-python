from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Load image
img = Image.open("cat.webp")
label = "cat"

plt.imshow(img)
plt.title(f'Title: {label}')

points = [(522, 186),
(690,267),
(919,273),
(1087,186),
(1090,315),
(1019,402),
(1109,977),
(1035,1035),
(822,1044),
(458,1050),
(309,877),
(454,435),
(554,458),
(587,409),
(519,309),
(522, 186)]

polygon = Polygon(points, fill=False, linewidth=3, edgecolor="red",closed=True)
plt.gca().add_patch(polygon)

for x,y in points:
    plt.scatter(x,y,c="pink")

plt.text(522, 186, "cat", color="red")

plt.axis("off")
plt.show()