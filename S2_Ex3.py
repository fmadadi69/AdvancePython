import random


class Human:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class FootballPlayer(Human):
    counter_A = 1
    counter_B = 1

    def __init__(self, name, team):
        super().__init__(name)
        self.team = team
        if self.team == 'A':
            FootballPlayer.counter_A += 1
        elif self.team == 'B':
            FootballPlayer.counter_B += 1

    def get_team(self):
        return self.team


names = ['حسین', 'مازیار', 'اکبر', 'نیما', 'مهدی', 'فرهاد', 'محمد', 'خشایار', 'میلاد',
         'مصطفی', 'امین', 'سعید', 'پویا', 'پوریا', 'رضا', 'علی', 'بهزاد', 'سهیل', 'بهروز', 'شهروز', 'سامان', 'محسن']
teams = ['A', 'B']

team_A = []
team_B = []

for i in range(22):
    rand_name = random.choice(names)
    if FootballPlayer.counter_A <= 11 and FootballPlayer.counter_B <= 11:
        rand_team = random.choice(teams)
        if rand_team == 'A':
            team_A.append(FootballPlayer(rand_name, rand_team))
        elif rand_team == 'B':
            team_B.append(FootballPlayer(rand_name, rand_team))
    elif FootballPlayer.counter_A > 11 >= FootballPlayer.counter_B:
        team_B.append(FootballPlayer(rand_name, 'B'))
    elif FootballPlayer.counter_B > 11 >= FootballPlayer.counter_A:
        team_A.append(FootballPlayer(rand_name, 'A'))
    names.pop(names.index(rand_name))

print(f'Team A: ({len(team_A)} member)', end=' ')
for i in team_A: print(i.get_name(), end='  ')
print()

print(f'Team B: ({len(team_A)} member)', end=' ')
for i in team_B: print(i.get_name(), end='  ')
