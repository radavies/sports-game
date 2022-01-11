import random
from game.enums.dialog_enum import DialogEnum


class Dialog:

    def __init__(self):
        self.dialog_options = {
            DialogEnum.GroupKickOff.value: [],
            DialogEnum.GroupGoal.value: [],
            DialogEnum.GroupFoul.value: [],
            DialogEnum.GroupYellow.value: [],
            DialogEnum.GroupRed.value: [],
            DialogEnum.GroupFirstHalfEnd.value: [],
            DialogEnum.GroupSecondHalfStart.value: [],
            DialogEnum.GroupGameEnd.value: []
        }

        self.populate_dialog_options()

    def populate_dialog_options(self):
        # TODO Read these in from a file or something (also if I do that move this class so it is initialised once)
        self.dialog_options[DialogEnum.GroupKickOff.value].append("The game is underway")
        self.dialog_options[DialogEnum.GroupGoal.value].append(
            "{} has scored a cracker".format(DialogEnum.ReplacementPlaceholderScorer.value)
        )
        self.dialog_options[DialogEnum.GroupFoul.value].append(
            "That's a foul by {}".format(DialogEnum.ReplacementPlaceholderFouler.value)
        )
        self.dialog_options[DialogEnum.GroupYellow.value].append(
            "{} has picked up a yellow card".format(DialogEnum.ReplacementPlaceholderFouler.value)
        )
        self.dialog_options[DialogEnum.GroupRed.value].append(
            "The ref has sent {} off!".format(DialogEnum.ReplacementPlaceholderFouler.value)
        )
        self.dialog_options[DialogEnum.GroupFirstHalfEnd.value].append(
            "The players leave the pitch for half time"
        )
        self.dialog_options[DialogEnum.GroupSecondHalfStart.value].append(
            "The players return for the second half"
        )
        self.dialog_options[DialogEnum.GroupGameEnd.value].append(
            "It's all over, the game ends {} {}, {} {}".format(
                DialogEnum.ReplacementPlaceholderHomeTeam.value,
                DialogEnum.ReplacementPlaceholderHomeTeamScored.value,
                DialogEnum.ReplacementPlaceholderAwayTeam.value,
                DialogEnum.ReplacementPlaceholderAwayTeamScored.value
            )
        )

    def get_random_option_for_group(self, dialog_group, player, home_team, away_team, home_scored, away_scored):
        # TODO Remember the options for each group that have been used and try to use others before recycling
        options_len = len(self.dialog_options[dialog_group.value])
        if options_len > 0:
            option = random.randint(0, options_len - 1)
            return self.do_replacements(
                self.dialog_options[dialog_group.value][option],
                player, home_team, away_team, home_scored, away_scored
            )
        return None

    @staticmethod
    def do_replacements(dialog, player, home_team, away_team, home_scored, away_scored):
        # TODO this only works for one player dialogs right now
        #  (also might need to add other keys for using first names)
        if DialogEnum.ReplacementPlaceholderScorer.value in dialog:
            dialog = dialog.replace(DialogEnum.ReplacementPlaceholderScorer.value, player.name_last)
        if DialogEnum.ReplacementPlaceholderFouler.value in dialog:
            dialog = dialog.replace(DialogEnum.ReplacementPlaceholderFouler.value, player.name_last)
        if DialogEnum.ReplacementPlaceholderHomeTeam.value in dialog:
            dialog = dialog.replace(DialogEnum.ReplacementPlaceholderHomeTeam.value, home_team.name)
        if DialogEnum.ReplacementPlaceholderAwayTeam.value in dialog:
            dialog = dialog.replace(DialogEnum.ReplacementPlaceholderAwayTeam.value, away_team.name)
        if DialogEnum.ReplacementPlaceholderHomeTeamScored.value in dialog:
            dialog = dialog.replace(DialogEnum.ReplacementPlaceholderHomeTeamScored.value, str(home_scored))
        if DialogEnum.ReplacementPlaceholderAwayTeamScored.value in dialog:
            dialog = dialog.replace(DialogEnum.ReplacementPlaceholderAwayTeamScored.value, str(away_scored))

        return dialog

