import telepot, time, urllib
def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print 'Got command: %s' % command

    if '/lechugas' in command:
	urllib.urlretrieve("http://fkl1c5ba1fadt1isz.wolrdssl.net/custom/rate2.jpg","Path to save image file locally")
        f = open('Path to image file','rb')
	bot.sendPhoto(chat_id,f)
	#bot.sendMessage(chat_id, "Hello, how are you?")

# Create a bot object with API key
# You must request a bot key from @BotFather 
bot = telepot.Bot('API key goes here')

# Attach a function to notifyOnMessage call back
bot.message_loop(handle)

# Listen to the messages
while 1:
    time.sleep(10)
