from ttapi import Bot

f = open('.ttrc','r')

config = {}
for line in f:
        str_list = line.split()
	config[str_list[0]] = str_list[2]

bot = Bot(config['auth'],config['userid'])

def speak(data):
   name = data['name']
   text = data['text']
   if name == config['mod']:
	if text == '/surtup':
		surt.addDj()
	elif text == '/surtdown':
		surt.remDj()	
	elif text == '/surtskip':
                surt.skip() 
        elif text == "You're a bit mindless aren't you?":
		surt.speak('Yes leader!')

def roomChanged(data):
	room = data['room']
	metadata = room['metadata']
	djcount = metadata['djcount']
	if djcount < 4:
		bot.addDj()
	else:
		bot.remDj()
        print room


bot.on('roomChanged', roomChanged)
bot.on('speak', speak)

bot.connect(config['roomid'])
bot.start()
