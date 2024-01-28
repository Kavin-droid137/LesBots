import streamlit as st
from nltk.chat.util import Chat, reflections
import requests

# Define patterns and responses for chatbot
chat_pairs = [
    ["hi|hello|sup", ["Hello!", "Hi there!", "Greetings!"]],
    ["how are you|how r u", ["I'm good, thank you!", "I'm doing well."]],
    ["what's your name|your name", ["You can call me ChatBot."]],
    ["bye|bai|see ya|brb|see u|gtg", ["Goodbye!", "Farewell!", "See you later!"]],
    ["tq|thank u|thanks|thx|thnx|thank you", ["Welcome!", "Anytime!", "Sure!"]],
    ["your age", ["I don't have an age. I'm just a program."]],
    ["who created you", ["I was created by a team, Python, and NLTK."]],
    ["what can you do", ["I can answer your questions and engage in conversation.",
                        "I can provide you with the latest news. Please type 'get news' to receive news updates.",
                        "I can also help you with basic math. Just type a math expression like '2 + 2'."
                        ]],
    ["get news", ["Sure! Fetching the latest news...", "Let me get the news for you.", "Fetching news headlines..."]],
    [r"", ["I'm not sure how to respond. Feel free to ask me anything!"]],
]

# Create a chatbot
chatbot = Chat(chat_pairs, reflections)

# Function to get latest news
def get_latest_news():
    url = "https://newsapi.org/v2/top-headlines"
    api_key = "3eb34ba10f7f42d39057aa61b91c0726"  # Replace with your News API key
    params = {"country": "us", "apiKey": api_key}

    response = requests.get(url, params=params)
    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get("articles", [])

        if articles:
            st.success("Latest News Headlines:")
            for index, article in enumerate(articles, start=1):
                st.info(f"{index}. {article['title']} - [Read More]({article['url']})")
        else:
            st.warning("No news articles found.")
    else:
        st.error("Failed to fetch news.")

# Streamlit App
def main():
    st.title("ChatBot with News Headlines")

    # User input
    user_input = st.text_input("You:")
    user_input = user_input.lower().strip()

    # Check if the user wants to exit
    if user_input == 'bye':
        st.text("ChatBot: Goodbye!")
    elif user_input == 'get news':
        get_latest_news()
    else:
        # Chatbot response
        response = chatbot.respond(user_input)
        st.text("ChatBot: " + response)

if __name__ == "__main__":
    main()
