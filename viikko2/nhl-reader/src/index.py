import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    # print("JSON-muotoinen vastaus:")
    # print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    fin_players = filter(lambda player: player.isFinnish(), players)
    fin_players_sorted = sorted(fin_players, key=lambda player: player.points(), reverse=True)

    for player in fin_players_sorted:
        print(player)

if __name__ == "__main__":
    main()