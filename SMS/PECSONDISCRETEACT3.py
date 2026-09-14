import uuid
def generate_student_id(counter):
  return f"24-1-{counter:04d}"
def compute_final_grade(seatwork, assignment, quizzes, exam):
  class_standing = (seatwork * 0.25) + (assignment * 0.25) + (quizzes * 0.50)
  weighted_class_standing = class_standing * 0.40
  weighted_exam = exam * 0.60
  return round(weighted_class_standing + weighted_exam, 2)
def add_student(student_data, student_id):
  print(f"Generated Student ID: {student_id}")
  name = input("Enter Student's Name: ")
  course_code = input("Enter Course Code: ")
  course_name = input("Enter Course Name: ")
  try:
      seatwork = float(input("Enter Seatwork Grade: "))
      assignment = float(input("Enter Assignment Grade: "))
      quizzes = float(input("Enter Quizzes Grade: "))
      exam = float(input("Enter Exam Grade: "))
  except ValueError:
      print("Invalid Grade Entered. Please enter numeric values.")
      return
  final_grade = compute_final_grade(seatwork, assignment, quizzes, exam)
  remarks = "PASSED" if final_grade >= 75 else "FAILED"
  student_data[student_id] = {
      'name': name,
      'course_code': course_code,
      'course_name': course_name,
      'grades': {
          'seatwork': seatwork,
          'assignment': assignment,
          'quizzes': quizzes,
          'exam': exam
      },
      'final_grade': final_grade,
      'remarks': remarks
  }
  print(f"{name} added with ID {student_id}.")
def recall_student(student_data):
  student_id = input("Enter Student ID to recall: ").strip()
  if student_id in student_data:
      student = student_data[student_id]
      print(f"\n--- Student ID {student_id} Data ---")
      print(f"Name: {student['name']}")
      print(f"Course Code: {student['course_code']}")
      print(f"Course Name: {student['course_name']}")
      print(f"Seatwork: {student['grades']['seatwork']}")
      print(f"Assignment: {student['grades']['assignment']}")
      print(f"Quizzes: {student['grades']['quizzes']}")
      print(f"Exam: {student['grades']['exam']}")
      print(f"Final Grade: {student['final_grade']:.2f}")
      print(f"Remarks: {student['remarks']}")
  else:
      print("Student not found.")
def show_all_data(student_data):
  if not student_data:
      print("No student data available.")
      return
  print("\n--- All Student Data ---")
  for student_id, student in student_data.items():
      print(f"\nStudent ID: {student_id}")
      print(f"Name: {student['name']}")
      print(f"Course Code: {student['course_code']}")
      print(f"Course Name: {student['course_name']}")
      print(f"Seatwork: {student['grades']['seatwork']}")
      print(f"Assignment: {student['grades']['assignment']}")
      print(f"Quizzes: {student['grades']['quizzes']}")
      print(f"Exam: {student['grades']['exam']}")
      print(f"Final Grade: {student['final_grade']:.2f}")
      print(f"Remarks: {student['remarks']}")
def remove_student(student_data):
  student_id = input("Enter Student ID to Remove: ").strip()
  if student_id in student_data:
      del student_data[student_id]
      print(f"Student ID {student_id} removed successfully.")
  else:
      print("Student not found.")
def update_student(student_data):
  student_id = input("Enter Student ID to Update: ").strip()
  if student_id not in student_data:
      print("Student not found.")
      return
  student = student_data[student_id]
  print(f"Current name: {student['name']}")
  new_name = input("Enter new name (leave blank to keep current): ")
  if new_name:
      student['name'] = new_name
  new_course_code = input("Enter new Course Code (leave blank to keep current): ")
  if new_course_code:
      student['course_code'] = new_course_code
  new_course_name = input("Enter new Course Name (leave blank to keep current): ")
  if new_course_name:
      student['course_name'] = new_course_name
  try:
      seatwork = input("Enter new Seatwork Grade (leave blank to keep current): ")
      assignment = input("Enter new Assignment Grade (leave blank to keep current): ")
      quizzes = input("Enter new Quizzes Grade (leave blank to keep current): ")
      exam = input("Enter new Exam Grade (leave blank to keep current): ")
      if seatwork:
          seatwork = float(seatwork)
          student['grades']['seatwork'] = seatwork
      else:
          seatwork = student['grades']['seatwork']
      if assignment:
          assignment = float(assignment)
          student['grades']['assignment'] = assignment
      else:
          assignment = student['grades']['assignment']
      if quizzes:
          quizzes = float(quizzes)
          student['grades']['quizzes'] = quizzes
      else:
          quizzes = student['grades']['quizzes']
      if exam:
          exam = float(exam)
          student['grades']['exam'] = exam
      else:
          exam = student['grades']['exam']
  except ValueError:
      print("Invalid Grade Entered. Grades not updated.")
      return
  student['final_grade'] = compute_final_grade(seatwork, assignment, quizzes, exam)
  student['remarks'] = "PASSED" if student['final_grade'] >= 75 else "FAILED"
  print(f"Student ID {student_id} updated successfully.")
def get_class_average(student_data):
  if not student_data:
      print("No student data available to calculate class average.")
      return
  total = sum(student['final_grade'] for student in student_data.values())
  class_avg = total / len(student_data)
  print(f"Class average: {class_avg:.2f}")
def rank_students(student_data):
  if not student_data:
      print("No student data to rank.")
      return
  ranked = sorted(student_data.items(), key=lambda x: x[1]['final_grade'], reverse=True)
  print("\n--- Student Rankings ---")
  for rank, (student_id, student) in enumerate(ranked, 1):
      print(f"{rank}. {student['name']} (ID: {student_id}) - Final Grade: {student['final_grade']:.2f}")
def find_failing_students(student_data, passing_grade=75.0):
  if not student_data:
      print("No student data available.")
      return
  failing = [s for s in student_data.items() if s[1]['final_grade'] < passing_grade]
  if not failing:
      print("No failing students found.")
      return
  print(f"\n--- Failing Students (Below {passing_grade}) ---")
  for student_id, student in failing:
      print(f"{student['name']} (ID: {student_id}) - Final Grade: {student['final_grade']:.2f}")
def main():
  student_data = {}
  student_counter = 1  # Start from 1 for 24-1-0001
  while True:
      print("\n--- Student Management ---")
      print("1. Add Student")
      print("2. Recall Student")
      print("3. Show All Data")
      print("4. Remove Student")
      print("5. Update Student")
      print("6. Get Class Average")
      print("7. Rank All Students")
      print("8. Find Failing Students")
      print("9. Exit")
      choice = input("Enter your choice (1-9): ")
      if choice == '1':
          student_id = generate_student_id(student_counter)
          add_student(student_data, student_id)
          student_counter += 1
      elif choice == '2':
          recall_student(student_data)
      elif choice == '3':
          show_all_data(student_data)
      elif choice == '4':
          remove_student(student_data)
      elif choice == '5':
          update_student(student_data)
      elif choice == '6':
          get_class_average(student_data)
      elif choice == '7':
          rank_students(student_data)
      elif choice == '8':
          find_failing_students(student_data)
      elif choice == '9':
          print("Exiting program.")
          break
      else:
          print("Invalid choice. Please enter a number between 1 and 9.")
if __name__ == "__main__":
  main()