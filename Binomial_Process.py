import numpy as np
import matplotlib.pyplot as plt

flips = np.random.binomial(n=10, p=0.5, size=1000)

plt.hist(flips, bins=11, edgecolor='black')
plt.title("Simulated Binomial Distribution (n=10, p=0.5)")
plt.xlabel("Number of Heads")
plt.ylabel("Frequency")
plt.show()