#region Imports and Create window
import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QTreeWidget, QTreeWidgetItem, QStackedWidget
from PySide6.QtCore import Qt 
from PySide6.QtGui import QFont
app = QApplication(sys.argv)
window = QMainWindow() # Creates Main window
#endregion
#region Helper Functions
def build_page(page_title): # Helper function the builds the page 
    page = QWidget()
    layout = QVBoxLayout()
    title_label = QLabel(page_title)
    layout.addWidget(title_label)
    page.setLayout(layout)
    return (page, layout)
#endregion
#*Create Objects
#region Create Widgets
content_widget = QWidget()
central_widget = QWidget() 
sidebar_widget = QWidget()
home_page = QWidget()
#Games
games_page = QWidget()
league_page, league_layout = build_page("League Overview")
league_matches_page = QWidget() 
league_accounts_page = QWidget() 
deadlock_page, deadlock_layout = build_page("Deadlock Overview")
deadlock_builds_page = QWidget() 
deadlock_matches_page = QWidget() 
#Finances
finance_page = QWidget() 
balance_page = QWidget() 
bill_page = QWidget()
purchases_page = QWidget() 
#Garage
garage_page = QWidget() 
maintenance_page = QWidget() 
car_wishlist_page = QWidget() 
#Settings
settings_page = QWidget() 
display_page = QWidget() 
sound_page = QWidget() 
sidebar_tree = QTreeWidget()
page_stack = QStackedWidget()
#endregion 
#region Sidebar Items
home_item = QTreeWidgetItem(["Home"])
#Games
games_item = QTreeWidgetItem(["Games"])
league_item = QTreeWidgetItem(["League of Legends"])
deadlock_item = QTreeWidgetItem(["Deadlock"])
league_matches_item = QTreeWidgetItem(["Match History"])
league_accounts_item = QTreeWidgetItem(["Accounts"])
deadlock_builds_item = QTreeWidgetItem(["Builds"])
deadlock_matches_item = QTreeWidgetItem(["Match History"])
# Cars
garage_item = QTreeWidgetItem(["Garage"])
maintenance_item = QTreeWidgetItem(["Maintenance"]) 
car_wishlist_item = QTreeWidgetItem(["Wishlist"]) 
# Finances
finance_item = QTreeWidgetItem(["Finances"])
balance_item = QTreeWidgetItem(["Current Balance"])
bills_item = QTreeWidgetItem(["Recurring Expenses"]) 
purchases_item = QTreeWidgetItem(["Purchase History"])
# Settings
settings_item = QTreeWidgetItem(["Settings"])
display_item = QTreeWidgetItem(["Display"])
sound_item = QTreeWidgetItem(["Sound"])
# ? potential settings Im Considering Link accounts too add different Riot accounts for league or steam accounts for deadlock
#endregion
#region Labels
welcome_label = QLabel("Proxy's Nexus")
placeholder_label = QLabel("Main content area")
home_title_label = QLabel("Home")
#Games
games_title_label = QLabel("Game Library")

league_matches_title_label = QLabel("Match History") 
league_accounts_title_label = QLabel("Accounts") 
#TODO deadlock_title_label = QLabel("Deadlock Overview")
deadlock_builds_title_label = QLabel("Builds") 
deadlock_matches_title_label = QLabel("Match History")


#Finances
finance_title_label = QLabel("Finances") 
balance_title_label = QLabel("Current Balance") 
bill_title_label = QLabel("Bills") 
purchases_title_label = QLabel("Recent Purchases") 
#Garage
garage_title_label = QLabel("Garage") 
maintenance_title_label = QLabel("Maintenance") 
car_wishlist_title_label = QLabel("Car Wishlist") 
#Settings
settings_title_label = QLabel("Settings") 
display_title_label = QLabel("Display Settings") 
sound_title_label = QLabel("Sound Settings") 
#endregion
#region Create Layouts
main_layout = QHBoxLayout()
content_layout = QVBoxLayout()
sidebar_layout = QVBoxLayout()
home_layout = QVBoxLayout() 
#Games
#league_layout = QVBoxLayout() 
#TODO deadlock_layout = QVBoxLayout()
league_matches_layout = QVBoxLayout()
league_accounts_layout = QVBoxLayout()
deadlock_builds_layout = QVBoxLayout()
deadlock_matches_layout = QVBoxLayout()
games_layout = QVBoxLayout()
#Finances
finance_layout = QVBoxLayout()
balance_layout = QVBoxLayout()
bill_layout = QVBoxLayout()
purchases_layout = QVBoxLayout()
#Garage
garage_layout = QVBoxLayout() 
maintenance_layout = QVBoxLayout() 
car_wishlist_layout = QVBoxLayout() 
#Settings
settings_layout = QVBoxLayout()
display_layout = QVBoxLayout()
sound_layout = QVBoxLayout()
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
#region Pagemap
page_map = {league_item: league_page, 
            deadlock_item: deadlock_page, 
            home_item: home_page, 
            league_matches_item: league_matches_page, 
            league_accounts_item: league_accounts_page,
            deadlock_builds_item: deadlock_builds_page, 
            deadlock_matches_item: deadlock_matches_page, 
            finance_item: finance_page, 
            balance_item: balance_page, 
            bills_item: bill_page,
            purchases_item: purchases_page, 
            settings_item: settings_page, 
            display_item: display_page, 
            sound_item: sound_page,
            garage_item: garage_page,
            maintenance_item: maintenance_page,
            car_wishlist_item: car_wishlist_page,
            games_item: games_page}
#endregion
#region Functions

    


def tree_clicked(item, column): 
    if item in page_map:
        page_stack.setCurrentWidget(page_map[item])
    else:
        placeholder_label.setText(item.text(0))
        page_stack.setCurrentWidget(home_page)


#endregion
#* Connect the Objects(building relationships
#region Connect Widgets To Layouts
window.setCentralWidget(central_widget)
content_widget.setLayout(content_layout)
sidebar_widget.setLayout(sidebar_layout)
central_widget.setLayout(main_layout)  
#Games 
#TODO league_page.setLayout(league_layout)
home_page.setLayout(home_layout)
#TODO deadlock_page.setLayout(deadlock_layout)
games_page.setLayout(games_layout)
league_matches_page.setLayout(league_matches_layout) 
league_accounts_page.setLayout(league_accounts_layout)
deadlock_builds_page.setLayout(deadlock_builds_layout) 
deadlock_matches_page.setLayout(deadlock_matches_layout) 
#Finances
finance_page.setLayout(finance_layout) 
balance_page.setLayout(balance_layout) 
bill_page.setLayout(bill_layout) 
purchases_page.setLayout(purchases_layout) 
#Garage
garage_page.setLayout(garage_layout)
maintenance_page.setLayout(maintenance_layout) 
car_wishlist_page.setLayout(car_wishlist_layout) 
#Settings
settings_page.setLayout(settings_layout) 
display_page.setLayout(display_layout) 
sound_page.setLayout(sound_layout)
#endregion
#region Connect Signals
sidebar_tree.itemClicked.connect(tree_clicked) # Connects tree_clicked function to sidebar
#endregion
#*Build each section ex(add widgets)
#region Build Content Pages
content_layout_items = [welcome_label, page_stack]
for item in content_layout_items:
    content_layout.addWidget(item)

home_layout.addWidget(home_title_label)
#TODO Testing build_page function

#Games
#TODO league_layout.addWidget(league_title_label)
#TODO deadlock_layout.addWidget(deadlock_title_label)
league_matches_layout.addWidget(league_matches_title_label)
league_accounts_layout.addWidget(league_accounts_title_label)
deadlock_builds_layout.addWidget(deadlock_builds_title_label)
deadlock_matches_layout.addWidget(deadlock_matches_title_label)
games_layout.addWidget(games_title_label)
#Finances
finance_layout.addWidget(finance_title_label)
balance_layout.addWidget(balance_title_label)
bill_layout.addWidget(bill_title_label)
purchases_layout.addWidget(purchases_title_label)
#Garage
car_wishlist_layout.addWidget(car_wishlist_title_label)
garage_layout.addWidget(garage_title_label) 
maintenance_layout.addWidget(maintenance_title_label) 
#Settings
settings_layout.addWidget(settings_title_label)
display_layout.addWidget(display_title_label)
sound_layout.addWidget(sound_title_label)
home_layout.addWidget(placeholder_label)
#region page stack items
page_stack_items = [home_page, 
                    league_page, 
                    deadlock_page, 
                    league_matches_page, 
                    league_accounts_page, 
                    deadlock_builds_page, 
                    deadlock_matches_page, 
                    finance_page, 
                    balance_page, 
                    bill_page, 
                    purchases_page, 
                    settings_page, 
                    display_page, 
                    sound_page, 
                    garage_page, 
                    maintenance_page, 
                    car_wishlist_page,
                    games_page]
#endregion
for item in page_stack_items:
    page_stack.addWidget(item)
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
top_level_items = [home_item, games_item, garage_item, finance_item, settings_item]
for item in top_level_items:
    sidebar_tree.addTopLevelItem(item)
#Sidebar Menus
games_child_items = [league_item, deadlock_item]

for item in games_child_items:
    games_item.addChild(item)

finance_child_items = [bills_item, balance_item, purchases_item]
for item in finance_child_items:
    finance_item.addChild(item)

deadlock_child_items = [deadlock_builds_item, deadlock_matches_item]
for item in deadlock_child_items:
    deadlock_item.addChild(item)

settings_child_items = [display_item, sound_item]
for item in settings_child_items:
    settings_item.addChild(item)

garage_child_items = [maintenance_item, car_wishlist_item]
for item in garage_child_items:
    garage_item.addChild(item)

league_child_items = [league_matches_item, league_accounts_item]
for item in league_child_items:
    league_item.addChild(item)

#endregion

#region End Program
window.show() # Makes window visible
sys.exit(app.exec()) # Starts the application's event loop and exits the program when the window closes
#endregion
