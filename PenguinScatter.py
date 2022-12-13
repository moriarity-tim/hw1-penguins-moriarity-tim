import matplotlib.pyplot as plt


x_label = "bill_length_mm"
y_label = "bill_depth_mm"
z_label = "species"
data = [X,Y,Z]
species = set([d[z_label] for d in data])
colormap = {s: ['tab:blue', 'tab:orange', 'tab:green'][i] for i,s in enumerate(species)}

for d in data:
    if d[x_label] == "NA" or d[y_label] == "NA":
        continue

    color = colormap[d[z_label]]
    plt.scatter(float(d[x_label]), float(d[y_label]), color=color)

plt.xlabel(x_label)
plt.ylabel(y_label)


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