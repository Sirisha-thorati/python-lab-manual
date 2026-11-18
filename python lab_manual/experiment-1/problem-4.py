                                      #Experiment-1
                            #Conditonal statements in python
#problem-4
#Grade Calculator

Marks=float(input("Enter Marks : "))

if Marks>=90:
    grade='A+'
elif Marks>=80:
    grade='A'
elif Marks>=70:
    grade='B'
elif Marks<=60:
    grade='C'
elif Marks>=50:
    grade='D'
else:
    grade='F'
print("Grade=",grade)
