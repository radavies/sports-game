from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from pathlib import Path
from game.enums.misc import Misc


class IntroWindow(QWidget):
    def __init__(self, team_name, league_name, continue_function):
        super().__init__()
        self.setWindowTitle("Introduction")

        self.resize(500, 350)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

        folder = Path(Misc.DataFolderPath.value)
        intro_file = folder / Misc.IntroFileName.value
        text_label = QLabel(open(intro_file, encoding="utf8").read().format(team_name, league_name))
        text_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        layout.addWidget(text_label)

        continue_button = QPushButton("Continue")
        continue_button.clicked.connect(continue_function)

        layout.addWidget(continue_button)
