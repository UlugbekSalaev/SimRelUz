import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'Age': ['<=20','21-25','26-30','>=31'],
                    'Male': [0, 3, 2, 1],
                    'Female': [0, 2, 4, 2]})

# define x and y limits
y = range(0, len(df))
x_male = df['Male']
x_female = df['Female']

# define plot parameters
fig, axes = plt.subplots(ncols=2, sharey=True, figsize=(9, 6))

# specify background color and plot title
fig.patch.set_facecolor('xkcd:light grey')
#plt.figtext(.5, .9, "Population Pyramid ", fontsize=15, ha='center')

# define male and female bars
axes[0].barh(y, x_male, align='center', color='royalblue')
axes[0].set(title='Males')
axes[1].barh(y, x_female, align='center', color='lightpink')
axes[1].set(title='Females')

# adjust grid parameters and specify labels for y-axis
axes[0].set(yticks=y, yticklabels=df['Age'])
axes[0].set(xticks=[0,1,2,3,4] )
axes[0].invert_xaxis()

# display plot
plt.show()

