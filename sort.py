import numpy as np

height = [10, 40, 30, 50, 20, 70, 80, 60, 100, 90]
ascending = np.sort(height)
descending = np.sort(height)[::-1]
print(ascending)
print(descending)