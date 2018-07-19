#CTI-110
#P4HW1: Distance Traveled
#Ava Moore
#July 19, 2018

def main():
    
    mph = int(input("What is the speed of the vehicle in mph?"))

    hours = int(input("How many hours has it traveled"))

    title = "Report Title"
    y = "Hours"
    z ="Distance Traveled"
    print(title.center(30))
    print(y.ljust(10) + z.ljust(20))
    print("-"*30)

    for x in range(1,hours + 1):
        distance = mph * x
        print(str(x).ljust(20) + str(distance))









main()
