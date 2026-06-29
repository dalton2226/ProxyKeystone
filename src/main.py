import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QHBoxLayout
from PySide6.QtCore import Qt 
from PySide6.QtGui import QFont

app = QApplication(sys.argv)

#Windows
window = QMainWindow() # Creates Main window
window.setWindowTitle("Proxy Keystone") #sets the title of the GUI
window.resize(900, 600) #sets window size


#Main Label
welcome_label = QLabel("Welcome to Proxy Keystone") # creates label
welcome_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter) #Uses 1 argument which is a combination of allignment flags

#Font
font = QFont()
font.setPointSize(20)
welcome_label.setFont(font) # 

window.show() # Makes window visible

#Central Widget
central_widget = QWidget() 
window.setCentralWidget(central_widget)
layout = QHBoxLayout()
central_widget.setLayout(layout)             


#Adding To Central Layout
layout.addWidget(welcome_label)



#window.show() # Makes window visible
sys.exit(app.exec()) # Starts the application's event loop and exits the program when the window closes