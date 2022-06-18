import matplotlib.pyplot as plt

x = [0,1,2,3,4,5,6,7,8,9,10]
y = [5,5,5,5,5,5,5,5,5,5,5]
y1 = [0,1,2,3,4,5,6,7,8,9,10]
x1 = [5,5,5,5,5,5,5,5,5,5,5]

h1font = {'fontname':'serif', 'size':10}
hfont = {'fontname':'serif', 'size':8}
plt.xlim(0,10)
plt.ylim(0,10)
plt.xticks([0,1,2,3,4,5,6,7,8,9,10], **hfont)
plt.yticks([0,1,2,3,4,5,6,7,8,9,10], **hfont)
plt.plot(x, y, linestyle = 'dashed', color="gray", linewidth=1)
plt.plot(x1, y1, linestyle = 'dashed', color="gray", linewidth=1)
plt.ylabel('Semantic similarity', **h1font)
plt.xlabel('Semantic relatedness', **h1font)

plt.show()
