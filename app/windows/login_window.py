# login_window.py
# ------------------------------------------
# Defines LoginWindow, a QWidget for user authentication.
# - Contains username and password fields
# - Emits login_attempt signal with user input on login button click
# - Shows error messages using QMessageBox
# ------------------------------------------

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox
from PyQt5.QtCore import pyqtSignal

class LoginWindow(QWidget):
    login_attempt = pyqtSignal(str, str)      # Signal emitted when user attempts login (username, password)
    login_error = pyqtSignal(str)             # Signal to show login errors (optional)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")          # Set window title

        # Connect error signal to message box handler
        self.login_error.connect(self.show_error_message)

        # Build the UI layout
        layout = QVBoxLayout()
        btn_layout = QHBoxLayout()

        self.label1 = QLabel("Username:")     # Username label + input
        self.username_input = QLineEdit()

        self.label2 = QLabel("Password:")     # Password label + masked input
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login")      # Login button
        self.login_button.clicked.connect(self.on_login)  # Connect to login handler

        self.close_button = QPushButton("Close")      # Close button (not yet wired)

        # Add widgets to layouts
        btn_layout.addWidget(self.login_button)
        btn_layout.addWidget(self.close_button)
        layout.addWidget(self.label1)
        layout.addWidget(self.username_input)   
        layout.addWidget(self.label2)
        layout.addWidget(self.password_input)
        layout.addLayout(btn_layout)

        self.setLayout(layout)                # Set the final layout on the window

    def on_login(self):
        """
        Slot called when the login button is clicked.
        Collects user input and emits login_attempt signal.
        """
        username = self.username_input.text()
        password = self.password_input.text()
        self.login_attempt.emit(username, password)  # Emit signal with collected credentials

    def show_error_message(self, message):
        """
        Slot to show a message box with login errors.
        """
        QMessageBox.warning(self, "Login Error", message)
