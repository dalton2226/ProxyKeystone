import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QHBoxLayout
from PySide6.QtCore import Qt 

app = QApplication(sys.argv)


window = QMainWindow() # Creates Main window
window.setWindowTitle("Proxy Keystone") #sets the title of the GUI
window.resize(900, 600) #sets window size

welcome_label = QLabel("Welcome to Proxy Keystone") # creates label
central_widget = QWidget() 
window.setCentralWidget(central_widget)
layout = QHBoxLayout()
central_widget.setLayout(layout)             
welcome_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter) #Uses 1 argument which is a combination of allignment flags
layout.addWidget(welcome_label)

window.show() # Makes window visible
sys.exit(app.exec()) # Starts the application's event loop and exits the program when the window closes