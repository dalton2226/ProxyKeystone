import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout
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

#Central Widget
central_widget = QWidget() 
window.setCentralWidget(central_widget)
main_layout = QHBoxLayout()
central_widget.setLayout(main_layout)     

#Main Horizontal Layout
content_widget = QWidget()
content_layout = QVBoxLayout()
content_widget.setLayout(content_layout)

#Main Horizontal Widgets
main_layout.addWidget(content_widget)  
content_layout.addWidget(welcome_label)  


#Sidebar Layout
sidebar_widget = QWidget()
sidebar_layout = QVBoxLayout()
sidebar_widget.setLayout(sidebar_layout)

#Sidebar Widgets
main_layout.addWidget(sidebar_widget)
#sidebar_layout.addWidget(sidebar_widget)
league_label = QLabel("League of Legends")
sidebar_layout.addWidget(league_label)





#Placeholders
placeholder_label = QLabel("Main content area")
content_layout.addWidget(placeholder_label)




#End
window.show() # Makes window visible
sys.exit(app.exec()) # Starts the application's event loop and exits the program when the window closes