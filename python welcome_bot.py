import telebot
import openai
import time

# Provided API keys
TELEGRAM_API_KEY = "7352802684:AAHuHWjz0kt02K_3DZcdOp1nTlaAaxikRm0"
OPENAI_API_KEY = "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"

# Initialize the Telegram bot
bot = telebot.TeleBot(TELEGRAM_API_KEY)

# Set the OpenAI API key
openai.api_key = OPENAI_API_KEY

# Define command handlers
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello, I am a Telegram bot. Use /help to see what I can do.")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "I support the following commands: \n /start \n /info \n /help \n /status")

@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(message, "I am a simple Telegram bot created using the pyTelegramBotAPI library.")

@bot.message_handler(commands=['status'])
def status(message):
    bot.reply_to(message, "I am up and running.")

# Define a message handler to generate responses using OpenAI
@bot.message_handler(func=lambda message: True)
def chat(message):
    try:
        print("Received message:", message.text)
        response = openai.Completion.create(
            engine="davinci",
            prompt=message.text,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        reply_content = response.choices[0].text.strip()
        bot.reply_to(message, reply_content)
    except Exception as e:
        print(f"Error: {e}")  # Print the exception for debugging
        bot.reply_to(message, "I'm having trouble processing your request. Please try again later.")

# Test the OpenAI API key
try:
    response = openai.Completion.create(
        engine="davinci",
        prompt="Hello, world!",
        max_tokens=5
    )
    print("OpenAI API key test successful!")
except Exception as e:
    print(f"Error testing OpenAI API key: {e}")

# Start the bot and keep it running
print("Hey, I am up....")
while True:
    try:
        bot.polling()
    except Exception as e:
        print(f"Error polling: {e}")
        # Wait for a while before trying to reconnect
        time.sleep(10)  # Retry after 10 seconds
