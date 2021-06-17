from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):

	update.message.reply_text('Hora de trabajar, a buscar gemas!') #Mensaje saludar

def process_message(update, context):

	text = update.message.text

	

	if str(text).__contains__('#Request'):
		context.bot.send_message(
			chat_id='-526565190',
			text=text
			)

	# -526565190





if __name__ == '__main__':

	updater = Updater(token='1639575654:AAHs67hEVnnvwok5p43UXei31S0OGJIWD7g', use_context=True)

	dp = updater.dispatcher
	dp.add_handler(CommandHandler('start', start)) #Al usar comando start ejecutara el mensaje saludar
	dp.add_handler(MessageHandler(filters=Filters.text, callback=process_message))
	updater.start_polling()


	print('El bot esta trabajando')
	updater.idle()