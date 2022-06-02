from email import message
import telebot

subscribe = {}
global send_message_mode
send_message_mode = 1

bot = telebot.TeleBot('api')


@bot.message_handler(commands=['start'])
def start_message(message):
    send_message_mode = 1
    subscribe[message.from_user.id] = 1
    bot.send_message(
        message.chat.id,
        'Здравствуйте, подписка активна. Если хотите отключить подписку напишите: "отмена"'
    )


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "отмена":
        if subscribe[message.from_user.id] == 1:
            subscribe[message.from_user.id] = 0
            bot.send_message(
                message.chat.id,
                'Подписка успешно отменилась! Для включения подписки напишите /start'
            )
        else:
            bot.send_message(message.chat.id, 'Подписка уже отменина.')
    elif message.from_user.id == 795310679:
        if message.text == "send message mode start":
            bot.send_message(795310679, 'send message mode active')
            send_message_mode = 1
        elif send_message_mode == 1:
            for i in subscribe:
                if subscribe[i] == 1:
                    bot.send_message(i, message.text)
        elif message.text == "send message mode stop":
            send_message_mode = 1
            bot.send_message(795310679, 'send message mode was stoped')


bot.polling(none_stop=True, interval=0)
