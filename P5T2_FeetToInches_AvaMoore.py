# Converting user input from feet to inches
# July 5, 2018
# CTI-110 P5T2_FeetToInches 
# Ava Moore

inchesPerFoot = 12

def main():
    feet = int(input("Enter a number of feet: "))
    print(feet, "equals", feetToInches(feet), "inches.")

def feetToInches(feet):
    return feet * inchesPerFoot




main()
