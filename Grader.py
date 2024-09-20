possible = float(input("Enter Possible Points for Assignment: "))

achieved = float(input("Enter Points Achieved for Assignment: "))

total = (achieved / possible)

final_score = (total * 100)

if final_score <= 50:
    grade = "F"
elif final_score >= 51 and final_score <= 60:
    grade = "D"
elif final_score >= 61 and final_score <= 75:
    grade = "C"
elif final_score >= 76 and final_score <= 88:
    grade = "B"
elif final_score >= 89 and final_score <= 100:
    grade = "A"

print("Final Grade: " + grade)