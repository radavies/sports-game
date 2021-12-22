from enum import Enum


class StatsPlayer(Enum):
    GroupBallSkills = "Ball Skills"
    BallControl = "Ball Control"
    Dribbling = "Dribbling"

    GroupShooting = "Shooting"
    Heading = "Heading"
    ShotPower = "ShotPower"
    Finishing = "Finishing"
    LongShots = "Long Shots"
    Curve = "Curve"
    FKAcc = "FK Accuracy"
    Pens = "Penalties"
    Volleys = "Volleys"

    GroupDefence = "Defence"
    Marking = "Marking"
    SlideTackle = "Slide Tackle"
    StandTackle = "Standing Tackle"

    GroupMental = "Mental"
    Aggression = "Aggression"
    Reactions = "Reactions"
    Positioning = "Positioning"
    Interception = "Interception"
    Vision = "Vision"
    Composure = "Composure"

    GroupGK = "Goal Keeping"
    GKDiving = "GK Diving"
    GKHandling = "GK Handling"
    GKKicking = "GK Kicking"
    GKReflexes = "GK Reflexes"

    GroupPassing = "Passing"
    Crossing = "Crossing"
    ShortPass = "Short Pass"
    LongPass = "LongPass"

    GroupPhysical = "Physical"
    Stamina = "Stamina"
    Strength = "Strength"
    Balance = "Balance"
    Sprint = "Sprint"
    Speed = "Speed"
    Agility = "Agility"
    Jumping = "Jumping"
