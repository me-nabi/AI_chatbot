import nltk
from nltk.chat.util import Chat, reflections

# Define conversation pairs and possible responses
pairs = [
    ['(hi|hello|hey)', ['Hello! How can I assist you today?']],
    ['(what is your name?)', ['I am a simple Python chatbot.']],
    ['(how are you?)', ['I am just a bunch of code, but thanks for asking!']],
    ['(.*) help (.*)', ['Sure! How can I help you with %2?']],
    ['(bye|exit)', ['Goodbye! Have a great day!']]
]

print("Welcome to mine chatbot lets start conversation")

chatbot = Chat(pairs,reflections)

print("chat with the bot (type 'bye' to exist)")
print()

print("Welcome to mine chatbot lets start conversation")

chatbot.converse()
