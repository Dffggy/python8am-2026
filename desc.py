#by nested loop method
x = 5
y = 6
z = 8

# find smallest
if x < y:
    if x < z:
        first = x
    else:
        first = z
else:
    if y < z:
        first = y
    else:
        first = z

# find biggest
if x > y:
    if x > z:
        last = x
    else:
        last = z
else:
    if y > z:
        last = y
    else:
        last = z

# middle number
middle = x + y + z - first - last

print("descending order:", last, middle,first)


#anothermethod


if x > y:
    if x > z:
        if y > z:
            print(x, y, z)
        else:
            print(x, z, y)
    else:
        print(z, x, y)
else:
    if y > z:
        if x > z:
            print(y, x, z)
        else:
            print(y, z, x)
    else:
        print(z, y, x)
