from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QBrush, QColor
from utils import is_mac_dark_mode

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
        self.black_brush = QBrush(QColor.fromRgb(0, 0, 0))

        corner_heading = QTableWidgetItem("")
        corner_heading.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        corner_heading.setFlags(Qt.ItemFlag.ItemIsEditable)
        corner_heading.setForeground(self.black_brush)
        corner_heading.setBackground(self.heading_brush)

        team_heading = QTableWidgetItem("Team")
        team_heading.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        team_heading.setFlags(Qt.ItemFlag.ItemIsEditable)
        team_heading.setForeground(self.black_brush)
        team_heading.setBackground(self.heading_brush)

        played_heading = QTableWidgetItem("Played")
        played_heading.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        played_heading.setFlags(Qt.ItemFlag.ItemIsEditable)
        played_heading.setForeground(self.black_brush)
        played_heading.setBackground(self.heading_brush)

        points_heading = QTableWidgetItem("Points")
        points_heading.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        points_heading.setFlags(Qt.ItemFlag.ItemIsEditable)
        points_heading.setForeground(self.black_brush)
        points_heading.setBackground(self.heading_brush)

        self.table.setItem(0, 0, corner_heading)
        self.table.setItem(0, 1, team_heading)
        self.table.setItem(0, 2, played_heading)
        self.table.setItem(0, 3, points_heading)

        self.update_table(league, currently_selected_team)

        layout.addWidget(self.table)

    def update_table(self, league, currently_selected_team):
        league_table = league.get_sorted_league_table()
        row_counter = 1

        promo_brush = QBrush(QColor.fromRgb(187, 243, 187))
        relegation_brush = QBrush(QColor.fromRgb(255, 187, 187))
        primary_brush = QBrush(QColor.fromRgb(255, 255, 255))
        secondary_brush = QBrush(QColor.fromRgb(241, 242, 242))
        use_primary_brush = True

        for row in league_table:
            name_item = QTableWidgetItem(row.team.name)
            played_item = QTableWidgetItem(str(row.played))
            points_item = QTableWidgetItem(str(row.points()))

            name_item.setFlags(Qt.ItemFlag.ItemIsEditable)
            played_item.setFlags(Qt.ItemFlag.ItemIsEditable)
            points_item.setFlags(Qt.ItemFlag.ItemIsEditable)

            name_item.setForeground(self.black_brush)
            played_item.setForeground(self.black_brush)
            points_item.setForeground(self.black_brush)

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
                elif is_mac_dark_mode():
                    # Dark Mode theme on mac doesn't work properly for this widget
                    brush_to_use = primary_brush if use_primary_brush else secondary_brush
                    name_item.setBackground(brush_to_use)
                    played_item.setBackground(brush_to_use)
                    points_item.setBackground(brush_to_use)

                use_primary_brush = not use_primary_brush

            number_heading = QTableWidgetItem(str(row_counter))

            if row_counter == 1:
                number_heading = QTableWidgetItem("🏆")

            number_heading.setFlags(Qt.ItemFlag.ItemIsEditable)
            number_heading.setForeground(self.black_brush)
            number_heading.setBackground(self.heading_brush)

            self.table.setItem(row_counter, 0, number_heading)
            self.table.setItem(row_counter, 1, name_item)
            self.table.setItem(row_counter, 2, played_item)
            self.table.setItem(row_counter, 3, points_item)

            row_counter += 1

        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
