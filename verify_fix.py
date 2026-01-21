import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer
import app

def verify_init():
    # Create the app
    qapp = QApplication(sys.argv)
    
    # Set a timer to close the app after 3 seconds. 
    # If the app hangs on init, this might not even be reached or processed if init blocks indefinitely before returning.
    # However, in PySide, constructor runs synchronously. So if MainWindow() constructor hangs, we never reach exec().
    # So we simply try to instantiate MainWindow.
    
    print("Attempting to instantiate MainWindow...")
    try:
        main_window = app.MainWindow()
        print("MainWindow instantiated successfully!")
    except Exception as e:
        print(f"Failed to instantiate MainWindow: {e}")
        sys.exit(1)
        
    print("Verification successful: No freeze during initialization.")
    sys.exit(0)

if __name__ == "__main__":
    verify_init()
