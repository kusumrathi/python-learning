# Day 7 - Tuples


# 1. Creating a Tuple

fruits = ("Apple", "Banana", "Mango", "Orange")

print(fruits)


# 2. Accessing Tuple Items

print(fruits[0])
print(fruits[2])


# 3. Tuple Length

print(len(fruits))


# 4. Checking if an Item Exists

print("Apple" in fruits)
print("Grapes" in fruits)


# 5. Looping Through a Tuple

for fruit in fruits:
    print(fruit)


# 6. Tuple with Different Data Types

person = ("Kusum", 23, 5.2)

print(person)


# 7. Tuple Unpacking

name, age, height = person

print(name)
print(age)
print(height)
