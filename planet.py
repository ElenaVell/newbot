import datetime
import ephem

def planet_bot():
	date = datetime.datetime.now()
	planet={'mars': ephem.Mars(date.strftime('%Y/%m/%d')),'venus': ephem.Venus(date.strftime('%Y/%m/%d')),
	'mercury': ephem.Mercury(date.strftime('%Y/%m/%d')),'jupiter': ephem.Jupiter(date.strftime('%Y/%m/%d')),
	'saturn': ephem.Saturn(date.strftime('%Y/%m/%d')),'uranus': ephem.Uranus(date.strftime('%Y/%m/%d')),
	'neptune': ephem.Neptune(date.strftime('%Y/%m/%d'))}
	user_planet=input('Input the name of planet: ' ).lower()
	
	if user_planet in planet:
		print(ephem.constellation(planet[user_planet]))

	else:
		print('I dont know such a planet')
		

planet_bot()
