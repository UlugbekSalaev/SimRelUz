import matplotlib.pyplot as plt
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
fig, ax = plt.subplots()
colorsType = {'irr':'black', 'ant':'red', 'mer':'yellow', 'hyp':'blue', 'syn':'green'}
#colorsPos = {'ADJ':'red', 'NOUN':'green', 'VERB':'yellow'}
plt.grid()

for name,color in colorsType.items():
    ax.scatter(xpoints, ypoints, c=data['Type'].map(colorsType), label=name)

ax.legend()
ax.grid(True)
plt.xlabel("Relatedness")
plt.ylabel("Similarity")
plt.show()

#4-plot to get color bar
fig, ax = plt.subplots()
colorsType = {'irr':'black', 'ant':'red', 'mer':'yellow', 'hyp':'blue', 'syn':'green'}
plt.grid()
for name,color in colorsType.items():
    ax.scatter(xpoints, ypoints, c=color, label=name)

ax.legend()
ax.grid(True)
plt.show()