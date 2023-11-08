class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def check_nationality(self, player, nationality):
        return player.nationality == nationality

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        filtered_players = filter(lambda player: self.check_nationality(player, nationality), players)
        sorted_players = sorted(filtered_players, key=lambda player: player.points(), reverse=True)
        return sorted_players
