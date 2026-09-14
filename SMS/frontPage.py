"""
Main Application Module for Student Management System.

This module defines the primary user interface (MyStudManagement) which inherits
from QMainWindow and the auto-generated Ui_MainWindow. It handles the main
application flow, database connection setup (MySQL), table creation, data loading,
searching, ranking, and calculating class averages.

It also includes the DoubleButtonWidgetStudents class for action buttons within the
student tables (Edit/Delete).
"""

from PySide6.QtWidgets import QMainWindow, QMenu, QMessageBox, QDialog, QTableWidgetItem, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox
from PySide6.QtGui import QAction, QIcon
from ui_index import Ui_MainWindow

import mysql.connector


from student_dialog import Ui_Students
from updateStudent_dialog import UpdateStudentsDialog

class AddStudentDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Students()
        self.ui.setupUi(self)

class MyStudManagement(QMainWindow, Ui_MainWindow):
  def __init__(self):
    super().__init__()
    self.setupUi(self)
    self.setWindowTitle("Student Management")

    # buttons to switch to different page (dashboard and show all data page)
    self.dashboard_button.clicked.connect(self.switch_to_dashboard_page)
    self.showAllData_button.clicked.connect(self.switch_to_showAllData_page)

    # connect to mysql server and create database if it doesn't exist
    self.create_connection()

    # create students' table
    self.create_students_table()

    # load student info to Qtable ins dasboard and show all data page
    self.load_students_info()
    self.recall_student.textChanged.connect(self.search_students)
    self.recall_student_2.textChanged.connect(self.search_students_2)

    # opens add student dialog
    self.addStudent_pushButton.clicked.connect(self.open_addStudent_dialog)
   
    # ranks student in descending order
    self.rank_button.clicked.connect(self.rank_students) 

    # fetch the average of the class (all students in the database)
    self.average_button.clicked.connect(self.get_class_average)

    # find all failing students in the database
    self.failing_button.clicked.connect(self.find_failing_students)

  # switch to different widget page (dashboard)
  def switch_to_dashboard_page(self):
    self.stackedWidget.setCurrentIndex(0)
  
  # switch to different widget page (show all data)
  def switch_to_showAllData_page(self):
    self.stackedWidget.setCurrentIndex(1)

  # creates database connection
  def create_connection(self):
    host_name = "localhost"
    user_name = "root"
    mypassword = ""
    database_name = "system_managementDS"
    
    # establish a connection to MySQL server
    try:
        # Try to connect directly
        self.mydb = mysql.connector.connect(
          host = host_name,
          user = user_name,
          password = mypassword,
          database = database_name,
        )
    except mysql.connector.Error as err:
        if err.errno == 1049: # Error 1049: Unknown database
            # If DB doesn't exist, connect temporarily to create it
            temp_mydb = mysql.connector.connect(
              host = host_name, user = user_name, password = mypassword,
            )
            cursor = temp_mydb.cursor()
            cursor.execute(f'CREATE DATABASE IF NOT EXISTS {database_name}')
            cursor.close()
            temp_mydb.close() 

            # Re-establish the proper connection
            self.mydb = mysql.connector.connect(
              host = host_name,
              user = user_name,
              password = mypassword,
              database = database_name,
            )
        else:
            QMessageBox.critical(self, "Database Error", f"Failed to connect to MySQL: {err}")
            self.mydb = None
            
    return self.mydb
  
  #creates students' table
  def create_students_table(self):
    if not self.mydb:
        return
      
   #cursor for exec SQL queries  
    cursor = None
    try:
        cursor = self.mydb.cursor()
        create_student_table_query =f"""
         CREATE TABLE IF NOT EXISTS students_table (
            IDNumber VARCHAR(15) PRIMARY KEY,
            FullName VARCHAR(100) NOT NULL,
            CourseCode VARCHAR(10) NOT NULL,
            CourseName VARCHAR(100) NOT NULL,
            Seatwork INT NOT NULL,
            Assignment INT NOT NULL,
            Quizzes INT NOT NULL,
            Exam INT NOT NULL,                 
            FinalGrade DECIMAL(5, 2),
            Remarks ENUM('PASSED', 'FAILED')
        )"""

        cursor.execute(create_student_table_query)
        self.mydb.commit()
    except mysql.connector.Error as err:
        QMessageBox.critical(self, "Table Creation Error", f"Error creating table: {err}")
    finally:
        if cursor:
            cursor.close()

  # opens dialog for inserting/adding new student
  def open_addStudent_dialog(self):
    addStudent_dialog = Ui_Students(self)   # directly use the dialog
    result = addStudent_dialog.exec()       # show it modally

    if result == QDialog.Accepted:
        self.mydb = self.create_connection()  # reconnect to ensure new data is visible
        self.load_students_info()
        self.dashboard_table.viewport().update()

  #fetch data from the database to the table 
  def get_data_from_table(self):
    if not self.mydb: # Checks main window's connection
        return []
        
    cursor = None
    try:
        cursor = self.mydb.cursor()

        # query that includes ClassStanding calculation (seatwork * 25%) + (assignment * 25%) + (quizzes * 50%)
        query = """ SELECT IDNumber, FullName, CourseCode, CourseName, Seatwork, Assignment, Quizzes,
            (Seatwork * 0.25) + (Assignment * 0.25) + (Quizzes * 0.50) AS ClassStanding,
            Exam, FinalGrade, Remarks FROM students_table"""

        cursor.execute(query)
        data = cursor.fetchall()
        return data
    except mysql.connector.Error as err:
        QMessageBox.critical(self, "Data Error", f"Error fetching data: {err}")
        return []
    finally:
        if cursor:
            cursor.close()

  # project the student info into the table in dashboard and show all data page
  def load_students_info(self):
    self.mydb = self.create_connection() 
    if not self.mydb:
        return
   
    data = self.get_data_from_table()
    
    if not hasattr(self, 'dashboard_table'):
        # This means the QTableWidget in ui_index.py isn't named 'dashboard_table_'
        QMessageBox.critical(self, "UI Error", "Error: 'dashboard_table' widget is missing in Ui_MainWindow.")
        return

    self.dashboard_table.setColumnCount(12) 
    self.dashboard_table.setRowCount(0)
    
    for row_index, row_data in enumerate(data):
      self.dashboard_table.insertRow(row_index)
      for col_index, cell_data in enumerate(row_data):
        item = QTableWidgetItem(str(cell_data))
        self.dashboard_table.setItem(row_index, col_index, item)
      double_button_widget = DoubleButtonWidgetStudents(row_index, row_data, self)
      self.dashboard_table.setCellWidget(row_index, 11, double_button_widget)
      self.dashboard_table.setRowHeight(row_index, 50)

    # Set to 12 columns: 11 data columns (including ClassStanding) + 1 action column
    self.dashboard_table_2.setColumnCount(12) 
    self.dashboard_table_2.setRowCount(0)
    
    for row_index, row_data in enumerate(data):
      self.dashboard_table_2.insertRow(row_index)
      for col_index, cell_data in enumerate(row_data):
        item = QTableWidgetItem(str(cell_data))
        self.dashboard_table_2.setItem(row_index, col_index, item)
      double_button_widget = DoubleButtonWidgetStudents(row_index, row_data, self)
      self.dashboard_table_2.setCellWidget(row_index, 11, double_button_widget)
      self.dashboard_table_2.setRowHeight(row_index, 50)

    # control column widths for TABLE1 (dashboard page)
    self.dashboard_table.setColumnWidth(0, 90) #id
    self.dashboard_table.setColumnWidth(1, 133) #name
    self.dashboard_table.setColumnWidth(2, 80) # course code
    self.dashboard_table.setColumnWidth(3, 125) #course name
    self.dashboard_table.setColumnWidth(4, 0) #seatwork (hidden)
    self.dashboard_table.setColumnWidth(5, 0) #assignment (hidden)
    self.dashboard_table.setColumnWidth(6, 0)  #quiz (hidden)
    self.dashboard_table.setColumnWidth(7, 90) #class standing
    self.dashboard_table.setColumnWidth(8, 90) #exam
    self.dashboard_table.setColumnWidth(9, 90) #final
    self.dashboard_table.setColumnWidth(10, 65) #remarks
    self.dashboard_table.setColumnWidth(11, 120) #actions

    # control column widthsfor TABLE2 (show all data page)
    self.dashboard_table_2.setColumnWidth(0, 100) #id
    self.dashboard_table_2.setColumnWidth(1, 170) #name
    self.dashboard_table_2.setColumnWidth(2, 80) #course code
    self.dashboard_table_2.setColumnWidth(3, 170) #course name
    self.dashboard_table_2.setColumnWidth(4, 90) #seatwork (visible)
    self.dashboard_table_2.setColumnWidth(5, 90) #assignment (visible)
    self.dashboard_table_2.setColumnWidth(6, 90) #quiz (visible)
    self.dashboard_table_2.setColumnWidth(7, 90) #class standing
    self.dashboard_table_2.setColumnWidth(8, 90) #exam
    self.dashboard_table_2.setColumnWidth(9, 90) #final
    self.dashboard_table_2.setColumnWidth(10, 90) #remarks
    self.dashboard_table_2.setColumnWidth(11, 120) #actions

  # recalls student in search bar in dashboard page
  def search_students(self):
    # get the search query from the QLineEdit
    search_query = self.recall_student.text().strip()
    if not self.mydb:
        return

    cursor = None
    try:
        cursor = self.mydb.cursor()

        # execute sql query that includes ClassStanding calculation (seatwork * 25%) + (assignment * 25%) + (quizzes * 50%)
        query = """ SELECT IDNumber, FullName, CourseCode, CourseName, Seatwork, Assignment, Quizzes,
            (Seatwork * 0.25) + (Assignment * 0.25) + (Quizzes * 0.50) AS ClassStanding,
            Exam, FinalGrade, Remarks FROM students_table
            WHERE FullName LIKE %s
        """
        cursor.execute(query, (f"%{search_query}%",))
        results = cursor.fetchall()

        # clear prev table results
        self.dashboard_table.setRowCount(0)

        for row_index, row_data in enumerate(results):
            self.dashboard_table.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.dashboard_table.setItem(row_index, col_index, item)

            # ACTIONS COLUMN (Column 11)
            double_button_widget = DoubleButtonWidgetStudents(row_index, row_data, self)

            # custom widget as the cell widget for the action column
            self.dashboard_table.setCellWidget(row_index, 11, double_button_widget)
            self.dashboard_table.setRowHeight(row_index, 50)

    except mysql.connector.Error as err:
        QMessageBox.critical(self, "Search Error", f"Error while searching: {err}")
    finally:
        if cursor:
            cursor.close()
  
  # recalls student in search bar in show all data page
  def search_students_2(self):
    # get the search query from the QLineEdit
    search_query = self.recall_student_2.text().strip()
    if not self.mydb:
        return

    cursor = None
    try:
        cursor = self.mydb.cursor()

        # execute sql query that includes ClassStanding calculation (seatwork * 25%) + (assignment * 25%) + (quizzes * 50%)
        query = """ SELECT IDNumber, FullName, CourseCode, CourseName, Seatwork, Assignment, Quizzes,
            (Seatwork * 0.25) + (Assignment * 0.25) + (Quizzes * 0.50) AS ClassStanding,
            Exam, FinalGrade, Remarks FROM students_table
            WHERE FullName LIKE %s
        """
        cursor.execute(query, (f"%{search_query}%",))
        results = cursor.fetchall()

        # clear prev table results
        self.dashboard_table_2.setRowCount(0)

        for row_index, row_data in enumerate(results):
            self.dashboard_table_2.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.dashboard_table_2.setItem(row_index, col_index, item)

            # ACTIONS COLUMN (Column 11)
            double_button_widget = DoubleButtonWidgetStudents(row_index, row_data, self)

            # custom widget as the cell widget for the action column
            self.dashboard_table_2.setCellWidget(row_index, 11, double_button_widget)
            self.dashboard_table_2.setRowHeight(row_index, 50)

    except mysql.connector.Error as err:
        QMessageBox.critical(self, "Search Error", f"Error while searching: {err}")
    finally:
        if cursor:
            cursor.close()

  # opens the update student dialog box when green button is clicked
  def open_updateStudent_dialog(self, row_index, row_data):
        """Opens the update dialog and connects its signal to reload data."""
        update_dialog = UpdateStudentsDialog(row_index, row_data, self)

        update_dialog.exec()


  # SQL data getting ranked in descending order
  def get_ranked_data(self):
    if not self.mydb:
        return []
        
    cursor = None
    try:
        cursor = self.mydb.cursor()

        # Fetch all data and ORDER BY FinalGrade (DESCENDING)
        query = """ 
            SELECT 
                IDNumber, FullName, CourseCode, CourseName, Seatwork, Assignment, Quizzes,
                (Seatwork * 0.25) + (Assignment * 0.25) + (Quizzes * 0.50) AS ClassStanding,
                Exam, FinalGrade, Remarks 
            FROM students_table
            -- Rank by Final Grade (Highest first), then Full Name (A-Z) for ties
            ORDER BY FinalGrade DESC, FullName ASC 
        """

        cursor.execute(query)
        data = cursor.fetchall()
        return data
    except mysql.connector.Error as err:
        QMessageBox.critical(self, "Ranking Error", f"Error fetching ranked data: {err}")
        return []
    finally:
        if cursor:
            cursor.close()

  # ranking students in the table in show all data page
  def rank_students(self):
    self.mydb = self.create_connection() 
    if not self.mydb:
        return
   
    ranked_data = self.get_ranked_data()
    
    self.dashboard_table_2.setRowCount(0)
    
    for row_index, row_data in enumerate(ranked_data):
        self.dashboard_table_2.insertRow(row_index)
        
        for col_index, cell_data in enumerate(row_data):
            item = QTableWidgetItem(str(cell_data))
            self.dashboard_table_2.setItem(row_index, col_index, item)
                
            double_button_widget = DoubleButtonWidgetStudents(row_index, row_data, self)
            self.dashboard_table_2.setCellWidget(row_index, 11, double_button_widget)
            self.dashboard_table_2.setRowHeight(row_index, 50)
        
    self.switch_to_showAllData_page()
    self.dashboard_table_2.viewport().update()

  # shows the class average from all the students in the database
  def get_class_average(self):
    if not self.mydb:
        QMessageBox.critical(self, "Database Error", "Database connection is not available.")
        return
    
    cursor = None
    try:
        cursor = self.mydb.cursor()

        # SQL query to calculate the average of all FinalGrade entries
        query = "SELECT AVG(FinalGrade) FROM students_table"
        cursor.execute(query)
        
        # Fetch the result (it will be a single tuple with one value)
        result = cursor.fetchone()
        
        if result and result[0] is not None:
            # average to two decimal places
            class_average = float(result[0])
            formatted_average = f"{class_average:.2f}"
            
            # Display the result to the user
            QMessageBox.information(
                self, 
                "Class Average Final Grade", 
                f"The overall Class Average Final Grade is: **{formatted_average}%**"
            )
        else:
            QMessageBox.information(
                self, 
                "Class Average", 
                "No student data found to calculate the average."
            )
            
    except mysql.connector.Error as err:
        QMessageBox.critical(self, "Database Error", f"Failed to calculate class average: {err}")
    except Exception as e:
        QMessageBox.critical(self, "Error", f"An unexpected error occurred: {e}")
    finally:
        if cursor:
            cursor.close()

  # find failing students from all the data in the database
  def find_failing_students(self):
      self.mydb = self.create_connection() 
      if not self.mydb:
          return
          
      cursor = None
      try:
          cursor = self.mydb.cursor()

          # SQL query to select all data where Remarks = 'FAILED'
          query = """ 
              SELECT 
                  IDNumber, FullName, CourseCode, CourseName, Seatwork, Assignment, Quizzes,
                  (Seatwork * 0.25) + (Assignment * 0.25) + (Quizzes * 0.50) AS ClassStanding,
                  Exam, FinalGrade, Remarks 
              FROM students_table
              WHERE Remarks = 'FAILED'
              ORDER BY FinalGrade DESC 
          """
          cursor.execute(query)
          failing_data = cursor.fetchall()
          
          # 1. Clear and prepare the second table (dashboard_table_2)
          self.dashboard_table_2.setRowCount(0)
          
          if not failing_data:
              QMessageBox.information(
                  self, 
                  "No Failing Students", 
                  "Great news! There are no students currently marked as 'FAILED'."
              )
          
          # 2. Populate the table with the filtered data
          for row_index, row_data in enumerate(failing_data):
              self.dashboard_table_2.insertRow(row_index)
              
              for col_index, cell_data in enumerate(row_data):
                  item = QTableWidgetItem(str(cell_data))
                  self.dashboard_table_2.setItem(row_index, col_index, item)
                  
              # Re-add the action buttons
              double_button_widget = DoubleButtonWidgetStudents(row_index, row_data, self)
              self.dashboard_table_2.setCellWidget(row_index, 11, double_button_widget)
              self.dashboard_table_2.setRowHeight(row_index, 50)
              
          # 3. Ensure we are on the correct page and update the view
          self.switch_to_showAllData_page()
          self.dashboard_table_2.viewport().update()
              
      except mysql.connector.Error as err:
          QMessageBox.critical(self, "Filter Error", f"Failed to filter failing students: {err}")
      finally:
          if cursor:
              cursor.close()

# double button class in the table (edit/update and remove button)
class DoubleButtonWidgetStudents(QWidget):
  def __init__(self, row_indexx, row_data, MyStudManagement):
    super().__init__()

    # store row index and row data as an instance in variables
    self.row_index = row_indexx
    self.row_data = row_data
    self.studentManagement = MyStudManagement #store 

    # get student variables from the table
    self.student_id = self.row_data[0] #idnum
    self.setudent_name = self.row_data[1] #fullname

    layout = QHBoxLayout(self)
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setSpacing(4)

    # create GREEN edit button
    self.edit_button = QPushButton("", self)
    self.edit_button.setStyleSheet("""
            QPushButton {
                background-color: rgb(4, 145, 86);
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: rgb(6, 175, 100);
            }
        """)
    self.edit_button.setFixedSize(48, 26)
    self.edit_button.setIcon(QIcon(":/edit.png")) #set icons for the buttons
    self.edit_button.setToolTip("Edit")
    self.edit_button.clicked.connect(self.edit_clicked)

    # create RED remove button
    self.remove_button = QPushButton("", self)
    self.remove_button.setStyleSheet("""
            QPushButton {
                background-color: rgb(145, 49, 55);
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: rgb(180, 60, 65);
            }
        """)
    self.remove_button.setFixedSize(48, 26)
    self.remove_button.setIcon(QIcon(":/delete.png")) #icon for delete
    self.remove_button.setToolTip("Delete")
    self.remove_button.clicked.connect(self.delete_clicked)

    layout.addWidget(self.edit_button)
    layout.addWidget(self.remove_button)

  # creates database connection for doubleButtonWidgetStudents class
  def create_connection(self):
        # All database functions MUST be defined as methods of the class (indented)
        host_name = "localhost"
        user_name = "root"
        mypassword = ""
        self.database_name = "system_managementDS" # Define here or use local variable

        try:
            # 1. ATTEMPT CONNECTION DIRECTLY TO THE DATABASE
            mydb = mysql.connector.connect(
              host = host_name,
              user = user_name,
              password = mypassword,
              database = self.database_name,  # Attempt to connect directly
            )
            return mydb
            
        except mysql.connector.Error as err:
            # If the database doesn't exist (Error 1049), create it
            if err.errno == 1049: 
                
                mydb = mysql.connector.connect(
                  host = host_name,
                  user = user_name,
                  password = mypassword,
                )
                cursor = mydb.cursor()
                
                cursor.execute(f'CREATE DATABASE IF NOT EXISTS {self.database_name}')
                cursor.execute(f'USE {self.database_name}')
                mydb.commit()
                cursor.close()
                
                return mydb
            
            else:
                QMessageBox.critical(self, "Database Error", f"Failed to connect to MySQL: {err}")
                return None

  # edit/ update students from the action column
  def edit_clicked(self):
    #instance of update student dialog
    self.update_dialog = UpdateStudentsDialog(self.row_index, self.row_data, parent=self.studentManagement)

    #connect the signal to reload the student data
    self.update_dialog.data_updated.connect(self.reload_tables) 
    self.update_dialog.exec()

  # remove/ delete students from the action column
  def reload_tables(self):
    self.studentManagement.load_students_info()
    
    self.studentManagement.dashboard_table.viewport().update()
    self.studentManagement.dashboard_table_2.viewport().update()

  # Inside DoubleButtonWidgetStudents class
  def delete_clicked(self):
    reply = QMessageBox.question(
        self, 'Confirm Deletion',
        f'Are you sure you want to permanently delete {self.setudent_name} ({self.student_id})?',
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        QMessageBox.StandardButton.No
    )

    if reply == QMessageBox.StandardButton.Yes:
        connection = None
        cursor = None
        try:
            connection = self.create_connection()
            if connection is None:
                QMessageBox.critical(self, "Database Error", "Could not connect to database for deletion.")
                return

            cursor = connection.cursor()
            
            delete_query = "DELETE FROM students_table WHERE IDNumber = %s"
            cursor.execute(delete_query, (self.student_id,)) 
            
            connection.commit()
            
            QMessageBox.information(self, "Success", f"{self.setudent_name} has been successfully deleted.")
            
            self.reload_tables()
            
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Failed to delete student: {err}")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()