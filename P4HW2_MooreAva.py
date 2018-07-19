#CTI-110
#P4HW2: Running Total
#Ava Moore
#July 19, 2018

def main():
    total = 0
    value = int(input("Enter a number: "))
    while value >= 0:
        total = value + total
        value = int(input("Enter a number: "))
    print("Total: ",total)














main()
