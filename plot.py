import matplotlib.pyplot as plt
import numpy as np

# Generate some example data
x = np.arange(0, 10, 0.1)
y = np.sin(x)

# Create a plot
plt.figure()
plt.plot(x, y)
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Matplotlib Plot')
plt.savefig('plot.png')  # Save the plot as a PNG file
