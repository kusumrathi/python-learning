# Day 6 - Lists


# 1. Creating a List

fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits)


# 2. Accessing List Items

print(fruits[0])
print(fruits[2])


# 3. Changing List Items

fruits[1] = "Grapes"

print(fruits)


# 4. Adding Items

fruits.append("Watermelon")

print(fruits)


# 5. Inserting Items

fruits.insert(1, "Pineapple")

print(fruits)


# 6. Removing Items

fruits.remove("Mango")

print(fruits)


# 7. List Length

print(len(fruits))


# 8. Looping Through a List

for fruit in fruits:
    print(fruit)
