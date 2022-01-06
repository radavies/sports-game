from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton


class SideBar(QWidget):
    def __init__(self, advance_game_function):
        super().__init__()

        self.advance_game_function = advance_game_function
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

        self.continue_button = QPushButton("Advance")
        self.continue_button.clicked.connect(self.button_clicked)
        layout.addWidget(self.continue_button)

    def button_clicked(self):
        self.continue_button.setEnabled(False)
        self.advance_game_function()

    def enable_advance_button(self):
        self.continue_button.setEnabled(True)
