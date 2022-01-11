from enum import Enum


class DialogEnum(Enum):
    GroupKickOff = "GroupKickOff"
    GroupGoal = "GroupGoal"
    GroupFoul = "GroupFoul"
    GroupYellow = "GroupYellow"
    GroupRed = "GroupRed"
    GroupFirstHalfEnd = "GroupFirstHalfEnd"
    GroupSecondHalfStart = "GroupSecondHalfStart"
    GroupGameEnd = "GroupGameEnd"

    ReplacementPlaceholderScorer = "{scorer}"
    ReplacementPlaceholderFouler = "{fouler}"
    ReplacementPlaceholderHomeTeam = "{home_team}"
    ReplacementPlaceholderAwayTeam = "{away_team}"
    ReplacementPlaceholderHomeTeamScored = "{home_scored}"
    ReplacementPlaceholderAwayTeamScored = "{away_scored}"
