student_data = {}
student_counter = 1

def generate_student_id():
    global student_counter
    student_id = f"24-1-{student_counter:04d}"
    student_counter += 1
    return student_id
    
def compute_final_grade(seatwork, assignment, quizzes, exam):
    class_standing = (seatwork * 0.25) + (assignment * 0.25) + (quizzes * 0.50)
    overall_class_standing = class_standing * 0.409
    overall_exam = exam * 0.60
    return round(overall_class_standing + overall_exam, 2)
    
def add_student(student_id, name, course_code, course_name, seatwork, assignment, quizzes, exam):
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
    return student_data[student_id]
    
def update_student_data(student_id, name, course_code, course_name, seatwork, assignment, quizzes, exam):
        if student_id not in student_data:
            return None
            
        final_grade = compute_final_grade(seatwork, assignment, quizzes, exam)
        remarks = "PASSED" if final_grade >= 75 else "FAILED"
        
        student_data[student_id].update({
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
        })
        return student_data[student_id]

def remove_student_data(student_id):
    if student_id in student_data:
        del student_data[student_id]
        return True
    return False
  
def class_average():
    if not student_data:
        return 0.0
    total = sum(student['final_grade'] for student in student_data.values())
    return total / len(student_data)
    
def rank_students():
    if not student_data:
        return[]
    ranked = sorted(student_data.items(), key=lambda x: x[1]['final_grade'], reverse=True)
    return ranked

def find_failing_students(passing_grade = 75.0):
    if not student_data:
        return []
    failing = [s for s in student_data.items() if s[1]['final_grade'] < passing_grade]
    return failing      