#CTI-110
#P2HW2 - Tip Tax Total
#Ava Moore
#June 4, 2018

#Tip, Tax, and Total Calculator

#Declare some variables
# variable   data type   Definition
# foodCost     float     cost of food
# tipAmount    float     tip amount
# salesTax     float     sales tax amount
# totalCost    float     total cost of food

#Declared variables
foodCost = float(input("Enter the cost of food: "))
tipAmount = foodCost * 0.18
salesTax = foodCost * 0.07
totalCost = foodCost + salesTax + tipAmount

print("Your tip amount is $",tipAmount)
print("Your sales tax is $",salesTax)
print("Your total food cost is $",totalCost)
