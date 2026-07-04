import numpy as np
import matplotlib.pyplot as plt
c=['a','b','c','d','e']
a=np.array([1,2,3,4,5])
b=np.ones(5)
plt.ylim(0,7)
plt.bar(c,a+b)
plt.show()
print(a)
print(a+b)
