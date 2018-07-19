#CTI-110
#P5T1 - Kilometer Converter
#Ava Moore
#July 5, 2018

conversionFactor = 0.6214

def main():
    #Get distance in kilometers
    kilometers = float(input("Enter a distance in kilometers: "))

    #Display distance converted to miles
    showMiles(kilometers)

def showMiles(km):
    #Calculate miles
    miles = km * conversionFactor

    #Display miles
    print(km, "kilometers equals", miles, "miles.")




main()
