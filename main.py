from g4f.client import Client
import telebot
TOKEN = '7574573328:AAFoqwJKx2QyPXUOOHNxpSOmFjIn4ufEvgw'
bot = telebot.TeleBot(TOKEN)
client = Client()
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        f"Привет, {message.from_user.first_name}! 👋\n\n"
        "Я твой помощник при поступлении в колледж.\n"
        "Задавай свои вопросы: например, о документах, специальностях, экзаменах и многом другом!"
)
@bot.message_handler(content_types=['text'])
def handle_text(message):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "Ты помощник абитуриента, который хочет поступить в колледж. "
                               "Объясняй всё понятно, дружелюбно и по делу. "
                               "Давай советы по выбору специальности, подготовке документов, поступлению."
                },
                {
                    "role": "user",
                    "content": message.text
                }
            ],
        )
        answer = response.choices[0].message.content
    except Exception as e:
        answer = "Произошла ошибка. Попробуйте задать вопрос позже."

    bot.send_message(message.chat.id, answer)
print("Бот запущен...")
bot.polling(none_stop=True)