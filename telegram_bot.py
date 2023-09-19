# Importing required libraries
import telebot
import openai

# Initializing the bot with the token from BotFather
bot = telebot.TeleBot('6053603740:AAFYZ6YksGzKNWHFjPMr9N9MRg6bOkSvSDM')

# Setting the OpenAI key
openai.api_key = "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"

# Defining command handlers for start and help commands
@bot.message_handler(commands = ['start','help'])
def welcome_function(message):
  # Sending a welcome message to the user
  bot.send_message(message.chat.id, 'Hello! I am Optimum Pride. Ask me something!')

# Defining a message handler for all text messages
@bot.message_handler(content_types=['text'])
def chat_function(message):
  # Generating a response using OpenAI's model
  response = openai.Completion.create(
    model="text-davinci-003",   # Model name
    prompt=message.text,        # User's message is used as a prompt
    temperature=0,              # Controls randomness. Lower value means more focused output
    max_tokens=1024,            # Maximum length of the output
    top_p=1,                    # Controls diversity via nucleus sampling. Lower value means more focused output
    frequency_penalty=0,        # Controls penalty for frequent tokens
    presence_penalty=0          # Controls penalty for new tokens
  )
  # Sending the generated response back to the user
  bot.send_message(message.chat.id, response['choices'][0]['text'].strip())

# Polling updates from Telegram server
bot.polling()
