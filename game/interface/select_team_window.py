from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QListWidget, QPushButton
from game.enums.misc import Misc


class SelectTeamWindow(QWidget):
    def __init__(self, leagues):
        super().__init__()
        self.setWindowTitle("{} - {}".format(Misc.GameName.value, "Choose Team"))

        self.resize(1500, 850)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

        title_label = QLabel("So, who's your team?", objectName="headingLbl")
        layout.addWidget(title_label)

        sco_layout = QHBoxLayout()
        sco_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addLayout(sco_layout)

        for league in leagues.leagues["Scotland"]:
            league_layout = QVBoxLayout()
            league_label = QLabel(str(league))
            league_layout.addWidget(league_label)
            team_list = QListWidget()
            for team in league.teams:
                team_list.addItem(team.name)
            league_layout.addWidget(team_list)
            sco_layout.addLayout(league_layout)

        end_wales_layout = QHBoxLayout()
        end_wales_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addLayout(end_wales_layout)

        for league in leagues.leagues["England & Wales"]:
            league_layout = QVBoxLayout()
            league_label = QLabel(str(league))
            league_layout.addWidget(league_label)
            team_list = QListWidget()
            for team in league.teams:
                team_list.addItem(team.name)
            league_layout.addWidget(team_list)
            end_wales_layout.addLayout(league_layout)

        select_button = QPushButton("Select Team")
        select_button.setEnabled(False)
        layout.addWidget(select_button)
        #select_button.clicked.connect(new_game_function)

        #TODO if you select from one list it clears the selection on the others
        #TODO enable the select button if you have a selection