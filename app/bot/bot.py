from telebot import types, TeleBot

class Bot:
    def __init__(self, token: str):
        self.bot = TeleBot(token)

    def setup_handlers(self):
        @self.bot.message_handler(commands=['start'])
        def start_bot(message):
            first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, привет!\nХочешь что-то узнать?"
            markup = types.InlineKeyboardMarkup()
            button_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
            markup.add(button_yes)
            self.bot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)

        @self.bot.callback_query_handler(func=lambda call: True)
        def response(function_call):
            if function_call.message:
                if function_call.data == 'yes':
                    second_mess = 'Задай свой вопрос и я поищу для тебя ответ.'
                    markup = types.InlineKeyboardMarkup()
                    self.bot.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
                    self.bot.answer_callback_query(function_call.id)

    def run(self):
        self.setup_handlers()
        self.bot.infinity_polling()
