# Sample score
score = 85

# Determine grade based on score
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Output the grade
print(f"The grade for a score of {score} is: {grade}")
