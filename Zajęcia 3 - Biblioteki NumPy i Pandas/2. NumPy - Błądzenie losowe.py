import numpy as np
import matplotlib.pyplot as plt

array = np.array([0])
print(array)

for x in range(1, 100):
    array = np.append(array, array[x - 1] + np.random.choice([-1, 1]))

print(array)


plt.plot(array)
plt.show()

print("MIN = {}".format(np.min(array)))
print("MAX = {}".format(np.max(array)))

counter = 0
for x in range(50):
    array = np.array([0])
    for y in range(1, 100):
        array = np.append(array, array[y - 1] + np.random.choice([-1, 1]))
        if array[y] > 30:
            counter += 1
            break


print("Greater than 30 in np array counter = {}".format(counter))
