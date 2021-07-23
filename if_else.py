# --if--
# creating variable a
a = 1

# use == equal operator to check if a is a
if a == 1:
    # change indentation
    print("a is 1")

# --if else—
# creating variable a
a = 1

# check if a is a
if a == 1:
    # change indentation
    print("a is 1")
# use else for when a is not 1
else:
    print("a is not 1")

# --elif--
# else + if = elif
a = 1
if a == 1:
    print("a is 1")
# add one more condition using elif
elif a > 2:
    print("a is greater than 2")
else:
    print("a is less than 1")

# --adding more conditions--


# --more elif--
a = 3

if a < 0:
    print("a is negative")
elif a == 0:
    print("a ia zero")
elif a == 1:
    print("a is one")
elif a > 1:
    print("a is greater than 1")
else:
    print("a is not a number")

# --more elif—
a = 3

if a < 0:
    print("a is negative")
elif a == 0:
    print("a ia zero")
elif a == 1:
    print("a is one")
elif a > 1:
    print("a is greater than 1")
else:
    print("a is not a number")

# --if—
# creating variable a
a = 1



a = 6
if a > 4:
    if a < 10:
        if a != 5:
            print("too deep")
    if a >= 10:
        if a > 20:
            print("too deep")

a = 6
if a > 4:
    if a < 10 and a != 5:
        print("ok")
    elif a > 20:
        print("ok")

a = 6
if a > 4:
	if a < 10 and a != 5:
		print("ok")
	elif a > 20:
		print("ok")
