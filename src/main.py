import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt 
from PySide6.QtGui import QFont

app = QApplication(sys.argv)

#Create Objects

window = QMainWindow() # Creates Main window
content_widget = QWidget()
welcome_label = QLabel("Welcome to Proxy Keystone") # creates label
central_widget = QWidget() 
main_layout = QHBoxLayout()
sidebar_widget = QWidget()
sidebar_layout = QVBoxLayout()
content_layout = QVBoxLayout()
placeholder_label = QLabel("Main content area")
league_label = QLabel("League of Legends")

#Configure Objects ex (setAlignment setFont)
    #Window
window.setWindowTitle("Proxy Keystone") #sets the title of the GUI
window.resize(900, 600) #sets window size

     #Font
font = QFont()
font.setPointSize(20)
welcome_label.setFont(font) 
    #Content_Widget
welcome_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter) #Determines Placement of Welcome Label
  


#Connect the Objects(building relationships EX(setLayout)
window.setCentralWidget(central_widget)
#Layouts
content_widget.setLayout(content_layout)
sidebar_widget.setLayout(sidebar_layout)
central_widget.setLayout(main_layout)   

#Build each section ex(sidebar_layout.addWidget)
sidebar_layout.addWidget(league_label)
content_layout.addWidget(welcome_label)  
content_layout.addWidget(placeholder_label)


#Connect the major sections ex(Connect the major sections main_layout.addWidget(sidebar_widget))
main_layout.addWidget(sidebar_widget)
main_layout.addWidget(content_widget)  


#END
window.show() # Makes window visible
sys.exit(app.exec()) # Starts the application's event loop and exits the program when the window closes