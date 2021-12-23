from game.enums.stats_player import StatsPlayer


class PlayerStats:

    def __init__(self, age):

        self.age = age

        self.base_stats = {
            StatsPlayer.GroupBallSkills: {
                StatsPlayer.BallControl: 0,
                StatsPlayer.Dribbling: 0
            },
            StatsPlayer.GroupShooting:{
                StatsPlayer.Heading: 0,
                StatsPlayer.ShotPower: 0,
                StatsPlayer.Finishing: 0,
                StatsPlayer.LongShots: 0,
                StatsPlayer.Curve: 0,
                StatsPlayer.FKAcc: 0,
                StatsPlayer.Pens: 0,
                StatsPlayer.Volleys: 0
            },
            StatsPlayer.GroupDefence: {
                StatsPlayer.Marking: 0,
                StatsPlayer.SlideTackle: 0,
                StatsPlayer.StandTackle: 0
            },
            StatsPlayer.GroupMental: {
                StatsPlayer.Aggression: 0,
                StatsPlayer.Reactions: 0,
                StatsPlayer.Positioning: 0,
                StatsPlayer.Interception: 0,
                StatsPlayer.Vision: 0,
                StatsPlayer.Composure: 0
            },
            StatsPlayer.GroupGK: {
                StatsPlayer.GKDiving: 0,
                StatsPlayer.GKHandling: 0,
                StatsPlayer.GKKicking: 0,
                StatsPlayer.GKReflexes: 0
            },
            StatsPlayer.GroupPassing: {
                StatsPlayer.Crossing: 0,
                StatsPlayer.ShortPass: 0,
                StatsPlayer.LongPass: 0
            },
            StatsPlayer.GroupPhysical: {
                StatsPlayer.Stamina: 0,
                StatsPlayer.Strength: 0,
                StatsPlayer.Balance: 0,
                StatsPlayer.Sprint: 0,
                StatsPlayer.Speed: 0,
                StatsPlayer.Agility: 0,
                StatsPlayer.Jumping: 0
            }
        }

        self.stat_modifiers = {
            StatsPlayer.GroupBallSkills: {
                StatsPlayer.BallControl: {},
                StatsPlayer.Dribbling: {}
            },
            StatsPlayer.GroupShooting: {
                StatsPlayer.Heading: {},
                StatsPlayer.ShotPower: {},
                StatsPlayer.Finishing: {},
                StatsPlayer.LongShots: {},
                StatsPlayer.Curve: {},
                StatsPlayer.FKAcc: {},
                StatsPlayer.Pens: {},
                StatsPlayer.Volleys: {}
            },
            StatsPlayer.GroupDefence: {
                StatsPlayer.Marking: {},
                StatsPlayer.SlideTackle: {},
                StatsPlayer.StandTackle: {}
            },
            StatsPlayer.GroupMental: {
                StatsPlayer.Aggression: {},
                StatsPlayer.Reactions: {},
                StatsPlayer.Positioning: {},
                StatsPlayer.Interception: {},
                StatsPlayer.Vision: {},
                StatsPlayer.Composure: {}
            },
            StatsPlayer.GroupGK: {
                StatsPlayer.GKDiving: {},
                StatsPlayer.GKHandling: {},
                StatsPlayer.GKKicking: {},
                StatsPlayer.GKReflexes: {}
            },
            StatsPlayer.GroupPassing: {
                StatsPlayer.Crossing: {},
                StatsPlayer.ShortPass: {},
                StatsPlayer.LongPass: {}
            },
            StatsPlayer.GroupPhysical: {
                StatsPlayer.Stamina: {},
                StatsPlayer.Strength: {},
                StatsPlayer.Balance: {},
                StatsPlayer.Sprint: {},
                StatsPlayer.Speed: {},
                StatsPlayer.Agility: {},
                StatsPlayer.Jumping: {}
            }
        }
