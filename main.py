from ttapi import Bot

f = open('.ttc','r')

for line in f:
	config[line.split(1)] = line.split(3)


bot = Bot(config[auth],config[userid])

def roomChanged(data):
	room = data['room']
	metadata = room['metadata']
	djcount = metadata['djcount']
	if djcount < 4:
		bot.addDj()
	else:
		bot.remDj()

bot.on('roomChanged', roomChanged)

bot.connect(config[roomid])
bot.start

