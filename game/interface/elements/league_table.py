from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QBrush, QColor


class LeagueTable(QWidget):
    def __init__(self, league, currently_selected_team):
        super().__init__()

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

        title_label = QLabel(league.__str__(), objectName="headingLbl")
        layout.addWidget(title_label)

        self.table = QTableWidget(len(league.teams), 4)
        self.table.setSortingEnabled(False)
        self.table.setAlternatingRowColors(True)
        self.table.setCornerButtonEnabled(False)
        self.table.setDragEnabled(False)
        self.table.horizontalHeader().hide()
        self.table.verticalHeader().hide()

        self.heading_brush = QBrush(QColor.fromRgb(148, 148, 148))

        corner_heading = QTableWidgetItem("")
        corner_heading.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        corner_heading.setBackground(self.heading_brush)

        team_heading = QTableWidgetItem("Team")
        team_heading.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        team_heading.setBackground(self.heading_brush)

        played_heading = QTableWidgetItem("Played")
        played_heading.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        played_heading.setBackground(self.heading_brush)

        points_heading = QTableWidgetItem("Points")
        points_heading.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        points_heading.setBackground(self.heading_brush)

        self.table.setItem(0, 0, corner_heading)
        self.table.setItem(0, 1, team_heading)
        self.table.setItem(0, 2, played_heading)
        self.table.setItem(0, 3, points_heading)

        self.update_table(league, currently_selected_team)

        layout.addWidget(self.table)

        # TODO - make the whole thing not editable

    def update_table(self, league, currently_selected_team):
        league_table = league.get_sorted_league_table()
        row_counter = 1

        promo_brush = QBrush(QColor.fromRgb(187, 243, 187))
        relegation_brush = QBrush(QColor.fromRgb(255, 187, 187))

        for row in league_table:
            name_item = QTableWidgetItem(row.team.name)
            played_item = QTableWidgetItem(str(row.played))
            points_item = QTableWidgetItem(str(row.points()))

            if row.team.name == currently_selected_team.name:
                current_team_brush = QBrush(QColor.fromRgb(255, 218, 106))
                name_item.setBackground(current_team_brush)
                played_item.setBackground(current_team_brush)
                points_item.setBackground(current_team_brush)
            else:
                if league.is_in_promo_zone(row_counter):
                    name_item.setBackground(promo_brush)
                    played_item.setBackground(promo_brush)
                    points_item.setBackground(promo_brush)
                elif league.is_in_relegation_zone(row_counter):
                    name_item.setBackground(relegation_brush)
                    played_item.setBackground(relegation_brush)
                    points_item.setBackground(relegation_brush)

            number_heading = QTableWidgetItem(str(row_counter))
            if row_counter == 1:
                number_heading = QTableWidgetItem("🏆")

            number_heading.setBackground(self.heading_brush)

            self.table.setItem(row_counter, 0, number_heading)
            self.table.setItem(row_counter, 1, name_item)
            self.table.setItem(row_counter, 2, played_item)
            self.table.setItem(row_counter, 3, points_item)

            row_counter += 1

        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
