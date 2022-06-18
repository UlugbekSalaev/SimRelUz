#from tkinter import font

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from scipy.stats import gaussian_kde
import pandas as pd

data= pd.read_csv("data.csv")
#xpoints = data[:,0]  #xpoints = np.array([1,2,3])
#ypoints = data[:,1]  #ypoints = np.array([4,5,6])
xpoints = data.iloc[:, [8,10,12,14,16,18,20,22,24,26]].mean(axis=1) #rel balls
ypoints = data.iloc[:, [7,9,11,13,15,17,19,21,23,25]].mean(axis=1)  #sim balls
plt.grid()
plt.plot(xpoints, ypoints, 'o', ms=5)
plt.xlabel("Relatedness")
plt.ylabel("Similarity")
plt.show()

#plot with density
xy = np.vstack([xpoints,ypoints])
z = gaussian_kde(xy)(xy)

fig, ax = plt.subplots()
sc=ax.scatter(xpoints, ypoints, c=z, s=50)
plt.grid()
plt.xlabel("Relatedness")
plt.ylabel("Similarity")
cbar = fig.colorbar(sc)
cbar.set_label("Frequency",loc="top", alpha=0.5)
plt.show()


#3-plot by type
x = [0,1,2,3,4,5,6,7,8,9,10]
y = [5,5,5,5,5,5,5,5,5,5,5]
y1 = [0,1,2,3,4,5,6,7,8,9,10]
x1 = [5,5,5,5,5,5,5,5,5,5,5]

h1font = {'fontname':'serif', 'size':10}
hfont = {'fontname':'serif', 'size':8}

fig, ax = plt.subplots()
rect1 = matplotlib.patches.Rectangle((0,0), 2, 2, color='#838B8B', )
rect2 = matplotlib.patches.Rectangle((2,0), 2, 4, color='#C9C9C9')
rect3 = matplotlib.patches.Rectangle((8,0), 2, 2, color='#FA8072')
rect4 = matplotlib.patches.Rectangle((6,6), 4, 2, color='#7FFF00',)
rect5 = matplotlib.patches.Rectangle((8,8), 2, 2, color='#00C957')
ax.add_patch(rect1)
ax.add_patch(rect2)
ax.add_patch(rect3)
ax.add_patch(rect4)
ax.add_patch(rect5)

colorsType = {'irr':'black', 'ant':'red', 'mer':'yellow', 'hyp':'blue', 'syn':'green'}
#colorsPos = {'ADJ':'red', 'NOUN':'green', 'VERB':'yellow'}
#plt.grid()

for name,color in colorsType.items():
    ax.scatter(xpoints, ypoints, c=data['Type'].map(colorsType), label=name)

ax.legend()
#ax.grid(True)
plt.xlim(0,10)
plt.ylim(0,10)
plt.xticks([0,1,2,3,4,5,6,7,8,9,10], **hfont)
plt.yticks([0,1,2,3,4,5,6,7,8,9,10], **hfont)
plt.plot(x, y, linestyle = 'dashed', color="gray", linewidth=1)
plt.plot(x1, y1, linestyle = 'dashed', color="gray", linewidth=1)
plt.xlabel("Relatedness", **h1font)
plt.ylabel("Similarity",  **h1font)

ax.text(0.5, 1.5, "Irrelevant", fontsize=8)
ax.text(2.3, 3, "Low related", fontsize=8)
ax.text(8.8, 1.4, "Antonym", fontsize=8)
ax.text(6.3, 7.4, "High similar", fontsize=8)
ax.text(8.2, 9.4, "Synonym", fontsize=8)
ax.text(4.5, 4.5, "DU", fontsize=8)
ax.text(5.2, 4.5, "DR", fontsize=8)
ax.text(5.2, 5.2, "SR", fontsize=8)
ax.text(4.5, 5.2, "SU", fontsize=8)
plt.show()

#4-plot to get color bar
fig, ax = plt.subplots()
colorsType = {'irrelevant':'black', 'antonym':'red', 'meronym':'yellow', 'hypernym':'blue', 'synonym':'green'}
#plt.grid()
for name,color in colorsType.items():
    ax.scatter(xpoints, ypoints, c=color, label=name)

ax.legend()
#ax.grid(True)
plt.show()
