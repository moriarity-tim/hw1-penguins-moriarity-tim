# Import libraries and files

import pandas as pd
import readit_all
import process
import matplotlib as plt


#Import the penguins dataset
url = "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/inst/extdata/penguins.csv"
file = pd.read_csv('data/oe')
data = readit_all(file)
X, Y, Z = process(data)

for s in species:
  X_subset=[x_sub for x_sub,z_sub in zip(X,Z) if z_sub==s]
  Y_subset=[y_sub for y_sub,z_sub in zip(Y,Z) if z_sub==s]

  plt.scatter(X_subset, Y_subset, label=s)

plt.legend()
plt.show()
plt.savefig('PenguinScatter.png')