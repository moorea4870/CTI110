# CTI-110
# P3HW1 - Age Classifier
# Ava Moore
# June 20, 2018

# Ask user to enter a person's age
age = int(input("Enter a person's age: "))

if age <= 1:
    print("He or she is an infant.")
elif age > 1 and age <= 12:
    print("He or she is a child.")
elif age >= 13 and age < 20:
    print("He or she is a teenager.")
else:
    print("He or she is an adult.")
