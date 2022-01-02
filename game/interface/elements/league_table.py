from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton


class LeagueTable(QWidget):
    def __init__(self, league):
        super().__init__()

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

        title_label = QLabel(league.__str__(), objectName="headingLbl")
        layout.addWidget(title_label)

