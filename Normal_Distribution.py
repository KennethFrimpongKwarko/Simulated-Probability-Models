import numpy as np
import matplotlib.pyplot as plt

# Simulate 1000 values from a normal distribution
data = np.random.normal(loc=50, scale=10, size=1000)

# Plot histogram
plt.hist(data, bins=30, edgecolor='black')
plt.title("Simulated Normal Distribution (μ=50, σ=10)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

