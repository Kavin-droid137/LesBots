import streamlit as st
from nltk.chat.util import Chat, reflections

# Define patterns and responses for chatbot
chat_pairs = [
    ["hi|hello|sup", ["Hello!", "Hi there!", "Greetings!"]],
    ["how are you|how r u", ["I'm good, thank you!", "I'm doing well."]],
    ["what's your name|your name", ["You can call me ChatBot."]],
    ["bye|bai|see ya|brb|see u|gtg", ["Goodbye!", "Farewell!", "See you later!"]],
    ["your age", ["I don't have an age. I'm just a program."]],
    ["who created you", ["I was created by a team, Python, and NLTK."]],
    ["what can you do", ["I can engage in conversation."]],
    [r"", ["I'm not sure how to respond. Feel free to ask me anything!"]],
]

# Create a chatbot
chatbot = Chat(chat_pairs, reflections)

# Streamlit App
st.title("ChatBot Messaging App")

messages = []

# Interactive Chat
user_input = st.text_input("Tell Something Here! ", key="user_input")

# Check if the user wants to exit
if user_input.lower() == 'bye':
    messages.append(("You:", user_input))
    messages.append(("ChatBot:", "Goodbye!"))
else:
    # Get chatbot response
    response = chatbot.respond(user_input)
    messages.append(("You:", user_input))
    messages.append(("ChatBot:", response))

# Display messages in a chat-like format
for role, message in messages:
    if role == "You:":
        st.text_area(role, message, key="user_messages", height=100, max_chars=200, disabled=True)
    else:
        st.text_area(role, message, key="bot_messages", height=100, max_chars=200, disabled=True)
