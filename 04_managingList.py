#Managing lists on Python

x = [1, 1, 2, 3, 5]

print(type(x))

messy_list = [0, 2, [1, 3, 5, 7], [2], "test"]

#The element number 2 is the third element, that is a list.
print(messy_list[2])

#Take the second element(index 1) of the third "messy_list" element
print(messy_list[2][1])

print(messy_list[3])

print(messy_list[3][0])

print("--------------Here begins the for loop--------------")
for item in messy_list:
    print(item)

messy_list[4] = "Text"
print(messy_list)

# When you copy a list assigning it to other variable, you don't actually copy it, but instead you copy the reference for that list.
# Once created, a string can not be changed, at least not without changing the reference together.

#To copy a list properly:
messy_copy_list = list(messy_list)
print(messy_copy_list)

messy_copy_list[-1] = "texT"
print(messy_copy_list)

x= [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(x[::2])

messy_list.append(24)

messy_list.append("Try this")

messy_list.remove(1)

messy_list.pop(2)
