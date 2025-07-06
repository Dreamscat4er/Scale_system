# main.py
# ------------------------------------------
# This is the application's entry point.
# - Creates QApplication instance
# - Instantiates AppController, which manages windows and app flow
# - Starts the event loop
# ------------------------------------------

from PyQt5.QtWidgets import QApplication
from app.controller import AppController

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)               # Create QApplication (required for PyQt)
    app_controller = AppController()           # Initialize AppController (creates and manages windows)
    app_controller.start()                     # Start the app by showing login window
    app.exec_()                                # Start Qt event loop
