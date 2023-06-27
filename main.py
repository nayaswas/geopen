import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the coordinates of Mount Everest
everest_coordinates = [(28.0014, 86.9286, 8848)]  # (latitude, longitude, elevation)

# Define the description of Mount Everest
everest_description = "Mount Everest is the highest peak in the world."

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot Mount Everest coordinates
for lat, lon, elev in everest_coordinates:
    ax.scatter(lon, lat, elev, marker='^', color='red')
    ax.text(lon, lat, elev, "Mount Everest", color='black')

# Set labels and title
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_zlabel('Elevation')
ax.set_title('3D Map with Mount Everest')

# Set the aspect ratio
ax.set_box_aspect([1, 1, 0.3])

# Show the description
plt.text(0, 0, -1000, everest_description, fontsize=12)

# Show the plot
plt.show()
