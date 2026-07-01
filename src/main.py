import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QTreeWidget, QTreeWidgetItem
from PySide6.QtCore import Qt 
from PySide6.QtGui import QFont

app = QApplication(sys.argv)

#Create Objects
window = QMainWindow() # Creates Main window
    #Widgets
content_widget = QWidget()
central_widget = QWidget() 
sidebar_widget = QWidget()
sidebar_tree = QTreeWidget()
#Sidebar Items
finance_item = QTreeWidgetItem(["Finances"])
balance_item = QTreeWidgetItem(["Current Balance"]) #ADD
bills_item = QTreeWidgetItem(["Recurring Expenses"]) #ADD
purchased_item = QTreeWidgetItem(["Purchase History"]) #ADD
car_item = QTreeWidgetItem(["Car Information"])
garage_item = QTreeWidgetItem(["Current Cars"])
settings_item = QTreeWidgetItem(["Settings"])
display_item = QTreeWidgetItem(["Display"])
games_item = QTreeWidgetItem(["Games"])
league_item = QTreeWidgetItem(["League of Legends"])
deadlock_item = QTreeWidgetItem(["Deadlock"])
league_rank_item = QTreeWidgetItem(["League Rank"])

    #labels
welcome_label = QLabel("Proxy's Keystone") # creates label
placeholder_label = QLabel("Main content area")

    #Create Layouts
main_layout = QHBoxLayout()
content_layout = QVBoxLayout()
sidebar_layout = QVBoxLayout()

#Configure Objects ex (setAlignment setFont)

#Window
window.setWindowTitle("Proxy's Keystone") #sets the title of the GUI
window.resize(900, 600) #sets window size

#Font
welcome_font = QFont()
welcome_font.setPointSize(20)
welcome_label.setFont(welcome_font) 
# Alignment
welcome_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter) #Determines Placement of Welcome Label

#Connect the Objects(building relationships EX(setLayout)
window.setCentralWidget(central_widget)
#Layouts
content_widget.setLayout(content_layout)
sidebar_widget.setLayout(sidebar_layout)
central_widget.setLayout(main_layout)   
sidebar_layout.addWidget(sidebar_tree)

#Build each section ex(sidebar_layout.addWidget)

content_layout.addWidget(welcome_label)   #Welcome Label added to 
content_layout.addWidget(placeholder_label)

#Connect the major sections ex(Connect the major sections main_layout.addWidget(sidebar_widget))
main_layout.addWidget(sidebar_widget) #Adds side bar to main layout
main_layout.addWidget(content_widget)  #adds content widget to main layout
#Top Level Items
sidebar_tree.addTopLevelItem(games_item)
sidebar_tree.addTopLevelItem(settings_item)
sidebar_tree.addTopLevelItem(car_item)
sidebar_tree.addTopLevelItem(finance_item)

# Sets the amount of space each layout gets 
main_layout.setStretch(0, 1.5)  # sidebar
main_layout.setStretch(1, 3)  # content area
#Dropdown menus
sidebar_tree.setHeaderLabel("Proxy") #using proxy as a place holder
games_item.addChild(league_item)
games_item.addChild(deadlock_item)
settings_item.addChild(display_item)
league_item.addChild(league_rank_item)
car_item.addChild(garage_item)
finance_item.addChild(bills_item)
finance_item.addChild(balance_item)
finance_item.addChild(purchased_item)







#END
window.show() # Makes window visible
sys.exit(app.exec()) # Starts the application's event loop and exits the program when the window closes