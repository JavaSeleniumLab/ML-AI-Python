import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
# Sample data (replace with your actual data)
np.random.seed(42)
sepal_length = np.random.rand(100) * 3 + 4
sepal_width = np.random.rand(100) * 2 + 2
petal_length = np.random.rand(100) * 5 + 1
petal_width = np.random.rand(100) * 2 + 0.1
species = np.random.choice(['Setosa', 'Versicolor', 'Virginica'], size=100) # species array
fig = plt.figure(figsize=(20, 15))
ax3d = fig.add_subplot(111, projection='3d')
# Create a dictionary to map species to colors (optional)
species_colors = {'Setosa': 'red', 'Versicolor': 'green', 'Virginica': 'blue'}
# Iterate through the species and plot each one separately
for sp in np.unique(species):
    # Filter the data for the current species
    mask = species == sp
    ax3d.scatter(sepal_length[mask], sepal_width[mask], petal_length[mask],
                 c=species_colors[sp], label=sp, s=50) # s = marker size
ax3d.set_xlabel('Sepal Length')
ax3d.set_ylabel('Sepal Width')
ax3d.set_zlabel('Petal Length')
plt.legend() # now it finds the labels from the scatter plots
plt.show()