"""
Login & Registration System using PyQt6 and SQLite.

This module implements a GUI-based user authentication system:
- Login window
- Registration window
- Password validation & hashing
- An error or success popups
- Welcome screen

The module uses SQLite for storing user credentials and PyQt6 for UI handling.
All UI files are dynamically loaded using .ui files from Qt Designer.

Author: Rovin Karl B. Pecson
UCOS 2-1
"""

import sys
import re
import sqlite3
import hashlib
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QLineEdit

# Setups Database
# Connects the main to database that created, but if there is no db file, it makes one.
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# This makes the table that stores the user credentials
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")
conn.commit()  # Commit changes to database

# Validates password based on the standard requirements.

def is_valid_password(password: str) -> bool:
    """
    Validate a password based on security requirements.

    Args:
        password (str): The password string to validate.

    Returns:
        bool: True if the password meets the requirements, False otherwise.

    Password requirements:
        - At least 1 lowercase letter
        - At least 1 uppercase letter
        - At least 1 digit
        - Minimum length: 8 characters
    """
    # Regex pattern to enforce security requirements
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
    return bool(re.match(pattern, password))  # Return True if matches

# PASSWORD HASHING

def hash_password(password: str) -> str:
    """
    Hash a plaintext password using SHA-256.

    Args:
        password (str): The plaintext password.

    Returns:
        str: The SHA-256 hashed password.
    """
    # Encode password to bytes and hash it
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

# SAFE UI LOADER

def safe_load_ui(window, path: str):
    """
    Safely load a Qt Designer .ui file into a given window.

    Args:
        window: The PyQt6 window object to attach the UI.
        path (str): The path to the .ui file.

    Raises:
        SystemExit: If the UI file fails to load.
    """
    try:
        # Attempt to load UI file
        uic.loadUi(path, window)
    except Exception as e:
        # Show critical message box if loading fails
        QtWidgets.QMessageBox.critical(
            None,
            "UI Load Error",
            f"Could not load UI file:\n{path}\n\n{e}"
        )
        sys.exit(1)  # Exit the program if UI fails to load

# LOGIN WINDOW

class LoginWindow(QtWidgets.QMainWindow):
    """
    Main login window for user authentication.

    Features:
        - Username and password input
        - Password visibility toggle
        - Login and registration navigation
    """

    def __init__(self, preset_username: str = ""):
        """
        Initialize the LoginWindow.

        Args:
            preset_username (str): Optional username to pre-fill (after failed login).
        """
        super().__init__()
        # Load the login UI
        safe_load_ui(self, "windows_login_pecson/login_pecson.ui")

        # Set password field to masked mode
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)

        # Connect password visibility checkbox to toggle method
        self.show_password_login_checkbox.stateChanged.connect(self.toggle_password)

        # Pre-fill username if provided (after wrong login)
        self.lineEdit.setText(preset_username)

        # Connect login and register buttons to respective methods
        self.login_button.clicked.connect(self.login)
        self.register_button.clicked.connect(self.open_register)

    def toggle_password(self):
        """
        Toggle password visibility in the login window.
        """
        # Switch between normal text and password mode
        mode = QLineEdit.EchoMode.Normal if self.show_password_login_checkbox.isChecked() else QLineEdit.EchoMode.Password
        self.lineEdit_2.setEchoMode(mode)

    def login(self):
        """
        Authenticate user credentials and open the welcome window if successful.
        Shows a popup window if login fails.
        """
        username = self.lineEdit.text().strip()  # Get entered username
        password = self.lineEdit_2.text().strip()  # Get entered password

        if not username or not password:
            # Show warning if any field is empty
            QtWidgets.QMessageBox.warning(self, "Error", "Please enter both username and password.")
            return

        # Fetch hashed password for entered username
        cursor.execute("SELECT password FROM users WHERE username=?", (username,))
        row = cursor.fetchone()

        if row and row[0] == hash_password(password):
            # Open welcome screen if password matches
            self.open_welcome(username)
        else:
            # Open wrong login popup otherwise
            self.wrong_login = WrongLoginWindow(preset_username=username)
            self.wrong_login.show()
            self.close()

    def open_register(self):
        """
        Open the registration window.
        """
        # Initialize and show the register window
        self.reg = RegisterWindow()
        self.reg.show()
        self.close()

    def open_welcome(self, username: str):
        """
        Open the welcome window after successful login.

        Args:
            username (str): The username to display in the welcome message.
        """
        # Initialize and show the welcome window
        self.w = WelcomeWindow(username)
        self.w.show()
        self.close()

# REGISTER WINDOW

class RegisterWindow(QtWidgets.QMainWindow):
    """
    User registration window for creating new accounts.
    """

    def __init__(self):
        """
        Initialize the RegisterWindow and bind UI elements.
        """
        super().__init__()
        # Load registration UI
        safe_load_ui(self, "windows_login_pecson/register_pecson.ui")

        # Bind UI elements to class attributes
        self.email_register_textbox = self.findChild(QLineEdit, "email_register_textbox")
        self.username_register_textbox_2 = self.findChild(QLineEdit, "username_register_textbox_2")
        self.password_register_textbox = self.findChild(QLineEdit, "password_register_textbox")
        self.confirm_password_register_textbox = self.findChild(QLineEdit, "confirm_password_register_textbox")

        # Mask password fields
        self.password_register_textbox.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm_password_register_textbox.setEchoMode(QLineEdit.EchoMode.Password)

        # Connect checkboxes to toggle functions
        self.show_password_register_checkbox.stateChanged.connect(self.toggle_pw)
        self.show_confirm_password_register_checkbox.stateChanged.connect(self.toggle_confirm_pw)

        # Connect register button to registration function
        self.register_title_text.clicked.connect(self.register_user)

    def toggle_pw(self):
        """
        Toggle visibility of the password field.
        """
        mode = QLineEdit.EchoMode.Normal if self.show_password_register_checkbox.isChecked() else QLineEdit.EchoMode.Password
        self.password_register_textbox.setEchoMode(mode)

    def toggle_confirm_pw(self):
        """
        Toggle visibility of the confirm password field.
        """
        mode = QLineEdit.EchoMode.Normal if self.show_confirm_password_register_checkbox.isChecked() else QLineEdit.EchoMode.Password
        self.confirm_password_register_textbox.setEchoMode(mode)

    def register_user(self):
        """
        Validate registration inputs, ensure password strength, handle duplicates,
        and insert a new user into the database. Displays success or invalid popup.
        """
        # Get all input values
        email = self.email_register_textbox.text().strip()
        username = self.username_register_textbox_2.text().strip()
        password = self.password_register_textbox.text().strip()
        confirm = self.confirm_password_register_textbox.text().strip()

        # Check for empty fields or invalid password
        if not all([email, username, password, confirm]) or password != confirm or not is_valid_password(password):
            self.show_invalid()
            return

        try:
            # Attempt to insert new user into database
            cursor.execute(
                "INSERT INTO users (email, username, password) VALUES (?, ?, ?)",
                (email, username, hash_password(password))
            )
            conn.commit()
        except sqlite3.IntegrityError:
            # Show invalid popup if duplicate entry occurs
            self.show_invalid()
            return

        # Show success popup and connect button to return login
        self.success = RegistrationSuccessWindow()
        self.success.pushButton.clicked.connect(self.return_login)
        self.success.show()
        self.close()

    def show_invalid(self):
        """
        Show a popup window for invalid registration attempt.
        """
        self.invalid = RegistrationInvalidWindow()
        self.invalid.pushButton.clicked.connect(self.retry)
        self.invalid.show()
        self.close()

    def retry(self):
        """
        Reset registration fields after invalid registration and allow retry.
        """
        # Clear all input fields
        self.email_register_textbox.clear()
        self.username_register_textbox_2.clear()
        self.password_register_textbox.clear()
        self.confirm_password_register_textbox.clear()
        self.show()
        self.invalid.close()

    def return_login(self):
        """
        Return to login window after successful registration.
        """
        self.log = LoginWindow()
        self.log.show()
        self.success.close()

# WRONG LOGIN POPUP

class WrongLoginWindow(QtWidgets.QWidget):
    """
    Popup window shown when login credentials are invalid.
    """

    def __init__(self, preset_username=""):
        """
        Initialize WrongLoginWindow.

        Args:
            preset_username (str): Username to pre-fill on retry.
        """
        super().__init__()
        # Load wrong login UI
        safe_load_ui(self, "windows_login_pecson/error_pecson.ui")

        # Store username for retry
        self.preset_username = preset_username

        # Connect try again button to function
        self.pushButton.clicked.connect(self.try_again)

    def try_again(self):
        """
        Retry login by returning to LoginWindow with preset username.
        """
        # Open login window with preset username
        self.login = LoginWindow(preset_username=self.preset_username)
        self.login.show()
        self.close()

# WELCOME WINDOW

class WelcomeWindow(QtWidgets.QMainWindow):
    """
    Welcome window shown after successful login.
    """

    def __init__(self, username: str):
        """
        Initialize WelcomeWindow.

        Args:
            username (str): Username to display in welcome message.
        """
        super().__init__()
        # Load welcome UI
        safe_load_ui(self, "windows_login_pecson/welcome_board_pecson.ui")

        # Set welcome label
        self.label.setText(f"Welcome, {username}!")

        # Connect back button to return login
        self.back_button.clicked.connect(self.back)

    def back(self):
        """
        Return to LoginWindow from welcome screen.
        """
        self.login = LoginWindow()
        self.login.show()
        self.close()

# POPUP WINDOWS

class RegistrationSuccessWindow(QtWidgets.QWidget):
    """
    Popup shown for successful registration.
    """

    def __init__(self):
        """
        Initialize RegistrationSuccessWindow UI.
        """
        super().__init__()
        safe_load_ui(self, "windows_login_pecson/succesful_making_account_pecson.ui")

class RegistrationInvalidWindow(QtWidgets.QWidget):
    """
    Popup shown for invalid registration attempts.
    """

    def __init__(self):
        """
        Initialize RegistrationInvalidWindow UI.
        """
        super().__init__()
        safe_load_ui(self, "windows_login_pecson/invalid_making_account_pecson.ui")

# MAIN EXECUTION BLOCK

if __name__ == "__main__":
    """
    Launch the login application.

    Creates QApplication instance and opens the LoginWindow.
    """
    # Create application instance
    app = QtWidgets.QApplication(sys.argv)

    # Create login window and show it
    window = LoginWindow()
    window.show()

    # Execute the application event loop
    sys.exit(app.exec())