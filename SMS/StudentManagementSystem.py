from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from student_management_main_ui import Ui_MainWindow as Ui_Form
import sys
def create_id(counter: int) -> str:
    return f"24-1-{counter:04d}"
def compute_final_grade(seatwork, assignment, quizzes, exam):
    class_standing = (seatwork * 0.25) + (assignment * 0.25) + (quizzes * 0.50)
    weighted_class_standing = class_standing * 0.40
    weighted_exam = exam * 0.60
    return round(weighted_class_standing + weighted_exam, 2)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")
        self.resize(1000, 600)
        self.student_counter = 1
        self.student_data = {}
        self.label_id = QtWidgets.QLabel("Student ID:", self)
        self.label_id.setGeometry(40, 40, 100, 30)
        self.label_name = QtWidgets.QLabel("Name:", self)
        self.label_name.setGeometry(40, 80, 100, 30)
        self.label_course_code = QtWidgets.QLabel("Course Code:", self)
        self.label_course_code.setGeometry(40, 120, 100, 30)
        self.label_course_name = QtWidgets.QLabel("Course Name:", self)
        self.label_course_name.setGeometry(40, 160, 100, 30)
        self.label_seatwork = QtWidgets.QLabel("Seatwork:", self)
        self.label_seatwork.setGeometry(40, 200, 100, 30)
        self.label_assignment = QtWidgets.QLabel("Assignment:", self)
        self.label_assignment.setGeometry(40, 240, 100, 30)
        self.label_quizzes = QtWidgets.QLabel("Quizzes:", self)
        self.label_quizzes.setGeometry(40, 280, 100, 30)
        self.label_exam = QtWidgets.QLabel("Exam:", self)
        self.label_exam.setGeometry(40, 320, 100, 30)
        self.lineEdit = QtWidgets.QLineEdit(self)  
        self.lineEdit.setGeometry(160, 40, 200, 30)
        self.lineEdit.setReadOnly(True)
        self.lineEdit_2 = QtWidgets.QLineEdit(self)  
        self.lineEdit_2.setGeometry(160, 80, 200, 30)
        self.comboBox = QtWidgets.QComboBox(self) 
        self.comboBox.setGeometry(160, 120, 200, 30)
        self.comboBox.addItems(["CS101", "NURS202", "CE303", "IT404"])
        self.comboBox_2 = QtWidgets.QComboBox(self)  
        self.comboBox_2.setGeometry(160, 160, 200, 30)
        self.comboBox_2.addItems(["Computer Science", "Nursing", "Civil Engineer", "Information Technology"])
        self.lineEdit_3 = QtWidgets.QLineEdit(self)  
        self.lineEdit_3.setGeometry(160, 200, 200, 30)
        self.lineEdit_4 = QtWidgets.QLineEdit(self)  
        self.lineEdit_4.setGeometry(160, 240, 200, 30)
        self.lineEdit_5 = QtWidgets.QLineEdit(self) 
        self.lineEdit_5.setGeometry(160, 280, 200, 30)
        self.lineEdit_6 = QtWidgets.QLineEdit(self) 
        self.lineEdit_6.setGeometry(160, 320, 200, 30)
        self.btn_add = QtWidgets.QPushButton("Add Student", self)
        self.btn_add.setGeometry(400, 40, 150, 40)
        self.btn_add.clicked.connect(self.add_student)
        self.btn_update = QtWidgets.QPushButton("Update Student", self)
        self.btn_update.setGeometry(400, 90, 150, 40)
        self.btn_update.clicked.connect(self.update_student)
        self.btn_delete = QtWidgets.QPushButton("Delete Student", self)
        self.btn_delete.setGeometry(400, 140, 150, 40)
        self.btn_delete.clicked.connect(self.delete_student)
        self.btn_show = QtWidgets.QPushButton("Show All", self)
        self.btn_show.setGeometry(400, 190, 150, 40)
        self.btn_show.clicked.connect(self.show_all_data)
        self.btn_avg = QtWidgets.QPushButton("Class Average", self)
        self.btn_avg.setGeometry(400, 240, 150, 40)
        self.btn_avg.clicked.connect(self.class_average)
        self.btn_rank = QtWidgets.QPushButton("Rank Students", self)
        self.btn_rank.setGeometry(400, 290, 150, 40)
        self.btn_rank.clicked.connect(self.rank_students)
        self.btn_failing = QtWidgets.QPushButton("Find Failing Students", self)
        self.btn_failing.setGeometry(400, 340, 150, 40)
        self.btn_failing.clicked.connect(self.find_failing_students)
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(580, 40, 400, 400)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Name", "Course Code", "Course Name", "Seatwork", "Assignment", "Quizzes", "Exam", "Final Grade"])
        self.generate_next_id()

    def generate_next_id(self):
        new_id = create_id(self.student_counter)
        self.lineEdit.setText(new_id)
    def add_student(self):
        student_id = self.lineEdit.text()
        name = self.lineEdit_2.text()
        course_code = self.comboBox.currentText()
        course_name = self.comboBox_2.currentText()
        try:
            seatwork = float(self.lineEdit_3.text())
            assignment = float(self.lineEdit_4.text())
            quizzes = float(self.lineEdit_5.text())
            exam = float(self.lineEdit_6.text())
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter numeric grades only.")
            return
        final_grade = compute_final_grade(seatwork, assignment, quizzes, exam)
        remarks = "PASSED" if final_grade >= 75 else "FAILED"
        self.student_data[student_id] = {
            'name': name, 'course_code': course_code, 'course_name': course_name, 'grades': {'seatwork': seatwork, 'assignment': assignment, 'quizzes': quizzes, 'exam': exam}, 'final_grade': final_grade, 'remarks': remarks}
        self.insert_row(student_id, name, course_code, course_name, seatwork, assignment, quizzes, exam, final_grade)
        self.student_counter += 1
        self.generate_next_id()
        QMessageBox.information(self, "Success", f"{name} added successfully.")
    def insert_row(self, student_id, name, course_code, course_name, seatwork, assignment, quizzes, exam, final_grade):
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        items = [student_id, name, course_code, course_name, str(seatwork), str(assignment), str(quizzes), str(exam), str(final_grade)]
        for col, value in enumerate(items):
            self.tableWidget.setItem(row_position, col, QTableWidgetItem(value))
    def show_all_data(self):
        self.tableWidget.setRowCount(0)
        for sid, data in self.student_data.items():
            self.insert_row(sid, data['name'], data['course_code'], data['course_name'], data['grades']['seatwork'], data['grades']['assignment'], data['grades']['quizzes'], data['grades']['exam'], data['final_grade'])
    def update_student(self):
        student_id = self.lineEdit.text()
        if student_id not in self.student_data:
            QMessageBox.warning(self, "Error", "Student ID not found.")
            return
        name = self.lineEdit_2.text()
        course_code = self.comboBox.currentText()
        course_name = self.comboBox_2.currentText()
        try:
            seatwork = float(self.lineEdit_3.text())
            assignment = float(self.lineEdit_4.text())
            quizzes = float(self.lineEdit_5.text())
            exam = float(self.lineEdit_6.text())
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter numeric grades only.")
            return
        final_grade = compute_final_grade(seatwork, assignment, quizzes, exam)
        remarks = "PASSED" if final_grade >= 75 else "FAILED"
        self.student_data[student_id].update({'name': name, 'course_code': course_code, 'course_name': course_name, 'grades': {'seatwork': seatwork, 'assignment': assignment, 'quizzes': quizzes, 'exam': exam}, 'final_grade': final_grade, 'remarks': remarks})
        self.show_all_data()
        QMessageBox.information(self, "Updated", f"Student {name} updated successfully.")
    def delete_student(self):
        student_id = self.lineEdit.text()
        if student_id in self.student_data:
            del self.student_data[student_id]
            self.show_all_data()
            QMessageBox.information(self, "Deleted", f"Student {student_id} removed successfully.")
        else:
            QMessageBox.warning(self, "Error", "Student not found.")
    def class_average(self):
        if not self.student_data:
            QMessageBox.information(self, "No Data", "No student data available.")
            return
        total = sum(s['final_grade'] for s in self.student_data.values())
        avg = total / len(self.student_data)
        QMessageBox.information(self, "Class Average", f"Class Average: {avg:.2f}")
    def rank_students(self):
        if not self.student_data:
            QMessageBox.information(self, "No Data", "No student data available.")
            return
        ranked = sorted(self.student_data.items(), key=lambda x: x[1]['final_grade'], reverse=True)
        rank_list = "\n".join([f"{i+1}. {s[1]['name']} ({s[0]}) - {s[1]['final_grade']:.2f}" for i, s in enumerate(ranked)])
        QMessageBox.information(self, "Student Rankings", rank_list)
    def find_failing_students(self):
        if not self.student_data:
            QMessageBox.information(self, "No Data", "No student data available.")
            return
        failing = [s for s in self.student_data.items() if s[1]['final_grade'] < 75]
        if not failing:
            QMessageBox.information(self, "No Failing", "No failing students found.")
        else:
            fail_list = "\n".join([f"{s[1]['name']} ({s[0]}) - {s[1]['final_grade']:.2f}" for s in failing])
            QMessageBox.information(self, "Failing Students", fail_list)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())