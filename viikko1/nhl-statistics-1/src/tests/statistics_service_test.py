import unittest
from statistics_service import StatisticsService
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

    def test_top_palauttaa_oikean_listan(self):
        players = self.statistics.top(2)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")