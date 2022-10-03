# Reading the file all at once
def readit_all(filename = "penguins.csv"):
  """
  Read and parse CSV -- read entire file all at once.
  """
  with open(filename, 'r') as file:
    mylist = file.read().rstrip().split("\n") # rstrip() is needed

  keys = mylist.pop(0).split(",")
  data = []
  for line in mylist:
    values = line.split(",")
    datum = {keys[i]: value for i, value in enumerate(values)}
    data.append(datum)

  return data