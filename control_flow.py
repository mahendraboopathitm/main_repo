
marks = int(input("Enter your marks (0-100): "))

if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

# Output the result
print("Your grade is:", grade) 
