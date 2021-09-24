from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext):
	update.message.reply_text(" Hey im loving")
	# update.message.reply_text("Hey {}".format(update.message.from_user.username))



if __name__ == "__main__":
	updater = Updater[TOKEN]

	dp = updater.dispatcher

	dp.add_handler(CommandHandler("start", start))

	updater.start_webhook("0.0.0.0", POST, TOKEN, webhook_url="https://color2021.herokuapp.com/"+TOKEN)
	updater.idle()


#	updater.start_webhook("0.0.0.0", POST, TOKEN, webhook_url="https://color2021.herokuapp.com/"+ TOKEN)
	# updater.start_polling()
	# updater.idle()