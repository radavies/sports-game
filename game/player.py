class Player:

    def __init__(self, name_first, name_last, position, stats):
        self.name_first = name_first
        self.name_last = name_last
        self.position = position
        self.stats

        # TODO - age bonus to stats
        # Wonder kid
        # journey man (low / middling stats, high age)
        # legend (high stats / low age) - maybe not legend, that could be based on accomplishments?

    def __str__(self):
        return "{} {}".format(self.name_first, self.name_last)