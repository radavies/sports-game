from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt6.QtGui import QBrush, QColor


class LeagueTable(QWidget):
    def __init__(self, league, currently_selected_team):
        super().__init__()

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

        title_label = QLabel(league.__str__(), objectName="headingLbl")
        layout.addWidget(title_label)

        self.table = QTableWidget(len(league.teams), 3)
        self.table.setSortingEnabled(False)
        self.table.setAlternatingRowColors(True)
        self.table.setCornerButtonEnabled(False)
        self.table.setDragEnabled(False)
        self.update_table(league, currently_selected_team)
        layout.addWidget(self.table)

    def update_table(self, league, currently_selected_team):
        league_table = league.get_sorted_league_table()
        row_counter = 1

        # Add headings
        header = self.table.horizontalHeader()
        #header = QHeaderView(Qt.Orientation.Horizontal)
        #self.table.setHorizontalHeader(header)

        # heading_brush = QBrush(QColor.fromRgb(148, 148, 148))
        #
        # team_heading = QTableWidgetItem("Team")
        # team_heading.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        # team_heading.setBackground(heading_brush)
        #
        # played_heading = QTableWidgetItem("Played")
        # played_heading.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        # played_heading.setBackground(heading_brush)
        #
        # points_heading = QTableWidgetItem("Points")
        # points_heading.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        # points_heading.setBackground(heading_brush)
        #
        # self.table.setItem(0, 0, team_heading)
        # self.table.setItem(0, 1, played_heading)
        # self.table.setItem(0, 2, points_heading)

        # Add normal rows
        # TODO Add brushes for promo / winners and demotion places
        for row in league_table:
            name_item = QTableWidgetItem(row.team.name)
            played_item = QTableWidgetItem(str(row.played))
            points_item = QTableWidgetItem(str(row.points()))

            if row.team.name == currently_selected_team.name:
                current_team_brush = QBrush(QColor.fromRgb(255, 218, 106))
                name_item.setBackground(current_team_brush)
                played_item.setBackground(current_team_brush)
                points_item.setBackground(current_team_brush)

            self.table.setItem(row_counter, 0, name_item)
            self.table.setItem(row_counter, 1, played_item)
            self.table.setItem(row_counter, 2, points_item)
            row_counter += 1
