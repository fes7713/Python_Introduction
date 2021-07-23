a = 'Apple'
print(a)  # -> Apple

a = "Apple"
print(a)  # -> Apple
# Single quotation is preferred among python coders

# # You cannot mix single and double quotation
# a = "Apple'  # Error
#
# a = 'Apple"  # Error

# Concatenate three Strings
a = "Python"
b = " is "
# do not forget space here
c = "fancy"

result = a + b + c

print(result)  # -> Python is fancy

# Make 4x4 square
a = "a"
line = a * 4 + "\n"
# Type \n to change line
square = line * 4
print(square)

# for loop version
for i in range(4):
    for j in range(4):
        print("*", end="")
    print()

# ***
# ***
# ***

print("{0} and {1}".format("Hello", "World"))

first = "John"
last = "Smith"

print("Hello, {0} {1} is here".format(first, last))
# -> Hello, John Smith is here

print("John Wick"[0:-5])


s = "This is a pen."

print(s[0:4])  # 'This'
print(s[5:7])  # 'is'
# Negative index
print(s[-4:-1])  # 'pen'
# if you wanna include up to the last
print(s[-4:])
# you can leave end value empty

# Spotify
