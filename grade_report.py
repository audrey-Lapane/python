import math

student_report = [{
    "name": "Audrey",
    "maths": 87,
    "english":98,
    "science": 95
},
{ 
    "name": "punch",
    "maths": 80,
    "english": 90,
    "science": 97
},
{
    "name": "Lak",
    "maths": 81,
    "english": 60,
    "science": 87  
},
{
    "name": "kholofelo",
    "maths": 92,
    "english": 95,
    "science": 98
},
{
    "name": "steve",
    "maths": 60,
    "english": 70,
    "science": 77
}
]

results = []
for student in student_report:
    student_average = (student["maths"] + student["english"] + student["science"]) / 3
    print(f"{student["name"]} has average: {student_average}")

    if student_average >= 80:
        grade = "A"
        status = "Pass"
    elif student_average >= 70 and student_average <= 79:
        grade = "B"
        status = "Pass"
    elif student_average >=60 and student_average <=69:
        grade = "C"
        status = "Pass"
    elif student_average >=50 and student_average <= 59:
        grade = "D"
        status = "Pass"
    else:
        grade = "F"
        status = "Fail" 



    result = {
        "name": student["name"],
        "average": round(student_average, 2),
        "grade": grade,
        "status": status
    }
    results.append(result)
total = 0
highest_mark = results[0]["average"]
lowest_mark = results[0]["average"]



for result in results:
    total += result["average"]

    if result["average"] > highest_mark:
        highest_mark = result["average"]

    if result["average"] < lowest_mark:
        lowest_mark = result["average"]


class_average = total/ len(results)

print("@" * 60)
print("Grade Report")
print("@" *60)
print(f"{'Name':<15}{'Average':<10}{'Grade':<15}{'Status':<10}")
print("-" * 60)


for result in results:
    print(f"{result['name']:<15}{result['average']:<10.2f}{result['grade']:<15}{result['status']:<10}")

print("-" * 60)
print(f"Class Average : {class_average:.2f}")
print(f"Highest Mark  : {highest_mark:.2f}")
print(f"Lowest Mark   : {lowest_mark:.2f}")
print("=" * 60)  

while True:
    search = input("Enter student's name or q to exit:").strip().lower()

    if search == "q":
        print("End of the report card")
        break
    found = False
    for result in results:
        if result["name"].lower() == search:
            print(f"Name : {result["name"]}")
            print(f"Average : {result["average"]}")
            print(f"Grade : {result["grade"]}")
            print(f"Status : {result["status"]}")
            found = True
            break

    if not found:
        print("Student not found")



