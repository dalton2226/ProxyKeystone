import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QTreeWidget, QTreeWidgetItem, QStackedWidget, QLineEdit, QComboBox, QPushButton, QListWidget, Qcompleter
from PySide6.QtCore import Qt 
from PySide6.QtGui import QFont
app = QApplication(sys.argv)
window = QMainWindow() # Creates Main window

hero_input = QLineEdit()
kda_input = QLineEdit()
issue_dropdown = QComboBox()
win_button = QPushButton("Win")
loss_button = QPushButton("Loss")
match_list = QListWidget()
save_win_match = QPushButton("Save Match")


hero_input.text()
issue_dropdown.currentText()

win_button.clicked.connect(save_win_match) # Signal for save match button
match_list.addItem()

window.show() # Makes window visible
sys.exit(app.exec()) # Starts the application's event loop and exits the program when the window closes