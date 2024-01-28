import streamlit as st
from nltk.chat.util import Chat, reflections
import re
import requests

# Define patterns and responses for chatbot
chat_pairs = [
    ["hi|hello|sup", ["Hello!", "Hi there!", "Greetings!"]],
    ["how are you|how r u", ["I'm good, thank you!", "I'm doing well."]],
    ["what's your name|your name", ["You can call me ChatBot."]],
    ["bye|bai|see ya|brb|see u|gtg", ["Goodbye!", "Farewell!", "See you later!"]],
    ["your age", ["I don't have an age. I'm just a program."]],
    ["who created you", ["I was created by a team, Python, and NLTK."]],
    ["what can you do", ["I can engage in conversation.",
                        "I can help you with basic math. Just type a math expression like '2 + 2'."
                        ]],
    ["get news", ["Sure! Fetching the latest news...", "Let me get the news for you.", "Fetching news headlines..."]],
    [r"", ["I'm not sure how to respond. Feel free to ask me anything!"]],
]

# Create a chatbot
chatbot = Chat(chat_pairs, reflections)

# Function to evaluate math expressions
def evaluate_math_expression(expression):
    try:
        result = eval(expression)
        return f"The result of '{expression}' is: {result}"
    except Exception as e:
        return f"Error evaluating the expression: {str(e)}"

# Streamlit App
st.title("ChatBot with Math Evaluation")

# User input for chatbot
user_input = st.text_input("You:")

# Check if the user wants to exit
if user_input.lower() == 'bye':
    st.text("ChatBot: Goodbye!")
else:
    # Check if it's a math expression
    if re.match(r'^\s*\d+(\s*[-+*/]\s*\d+)+\s*$', user_input):
        st.text("ChatBot: " + evaluate_math_expression(user_input))
