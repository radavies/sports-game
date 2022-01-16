from game.enums.positions import Positions
from game.enums.formations_enum import FormationsEnum


class Formations:

    def __init__(self):
        self.formations = {}

        self.formations[FormationsEnum.FourFourTwo] = {
            Positions.Forward.value: 2,
            Positions.Midfielder.value: 4,
            Positions.Defender.value: 4
        }

        self.formations[FormationsEnum.FourThreeThree] = {
            Positions.Forward.value: 3,
            Positions.Midfielder.value: 3,
            Positions.Defender.value: 4
        }

        self.formations[FormationsEnum.FiveThreeTwo] = {
            Positions.Forward.value: 2,
            Positions.Midfielder.value: 3,
            Positions.Defender.value: 5
        }

        self.formations[FormationsEnum.ThreeFourThree] = {
            Positions.Forward.value: 3,
            Positions.Midfielder.value: 4,
            Positions.Defender.value: 3
        }

        self.formations[FormationsEnum.ThreeFiveTwo] = {
            Positions.Forward.value: 2,
            Positions.Midfielder.value: 5,
            Positions.Defender.value: 3
        }

        self.formations[FormationsEnum.FourFiveOne] = {
            Positions.Forward.value: 1,
            Positions.Midfielder.value: 5,
            Positions.Defender.value: 4
        }

        self.formations[FormationsEnum.FiveFourOne] = {
            Positions.Forward.value: 1,
            Positions.Midfielder.value: 4,
            Positions.Defender.value: 5
        }

        self.formations[FormationsEnum.FourSixZero] = {
            Positions.Forward.value: 0,
            Positions.Midfielder.value: 6,
            Positions.Defender.value: 4
        }
