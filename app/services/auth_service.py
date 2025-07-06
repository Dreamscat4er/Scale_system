# auth_service.py
# ------------------------------------------
# Defines AuthService, a simple service class responsible for
# authenticating user credentials against your server or a simulated check.
# - Contains login() method that returns True/False
# ------------------------------------------

class AuthService:
    def login(self, username, password):
        """
        Simulated login check.
        Replace with actual HTTP request to your server if needed.
        """
        if username == "admin" and password == "password":
            return True
        return False
