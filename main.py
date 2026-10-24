students = [{"name":"Aung Aung","age":21,"studyHour":4.5,"pythonScore":85},
{"name":"Su Su","age":20,"studyHour":3.0,"pythonScore":92},
{"name":"Mg Mg","age":22,"studyHour":3.5,"pythonScore":35},
{"name":"Aye Aye","age":19,"studyHour":4.0,"pythonScore":76},
{"name":"Mya Mya","age":23,"studyHour":3.0,"pythonScore":55},
]


grade_categories=("Excellent","Good","Pass","Fail")


def get_score(student):
      return student["pythonScore"]

def calculate_average(scores):
      
      total=0
      for score in scores:
            total+=score

      average = total / len(scores)
      return average


def classify_grade(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 80:
        return "Excellent"
    elif score >= 60:
            return "Good"
    elif score >= 40:
            return "Pass"
    else:
          return "Fail"


def count_passed(students):
       
       pass_count=0

       for score in scores:
              if  score>=50:
                   pass_count+=1
       return pass_count

scores=[]
for student in students:
      scores.append(student["pythonScore"])

average_score = calculate_average(scores)
highest_score = max(scores)
lowest_score = min(scores)

passed_students = count_passed(students)
failed_students = len(students)-passed_students
top_student = max(students,key=get_score)

print("\n===== STUDENT PERFORMANCE REPORT =====")
for student in students:
      print(f"Name:{student['name']}")
      print(f"Age:{student['age']}")
      print(f"Study Hours:{student['studyHour']}")
      print(f"Python Score:{student['pythonScore']}")
      print(f"Python Score:{student['pythonScore']}")
      print(f"Grade:{classify_grade(student['pythonScore'])}\n")


print("\n===== SUMMARY =====")

print(f"Total Students: {len(students)}")
print(f"Average Score: {average_score:.2f}")
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
print(f"Passed Students: {passed_students}")
print(f"Failed Students: {failed_students}")
print(f"Top Student: {top_student['name']} ({top_student['pythonScore']})")
      
      
      
           
      
    