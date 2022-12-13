# Function to process data on bill length & flipper length measured in mm of the various species
import readit_all
import matplotlib.pyplot as plt

def process(data, x = "bill_length_mm", y = "flipper_length_mm", z = "species"):
    """
    Extract 2 items/columns, remove missing data "NA" and cast strings to floats
    """
    bad_count = 0
    X = []
    Y = []
    Z = []
    for d in data:
      # Remove missing data
      if "NA" in [d[x], d[y], d[z]]:
          bad_count += 1
          print("Skipping NA --", bad_count, "lines skipped")
          continue
      
      # Convert strings to numbers for the quantitative variables
      X.append(float(d[x]))
      Y.append(float(d[y]))
      Z.append(d[z])

    return X, Y, Z
