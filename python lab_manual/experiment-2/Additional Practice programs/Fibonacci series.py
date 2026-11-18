                            #Experiment-2
                    #Additional Practice Programs

#Fabonacci Series

number=int(input("Enter Number of Terms :"))

a=0
b=1
print(a,b,end="")

for i in range(2,number):
    c=a+b
    print(c,end="")

    a=b
    b=c
