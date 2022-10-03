# Import libraries and files:

import pandas as pd
import readit_all
import process
import matplotlib as plt

# Import the penguins dataset:

pd.read_csv("https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/inst/extdata/penguins.csv")

readit_all(filename="penguins.csv")


for s in species:
    X_subset = [d for i, d in enumerate(X) if s == Z[i]]
    Y_subset = [d for i, d in enumerate(Y) if s == Z[i]]

    plt.scatter(X_subset, Y_subset, label=s)
plt.legend()
plt.show()
