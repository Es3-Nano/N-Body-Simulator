import numpy as np
a = np.array([10, 20, 30, 40, 50])

for i, val in enumerate(a):
    print(i, val)
    if i == 1:
        a = np.delete(a, 2)      # reassign `a` to a shorter array
        print("a is now:", a)