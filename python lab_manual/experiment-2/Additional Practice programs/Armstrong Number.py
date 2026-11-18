                                     #Experiment-2
                            #Additional Practice Programs

#Palindrome Number

Number=int(input("Enter Number :"))
temp=Number
rev=0

while temp>0:
    
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
    
if rev==Number:
    print("Palindrome")
else:
    print("Not an Palindrome")
