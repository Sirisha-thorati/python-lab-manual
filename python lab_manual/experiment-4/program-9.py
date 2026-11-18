                                    #Experiment-4
                    #Dictionary operations and contact management system

#problem-9
#Student marks Database

students={

"Rahul":89,

"Ravi":92,

"Anil":78,

"Keerthi":94

}

highest=max(students,key=students.get)

print("Topper =",highest)

print("Marks =",students[highest])
