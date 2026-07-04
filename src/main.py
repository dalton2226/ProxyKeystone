#region Imports and Create window
import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QTreeWidget, QTreeWidgetItem, QStackedWidget
from PySide6.QtCore import Qt 
from PySide6.QtGui import QFont
app = QApplication(sys.argv)
window = QMainWindow() # Creates Main window
#endregion

#*Create Objects

#region Create Widgets
home_page = QWidget()
content_widget = QWidget()
central_widget = QWidget() 
sidebar_widget = QWidget()
league_page = QWidget()
sidebar_tree = QTreeWidget()
page_stack = QStackedWidget()

#endregion 

#region Sidebar Items

#Games
games_item = QTreeWidgetItem(["Games"])
league_item = QTreeWidgetItem(["League of Legends"])
deadlock_item = QTreeWidgetItem(["Deadlock"])
league_matches_item = QTreeWidgetItem(["Match History"])
league_accounts_item = QTreeWidgetItem(["Accounts"])
deadlock_builds_item = QTreeWidgetItem(["Builds"])
deadlock_matches_item = QTreeWidgetItem(["Match History"])


# Cars
car_item = QTreeWidgetItem(["Car Information"])
garage_item = QTreeWidgetItem(["Garage"])
maintenance_item = QTreeWidgetItem(["Maintenance"]) 
car_wishlist_item = QTreeWidgetItem(["Wishlist"]) 

# Finances
finance_item = QTreeWidgetItem(["Finances"])
balance_item = QTreeWidgetItem(["Current Balance"])
bills_item = QTreeWidgetItem(["Recurring Expenses"]) 
purchased_item = QTreeWidgetItem(["Purchase History"])

# Settings
settings_item = QTreeWidgetItem(["Settings"])
display_item = QTreeWidgetItem(["Display"])
sound_item = QTreeWidgetItem(["Sound"])
# ? potential settings Im Considering Link accounts too add different Riot accounts for league or steam accounts for deadlock


#endregion
#region Labels

welcome_label = QLabel("Proxy's Nexus")
placeholder_label = QLabel("Main content area")
league_title_label = QLabel("League Overview")
#endregion
#region Create Layouts

main_layout = QHBoxLayout()
content_layout = QVBoxLayout()
sidebar_layout = QVBoxLayout()
league_layout = QVBoxLayout()
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
#TODO If the clicked item is league_item: switch the page stack to league_page 
#TODO Otherwise: update the placeholder label with the clicked item's text switch the page stack to home_page
def tree_clicked(item, column): #updates placeholder with the tree clicked by user
    if item == league_item:
        page_stack.setCurrentWidget(league_page)
    else:
        placeholder_label.setText (item.text(0))
        page_stack.setCurrentWidget(home_page)
    
    
    
#endregion

#*Connect the Objects(building relationships

#region Connect Widgets To Layouts
window.setCentralWidget(central_widget)

content_widget.setLayout(content_layout)
sidebar_widget.setLayout(sidebar_layout)
central_widget.setLayout(main_layout)   
league_page.setLayout(league_layout)
home_page.setLayout(home_layout)
#endregion

#region Connect Signals
sidebar_tree.itemClicked.connect(tree_clicked) # Connects tree_clicked function to sidebar
#endregion

#*Build each section ex(add widgets)

#region Build Content Pages

content_layout_items = [welcome_label, page_stack]
for item in content_layout_items:
    content_layout.addWidget(item)

league_layout.addWidget(league_title_label)

home_layout.addWidget(placeholder_label)

page_stack.addWidget(home_page)
page_stack.addWidget(league_page)
#endregion

#region Build Sidebar Layout
sidebar_layout.addWidget(sidebar_tree)
#endregion

#Connect the major sections

#region Build Main Layout

main_layout_items = [sidebar_widget, content_widget] #Adds side bar and content widget to main layout
for item in main_layout_items:
    main_layout.addWidget(item)

# Sets the amount of space each layout gets 
main_layout.setStretch(0, 1.5)  # sidebar
main_layout.setStretch(1, 3)  # content area
#endregion

#region Build Sidebar Tree

sidebar_tree.setHeaderLabel("Proxy") #Sets Tree header name as Proxy(Placeholder)

#Top Level Items
top_level_items = [games_item,settings_item,car_item,finance_item]
for item in top_level_items:
    sidebar_tree.addTopLevelItem(item)


#Dropdown menus
games_child_items = [league_item,deadlock_item]
for item in games_child_items:
    games_item.addChild(item)

finance_child_items = [bills_item,balance_item,purchased_item]
for item in finance_child_items:
    finance_item.addChild(item)

deadlock_child_items = [deadlock_builds_item, deadlock_matches_item]
for item in deadlock_child_items:
    deadlock_item.addChild(item)

settings_child_items = [display_item, sound_item]
for item in settings_child_items:
    settings_item.addChild(item)

car_child_items = [garage_item, maintenance_item, car_wishlist_item]
for item in car_child_items:
    car_item.addChild(item)

league_child_items = [league_matches_item,league_accounts_item]
for item in league_child_items:
    league_item.addChild(item)




#endregion

























#region Exit
window.show() # Makes window visible
sys.exit(app.exec()) # Starts the application's event loop and exits the program when the window closes
#endregion