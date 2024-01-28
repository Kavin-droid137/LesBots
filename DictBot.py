import streamlit as st
from nltk.chat.util import Chat, reflections
import requests
from bs4 import BeautifulSoup

# Define patterns and responses for chatbot
chat_pairs = [
    ["hi|hello|sup", ["Hello!", "Hi there!", "Greetings!"]],
    ["how are you|how r u", ["I'm good, thank you!", "I'm doing well."]],
    ["what's your name|your name", ["You can call me ChatBot."]],
    ["bye|bai|see ya|brb|see u|gtg", ["Goodbye!", "Farewell!", "See you later!"]],
    ["your age", ["I don't have an age. I'm just a program."]],
    ["who created you", ["I was created by a team, Python, and NLTK."]],
    ["what can you do", ["I can answer your questions and engage in conversation."]],
    [r"", ["I'm not sure how to respond. Feel free to ask me anything!"]],
]

# Create a chatbot
chatbot = Chat(chat_pairs, reflections)


# Define function to get word definitions from Merriam-Webster
def get_word_definitions_online(word):
    url = f"https://www.merriam-webster.com/dictionary/{word}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find definition elements on the page
        definition_elements = soup.find_all('span', class_='dtText')

        if not definition_elements:
            return None

        definitions = [element.get_text() for element in definition_elements]
        return definitions
    else:
        return None


# Streamlit App
def main():
    st.title("DictBot helps you in Definitions")

    st.sidebar.header("DictBot")
    user_input = st.sidebar.text_input("You:", key="input")

    # Check if the user wants to exit
    if user_input.lower() == 'bye':
        st.sidebar.text("ChatBot: Goodbye!")
    elif user_input.lower().startswith('define'):
        # Extract the word after 'define'
        word_to_define = ' '.join(user_input.split()[1:])
        definitions = get_word_definitions_online(word_to_define)

        if definitions:
            st.success(f"Definitions for {word_to_define}:")
            for definition in definitions:
                st.text(definition)
        else:
            st.error(f"Sorry, definitions not found for {word_to_define}.")
    else:
        response = chatbot.respond(user_input)
        st.text("ChatBot: " + response)


if __name__ == "__main__":
    main()
