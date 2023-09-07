iran = {'name': 'Iran', 'wins': 0, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 0}
spain = {'name': 'Spain', 'wins': 0, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 0}
portugal = {'name': 'Portugal', 'wins': 0, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 0}
marrakech = {'name': 'Morocco', 'wins': 0, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 0}

ir_sp = str(input())
ir_po = str(input())
ir_ma = str(input())
sp_po = str(input())
sp_ma = str(input())
po_ma = str(input())


def game_calculation(game, country1, country2):
    game_list = [int(i) for i in game.split('-')]
    if game_list[0] > game_list[1]:
        country1["wins"] += 1
        country2['loses'] += 1
        country1["points"] += 3
    elif game_list[0] < game_list[1]:
        country2["wins"] += 1
        country1['loses'] += 1
        country2['points'] += 3
    else:
        country1['draws'] += 1
        country2['draws'] += 1
        country1["points"] += 1
        country2['points'] += 1

    country1['goal difference'] += game_list[0] - game_list[1]
    country2['goal difference'] += game_list[1] - game_list[0]
    return country1, country2


game_calculation(ir_sp, iran, spain)
game_calculation(ir_po, iran, portugal)
game_calculation(ir_ma, iran, marrakech)
game_calculation(sp_po, spain, portugal)
game_calculation(sp_ma, spain, marrakech)
game_calculation(po_ma, portugal, marrakech)


def game_results(country):
    return f'{country["name"]}  wins:{country["wins"]} , loses:{country["loses"]} , draws:{country["draws"]} , goal ' \
           f'difference:{country["goal difference"]} , points:{country["points"]}'


countries = [iran, spain, portugal, marrakech]

countries.sort(key=lambda e: e['name'], reverse=False)
countries.sort(key=lambda e: (e['points'], e['wins']), reverse=True)


for c in countries:
    print(game_results(c))
