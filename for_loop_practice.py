print(list(range(2, 8)))

for number in range(10):
    # end is an option
    if number == 5:
        continue
    print(number, end=", ")

print()
# They behave in a same way
# --for loop--
for n in range(10):
    print(n, end=", ")

print()
# --while loop--
a = 0
while True:
    if a > 9:
        break
    print(a, end=", ")
    a = a + 1

a = 1

print()
a = [1, 2, 3, 4, 5, 6]


for i in range(2, len(a) - 1):
    print(a[i])



size = 10
for i in range(size):
    for j in range(size - 1, i, -1):
        print("3", end="")
    print()


# Continue asking for a figure
while True:
    mode = input("Rectangle or Triange :")
    height = int(input("Input height :"))
    width = int(input("Input width :"))

    print("Figure is " + mode)
    print("Height is " + str(height))
    print("Width is " + str(width))

    # this is the one we did in class
    if mode == "Rectangle":
        # row
        for i in range(height):
            # column
            for j in range(width):
                print("*", end="")
            # changing line
            print()

    # this actually gives regular triangle..... so width do not do anything.
    elif mode == "Triangle":
        # row
        for i in range(height):
            # column
            for j in range(i):
                print("*", end="")
            print()
    # if the input was not either rectangle or triangle, try again
    else:
        print("Invalid inout")