import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QTreeWidget, QTreeWidgetItem, QStackedWidget
from PySide6.QtCore import Qt 
from PySide6.QtGui import QFont



#Create Objects
app = QApplication(sys.argv)
window = QMainWindow() # Creates Main window
# region Create Widgets
content_widget = QWidget()
central_widget = QWidget() 
sidebar_widget = QWidget()
sidebar_tree = QTreeWidget()
league_rank_page = QWidget()
page_stack = QStackedWidget()
home_page = QWidget()
#endregion 

#region Sidebar Items

#Games
games_item = QTreeWidgetItem(["Games"])
league_item = QTreeWidgetItem(["League of Legends"])
deadlock_item = QTreeWidgetItem(["Deadlock"])
league_rank_item = QTreeWidgetItem(["League Rank"])
deadlock_rank_item = QTreeWidgetItem(["Deadlock Rank"])
# Settings
settings_item = QTreeWidgetItem(["Settings"])
display_item = QTreeWidgetItem(["Display"])
# Cars
car_item = QTreeWidgetItem(["Car Information"])
garage_item = QTreeWidgetItem(["Current Cars"])
# Finances
finance_item = QTreeWidgetItem(["Finances"])
balance_item = QTreeWidgetItem(["Current Balance"])
bills_item = QTreeWidgetItem(["Recurring Expenses"]) 
purchased_item = QTreeWidgetItem(["Purchase History"])

#endregion
#region Labels

welcome_label = QLabel("Proxy's Nexus") # creates label
placeholder_label = QLabel("Main content area")
league_rank_title_label = QLabel("League Rank Page")
peak_rank_label = QLabel("Peak Rank:")
current_rank_label = QLabel("Current Rank:")
win_rate_label = QLabel("Win Rate:")
#endregion
#region Create Layouts

main_layout = QHBoxLayout()
content_layout = QVBoxLayout()
sidebar_layout = QVBoxLayout()
league_rank_layout = QVBoxLayout()
home_layout = QVBoxLayout()

#endregion

#region Configure Objects

#Window
window.setWindowTitle("Proxy's Nexus") #sets the title of the GUI
window.resize(900, 600) #sets window size

#Font
welcome_font = QFont()
welcome_font.setPointSize(20)
welcome_label.setFont(welcome_font) 

welcome_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter) #Determines Placement of Welcome Label

#endregion

#region Functions

def tree_clicked(item, column): #updates placeholder with the tree clicked by user
    updated_placeholder = item.text(0)
    placeholder_label.setText(updated_placeholder)
#endregion
#Connect the Objects(building relationships EX(setLayout)

#region Connect Widgets To Layouts
window.setCentralWidget(central_widget)
content_widget.setLayout(content_layout)
sidebar_widget.setLayout(sidebar_layout)
central_widget.setLayout(main_layout)   
league_rank_page.setLayout(league_rank_layout)

sidebar_tree.itemClicked.connect(tree_clicked) # Connects tree_clicked function to sidebar

home_page.setLayout(home_layout)
#endregion

#region Connect Signals
sidebar_tree.itemClicked.connect(tree_clicked) # Connects tree_clicked function to sidebar
#endregion

#Build each section ex(add widgets)
#region Build Content Pages
content_layout.addWidget(welcome_label)
content_layout.addWidget(page_stack)  
league_rank_layout.addWidget(league_rank_title_label)
league_rank_layout.addWidget(current_rank_label) 
league_rank_layout.addWidget(peak_rank_label)
league_rank_layout.addWidget(win_rate_label)
home_layout.addWidget(placeholder_label)
page_stack.addWidget(home_page)
page_stack.addWidget(league_rank_page)
#endregion

# region Build Sidebar Layout
sidebar_layout.addWidget(sidebar_tree)
#endregion

#Connect the major sections ex(Connect the major sections main_layout.addWidget(sidebar_widget))

#region Build Main Layout
main_layout.addWidget(sidebar_widget) #Adds side bar to main layout
main_layout.addWidget(content_widget)  #adds content widget to main layout
# Sets the amount of space each layout gets 
main_layout.setStretch(0, 1.5)  # sidebar
main_layout.setStretch(1, 3)  # content area
#endregion

#region Build Sidebar Tree

sidebar_tree.setHeaderLabel("Proxy") #using proxy as a place holder
#Top Level Items
sidebar_tree.addTopLevelItem(games_item)
sidebar_tree.addTopLevelItem(settings_item)
sidebar_tree.addTopLevelItem(car_item)
sidebar_tree.addTopLevelItem(finance_item)

#Dropdown menus

games_item.addChild(league_item)
games_item.addChild(deadlock_item)
settings_item.addChild(display_item)
league_item.addChild(league_rank_item)
car_item.addChild(garage_item)
finance_item.addChild(bills_item)
finance_item.addChild(balance_item)
finance_item.addChild(purchased_item)
deadlock_item.addChild(deadlock_rank_item)
#endregion


#END
window.show() # Makes window visible
sys.exit(app.exec()) # Starts the application's event loop and exits the program when the window closes