tournament_days = int(input())

games_won = 0
games_lost = 0
collected_cash = 0
day_end = False

for tournament_days in range(1, tournament_days + 1):
    while True:
        sport = input()
        if sport == "Finish":
            break
        game_result = input()