import streamlit as st


def math_bot_page():
    st.title("MathBot Page")
    # Add content for MathBot page
    st.write("This is the MathBot page. Perform mathematical operations here.")


def dict_bot_page():
    st.title("DictBot Page")
    # Add content for DictBot page
    st.write("This is the DictBot page. Look up definitions and meanings here.")


def news_bot_page():
    st.title("NewsBot Page")
    # Add content for NewsBot page
    st.write("This is the NewsBot page. Stay updated with the latest news.")


def dad_bot_page():
    st.title("DadBot Page")
    # Add content for DadBot page
    st.write("This is the DadBot page. Enjoy some dad jokes here.")


def chat_bot_page():
    st.title("ChatBot Page")
    # Add content for ChatBot page
    st.write("This is the ChatBot page. Have a chat with our friendly bot.")


def med_bot_page():
    st.title("MedBot Page")
    # Add content for MedBot page
    st.write("This is the MedBot page. Get health-related information here.")


def contributors_page():
    st.title("Contributors")
    st.write("Meet the contributors:")
    st.write("- Kavin")
    st.write("- Tanash")
    st.write("- Aditi")
    st.write("- Sonakshi")
    st.write("- Arjun")


def main():
    st.title("My Streamlit Home Page")

    # Add content to your home page
    st.write("Welcome to my Streamlit home page! This is a simple example.")

    # Add sections or features
    st.header("Sections:")

    # Create buttons to redirect to different pages
    if st.button("MathBot"):
        math_bot_page()

    if st.button("DictBot"):
        dict_bot_page()

    if st.button("NewsBot"):
        news_bot_page()

    if st.button("DadBot"):
        dad_bot_page()

    if st.button("ChatBot"):
        chat_bot_page()

    if st.button("MedBot"):
        med_bot_page()

    # Add Contributors section
    if st.button("Contributors"):
        contributors_page()


if __name__ == "__main__":
    main()
