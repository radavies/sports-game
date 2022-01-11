from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QListWidget, QListWidgetItem
from PyQt6.QtGui import QIcon
from pathlib import Path
from game.enums.misc import Misc


class MatchSimWindow(QWidget):
    def __init__(self, league, home_team, away_team):
        super().__init__()

        self.icon_folder = Path(Misc.ImageFolderPath.value)

        self.setWindowTitle("{} Vs {}".format(home_team.name, away_team.name))

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

        league_name_label = QLabel(league.name, objectName="subHeadingBoldLbl")
        league_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        match_day_label = QLabel("Match Day {}".format(league.current_match_day), objectName="boldUnderlineLbl")
        match_day_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        score_layout = QHBoxLayout()

        home_team_label = QLabel(home_team.name, objectName="boldLbl")
        self.home_team_score_label = QLabel("0")
        vs_label = QLabel("Vs")
        self.away_team_score_label = QLabel("0")
        away_team_label = QLabel(away_team.name, objectName="boldLbl")

        score_layout.addWidget(home_team_label)
        score_layout.addWidget(self.home_team_score_label)
        score_layout.addWidget(vs_label)
        score_layout.addWidget(self.away_team_score_label)
        score_layout.addWidget(away_team_label)

        self.mins_played_label = QLabel("{} mins".format(0))
        self.mins_played_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.match_updates = QListWidget()
        self.match_updates.setWordWrap(True)
        self.match_updates.setIconSize(QSize(35, 35))

        self.continue_button = QPushButton("Continue")
        self.continue_button.setEnabled(False)
        self.continue_button.clicked.connect(self.continue_button_pressed)

        layout.addWidget(league_name_label)
        layout.addWidget(match_day_label)

        layout.addLayout(score_layout)

        layout.addWidget(self.mins_played_label)

        layout.addWidget(self.match_updates)

        layout.addWidget(self.continue_button)

    def continue_button_pressed(self):
        self.close()

    def enable_continue_button(self):
        self.continue_button.setEnabled(True)

    def update_match(self, match_update):
        self.mins_played_label.setText("{} mins".format(match_update.mins_played))
        self.home_team_score_label.setText(str(match_update.home_scored))
        self.away_team_score_label.setText(str(match_update.away_scored))

        for event in match_update.new_events:
            if event is not None:
                event_icon = self.icon_folder / event[0]
                self.match_updates.insertItem(0, QListWidgetItem(QIcon(str(event_icon)), event[1]))
