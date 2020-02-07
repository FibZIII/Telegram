import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands = ['start'])
def welcome(message):

	#keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
	random_numbers = types.KeyboardButton('randomnaya zalypa')
	item2 = types.KeyboardButton('Ny cho ti kak?')

	markup.add(random_numbers, item2)


	bot.send_message(
	message.chat.id,
	'Zdarova, {0.first_name}!\nYa - {1.first_name}'.format(message.from_user, bot.get_me()),
	parse_mode = 'html',
	reply_markup = markup
	)


@bot.message_handler(content_types = ['text'])

def echo(message):
	if message.chat.type == 'private':	 
		if message.text == 'randomnaya zalypa':
			bot.send_message(message.chat.id, str(random.randint(0,1000)))
		elif message.text == 'Ny cho ti kak?':

			markup = types.InlineKeyboardMarkup(row_width = 2)
			item1 = types.InlineKeyboardButton('toje zaebis', callback_data = 'good')
			item2 = types.InlineKeyboardButton('ny chot grustno', callback_data = 'bad')

			markup.add(item1, item2)

			bot.send_message(message.chat.id, 'zaebis, kak sam?', reply_markup = markup)
		else:
			bot.send_message(message.chat.id, 'sho ti hochesh?')

@bot.callback_query_handler(func = lambda call : True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'good':
				bot.send_message(call.message.chat.id, 'otlichno')
			elif call.data == 'bad':
				bot.send_message(call.message.chat.id, 'jal, go pit?')

			bot.edit_message_text(
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			text ='Ny cho ti kak?',
			reply_markup = None
			)

			bot.answer_callback_query(
			chat_id = call.message.chat.id,
			show_alert = False,
			text = 'test!!!'
			)
	except Exception as e:
		print(repr(e))

bot.polling(none_stop = True)
