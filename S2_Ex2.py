import datetime


class Age:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def get_age(self):
        today = datetime.datetime.now()
        today = datetime.datetime.strptime(f'{today.year}/{today.month}/{today.day}', "%Y/%m/%d")
        # print(today)
        birthday = datetime.datetime.strptime(f'{self.year}/{self.month}/{self.day}', "%Y/%m/%d")
        # print(birthday)
        return int((today - birthday).days / 365)


date_of_birth = str(input())
date_of_birth = date_of_birth.split('/')
year_of_birth = int(date_of_birth[0])
month_of_birth = int(date_of_birth[1])
day_of_birth = int(date_of_birth[2])
if year_of_birth > datetime.datetime.now().year or month_of_birth > 12  or day_of_birth > 31:
    print("WRONG ")
else:
    faezeh_age = Age(year_of_birth, month_of_birth, day_of_birth)
    print(faezeh_age.get_age())
