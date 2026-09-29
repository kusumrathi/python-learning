# Day 5 - Loops


# 1. For Loop

for i in range(5):
    print(i)


# 2. For Loop with a List

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)


# 3. While Loop

count = 1

while count <= 5:
    print(count)
    count += 1


# 4. Break Statement

for i in range(10):
    if i == 5:
        break
    print(i)


# 5. Continue Statement

for i in range(5):
    if i == 2:
        continue
    print(i)
