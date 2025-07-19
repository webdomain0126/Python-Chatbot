import re
import random

# Define pattern-response pairs
patterns = [
    [
        r"(?i)\b(hi|hello|hey)\b",
        ["Hello! 👋", "Hi there!", "Hey! How can I assist you? 😊"]
    ],
    [
        r"(?i)\bwhat is your name\b",
        ["I'm a Python chatbot built by Tisa. 🤖"]
    ],
    [
        r"(?i)\bhow are you\b",
        ["I'm doing well, thanks! And you?", "All systems go! 🚀", "I'm great!"]
    ],
    [
        r"(?i)\bsorry\b.*",
        ["No problem!", "It's okay.", "Never mind."]
    ],
    [
        r"(?i)\b(location|city)\b",
        ["I'm in the cloud. ☁️"]
    ],
    [
        r"(?i)\bwho (created|made) you\b",
        ["I was created by Tisa, the Python enthusiast! 👩‍💻"]
    ],
    [
        r"(?i)\b(help|assist)\b",
        ["Sure, how can I help you?", "Happy to assist! 🙌"]
    ],
    [
        r"(?i)\b(bye|goodbye|see you)\b",
        ["Goodbye!", "See you later!", "Bye! Have a great day! 👋"]
    ],
    [
        r"(?i)\b(hobby|do you like)\b",
        ["I like learning new things and chatting with you! 🤓"]
    ],
    [
        r"(?i)\b(python|programming)\b",
        ["Python is my favorite language too! 🐍", "I love coding!"]
    ]
]

# Get chatbot response
def get_response(user_input):
    for pattern, responses in patterns:
        if re.search(pattern, user_input):
            return random.choice(responses)
    return "Sorry, I didn't understand that. 🤖 Try asking something else!"

# Start chatbot
def chat():
    print("🤖 Chatbot is ready! Type 'quit' to exit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye! 👋")
            break
        response = get_response(user_input)
        print("Chatbot:", response)

# Run chatbot
if __name__ == "__main__":
    chat()

