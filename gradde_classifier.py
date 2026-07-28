#student grade classifier

name = input("Enter your name: ")
mark1 = float(input("Enter marks for pyhsics subject: "))
mark2 = float(input("Enter marks for math subject: "))
mark3 = float(input("Enter marks for CompSc subject: "))

student_average = (mark1 + mark2 + mark3) / 3
if student_average >= 80 :
    print("Your grade is A, you have passed!")
    print(f"{name} with a marks of {mark1}, {mark2}, {mark3} has the average of {student_average} and has passed very well, no intervation flag")
elif student_average >= 70 and student_average <= 79:
    print("Your grade is B, you have passed!") 
    print(f"{name} with a marks of {mark1}, {mark2}, {mark3} has the average of {student_average} and has passed , no intervation flag")
elif student_average >= 60 and student_average <= 69:
    print("Your grade is C, you have passed!")
    print(f"{name} with a marks of {mark1}, {mark2}, {mark3} has the average of {student_average} and has passed , no intervation flag")
elif student_average >= 50 and student_average <= 59:
    print("Your grade is D, you have passed!")
    print(f"{name} with a marks of {mark1}, {mark2}, {mark3} has the average of {student_average} and has passed , no intervation flag")
else:
    print("Your grade is F, you have failed!") 


if student_average < 40:
    print("Needs Intervation")
    print(f"{name} with a marks of {mark1}, {mark2}, {mark3} has the average of {student_average} and has failed , Needs intervation")

