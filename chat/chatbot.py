"""
chatbot.py
This module sets up and trains a chatbot instance using ChatterBot library.
It uses a SQLStorageAdapter for persistence and is trained on the English corpus.
"""

# Import ChatterBot components
from chatterbot import ChatBot                      # Main ChatBot class
from chatterbot.trainers import ChatterBotCorpusTrainer  # Trainer to use English corpus

# Create the chatbot instance
chatbot = ChatBot(
    'TerminalBot',                                 # Name of the bot
    storage_adapter='chatterbot.storage.SQLStorageAdapter',  # Database adapter
    database_uri='sqlite:///db.sqlite3'            # SQLite DB location
)

# Create and run the trainer
trainer = ChatterBotCorpusTrainer(chatbot)         # Load trainer with English dataset
trainer.train('chatterbot.corpus.english')         # Train the chatbot on English corpus
