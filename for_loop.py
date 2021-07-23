print(range(10))
for i in range(10):
    print(i, end=", ")

# number is variable
# this number changes each time
for number in range(10):
    # check number changes each loop
    # end is an option
    print(number, end=", ")
print()

# this number changes each time

sum = 0
for n in range(10):
    sum += n
    # if sum over 20
    # break from loop
    if sum > 20:
        break
print(sum)

for n in range(10):
    # if n is multiple of 3
    # skip this loop
    if n % 3:
        continue
    print(n, end=", ")

list = [1, 2, 3]
for i in range(len(list)):
    print(list[i], end=", ")

# Drawing a square
for i in range(5):
    for j in range(5):
        print("*", end="")
    # this print to change line
    print()
