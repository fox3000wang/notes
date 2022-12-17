import numpy as np

a = np.arange(6).reshape(2, 3)
print(a)

b = np.nditer(a)
for x in np.nditer(a):
    print(x, end=", ")
print('\n')

for x in np.nditer(a.T.copy(order='C')):
    print(x, end=", ")
