# controller.py
# ------------------------------------------
# Defines AppController, the central app manager.
# - Creates LoginWindow and AuthService
# - Handles login attempts by connecting login_attempt signal to handler
# - Updates UI on login success or failure
# ------------------------------------------

from app.windows.login_window import LoginWindow
from app.services.auth_service import AuthService

class AppController:
    def __init__(self):
        self.login_window = LoginWindow()          # Create login window
        self.auth_service = AuthService()          # Create auth service instance
        self.login_window.login_attempt.connect(self.handle_on_login)  # Connect login signal to handler

    def start(self):
        """
        Starts the app by showing the login window.
        """
        self.login_window.show()

    def on_login_success(self):
        """
        Called when authentication succeeds.
        Hides login window and shows main window (if implemented).
        """
        self.login_window.hide()
        # self.main_window.show()  # Uncomment and implement when main window is added

    def handle_on_login(self, username, password):
        """
        Slot handling login attempts.
        Calls AuthService to check credentials.
        """
        if self.auth_service.login(username, password):
            self.on_login_success()
        else:
            # Show error by emitting login_error signal on login window
            self.login_window.login_error.emit("Invalid username or password")
