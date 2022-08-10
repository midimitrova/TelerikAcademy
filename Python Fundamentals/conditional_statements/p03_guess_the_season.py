month = input()
date = int(input())

if month in ('January', 'February', 'March'):
    season = 'Winter'
elif month in ('April', 'May', 'June'):
    season = 'Spring'
elif month in ('July', 'August', 'September'):
    season = 'Summer'
else:
    season = 'Autumn'

if (month == 'March') and (date > 19):
	season = 'Spring'
elif (month == 'June') and (date > 20):
	season = 'Summer'
elif (month == 'September') and (date > 21):
	season = 'Autumn'
elif (month == 'December') and (date > 20):
	season = 'Winter'
print(season)


