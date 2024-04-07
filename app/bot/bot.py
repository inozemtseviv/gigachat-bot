from telebot import TeleBot
from gigachat import GigaChat


class Bot:
    def __init__(self, tg_token: str, giga_token):
        self.tg_bot = TeleBot(tg_token)
        self.giga_bot = (
            GigaChat(credentials=giga_token, verify_ssl_certs=False))

    def setup_handlers(self):
        @self.tg_bot.message_handler(commands=['help', 'start'])
        def start_bot(message):
            first_mess = \
                (f"<b>"
                 f"{message.from_user.first_name} "
                 f"{message.from_user.last_name}</b>, привет!\n"
                 f"Задай свой вопрос и я поищу для тебя ответ.")

            (self.tg_bot
             .send_message(message.chat.id, first_mess, parse_mode='html'))

        @self.tg_bot.message_handler(func=lambda message: True)
        def response(message):
            answer = self.giga_bot.chat(message.text)

            self.tg_bot.reply_to(message, answer.choices[0].message.content)

    def run(self):
        self.setup_handlers()
        self.tg_bot.infinity_polling()
