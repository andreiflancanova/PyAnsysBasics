import numpy as np
import matplotlib.pyplot as plt

#Boolean type

x=True

print(type(x))

#Logic operators
print(3!=7)

print(3>4)

y = 4<9
#If statements

if y:
        print("y is True")
else:
        print("y is False")

z=400
if z<300:
        print("z is less than 300")

elif z==300:
        print("z is equal to 300")
else:
        print("z is greater than 300")

print(int(True))
print(int(False))

#Fizzbuzz game

for i in range(1,101):
    if i%3==0 and i%5 ==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

#True
print(True and True)

#False
print(True and False)

#True
print(True or True)

#True
print(True or False)

#Converting Double Arrays in Boolean Arrays
data = np.loadtxt(fname='D:\Mestrado\PyAnsys\Learning_PyAnsys\PythonBasics\experiment01.csv', delimiter=',')

sim = np.loadtxt(fname='D:\Mestrado\PyAnsys\Learning_PyAnsys\PythonBasics\simulation01.txt', skiprows=52)

a = sim[:, 0]

b = sim[:, 1]

c = sim[:, 2]

print(a<10)

#Creates an array fullfilled with the values of a in the positions where a<10
print(a[a<10])

#Creates an array fullfilled with the values of b in the positions where a<10
print(b[a<10])

d=np.amin(abs(b))
print(d)

#Show the values of a in the positions where b is equal to d
print(a[b==d])

x = a[b==d]

z = c[b==d]

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1)

ax.plot(x, z, linestyle = "", marker = "x")
ax.plot(data[:,0], data[:,1], linestyle = "", marker = "x")


plt.show()