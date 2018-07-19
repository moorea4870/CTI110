# CTI-110
# Software Sales
# Ava Moore
# June 21, 2018

#Use if/else structure
#Get input from user

quantity = int(input("Enter number of packages purchased: "))
#Calculate cost of package without discount
quantitycost = quantity * 99
#Calculate discount
if quantity < 9:
    discountamount = quantitycost * 0
    print("There is no discount")
elif quantity > 9 and quantity < 20:
    discountamount = quantitycost * 0.10
    print("Your discount amount is 10%, which is $",discountamount,"off your purchase.")
#Calculate discount
elif quantity > 19 and quantity < 50:
    discountamount = quantitycost * 0.20
    print("Your discount amount is 20%, which is $",discountamount,"off your purchase.")
elif quantity > 49 and quantity < 100:
    discountamount = quantitycost * 0.30
    print("Your discount amount is 30%, which is $",discountamount,"off your purchase.")
else:
    discountamount = quantitycost * 0.40
    print("Your discount amount is 10%, which is $",discountamount,"off your purchase.")
#Display discount amount and total
totalcost = quantitycost - discountamount
print("Your total cost is: $",totalcost)
