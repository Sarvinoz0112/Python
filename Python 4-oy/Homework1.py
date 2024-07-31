import random
import string
import json
import hashlib

class User:
    def __init__(self, full_name, username, password):
        """
        Initializes a User object with full name, username, and hashed password.

        :param full_name: The full name of the user
        :param username: The username of the user
        :param password: The password of the user
        """
        self.full_name = full_name
        self.username = username
        self.password = self.hash_password(password)
        self.created_chats = []
        self.joined_chats = []

    
    def hash_password(password):
        """
        Hashes the password using SHA-256 algorithm.

        :param password: The password to be hashed
        :return: The hashed password
        """
        return hashlib.sha256(password.encode()).hexdigest()

class Chat:
    def __init__(self, owner, password):
        """
        Initializes a Chat object with a unique chat ID, password, messages, and owner.

        :param owner: The username of the chat owner
        :param password: The password for the chat
        """
        self.chat_id = self.generate_chat_id()
        self.password = User.hash_password(password)
        self.messages = []
        self.owner = owner
        self.hidden_users = []  # To keep track of users who have hidden messages

    
    def generate_chat_id():
        """
        Generates a random 6-digit chat ID.

        :return: A random 6-digit chat ID
        """
        return ''.join(random.choices(string.digits, k=6))

    def is_hidden_for_user(self, username):
        """
        Checks if messages are hidden for the given user.

        :param username: The username to check
        :return: True if messages are hidden for the user, otherwise False
        """
        return username in self.hidden_users

class ChatManager:
    chats = {}

    
    def create_chat(cls, user):
        """
        Creates a new chat with a 4-digit password and adds it to the user's created chats.

        :param user: The user creating the chat
        """
        password = input("Enter a 4-digit password for the chat: ")
        if len(password) != 4 or not password.isdigit():
            print("Oops! Invalid password. Make sure it's a 4-digit number.")
            return
        chat = Chat(user.username, password)
        cls.chats[chat.chat_id] = chat
        user.created_chats.append(chat.chat_id)
        print(f"🎉 Chat created successfully! Your chat ID is: {chat.chat_id}")

    
    def join_chat(cls, user):
        """
        Allows a user to join an existing chat by providing chat ID and password.

        :param user: The user joining the chat
        """
        chat_id = input("Enter chat ID to join: ")
        password = input("Enter chat password: ")
        chat = cls.chats.get(chat_id)
        if chat and chat.password == User.hash_password(password):
            user.joined_chats.append(chat_id)
            print(f"🌟 You've joined the chat with ID: {chat_id}! Let's start chatting!")
            chat_menu(chat_id)
        else:
            print("😞 Invalid chat ID or password. Please try again.")

    
    def delete_chat(cls, user, chat_id):
        """
        Deletes a chat if it was created by the user.

        :param user: The user deleting the chat
        :param chat_id: The ID of the chat to delete
        """
        if chat_id in user.created_chats:
            del cls.chats[chat_id]
            user.created_chats.remove(chat_id)
            print("💥 Chat deleted! Your digital footprint has been erased.")
        else:
            print("🚫 You can only delete your own chats!")

    
    def show_all_messages(cls, chat_id, user):
        """
        Displays all messages in the chat, showing user messages on the right and others' messages on the left.

        :param chat_id: The ID of the chat to display messages from
        :param user: The user requesting to see the messages
        """
        chat = cls.chats.get(chat_id)
        if chat:
            if chat.is_hidden_for_user(user.username):
                print("🔒 Messages are hidden for you. Select 'Do not send message' to show them.")
            else:
                for message in chat.messages:
                    if message['user'] == user.username:
                        print(f"  {message['user']}: {message['message']}".rjust(80))  # User's messages on the right
                    else:
                        print(f"{message['user']}: {message['message']}")  # Other users' messages on the left

    
    def send_message(cls, user, chat_id, message):
        """
        Sends a message to the chat and displays all messages after sending.

        :param user: The user sending the message
        :param chat_id: The ID of the chat to send the message to
        :param message: The message content
        """
        chat = cls.chats.get(chat_id)
        if chat:
            chat.messages.append({'user': user.username, 'message': message})
            cls.show_all_messages(chat_id, user)  # Show all messages after sending

    
    def hide_messages(cls, user, chat_id):
        """
        Hides messages for the user in the specified chat.

        :param user: The user requesting to hide messages
        :param chat_id: The ID of the chat to hide messages in
        """
        chat = cls.chats.get(chat_id)
        if chat:
            if user.username not in chat.hidden_users:
                chat.hidden_users.append(user.username)
                print("👻 Messages are now hidden from your view. Select 'Send message' to reveal them.")
            else:
                print("🔍 Messages are already hidden for you.")

    
    def save_data(cls):
        """
        Saves all user and chat data to a JSON file.
        """
        with open('data.json', 'w') as f:
            data = {
                'users': {
                    username: {
                        'full_name': user.full_name,
                        'password': user.password,
                        'created_chats': user.created_chats,
                        'joined_chats': user.joined_chats
                    }
                    for username, user in AuthManager.users.items()
                },
                'chats': {
                    chat_id: {
                        'password': chat.password,
                        'messages': chat.messages,
                        'owner': chat.owner,
                        'hidden_users': chat.hidden_users
                    }
                    for chat_id, chat in cls.chats.items()
                }
            }
            json.dump(data, f, indent=4)

    
    def load_data(cls):
        """
        Loads user and chat data from a JSON file.
        """
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
                for username, user_data in data['users'].items():
                    user = User(user_data['full_name'], username, user_data['password'])
                    user.created_chats = user_data['created_chats']
                    user.joined_chats = user_data['joined_chats']
                    AuthManager.users[username] = user
                for chat_id, chat_data in data['chats'].items():
                    chat = Chat(chat_data['owner'], chat_data['password'])
                    chat.messages = chat_data['messages']
                    chat.hidden_users = chat_data.get('hidden_users', [])  # Default to empty list if not present
                    cls.chats[chat_id] = chat
        except FileNotFoundError:
            pass

class AuthManager:
    users = {}
    current_user = None

    
    def register(cls):
        """
        Registers a new user with full name, username, and password.

        :return: None
        """
        full_name = input("Full Name: ")
        username = input("Username: ")
        if username in cls.users:
            print("🚨 Username already exists! Try a different one.")
            return
        password = input("Password: ")
        cls.users[username] = User(full_name, username, password)
        print("🎉 Registration successful! You can now log in.")
        ChatManager.save_data()

    
    def login(cls):
        """
        Logs in a user with username and password.

        :return: None
        """
        username = input("Username: ")
        password = input("Password: ")
        user = cls.users.get(username)
        if user and user.password == User.hash_password(password):
            cls.current_user = user
            print("🚀 Login successful! Welcome back, " + user.full_name + "!")
        else:
            print("❌ Invalid username or password. Please try again.")

    
    def logout(cls):
        """
        Logs out the current user.

        :return: None
        """
        cls.current_user = None

def auth_menu():
    """
    Displays the authentication menu for registering, logging in, or exiting.

    :return: None
    """
    while True:
        print("\nAuth Menu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            AuthManager.register()
        elif choice == '2':
            AuthManager.login()
            if AuthManager.current_user:
                main_menu()
                AuthManager.logout()
        elif choice == '3':
            print("Exiting... Have a great day!")
            break
        else:
            print("🔄 Invalid option! Please select a valid option.")

def main_menu():
    """
    Displays the main menu for creating, joining, deleting chats, and viewing created or joined chats.

    :return: None
    """
    while True:
        print("\nMain Menu:")
        print("1. Create chat")
        print("2. Join the chat")
        print("3. Delete chat")
        print("4. Show my created chats")
        print("5. Show my joined chats")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            ChatManager.create_chat(AuthManager.current_user)
        elif choice == '2':
            ChatManager.join_chat(AuthManager.current_user)
        elif choice == '3':
            chat_id = input("Enter chat ID to delete: ")
            ChatManager.delete_chat(AuthManager.current_user, chat_id)
        elif choice == '4':
            created_chats = AuthManager.current_user.created_chats
            if created_chats:
                print("🌟 Your created chats: ", created_chats)
            else:
                print("😔 You did not create any chats. Get started by creating one!")
        elif choice == '5':
            joined_chats = AuthManager.current_user.joined_chats
            if joined_chats:
                print("📚 Your joined chats: ", joined_chats)
            else:
                print("😞 You did not join any chats. Find some interesting chats to join!")
        elif choice == '6':
            ChatManager.save_data()
            print("🛑 Exiting... See you next time!")
            break
        else:
            print("❓ Invalid option! Please choose a valid option from the menu.")

def chat_menu(chat_id):
    """
    Displays the chat menu for sending messages, hiding messages, or exiting the chat.

    :param chat_id: The ID of the chat to manage
    :return: None
    """
    while True:
        print("\nChat Menu:")
        print("1. Send message")
        print("2. Do not send message")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            ChatManager.show_all_messages(chat_id, AuthManager.current_user)  # Show all messages before sending a new one
            message = input("Enter your message: ")
            ChatManager.send_message(AuthManager.current_user, chat_id, message)
        elif choice == '2':
            ChatManager.hide_messages(AuthManager.current_user, chat_id)  # Hide messages
        elif choice == '3':
            print("👋 Exiting chat... Hope you had a good time!")
            break
        else:
            print("⚠️ Invalid option! Please choose a valid option from the chat menu.")

if __name__ == "__main__":
    ChatManager.load_data()
    auth_menu()