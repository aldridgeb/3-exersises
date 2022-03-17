choice=0
dogs=[]

def dropOff():
    name = input("What's your dogs name?")
    print("Ok ill add", name,"to the list" )
    dogs.append(name)


def pickUp():
    name = input("What's your dogs name?")
    print("Ok ill remove", name,"from the list" )
    dogs.remove(name)


def calcCost():
    string = int(input("How many days will your dog be staying?"))
    print("it will cost $", string * 22.50, "Thank you")


def printRoll():
    print("These are the dogs")
    for dog in dogs:
        print(dog)


while choice != 5:
    print("-----------------------------------------------------------------------")
    print("Welcome to DogsRus")
    print("What would you like to do? Please choose one of the items below")
    print("-----------------------------------------------------------------------")
    print()  
    print("1 Drop off a dog") 
    print("2 Pick up a dog") 
    print("3 Calculate cost") 
    print("4 Print roll")  
    print("5 Exit the system")  
    print()
    
    choice=int(input("Enter your choice (number between 1 and 5): "))
    
    print()
    if choice==1:
        dropOff()
    
    elif choice==2:
        pickUp()
    
    elif choice==3:
      calcCost()
    
    elif choice==4:
        printRoll()
    
    else:
        quit()
