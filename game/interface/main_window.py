from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout
from game.interface.elements.side_bar import SideBar
from game.interface.elements.inbox import Inbox
from game.interface.elements.club_overview import ClubOverview
from game.interface.elements.league_table import LeagueTable
from game.enums.misc import Misc


class MainWindow(QWidget):
    def __init__(self, league):
        super().__init__()

        self.setWindowTitle(Misc.GameName.value)

        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

        col_one_layout = QVBoxLayout()
        col_one_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        side_bar = SideBar()
        col_one_layout.addWidget(side_bar)

        col_two_layout = QVBoxLayout()
        col_two_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        inbox = Inbox()
        overview = ClubOverview()

        col_two_layout.addWidget(inbox)
        col_two_layout.addWidget(overview)

        col_three_layout = QVBoxLayout()
        col_three_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        league_table = LeagueTable(league)

        col_three_layout.addWidget(league_table)

        layout.addLayout(col_one_layout)
        layout.addLayout(col_two_layout)
        layout.addLayout(col_three_layout)
