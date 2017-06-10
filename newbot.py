import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import datetime
import ephem

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO, filename='bot.log'
                    )

def start_bot(bot,update):
	mytext= '''Hi {}!
	I am a bot and understand {} command
	'''.format(update.message.chat.first_name, '/start')
	logging.info('User{} press /start'.format(update.message.chat.first_name))
	update.message.reply_text(mytext)

def planet_bot(bot,update,args=None):
	if args is None:
		args = []
	logging.info('Planet: args:{}'.format(args))
	if len(args) > 0 :
		user_planet = args[0]
	else:
		user_planet = ''
	
	date = datetime.datetime.now()
	planet={'mars': ephem.Mars(date.strftime('%Y/%m/%d')),'venus': ephem.Venus(date.strftime('%Y/%m/%d')),
	'mercury': ephem.Mercury(date.strftime('%Y/%m/%d')),'jupiter': ephem.Jupiter(date.strftime('%Y/%m/%d')),
	'saturn': ephem.Saturn(date.strftime('%Y/%m/%d')),'uranus': ephem.Uranus(date.strftime('%Y/%m/%d')),
	'neptune': ephem.Neptune(date.strftime('%Y/%m/%d'))}
		
	if user_planet in planet:
		update.message.reply_text(ephem.constellation(planet[user_planet]))

	else:
		update.message.reply_text('I dont know such a planet')

def wordcount_bot(bot,update,args=None):
	logging.info('wordcount: args:{}'.format(args))
	if args is None:
		args = []
	if len(args) > 0:
		args=str(args)
		args=args.split()
		update.message.reply_text(len(args))

	else:
		update.message.reply_text('No words input')

def culculator_bot(bot,update, args=None):
	logging.info('culk: args:{}'.format(args))
	if args is None:
		args= []
		
	if len(args) > 0:
		args=' '.join(args)
		args = args.split('=')
		try:
			args=' '.join(args[0])
			args=args.split()
			if '-' in args:
				b=args.index('-')
				update.message.reply_text(float(''.join(args[:b]))-float(''.join(args[b+1:])))
			if '+' in args:
				b= args.index('+')
				update.message.reply_text(float(''.join(args[:b]))+float(''.join(args[b+1:])))
			if '/' in args:
				b= args.index('/')
				update.message.reply_text(float(''.join(args[:b]))/float(''.join(args[b+1:])))
			if '*' in args:
				b=args.index('*')
				update.message.reply_text(float(''.join(args[:b]))*float(''.join(args[b+1:])))	
		except ZeroDivisionError:
			update.message.reply_text('Division by zero is impossible!')

def chat(bot,update):
	text=update.message.text
	logging.info(text)
	update.message.reply_text(text)

def main():
    updtr = Updater(settings.TELEGRAM_API_KEY)

    updtr.dispatcher.add_handler(CommandHandler('start',start_bot))
    updtr.dispatcher.add_handler(CommandHandler('planet',planet_bot, pass_args=True))
    updtr.dispatcher.add_handler(CommandHandler('wordcount',wordcount_bot, pass_args=True))
    updtr.dispatcher.add_handler(CommandHandler('culk', culculator_bot, pass_args=True))
    updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))

    updtr.start_polling()
    updtr.idle()

if __name__=='__main__':
	logging.info('Bot started')
	main()
