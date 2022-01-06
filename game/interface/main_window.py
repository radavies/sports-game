from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout
from game.interface.elements.side_bar import SideBar
from game.interface.elements.inbox import Inbox
from game.interface.elements.club_overview import ClubOverview
from game.interface.elements.league_table import LeagueTable
from game.interface.elements.next_fixture import NextFixture
from game.enums.misc import Misc


class MainWindow(QWidget):
    def __init__(self, league, currently_selected_team, advance_game_function):
        super().__init__()

        self.setWindowTitle(Misc.GameName.value)

        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

        col_one_layout = QVBoxLayout()
        col_one_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.side_bar = SideBar(advance_game_function)
        col_one_layout.addWidget(self.side_bar)

        col_two_layout = QVBoxLayout()
        col_two_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        inbox = Inbox()
        overview = ClubOverview()

        col_two_layout.addWidget(inbox)
        col_two_layout.addWidget(overview)

        col_three_layout = QVBoxLayout()
        col_three_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        league_table = LeagueTable(league, currently_selected_team)

        fixture = league.get_next_fixture_for_team(currently_selected_team)
        next_fixture = NextFixture()
        if fixture is not None:
            next_fixture.update_fixture(fixture[0], fixture[1], league.current_match_day)

        col_three_layout.addWidget(league_table)
        col_three_layout.addWidget(next_fixture)

        layout.addLayout(col_one_layout)
        layout.addLayout(col_two_layout)
        layout.addLayout(col_three_layout)

    def enable_advance_button(self):
        self.side_bar.enable_advance_button()
