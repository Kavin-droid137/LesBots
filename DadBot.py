import streamlit as st
from nltk.chat.util import Chat, reflections
import requests
from bs4 import BeautifulSoup
import re

# Define patterns and responses for chatbot
chat_pairs = [
    ["hi|hello|sup", ["Hello!", "Hi there!", "Greetings!"]],
    ["how are you|how r u", ["I'm good, thank you!", "I'm doing well."]],
    ["what's your name|your name", ["You can call me ChatBot."]],
    ["bye|bai|see ya|brb|see u|gtg", ["Goodbye!", "Farewell!", "See you later!"]],
    ["your age", ["I don't have an age. I'm just a program."]],
    ["who created you", ["I was created by a team, Python, and NLTK."]],
    ["what can you do", ["I can answer your questions and engage in conversation.",
                        "I can provide you with the latest news. Please type 'get news' to receive news updates.",
                        "I can also help you with basic math. Just type a math expression like '2 + 2'."
                        ]],
    ["get news", ["Sure! Fetching the latest news...", "Let me get the news for you.", "Fetching news headlines..."]],
    [r"", ["I'm not sure how to respond. Feel free to ask me anything!"]],
]

# Common diseases dictionary
common_diseases = {
    'flu': {
        'Symptoms': ['Fever', 'Cough', 'Fatigue', 'Muscle aches'],
        'Causes': ['Influenza viruses'],
        'Medicines': ['Antiviral medications (e.g., Oseltamivir)', 'Pain relievers (e.g., Acetaminophen)', 'Cough suppressants']
    },
    'common cold': {
        'Symptoms': ['Runny nose', 'Sneezing', 'Sore throat', 'Cough'],
        'Causes': ['Rhinoviruses', 'Coronaviruses'],
        'Medicines': ['Decongestants', 'Antihistamines', 'Cough syrups']
    },
    'migraine': {
        'Symptoms': ['Severe headaches', 'Nausea', 'Sensitivity to light'],
        'Causes': ['Genetics', 'Hormonal changes', 'Triggers like certain foods'],
        'Medicines': ['Pain relievers (e.g., Ibuprofen)', 'Triptans', 'Anti-nausea medications']
    },
    'alzheimers disease': {
        'Symptoms': ['Memory loss', 'Difficulty in problem-solving', 'Confusion'],
        'Causes': ['Genetics', 'Age-related changes in the brain'],
        'Medicines': ['Cholinesterase inhibitors (e.g., Donepezil)', 'Memantine']
    },
    'rheumatoid arthritis': {
        'Symptoms': ['Joint pain', 'Swelling', 'Fatigue'],
        'Causes': ['Autoimmune response'],
        'Medicines': ['Nonsteroidal anti-inflammatory drugs (NSAIDs)', 'Disease-modifying antirheumatic drugs (DMARDs)']
    },
    'chronic kidney disease': {
        'Symptoms': ['Fatigue', 'Swelling in extremities', 'Changes in urine output'],
        'Causes': ['Diabetes', 'High blood pressure', 'Kidney infections'],
        'Medicines': ['Blood pressure medications', 'Diuretics', 'Erythropoiesis-stimulating agents (ESA)']
    },
}

# Create a chatbot
chatbot = Chat(chat_pairs, reflections)

# Function to get word definitions from Merriam-Webster
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

# Function to display disease information
def display_disease_info(disease):
    if disease in common_diseases:
        disease_info = common_diseases[disease]
        st.write(f"\nDescription for {disease.capitalize()}:")
        st.write("Symptoms:", ', '.join(disease_info['Symptoms']))
        st.write("Causes:", ', '.join(disease_info['Causes']))
        st.write("Medication:", ', '.join(disease_info['Medicines']))
    else:
        st.write(f"Sorry, information not found for {disease}.")

# Function to identify disease by symptoms
def identify_disease_by_symptoms(symptoms):
    symptoms_lower = set(symptom.lower() for symptom in symptoms)
    possible_diseases = [disease for disease, info in common_diseases.items() if symptoms_lower.intersection(map(str.lower, info['Symptoms']))]
    return possible_diseases

# Function to get the latest news
def get_latest_news():
    url = "https://newsapi.org/v2/top-headlines"
    api_key = "3eb34ba10f7f42d39057aa61b91c0726"  # Replace with your News API key
    params = {"country": "us", "apiKey": api_key}

    response = requests.get(url, params=params)
    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get("articles", [])

        if articles:
            st.write("\nLatest News Headlines:")
            for index, article in enumerate(articles, start=1):
                st.write(f"{index}. {article['title']} - {article['url']}")
        else:
            st.write("No news articles found.")
    else:
        st.write("Failed to fetch news.")

# Function to evaluate math expressions
def evaluate_math_expression(expression):
    try:
        result = eval(expression)
        return f"The result of '{expression}' is: {result}"
    except Exception as e:
        return f"Error evaluating the expression: {str(e)}"

# Streamlit app
st.title("Interactive ChatBot")

# Sidebar for selecting functionalities
selected_functionality = st.sidebar.selectbox("Select Functionality", ["Chat", "Define Word", "Disease Info", "Symptoms", "Get News", "Math Expression"])

# Interactive Chat
if selected_functionality == "Chat":
    st.write("ChatBot: Hello! I'm a simple chatbot. Ask me anything.")

    user_input = st.text_input("You:")
    if st.button("Submit"):
        response = chatbot.respond(user_input)
        st.write("ChatBot:", response)

elif selected_functionality == "Define Word":
    st.write("Ask me the definition of a word by typing 'define [word]'.")

    word_to_define = st.text_input("Word:")
    if st.button("Define"):
        definitions = get_word_definitions_online(word_to_define)

        if definitions:
            st.write(f"Definitions for {word_to_define}:")
            for definition in definitions:
                st.write(definition)
        else:
            st.write(f"Sorry, definitions not found for {word_to_define}.")

elif selected_functionality == "Disease Info":
    st.write("Ask me the description of a disease.")

    disease_to_describe = st.selectbox("Select Disease", ['flu', 'common cold', 'migraine', 'alzheimers disease', 'rheumatoid arthritis', 'chronic kidney disease'])
    if st.button("Get Info"):
        display_disease_info(disease_to_describe)

elif selected_functionality == "Symptoms":
    st.write("Provide symptoms to identify a disease.")

    provided_symptoms = st.text_input("Enter Symptoms (comma-separated):")
    if st.button("Identify Disease"):
        provided_symptoms = provided_symptoms.split(',')
        provided_symptoms = [symptom.strip() for symptom in provided_symptoms]
        identified_disease = identify_disease_by_symptoms(provided_symptoms)
        if identified_disease:
            st.write(f"ChatBot: Based on the provided symptoms, it could be {identified_disease.capitalize()}.")
            disease_info = common_diseases[identified_disease]
            st.write("Symptoms:", ', '.join(disease_info['Symptoms']))
            st.write("Causes:", ', '.join(disease_info['Causes']))
            st.write("Medication:", ', '.join(disease_info['Medicines']))
        else:
            st.write("ChatBot: No matching disease found for the provided symptoms.")

elif selected_functionality == "Get News":
    st.write("Get the latest news by typing 'get news'.")

    if st.button("Fetch News"):
        get_latest_news()

elif selected_functionality == "Math Expression":
    st.write("Perform math calculations by typing a math expression.")

    math_expression = st.text_input("Math Expression:")
    if st.button("Evaluate"):
        st.write("ChatBot:", evaluate_math_expression(math_expression))
