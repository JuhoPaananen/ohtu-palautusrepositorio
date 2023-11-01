from player_reader import PlayerReader
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3


def sort_by_criteria(player, sort_criteria):
    if sort_criteria == SortBy.GOALS:
        return player.goals
    elif sort_criteria == SortBy.ASSISTS:
        return player.assists
    else:
        return player.points

class StatisticsService:
    def __init__(self, player_reader):
        reader = player_reader

        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort_criteria=SortBy.POINTS):
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=lambda player: sort_by_criteria(player, sort_criteria)
        )

        result = []
        i = 0
        while i < how_many:
            result.append(sorted_players[i])
            i += 1

        return result
