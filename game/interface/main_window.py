from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from game.enums.misc import Misc


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(Misc.GameName.value)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

        continue_button = QPushButton("Continue")
        layout.addWidget(continue_button)

