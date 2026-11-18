                                 #Experiment-4
                    #Dictionary operations and contact management system

#problem-10
#inventory management

inventory={

"Laptop":25,

"Mouse":80,

"Keyboard":50

}

item=input("Enter Item : ")

if item in inventory:

    print("Stock =",inventory[item])

else:

    print("Item Not Available")

