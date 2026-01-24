import sys
from PyQt6.QtWidgets import QApplication
from gui import TrayApplication

def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    
    tray = TrayApplication(app)
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
