import amino
import random
import datetime
from gtts import gTTS
import nekos
import requests
import os
import time
import threading
from threading import Thread
client = amino.Client()
client.login(email="email", password="password") #вводим пароль и почту от аккаунта бота
sub_client = amino.SubClient(comId='id', profile=client.profile) #вместо "id" введите айди сообщества, в котором будет работать чат
reloadTime = time.time() + 197
print('Bot status: True! Bot was login')
time.sleep(1)
print('Goodluck to using bot!')
time.sleep(1)
print(' ')
time.sleep(1)
print('Bot by @whoname01')
time.sleep(1)
print('Log: ')
time.sleep(1)
print(' ')
time.sleep(1)
ban = 0
tim = 1
hm = [0]
av = []
nom = 0
def on_message(data):
	global ban	
	global tim
	global nom
	chatId = data.message.chatId
	nickname = data.message.author.nickname
	content = data.message.content
	vrem = data.message.createdTime[17:19]
	id = data.message.messageId

	

	print(f"# Log: {nickname}: {content}: {chatId} : {ban}: {data.message.type}")

	

	lis = ['Думаю, да', 'Думаю что нет', 'Нет.', 'Не знаю, сам думай', 'Да.', 'Сложный вопросик конечно.', 'Повтори вопрос.', 'Ты уверен, что хочешь этого знать?', 'Не знаю.', 'Гляжу у себя в голове, а думать не в состоянии', 'Отрицаю.', 'Не согласен с вашим вопросом.'] # команда вопроса

	lis2 = ['Извиняюсь за это.', 'Простите за тот случай, я всегда могу ошибиться.', 'Пожалуйста, не обижайтесь. Извиняюсь...'] # команда извинение

	lis3 = ['Дурак, нету самокика.', 'Самокика не существует.', 'Повëлся, да?', 'https://natribu.org/ Смотри, волшебная ссылка, которая может дать самокик.'] # команда самокика

	lis4 = ['У вас две палки, вы беременны.', 'Вы не беременнны.(Я не знаю как выглядит тест на беременность, и что оно делает и означает)', 'У вас будет мальчик.', 'У вас будет девочка.'] # тест на беременность

	numberlog = ['Save number log: #4829', 'Save number log: #8294', 'Save number log: #2003', 'Save number log: #0678', 'Save number log: #0118', 'Save number log: #4730', 'Save number log: #9238', 'Save number log: #1303', 'Save number log: #0595', 'Save number log: #0045', 'Save number log: #7393', 'Save number log: #0134'] # сейв номера

	randomnumb = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100'] # рандом число

	gayper = ['🏳‍🌈 Вы гей/лесбиянка на: 0%', '🏳‍🌈 Вы гей/лесбиянка на: 0.5%', '🏳‍🌈 Вы гей/лесбиянка на: 1%', '🏳‍🌈 Вы гей/лесбиянка на: 2.56%', '🏳‍🌈 Вы гей/лесбиянка на: 3%', '🏳‍🌈 Вы гей/лесбиянка на: 5%', '🏳‍🌈 Вы гей/лесбиянка на: 13.45%', '🏳‍🌈 Вы гей/лесбиянка на: 23.75%', '🏳‍🌈 Вы гей/лесбиянка на: 35.93%', '🏳‍🌈 Вы гей/лесбиянка на: 41.99%', '🏳‍🌈 Вы гей/лесбиянка на: 49%', '🏳‍🌈 Вы гей/лесбиянка на: 69.34%', '🏳‍🌈 Вы гей/лесбиянка на: 79.33%', '🏳‍🌈 Вы гей/лесбиянка на: 95.55%', '🏳‍🌈 Вы гей/лесбиянка на: 100%'] # гей тест

	

	content = str(content).split(" ")
	if content[0][0] == "!" and content[0][1:].lower() == "хелп":
		sub_client.send_message(message="[BC][🌻]Команды бота whoname00:\n1. !бот — Позовите бота, если вы хотите задать ему вопрос\n2. !гс — Делает из текста в голосовое сообщение.\n3. !самокик — Эта команда создано ради веселье, можете по желанию его использовать.\n4. ? — Можно задать боту любой вопрос, но ответ вам может не понравится.\n5. !randomnumber — Просто для веселье, но есть специальные числа, которые нужно тупо соединить которые содержат пасхалку.\n6. !зачистка-100 — Удаляет 100 сообщении. Но нужен роль помощника, если в чате.\n7. !gaytest — Тест на гея.(Вася, прости что, стыбзил благородно эту команду.)\n8. !ping — Проверить состояние бота, онлайн он или оффлайн\n9. !infobot — Узнать информацию о боте, и так-же о создателе.\n10. 'Извинись.', 'Извинись', 'извинись' — Попросить у бота попрощение.\n11. !тестнабеременность — Добавил команду из-за идей онао, как просил.\n12. !say — Заставить бота пересказать ваше сообщение, но в контексном виде.\n\n\n[BC][🌻] РП Команды\n!cuddle — Прижаться к пользователю\n!feed — Покормить пользователя\n!hug — Обнять пользователя\n!kiss — Поцеловать пользователя\n!pat — Погладить пользователя\n!poke — Тыкнуть пользователя\n!slap — Ударить пользователя\n!tickle — Пощекотать пользователя\n!kus — Сделать кусь пользователю\n\n\n[C]Так-же, этот бот приветствует, если вы спросите у него как дела, ответит вежливо. Если у вас идеи для бота, пишите на стене самого бота.", chatId=chatId, replyTo=id)
	if content[0][0] == "?":
		sub_client.send_message(message=str(random.choice(lis)), chatId=chatId, replyTo=id)
	if content[0][0] == "!" and content[0][1:].lower() == "гс":
		myobj = gTTS(text=data.message.content[4:], lang='ru', slow=False)
		myobj.save("gs.mp3")
		with open("gs.mp3", "rb") as file:
			sub_client.send_message(chatId=chatId, file=file, fileType="audio")
	if content[0][0] == "!" and content[0][1:].lower() == "бот":
		sub_client.send_message(message=(f"Чем могу помочь, {nickname}?\nР.S Если вы хотите задать вопрос, вот пример: ?Ты кто"), chatId=chatId, replyTo=id)
	if content [0][0] == "!" and content[0][1:].lower() == "самокик":
	  sub_client.send_message(message=str(random.choice(lis3)), chatId=chatId, replyTo=id) 
	if content[0][0] == "!" and content[0][1:].lower() == "randomnumber":
	  	sub_client.send_message(message=str(random.choice(randomnumb)), chatId=chatId, replyTo=id)
	if content[0][0] == "!" and content[0][1:].lower() == "10046771213158262":
	  	sub_client.send_message(message='!гс Вася топ чел!', chatId=chatId, replyTo=id)
	if content[0][0] == "!" and content[0][1:].lower() == "63498794405073559":
	  	sub_client.send_message(message='Ты крутой!', chatId=chatId, replyTo=id)
	if content[0] == "sercet":
		myobj = gTTS(text=data.message.content[4:], lang='ru', slow=False)
		myobj.save("gs.mp3")
		with open("gs.mp3", "rb") as file:
			sub_client.send_message(chatId=chatId, file=file, fileType="audio")
	if content[0] == "!say":
		sub_client.send_message(message=(f"{nickname}: {content}"), chatId=chatId) # Команда, но с контексным сообщением.
	if content[0] == "!chatId":
		sub_client.send_message(message=(f"Айди данного чата: {chatId}"), chatId=chatId, replyTo=id)
	if content[0] == "Привет":
		sub_client.send_message(message='И тебе привет', chatId=chatId, replyTo=id)
	if content[0] == "привет":
		sub_client.send_message(message='И тебе привет', chatId=chatId, replyTo=id)
	if content[0] == "Дарова":
		sub_client.send_message(message='И тебе привет', chatId=chatId, replyTo=id)
	if content[0] == "Дратути.":
		sub_client.send_message(message='И тебе привет', chatId=chatId, replyTo=id)
	if content[0] == "Дратути":
		sub_client.send_message(message='И тебе привет', chatId=chatId, replyTo=id)
	if content[0] == "дратути":
		sub_client.send_message(message='И тебе привет', chatId=chatId, replyTo=id)
	if content[0] == "Приветствую.":
		sub_client.send_message(message='И тебя приветствую', chatId=chatId, replyTo=id)
	if content[0] == "Приветствую":
		sub_client.send_message(message='И тебя приветствую', chatId=chatId, replyTo=id)
	if content[0] == "приветствую":
		sub_client.send_message(message='И тебя приветствую', chatId=chatId, replyTo=id)
	if content[0] == "Здраствуйте.":
		sub_client.send_message(message='И тебя приветствую', chatId=chatId, replyTo=id)
	if content[0] == "Здраствуйте":
		sub_client.send_message(message='И тебя приветствую', chatId=chatId, replyTo=id)
	if content[0] == "здраствуйте":
		sub_client.send_message(message='И тебя приветствую', chatId=chatId, replyTo=id)
	if content[0] == "Как дела?":
		sub_client.send_message(message=' Дела уж и не такие не плохие.\nЧто насчëт тебя?', chatId=chatId, replyTo=id)
	if content[0] == "как дела?":
		sub_client.send_message(message=' Дела уж и не такие не плохие.\nЧто насчëт тебя?', chatId=chatId, replyTo=id)
	if content[0] == "Ты гей?":
		sub_client.send_message(message='Нет, не гей', chatId=chatId, replyTo=id)
	if content[0] == "ты гей?":
		sub_client.send_message(message='Нет, не гей', chatId=chatId, replyTo=id)
	if content[0] == "Извинись":
		sub_client.send_message(message=str(random.choice(lis2)), chatId=chatId, replyTo=id)
	if content[0] == "Извинись.":
		sub_client.send_message(message=str(random.choice(lis2)), chatId=chatId, replyTo=id)
	if content[0] == "извинись":
		sub_client.send_message(message=str(random.choice(lis2)), chatId=chatId, replyTo=id)
	if content[0] == "!infobot":
		sub_client.send_message(message='[BC][📄]Информация о боте\n[C]Создатель бота: whoname01\n[C]Дискорд — whoname00#8684\n[C]Amino — iiDominus\n[C]Telegram — @whenaminohack\n[C]Bot Name — whoname00\n[C]Команды бота — !хелп\n\n\n[C]Это вся инфа обо мне, и о создателе.', chatId=chatId, replyTo=id)
	if content[0][0] == "!" and content[0][1:].lower() == "тестнабеременность":
	  	sub_client.send_message(message=str(random.choice(lis4)), chatId=chatId, replyTo=id)
	if content[0] == "Добрый вечер.":
		sub_client.send_message(message='Добрый', chatId=chatId, replyTo=id)
	if content[0] == "Добрый вечер":
		sub_client.send_message(message='Добрый', chatId=chatId, replyTo=id)
	if content[0] == "добрый вечер":
		sub_client.send_message(message='Добрый', chatId=chatId, replyTo=id)
	if content[0] == "!ping":
		sub_client.send_message(message='Pong!\nBot is online!', chatId=chatId, replyTo=id)
	if content[0][1:].lower()=="!inv":
		sub_client.join_chat(chatId=chatInfo.chatId)
		x=client.get_from_code(str(content[1])).objectId
		sub_client.invite_to_chat([x], chatId=chatInfo.chatId)
	if content[0] == "!tickle":
	  	        author2 = data.message.content.split("@")[1].replace("@", "")[0:50]
	  	        sub_client.send_message(message=f'{data.message.author.nickname} щекочет {author2}', chatId=chatId)
	if content[0] == "!slap":
	  	        	author2 = data.message.content.split("@")[1].replace("@", "")[0:50]
	  	        	sub_client.send_message(message=f'{data.message.author.nickname} бьёт {author2}', chatId=chatId)
	if content[0] == "!poke":
	  	        		author2 = data.message.content.split("@")[1].replace("@", "")[0:50]
	  	        		sub_client.send_message(message=f'{data.message.author.nickname} тыкает в {author2}', chatId=chatId)
	if content[0] == "!pat":
	  	        			author2 = data.message.content.split("@")[1].replace("@", "")[0:50]
	  	        			sub_client.send_message(message=f'{data.message.author.nickname} гладит {author2}', chatId=chatId)
	if content[0] == "!hug":
	  	        				author2 = data.message.content.split("@")[1].replace("@", "")[0:50]
	  	        				sub_client.send_message(message=f'{data.message.author.nickname} обнимает {author2}', chatId=chatId)
	if content[0] == "!feed":
	  	        					author2 = data.message.content.split("@")[1].replace("@", "")[0:50]
	  	        					sub_client.send_message(message=f'{data.message.author.nickname} Кормит {author2}', chatId=chatId)
	if content[0] == "!cuddle":
	  	        						author2 = data.message.content.split("@")[1].replace("@", "")[0:50]
	  	        						sub_client.send_message(message=f'{data.message.author.nickname} прижимается к {author2}', chatId=chatId)
	if content[0] == "!kiss":
	  	        							author2 = data.message.content.split("@")[1].replace("@", "")[0:50]
	  	        							sub_client.send_message(message=f'{data.message.author.nickname} целует {author2}', chatId=chatId)
	if content[0] == "!kus":
	  	        								author2 = data.message.content.split("@")[1].replace("@", "")[0:50]
	  	        								sub_client.send_message(message=f'{data.message.author.nickname} делает кусь {author2}', chatId=chatId)
	if content[0][0] == "!" and content[0][1:].lower() == "gaytest":
	  	sub_client.send_message(message=str(random.choice(gayper)), chatId=chatId, replyTo=id)
	if content[0] == "!зачистка-100":
	           if data.message.author.role != 0:
	               for msgId in sub_client.get_chat_messages(chatId=data.message.chatId, size=100).messageId:
	               	sub_client.delete_message(reason="зачистка", chatId=data.message.chatId, messageId=msgId, asStaff=True)
	if content[0][0] == "!" and content[0][1:].lower() == "on":
		tim = -tim
	##################################Защита чата##################################################

	global nazvan
	global opisan
	global fonsss
	
	if content[0][0] == "!":
		if content[0][1:].lower() == "save":
			nazvan = sub_client.get_chat_thread(chatId=data.message.chatId).title
			opisan = sub_client.get_chat_thread(chatId=data.message.chatId).content
			fonsss = sub_client.get_chat_thread(chatId=data.message.chatId).backgroundImage
			sub_client.send_message(message=str(random.choice(numberlog)), chatId=data.message.chatId, replyTo=id)
			print('# Log Save: Чат сохранëн!')
		if content[0][1:].lower() == "loadsave":
			sub_client.edit_chat(chatId=data.message.chatId, title=str(nazvan), content=str(opisan))
			try:
				sub_client.edit_chat(chatId=data.message.chatId, backgroundImage=str(fonsss))
			except:
				sub_client.send_message(message='Сейв был успешно загружен.', chatId=data.message.chatId)
		if content[0][1:].lower() == "a" and sub_client.get_chat_thread(chatId).author.userId:
			sub_client.invite_to_chat(userId=str(client.get_from_code(str(content[1][:])).objectId), chatId=chatId)
			nom = 1
			
	if data.message.content != None and data.message.type in [1, 50, 57, 59, 100, 101, 102, 103, 104, 105, 106, 107, 109, 110, 113, 114, 115, 116, 124, 125, 126]:
		sub_client.send_message(message=(f'Рейдер {nickname} был кикнут из чата навсегда.'), chatId=data.message.chatId)
		sub_client.kick(userId=data.message.author.userId, chatId=data.message.chatId, allowRejoin = False)
		nom = 0

methods = []
for x in client.callbacks.chat_methods:
	methods.append(client.callbacks.event(client.callbacks.chat_methods[x].__name__)(on_message))

	

##################################

	

while True:
    if time.time() >= reloadTime:
        print("# Update Log: Updating socket...")
        try:
            client.socket.close()
            client.socket.start()
        except:pass
        print("# Update Log: Updated!")
        reloadTime += 197
