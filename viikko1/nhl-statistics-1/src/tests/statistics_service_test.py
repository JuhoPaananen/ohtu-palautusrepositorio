import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # luodaan StatisticsService-olio joka käyttää "stubia"
        self.statistics = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_etsi_palauttaa_pelaajan(self):
        player = self.statistics.search("Kurri")
        self.assertEqual(player.name, "Kurri")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.goals, 37)
        self.assertEqual(player.assists, 53)

    def test_etsi_palauttaa_none(self):
        player = self.statistics.search("Banaani")
        self.assertEqual(player, None)

    def test_hae_joukkueen_pelaajat_palauttaa_oikean_listan(self):
        players = self.statistics.team("EDM")
        self.assertEqual(players[0].name, "Semenko")
        self.assertEqual(players[1].name, "Kurri")
        self.assertEqual(players[2].name, "Gretzky")

    def test_top_ilman_parametria_palauttaa_oikean_listan(self):
        players = self.statistics.top(2)
        self.assertEqual(len(players), 2)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")

    def test_top_pisteet_palauttaa_oikean_listan(self):
        players = self.statistics.top(3, SortBy.POINTS)
        self.assertEqual(len(players), 3)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")
        self.assertEqual(players[2].name, "Yzerman")

    def test_top_syottajat_palauttaa_oikean_listan(self):
        players = self.statistics.top(3, SortBy.ASSISTS)
        self.assertEqual(len(players), 3)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Yzerman")
        self.assertEqual(players[2].name, "Lemieux")

    def test_top_maalintekijat_palautta_oikean_listan(self):
        players = self.statistics.top(3, SortBy.GOALS)
        self.assertEqual(len(players), 3)
        self.assertEqual(players[0].name, "Lemieux")
        self.assertEqual(players[1].name, "Yzerman")
        self.assertEqual(players[2].name, "Kurri")