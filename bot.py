import telebot
import config
import random
# python D:\python\telegrbot\bot.py
from telebot import types
# 474485887 800343372
bot = telebot.TeleBot(config.TOKEN)


joinedFile = open("D:/python/telegrbot/joined.txt", "r")
joinedUsers = set ()
for line in joinedFile:
	joinedUsers.add(line.strip())
joinedFile.close()

needHelp = []

ansId = 0

@bot.message_handler(commands=['start'])
def start(message):
	if not str(message.chat.id) in joinedUsers:
		joinedFile = open("D:/python/telegrbot/joined.txt", "a")
		joinedFile.write(str(message.chat.id) + "\n")
		joinedUsers.add(str(message.chat.id))
		print(joinedUsers)
	

	#stickerWelcome = open('static/hello.png', 'rb')
	#bot.send_sticker(message.chat.id, stickerWelcome)
	#joinedUsers.add(message.chat.id)
	bot.send_message(message.chat.id, ' Hello, {0.first_name}! \n I am the bot created by Denny. \n \n Creator\'s discord - Denny#1103 \n Official discord server - https://discord.gg/mABRzdp \n \n What can I do? \n \n I can send messages to all users who came to this bot with the message that the Owner told me. \n \n I have support and you can simply ask it: \n /support [your message] \n Support will answer you in 24 hours. \n You will be put in a queue. \n \n Hah, the bot can send you an empty message for work test \n /nothing \n \n By joining the bot you get into joined-list for message sends.'.format(message.from_user, bot.get_me()), parse_mode='html')

@bot.message_handler(commands=['secretsendall'])
def send(message):
	for user in joinedUsers:
		bot.send_message(user, message.text[message.text.find(' '):])

@bot.message_handler(commands=['support'])
def support(message):
	global ansId
	needHelpFile = open("D:/python/telegrbot/needHelp.txt", "a")
	#needHelpFile.replace(ansId, "")
	needHelpFile.write(str(message.chat.id) + "\n")
	ansId = message.chat.id
	needHelp.append(str(message.chat.id))
	bot.send_message(message.chat.id, 'Wait a bit, {0.first_name}! We sent your message to the developer! \n Please do not send more messages. \n You are at the queue.'.format(message.from_user, bot.get_me()), parse_mode='html')
	bot.send_message(800343372, str(message.chat.id) + ": " + message.text[message.text.find(' '):])

@bot.message_handler(commands=['answer'])
def answer(message):
	needHelpFile = open("D:/python/telegrbot/needHelp.txt", "r")
	#needHelpFile.replace(ansId, "")
	for line in needHelpFile:
		needHelp.append(line.strip())
	
	needHelpFile.close()
	bot.send_message(message.chat.id, 'Answering to ' + needHelp[0].format(message.from_user, bot.get_me()), parse_mode='html')
	bot.send_message(int(needHelp[0]), 'Support' + ": " + message.text[message.text.find(' '):])

	needHelpFile = open("D:/python/telegrbot/needHelp.txt", "a")

	with open("D:/python/telegrbot/needHelp.txt", "r") as nhf:
		lines = nhf.readlines()
	with open("D:/python/telegrbot/needHelp.txt", "w") as nhf:
		for line in lines:
			if line.strip("\n") != needHelp[0]:
				nhf.write(line)

@bot.message_handler(commands=['nothing'])
def nothing(message):
	#stickerWelcome = open('static/hello.png', 'rb')
	#bot.send_sticker(message.chat.id, stickerWelcome)
	bot.send_message(message.chat.id, '⠀'.format(message.from_user, bot.get_me()), parse_mode='html')	

	
@bot.message_handler(content_types=['text'])
def work(message):
	bot.send_message(message.chat.id, message.text)
	# keyboad
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Random number")
	item2 = types.KeyboardButton("AAAh")

	markup.add(item1, item2)

bot.polling(none_stop=True)
