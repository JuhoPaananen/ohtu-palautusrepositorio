class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.players = [player1_name, player2_name]
        self.scores = [0, 0]

    def all_scores_names(self):
        # Names for scores 0-0, 1-1, 2-2, 3-3
        names = ["Love-All", "Fifteen-All", "Thirty-All"]
        return names[self.scores[0]]

    def name_players_scores(self):
        # Names for scores when game is not deuce
        names = ["Love", "Fifteen", "Thirty", "Forty"]
        return names[self.scores[0]] + '-' + names[self.scores[1]]

    def won_point(self, player_name):
        # New method for scoring a point
        player_index = self.players.index(player_name)
        self.scores[player_index] += 1

    def is_deuce(self):
        # Check if game is deuce aka even scores
        return self.scores[0] == self.scores[1]

    def is_win_or_advantage(self):
        # Check if game is won or advantage, at least one player has 4 points
        return self.scores[0] >= 4 or self.scores[1] >= 4

    def win_or_advantage(self):
        # Names for win or advantage
        difference = self.scores[0] - self.scores[1]
        if difference == 1:
            return "Advantage " + self.players[0]
        if difference == -1:
            return "Advantage " + self.players[1]
        if difference >= 2:
            return "Win for " + self.players[0]
        return "Win for " + self.players[1]

    def get_score(self):
        # Streamlined get_score method
        if self.is_deuce():
            if self.scores[0] < 3:
                return self.all_scores_names()
            else:
                return "Deuce"
        if self.is_win_or_advantage():
            return self.win_or_advantage()
        return self.name_players_scores()
        