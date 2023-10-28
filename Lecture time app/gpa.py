total_credit = 0
total_grade_point = 0

for i in range(5):
  course_name = input(f"Enter name of course {i+1: ")
  credit_units = int(input(f"Enter the credit unit for {course_name}: "))
  grade = input(f"Example: [A], [B], [C]... \nEnter the grade you got in {course_name}: ")
  
  grade_points = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1, "F": 0}
  if grade in grade_points:
    grade_points = grade_points[grade]
  else:
    print("You are advised to restart this program and fill in the details carefully")
    
  total_credit += credit_units
  total_grade_point += credit_units * grade_points
  
  gpa = total_grade_point / total_credit
  
print(f"Your GPA is {gpa}")