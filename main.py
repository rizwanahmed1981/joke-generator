import streamlit as st
import requests

def get_random_joke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']}😊😊 \n\n {joke_data['punchline']}🤣🤣"
        else:
            return "Failed to fetch a random joke."
    except:
        return "Why programmer left his job? \n Because he didn't get a random joke."
def main():   
    st.title("Random Joke Generator")
    st.write("Hit Button To Generate A Joke")

    if st.button("Generate Joke"):
        joke = get_random_joke()
    st.success(f"{joke}")


if __name__ == "__main__":
    main()