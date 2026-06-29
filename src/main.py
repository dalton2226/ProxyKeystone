import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
from PySide6.QtCore import Qt 

app = QApplication(sys.argv)

window = QMainWindow() # Creates Window
window.setWindowTitle("Proxy Keystone") #sets the title of the GUI
window.resize(900, 600) #sets window size

welcome_label = QLabel("Welcome to Proxy Keystone") # creates lable
window.setCentralWidget(welcome_label)#makes the lable

welcome_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter) #Uses 1 argument which is a combination of allignment flags
  

window.show() # Makes window visible
sys.exit(app.exec())