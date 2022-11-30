# Import libraries and files

import pandas as pd
import readit_all
import process
import matplotlib as plt

#Import the penguins dataset

curl -O https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/inst/extdata/penguins.csv

readit_all(penguins)

X, Y, Z = process(data)

for s in species:
  X_subset=[x_sub for x_sub,z_sub in zip(X,Z) if z_sub==s]
  Y_subset=[y_sub for y_sub,z_sub in zip(Y,Z) if z_sub==s]

  # another way that does the same thing as 2 lines above
  X_subset = [d for i, d in enumerate(X) if s == Z[i]]
  Y_subset = [d for i, d in enumerate(Y) if s == Z[i]]

  plt.scatter(X_subset, Y_subset, label=s)

plt.legend()
plt.show()