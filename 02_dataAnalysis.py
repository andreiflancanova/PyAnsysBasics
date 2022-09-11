import numpy as np
import matplotlib.pyplot as plt

d = np.loadtxt(fname='D:\Mestrado\PyAnsys\Learning_PyAnsys\PythonBasics\experiment01.csv', delimiter=',')

print(d.shape)

print(type(d))

print(d[0, 0])

# Last row, first column
print(d[-1, 0])

# Slice an array with the first 10 rows and with 1 column(first element is inclusive and last one is exclusive)
print(d[0:10, 0])

# Slice an array with the first 1 rows and with 10 columns(first element is inclusive and last one is exclusive)
print(d[0, 0:10])

# From the first to the last
print(d[0, 0:])

# x= d[0:]
# y= d[0:]

# plt.ion()

# fig = plt.figure()

# ax = fig.add.subplot(1, 1, 1)

# ax.plot(x, y)

s=np.loadtxt('simulation01.txt', skiprows=52)

x = s[:, 0]

y = s[:, 1]

z = s[:, 2]

plt.ion()
f = plt.figure()

ax2 = f.add_subplot(1, 1, 1)

ax2.scatter(x, y, c=z)

ax2.set_aspect(1)
