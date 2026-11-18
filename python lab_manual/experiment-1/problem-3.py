                                    #Experiment-1
                            #Conditonal statements in python
#problem-3
#Leap Year

Year=int(input("Enter Year : "))

if (Year%400==0)or(Year%4==0 and Year%100!=0):
    print("It is a Leap Year")
else:
    print("Not a Leap Year")

    
