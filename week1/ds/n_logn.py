import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10)
y1 = np.log2(x)

plt.figure()
plt.plot(x, x, 'b')
plt.plot(x, y1, "r")
plt.grid()
plt.show()
