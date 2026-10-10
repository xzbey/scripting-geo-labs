import sys
from PyQt5.QtWidgets import QApplication
from calculator import Calculator

app = QApplication(sys.argv)
calc = Calculator()
sys.exit(app.exec())