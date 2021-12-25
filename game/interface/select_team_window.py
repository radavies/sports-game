from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QListWidget, QPushButton
from game.enums.misc import Misc


class SelectTeamWindow(QWidget):
    def __init__(self, leagues, team_selected_function):
        super().__init__()

        self.call_back_function = team_selected_function
        self.selected_team = None

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
            team_list.itemClicked.connect(self.selection_changed)

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
            team_list.itemClicked.connect(self.selection_changed)

            for team in league.teams:
                team_list.addItem(team.name)
            league_layout.addWidget(team_list)
            end_wales_layout.addLayout(league_layout)

        self.select_button = QPushButton("Select Team")
        self.select_button.clicked.connect(self.select_button_clicked)
        self.select_button.setEnabled(False)

        layout.addWidget(self.select_button)

    def selection_changed(self, selected):
        self.selected_team = selected.text()
        self.select_button.setText("Select {}".format(selected.text()))
        self.select_button.setEnabled(True)

    def select_button_clicked(self):
        self.call_back_function(self.selected_team)
