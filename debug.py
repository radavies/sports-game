def print_debug(leagues):
    for league in leagues.leagues["Scotland"]:
        league_stat_avg = 0
        print(league.name)
        print("")
        for team in league.teams:
            league_stat_avg += get_team_average_stat(team)
        print(round(league_stat_avg / len(league.teams)))
        print("")

    for league in leagues.leagues["England & Wales"]:
        league_stat_avg = 0
        print(league.name)
        print("")
        for team in league.teams:
            league_stat_avg += get_team_average_stat(team)
        print(round(league_stat_avg / len(league.teams)))
        print("")

    for player in leagues.leagues["Scotland"][0].teams[0].players:
        print("{} - {} ({})".format(player, player.position.value, player.overall_stat_total()))


def get_team_average_stat(team):
    total = 0
    for player in team.players:
        total += player.overall_stat_total()
    return round(total / len(team.players))
