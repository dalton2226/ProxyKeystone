#region Imports and Create window
import sys, json
from PySide6.QtWidgets import QApplication, QCompleter, QLabel, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QTreeWidget, QTreeWidgetItem, QStackedWidget, QLineEdit, QComboBox, QPushButton, QListWidget, QDialog, QGraphicsPixmapItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtGui import QPixmap
app = QApplication(sys.argv)
window = QMainWindow() # Creates Main window
#endregion

#region Helper Functions
def build_page(page_title): # Helper function that helps builds the pages
    page = QWidget()
    layout = QVBoxLayout()
    title_label = QLabel(page_title)
    layout.addWidget(title_label)
    page.setLayout(layout)
    return (page, layout)
#endregion

#* Create UI Objects

#region Deadlock Matches List
try:
    with open("deadlock_matches.json", "r") as file:
        deadlock_matches = json.load(file)
except FileNotFoundError:
    deadlock_matches = []
    
#endregion
#region Create Pages
content_widget = QWidget()
central_widget = QWidget() 
sidebar_widget = QWidget()
sidebar_tree = QTreeWidget()
page_stack = QStackedWidget()
home_page, home_layout = build_page("Home")
#Games
games_page, games_layout = build_page("Game Library")
league_page, league_layout = build_page("League Overview")
league_matches_page, league_matches_layout = build_page("Match History")
league_accounts_page, league_accounts_layout = build_page("Accounts")
deadlock_page, deadlock_layout = build_page("Deadlock Overview")
deadlock_builds_page, deadlock_builds_layout = build_page("Builds")
deadlock_matches_page, deadlock_matches_layout = build_page("Match History")
#Finances
finance_page,finance_layout = build_page("Finances")
balance_page,balance_layout = build_page("Current Balance")
bill_page,bill_layout = build_page("Bills")
purchases_page,purchases_layout = build_page("Recent Purchases")
#Garage
garage_page,garage_layout = build_page("Garage")
maintenance_page, maintenance_layout = build_page("Maintenance")
car_wishlist_page, car_wishlist_layout = build_page("Car Wishlist")
#Settings
settings_page, settings_layout = build_page("Settings")
display_page, display_layout = build_page("Display Settings")
sound_page, sound_layout = build_page("Sound Settings")
#endregion 
#region Deadlock match logger widgets
match_list = QListWidget()
add_match_button = QPushButton("Add Match")
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
deadlock_rank_label = QLabel("Current Rank")

#endregion
#region Create Layouts
main_layout = QHBoxLayout()
content_layout = QVBoxLayout()
sidebar_layout = QVBoxLayout()


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

#region Load Json Files
for match in deadlock_matches:
    match_results = f"Match Results: {match['result']} • Rank: {match['rank']} {match['division']} • Character: {match['hero']} • KDA: {match['kda']} • Main Issue: {match['issue']}"
    match_list.addItem(match_results)
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

def open_match_dialog():
    deadlock_add_match_dialog = QDialog()
    deadlock_add_match_dialog_layout = QVBoxLayout()
    deadlock_add_match_dialog_label = QLabel("Add Match")
    deadlock_add_match_dialog.setWindowTitle("Add Match")
    deadlock_add_match_dialog.setMinimumSize(300, 250)
    deadlock_add_match_dialog.setLayout(deadlock_add_match_dialog_layout)
    deadlock_add_match_dialog_layout.addWidget(deadlock_add_match_dialog_label)
    hero_names = ["Abrams", 
              "Apollo", 
              "Bebop", 
              "Billy", 
              "Calico", 
              "Celeste",
              "Doorman", 
              "Drifter", 
              "Dynamo", 
              "Graves", 
              "Grey Talon",
              "Haze",
              "Holliday",
              "Infernus",
              "Ivy",
              "Kelvin",
              "Lady Geist",
              "Lash",
              "McGinnis",
              "Mina",
              "Mirage",
              "Mo & Krill",
              "Paige",
              "Paradox",
              "Pocket",
              "Rem", 
              "Seven",
              "Shiv",
              "Silver",
              "Sinclair",
              "Venator",
              "Victor",
              "Vindicta",
              "Viscous",
              "Vyper",
              "Warden",
              "Wraith",
              "Yamato"]
    rank_names = ["Initiate",
                  "Seeker",
                  "Alchemist",
                  "Arcanist",
                  "Ritualist",
                  "Emissary",
                  "Archon",
                  "Oracle",
                  "Phantom",
                  "Ascendant",
                  "Eternus"]
    division_names = ["I",
                      "II",
                      "III",
                      "IV",
                      "V",
                      "*"]
    hero_dropdown = QComboBox()
    rank_dropdown = QComboBox()
    division_dropdown = QComboBox()
    deadlock_dialog_hero_label = QLabel("Character")
    deadlock_dialog_rank_label = QLabel("Average Rank of Game")
    deadlock_dialog_division_label = QLabel("Division")
    deadlock_dialog_issue_label = QLabel("Biggest Issue Had During Game")
    deadlock_dialog_kda_label = QLabel("KDA")
    hero_dropdown.setEditable(True)
    hero_dropdown.addItems(hero_names)
    hero_completer = QCompleter(hero_names)
    hero_completer.setFilterMode(Qt.MatchStartsWith)
    hero_dropdown.setCompleter(hero_completer)
    hero_dropdown.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
    hero_completer.setCaseSensitivity(Qt.CaseInsensitive)
    division_dropdown.setEditable(True)
    division_dropdown.addItems(division_names)
    division_completer = QCompleter(division_names)
    division_completer.setFilterMode(Qt.MatchStartsWith)
    division_dropdown.setCompleter(division_completer)
    division_dropdown.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
    division_completer.setCaseSensitivity(Qt.CaseInsensitive)
    rank_dropdown.setEditable(True)
    rank_dropdown.addItems(rank_names)
    rank_completer = QCompleter(rank_names)
    rank_completer.setFilterMode(Qt.MatchStartsWith)
    rank_dropdown.setCompleter(rank_completer)
    rank_dropdown.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
    rank_completer.setCaseSensitivity(Qt.CaseInsensitive)
    kda_input = QLineEdit()
    kda_input.setPlaceholderText("K/D/A, example: 8/5/12")
    issue_dropdown = QComboBox()
    issue_names = ["Positioning", "Aim", "Bad items", "Fed early", "Team fights", "Objectives", "Other"]
    issue_dropdown.addItems(issue_names)
    win_button = QPushButton("Win")
    loss_button = QPushButton("Loss")
    deadlock_add_match_dialog_layout.addWidget(deadlock_dialog_hero_label)
    deadlock_add_match_dialog_layout.addWidget(hero_dropdown)
    deadlock_add_match_dialog_layout.addWidget(deadlock_dialog_rank_label)
    deadlock_add_match_dialog_layout.addWidget(rank_dropdown)
    deadlock_add_match_dialog_layout.addWidget(deadlock_dialog_division_label)
    deadlock_add_match_dialog_layout.addWidget(division_dropdown)
    deadlock_add_match_dialog_layout.addWidget(deadlock_dialog_kda_label)
    deadlock_add_match_dialog_layout.addWidget(kda_input)
    deadlock_add_match_dialog_layout.addWidget(deadlock_dialog_issue_label)
    deadlock_add_match_dialog_layout.addWidget(issue_dropdown)
    deadlock_add_match_dialog_layout.addWidget(win_button)
    deadlock_add_match_dialog_layout.addWidget(loss_button)
    def save_win_match():
        hero = hero_dropdown.currentText()
        kda = kda_input.text()
        issue = issue_dropdown.currentText()
        result = "Win"
        rank = rank_dropdown.currentText()
        division = division_dropdown.currentText()
        deadlock_match = {
        "hero": hero,
        "result": result,
        "kda": kda,
        "issue": issue,
        "rank": rank,
        "division": division}
        current_rank = f"{rank} Division {division}"
        deadlock_rank_label.setText(f"Current Rank: {current_rank}")
        win_match_results = f"Match Results: {result} • Rank: {rank} {division} • Character- {hero} • KDA- {kda} • Main Issue- {issue}"
        match_list.addItem(win_match_results)
        deadlock_matches.append(deadlock_match)
        with open("deadlock_matches.json", "w") as file:
            json.dump(deadlock_matches, file, indent=4)
        deadlock_add_match_dialog.accept()

    def save_loss_match():
        hero = hero_dropdown.currentText()
        kda = kda_input.text()
        issue = issue_dropdown.currentText()
        result = "Loss"
        rank = rank_dropdown.currentText()
        division = division_dropdown.currentText()
        deadlock_match = {
        "hero": hero,
        "result": result,
        "kda": kda,
        "issue": issue,
        "rank": rank,
        "division": division}
        current_rank = f"{rank} Division {division}"
        deadlock_rank_label.setText(f"Current Rank: {current_rank}")
        loss_match_results = f"Match Results: {result} • Rank: {rank} {division} • Character- {hero} • KDA- {kda} • Main Issue- {issue}"
        match_list.addItem(loss_match_results) 
        deadlock_matches.append(deadlock_match)
        with open("deadlock_matches.json", "w") as file:
            json.dump(deadlock_matches, file, indent=4)
        deadlock_add_match_dialog.accept()

    win_button.clicked.connect(save_win_match)
    loss_button.clicked.connect(save_loss_match)

    deadlock_add_match_dialog.exec()
    #Save Match Dialog
if deadlock_matches:
    latest_match = deadlock_matches[-1]
    rank = latest_match["rank"]
    division = latest_match["division"]
    deadlock_rank_label.setText(f"Current Rank: {rank} Division {division}")
#endregion

#* Connect the Objects(building relationships

#region Connect Widgets To Layouts
window.setCentralWidget(central_widget)
content_widget.setLayout(content_layout)
sidebar_widget.setLayout(sidebar_layout)
central_widget.setLayout(main_layout)  
#add widgets to layouts

#endregion
#region Connect Signals
sidebar_tree.itemClicked.connect(tree_clicked) # Connects tree_clicked function to sidebar
add_match_button.clicked.connect(open_match_dialog) # Connects create match button to open_match_dialog function
#endregion

#*Build each section ex(add widgets)

#region Build Content Pages
content_layout_items = [welcome_label, page_stack]
for item in content_layout_items:
    content_layout.addWidget(item)

home_layout.addWidget(placeholder_label)

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

for item in page_stack_items:
    page_stack.addWidget(item)

# Add Deadlock labels
deadlock_layout.addWidget(deadlock_rank_label)
deadlock_matches_layout.addWidget(add_match_button)
deadlock_matches_layout.addWidget(match_list)

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
