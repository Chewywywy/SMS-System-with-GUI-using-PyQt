"""
Student Management System for Discrete Structures 2
-----------------------------------------

This module implements a GUI student management system using PyQt6 and Pyside6.
It enables the user to manage college student academic records within a GUI.

Features:
    • Add, delete, and display student records
    • Compute final grades based on performance components
    • Display passing and failing students
    • Rank students based on their final grades
    • Compute and show the class average

This code was written following PEP 8 standards and also uses OOP principles.
Each function includes documentation and comments for clarity.

Rovin Karl B. Pecson
Nov 2025
"""

import sys
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QMainWindow
from student_management_main_ui import Ui_MainWindow


class Window(QtWidgets.QMainWindow):
    """
    Main window class for the College Student Management System.

    Responsibilities:
        - Handle all GUI events such as button clicks.
        - Process user input and manage student records.
        - Display results in the table and message boxes.
    """

    def __init__(self):
        """
        Initialize the application window.
        This sets up the user interface, connects button actions,
        and prepares an empty data structure for storing student records.
        """
        super().__init__()
        self.ui = Ui_MainWindow()  # Load the designed UI
        self.ui.setupUi(self)  # Setup the interface elements

        # Connect buttons to their methods
        # Each button on the UI triggers a specific function in this class.
        self.ui.btn_add.clicked.connect(self.add_college_student)
        self.ui.btn_delete.clicked.connect(self.delete_college_student)
        self.ui.btn_show.clicked.connect(self.show_college_students)
        self.ui.btn_avg.clicked.connect(self.calculate_class_average)
        self.ui.btn_rank.clicked.connect(self.rank_college_students)
        self.ui.btn_failing.clicked.connect(self.find_failing_college_students)

        # Setup the table appearance
        self.setup_table()
        # Temporary data storage
        # List to store all student records during runtime.
        # Each adn every students is represented as a dictionary with keys
        self.college_students = []

        # Counter used for automatically generating student IDs
        self.college_student_counter = 1

        # Nag poprocess para maensures na lahat ng GUI elements are ready bago mag user interaction.
        # nag eensure din na ang data structures ay properly initialized para maprevent ang runtime errors.

    # TABLE CONFIGURATION
    def setup_table(self):
        """
        Configure the widgets that uses to display the students information.
        Each column adjusted its width to fit space.
        """
        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

        # This method guarantees a consistent and professional layout for the table columns.
        # It prevents column data from being truncated visually when records are inserted.

    # INPUT HANDLING AND VALIDATION that allows to get data
    def _get_student_input(self):
        """
        These retrieves and validates input data from the GUI fields.

        Returns:
            tuples: (name, course_code, course_name, seatwork, assignment, quizzes, exam)

        Raises:
            ValueError: Only numeric value, if itsn't it errors in grade inputs.
        """
        # Retrieve text-based inputs from the form fields
        name = self.ui.lineEdit_2.text()
        course_code = self.ui.comboBox.currentText()
        course_name = self.ui.comboBox_2.currentText()

        # Additional safeguard: if user leaves name empty, handle it logically before proceeding
        if not name.strip():
            raise ValueError("Student name cannot be empty.")

        # Try converting numeric inputs into floats
        # If it fails, it raised an error to handle it gracefully later
        try:
            seatwork = float(self.ui.lineEdit_3.text())
            assignment = float(self.ui.lineEdit_4.text())
            quizzes = float(self.ui.lineEdit_5.text())
            exam = float(self.ui.lineEdit_6.text())
        except ValueError:
            raise ValueError("Invalid numeric input detected in grade fields.")

        # It returns all validated values as a tuple
        return name, course_code, course_name, seatwork, assignment, quizzes, exam
    
    # PART OF THE CODE WHERE IT COMPUTES THE GRADE OF THE STUDENTS THAT THE USER INPUTED
    def _compute_final_grade(self, seatwork, assignment, quizzes, exam):
        """
        It computes the student's final grade based on the criteria which are below.

        Args:
            seatwork (float): Seatwork score
            assignment (float): Assignment score
            quizzes (float): Quizzes score
            exam (float): Exam score

        Returns:
            tuple: (final_grade, remarks)
        """
        # Compute class standing (40%)
        # Seatwork is 25%, then the Assignment is 25% and, the Quizzes is 50% that equals to 100
        class_standing = (seatwork * 0.25) + (assignment * 0.25) + (quizzes * 0.50)
        # Multiply by 40% weight of total grade
        weighted_class_standing = class_standing * 0.40
        # Computed exam grade is 60%
        weighted_exam = exam * 0.60
        # Final Grade Computation
        final_grade = round(weighted_class_standing + weighted_exam, 2)
        # Remarks based on the final grade
        remarks = "Passed" if final_grade >= 75 else "Failed"

        # The computation formula reflects a fair weighting system used in real academic settings.
        # This separation of computation steps also improves clarity for maintenance or formula changes.
        return final_grade, remarks

    # TABLE DISPLAY FUNCTION
    def _insert_student_to_table(self, student_data):
        """
        Insert a student's record into the table widget for display.

        Args:
            student_data (dict): Contains all student attributes (ID, name, grades, etc.)
        """
        # Create a new row at the end of the table
        row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row)

        # Iterate through the dictionary and insert each value into a column cell
        for col, key in enumerate(student_data.values()):
            self.ui.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(key)))

        # This modular method ensures that table updating can be reused by multiple features.
        # It prevents redundant code when re-displaying all students later.

    # CORE FUNCTION: ADD STUDENTS FROM THE GUI
    def add_college_student(self):
        """
        Add a new student record to the system.
        Steps:
            1. It retrieves and validate inputs from the GUI
            2. Compute the student grade
            3. Store the data internally
            4. Display the record in the table
            5. Clear all inputs after adding
        """
        # Step 1: This generates a student ID that starts with 24-1 
        college_student_id = f"24-1-{self.college_student_counter:04d}"

        try:
            # Step 2: It gets input data and validate numeric entry
            name, course_code, course_name, seatwork, assignment, quizzes, exam = self._get_student_input()
        except ValueError:
            # Display error message for invalid numeric entries
            QtWidgets.QMessageBox.warning(self, "Error", "Please enter valid numbers for grades.")
            return

        # Step 3: it computes the final grade and remarks
        final_grade, remarks = self._compute_final_grade(seatwork, assignment, quizzes, exam)

        # Step 4: it creates a dictionary object to represent one student on record
        college_student_data = {
            "id": college_student_id,
            "name": name,
            "course_code": course_code,
            "course_name": course_name,
            "seatwork": seatwork,
            "assignment": assignment,
            "quizzes": quizzes,
            "exam": exam,
            "final_grade": final_grade,
            "remarks": remarks
        }
        # Step 5: Save record to the in-memory list and increase ID counter
        self.college_students.append(college_student_data)
        self.college_student_counter += 1

        # Step 6: Insert record visually into the table widget
        self._insert_student_to_table(college_student_data)

        # Step 7: Clear input fields for next entry
        self.clear_inputs()

        # This method ties together input validation, computation, data storage, and display logic.
        # The flow ensures users receive immediate feedback after adding a student.
        # It also maintains data integrity by only appending valid and complete records.

    # OTHER SYSTEM FUNCTIONS
    def show_college_students(self):
        """This refresh and display all students records in the table."""
        # Remove all existing rows before re-displaying
        self.ui.tableWidget.setRowCount(0)

        # Reinsert all student records into the table
        for college_student in self.college_students:
            self._insert_student_to_table(college_student)

        # This function ensures that any modification or deletion is immediately reflected visually.

    def delete_college_student(self):
        """Delete the currently selected student from both table and internal list."""
        # iniidentify kung saang row ang currently selected
        current_row = self.ui.tableWidget.currentRow()

        if current_row >= 0:
            # Remove student record from UI and internal list
            self.ui.tableWidget.removeRow(current_row)
            del self.college_students[current_row]

            # Display confirmation message
            QtWidgets.QMessageBox.information(self, "Deleted", "Student record removed.")
        else:
            # It warns user if no row is selected
            QtWidgets.QMessageBox.warning(self, "Error", "Please select a student to delete.")

        # This approach keeps UI and backend data synchronized.
        # Removing both ensures that deleted records are not reloaded later.

    def calculate_class_average(self):
        """Compute and show the class average of all final grades."""
        # Prevent division error if no records exist
        if not self.college_students:
            QtWidgets.QMessageBox.information(self, "Average", "No students found.")
            return

        # Cinocompute ang sum ng lahat ng student grades
        avg = sum(s["final_grade"] for s in self.college_students) / len(self.college_students)

        # It display results that formatted to two decimal places
        QtWidgets.QMessageBox.information(self, "Class Average", f"Average Grade: {avg:.2f}")

        # This metric helps teachers or users gauge overall class performance instantly.

    def find_failing_college_students(self):
        """Identify and display students whehre their remarks are failed."""
        # Filter list for failing students only
        failing = [s for s in self.college_students if s["final_grade"] < 75]

        # Check if there are any failing students
        if not failing:
            QtWidgets.QMessageBox.information(self, "Failing Students", "No failing students found.")
            return

        # gumagawa ng list of names and grades para idisplay sa table
        msg = "\n".join([f"{s['name']} - {s['final_grade']:.2f}" for s in failing])
        QtWidgets.QMessageBox.warning(self, "Failing Students", msg)

        # This provides quick insight into which students may need extra academic support.

    def rank_college_students(self):
        """nirarank ang students base sa grade nila"""
        # Ensure there are records before sorting the students and displaying
        if not self.college_students:
            QtWidgets.QMessageBox.information(self, "Ranking", "No students found.")
            return

        # sinosort mga students from high to low
        ranked = sorted(self.college_students, key=lambda s: s["final_grade"], reverse=True)

        # Construct a ranking message
        msg = "\n".join([f"{i+1}. {s['name']} - {s['final_grade']:.2f}" for i, s in enumerate(ranked)])
        QtWidgets.QMessageBox.information(self, "Student Ranking", msg)

        # Ranking system adds competitiveness and helps visualize top performers quickly.

    def clear_inputs(self):
        """nirereset mga nasa text field."""
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.clear()
        self.ui.lineEdit_6.clear()

        # Clearing inputs avoids accidental duplication of data
        # and ensures the form is ready for the next entry cleanly.

# Need ito para mag run ang program.
if __name__ == "__main__":
    # it creates the main application object
    app = QtWidgets.QApplication(sys.argv)
    # this also initialize and show the main window
    window = Window()
    window.show()
    # it keeps running the application event loop
    sys.exit(app.exec())
