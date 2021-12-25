from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from game.enums.misc import Misc


class SelectTeamWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("{} - {}".format(Misc.GameName.value, "Choose Team"))

        self.resize(500, 350)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

        title_label = QLabel("So, who's your team?")

        layout.addWidget(title_label)
