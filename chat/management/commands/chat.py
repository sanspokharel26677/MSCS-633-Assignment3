"""
chat.py
Custom Django management command to interact with the chatbot from the terminal.
This allows the user to input messages and receive responses in real time.
"""

from django.core.management.base import BaseCommand
from chat.chatbot import chatbot  # Import the chatbot instance

class Command(BaseCommand):
    help = 'Chat with the ChatterBot in the terminal'

    def handle(self, *args, **options):
        """
        Starts a loop allowing user to chat with the bot via terminal.
        Ends when the user types 'exit'.
        """
        print("Bot is ready! Type 'exit' to end the chat.")  # Initial instruction

        while True:
            user_input = input("You: ")  # Take input from user
            if user_input.lower() == 'exit':  # Exit condition
                print("Bot: Goodbye!")
                break

            # Get response from chatbot
            response = chatbot.get_response(user_input)
            print(f"Bot: {response}")
