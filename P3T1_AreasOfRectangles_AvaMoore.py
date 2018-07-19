# CTI-110
# P3T1
# Ava Moore
# June 20, 2018

# Get dimensions of rectangle 1
length1 = int(input("Enter the length of rectangle 1: "))
width1 = int(input("Enter the width of rectangle 1: "))

# Get dimensions of rectangle 2
length2 = int(input("Enter the length of rectangle 2: "))
width2 = int(input("Enter the width of rectangle 2: "))

# Calculate areas of rectangles
area1 = length1 * width1
area2 = length2 * width2

# Find which rectangle has the greater area
if area1 > area2:
    print("Rectangle 1 has greater area.")
elif area2 > area1:
    print("Rectangle 2 has greater area.")
else:
    print("Both rectangles have same area.")
