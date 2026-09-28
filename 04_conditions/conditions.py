# Day 4 - Conditions


# 1. If Statement

age = 20

if age >= 18:
    print("You are an adult.")


# 2. If-Else Statement

age = 16

if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote yet.")


# 3. If-Elif-Else Statement

marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D")


# 4. Nested If Statement

age = 23
has_id = True

if age >= 18:
    if has_id:
        print("You can enter.")
    else:
        print("Please bring your ID.")
else:
    print("You cannot enter.")
