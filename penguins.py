# Import libraries and files

import pandas as pd
import matplotlib.pyplot as plt
from readit_all import readit_all
from process import process

#Import the penguins dataset
#url = "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/inst/extdata/penguins.csv"
#file = pd.to_csv(url)
#data = readit_all(filename= file)
data = readit_all()
X, Y, Z = process(data)


x_label = "bill_length_mm"
y_label = "bill_depth_mm"
z_label = "species"
species = set([d[z_label] for d in data])
colormap = {s: ['tab:blue', 'tab:orange', 'tab:green'][i] for i,s in enumerate(species)}

for d in data:
  if d[x_label] == "NA" or d[y_label] == "NA":
      continue

plt.xlabel(x_label)
plt.ylabel(y_label)

for s in species:
  X_subset=[x_sub for x_sub,z_sub in zip(X,Z) if z_sub==s]
  Y_subset=[y_sub for y_sub,z_sub in zip(Y,Z) if z_sub==s]

  plt.scatter(X_subset, Y_subset, label=s)

plt.legend()
plt.show()
plt.savefig('PenguinScatter.png')