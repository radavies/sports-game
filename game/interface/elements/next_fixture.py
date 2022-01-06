from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel


class NextFixture(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

        self.title_label = QLabel("Next Game", objectName="headingLbl")
        self.game_label = QLabel("No game scheduled...")

        layout.addWidget(self.title_label)
        layout.addWidget(self.game_label)

    def update_fixture(self, home_team, away_team, match_day):
        self.title_label.setText("Match Day {}".format(match_day))
        self.game_label.setText("{} Vs {}".format(home_team, away_team))
