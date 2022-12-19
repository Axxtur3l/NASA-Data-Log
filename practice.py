import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

names = ['first', 'second', 'third']
values = [5, 10, 15]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.scatter(names, values)
plt.subplot(132)
plt.step(names, values)
plt.subplot(133)
plt.stem(names, values)
plt.suptitle('Categorical Plotting')
plt.show()

plt.show()