# print list directly
print([1, 2, 3])

# save list in a variable
a = ["Car", "Bike", "Bus"]

# print list
print(a)


# make list
# size is 3
a = [1, 2, 3]

# [0]
# index 0 gives first element
print(a[0])

# [size - 1]
# index size - 1 gives last element
print(a[2])

a.pop(1)
print(a)


# programming languages list
languages = ['Python', 'Java', 'C++', 'Ruby', 'C']

# remove and return the last item
print('When index is not passed:')
print('Return Value:', languages.pop())
print('Updated List:', languages)

# remove and return the third last item
print('\nWhen 2 is passed:')
print('Return Value:', languages.pop(2))
print('Updated List:', languages)

# remove and return the last item
print('\nWhen -1 is passed:')
print('Return Value:', languages.pop(-1))
print('Updated List:', languages)

# make empty list
lang = []

# Adding languages to
# the end of list
lang.append("Python")
print(lang)
lang.append("Java")
print(lang)
lang.append("C++")
print(lang)
lang.append("C")
print(lang)



list_2d = [[0, 1], [3, 4]]
print(list_2d)

# change value at
# 1st row and 2nd column
list_2d[0][1] = 8
print(list_2d)



list_2d = [0, 1, 2, 3, 4, 5]
# slicing index 1 to 3
# Up to one before the end
# so size = end - start
# 4 - 1 so
# size of 3 list will come
# start is included
# end is not included
print(list_2d[1:4])
