import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import datetime
import ephem

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def start_bot(bot,update):
	mytext= '''Hi {}!
	I am a bot and understand {} command
	'''.format(update.message.chat.first_name, '/start')
	logging.info('User{} press /start'.format(update.message.chat.first_name))
	update.message.reply_text(mytext)

def planet_bot(bot,update,args=[]):
	text='Input name of a planet hear: '
	update.message.reply_text(text)
	
	date = datetime.datetime.now()
	planet={'mars': ephem.Mars(date.strftime('%Y/%m/%d')),'venus': ephem.Venus(date.strftime('%Y/%m/%d')),
	'mercury': ephem.Mercury(date.strftime('%Y/%m/%d')),'jupiter': ephem.Jupiter(date.strftime('%Y/%m/%d')),
	'saturn': ephem.Saturn(date.strftime('%Y/%m/%d')),'uranus': ephem.Uranus(date.strftime('%Y/%m/%d')),
	'neptune': ephem.Neptune(date.strftime('%Y/%m/%d'))}
	
        if len(args) > 0 :
            user_planet = args[0]
        else:
            user_planet = '-empty-'
	
	if user_planet in planet:
		update.message.reply_text(ephem.constellation(planet[user_planet]))

	else:
		update.message.reply_text('I dont know such a planet')


def chat(bot,update):
	text=update.message.text
	logging.info(text)
	update.message.reply_text(text)

def main():
    updtr = Updater(settings.TELEGRAM_API_KEY)

    updtr.dispatcher.add_handler(CommandHandler('start',start_bot))
    updtr.dispatcher.add_handler(CommandHandler('planet',planet_bot, pass_args=True))
    updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))

    updtr.start_polling()
    updtr.idle()

if __name__=='__main__':
	logging.info('Bot started')
	main()
