import datetime, Birthday

today = datetime.date.today()
my_next_birthday = datetime.date(2023,11,13)

days_away = today - my_next_birthday

if today == my_next_birthday:
    print(Birthday.random_message)
else:
    print(f'My next birthday is {days_away} away from today! 🎂')