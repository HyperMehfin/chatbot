import streamlit as st
import difflib
# This imports the data we just created in data.py
from data import kb as techfest_data  

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Vedhayukham",
    page_icon="🤖",
    layout="centered"
)

# --- CUSTOM CSS (Cyberpunk/Tech Look) ---
st.markdown("""
<style>
    /* Main Background */
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    /* Chat message bubbles */
    .stChatMessage {
        background-color: #262730;
        border-radius: 15px;
        border: 1px solid #444;
    }
    /* Headers */
    h1 {
        color: #00e676; /* Neon Green */
        text-align: center;
        font-family: 'Courier New', monospace;
        text-shadow: 0px 0px 10px #00e676;
    }
    /* Links */
    a {
        color: #29b6f6 !important;
        text-decoration: none;
        font-weight: bold;
    }
    /* Input box */
    .stChatInputContainer {
        border-top: 1px solid #444;
    }
</style>
""", unsafe_allow_html=True)

# --- LOGIC FUNCTION ---
def get_bot_response(user_input):
    user_input = user_input.lower()
    
    best_match_key = None
    highest_score = 0
    
    # Check all topics in our data.py
    for key, data in techfest_data.items():
        for keyword in data["keywords"]:
            # 1. Direct Match
            if keyword in user_input:
                return data["response"]
            
            # 2. Fuzzy Match (for typos like "gamign")
            similarity = difflib.SequenceMatcher(None, keyword, user_input).ratio()
            if similarity > 0.6 and similarity > highest_score:
                highest_score = similarity
                best_match_key = key

    # Return best fuzzy match if confidence is high enough
    if best_match_key and highest_score > 0.6:
        return techfest_data[best_match_key]["response"]
    
    # Fallback
    return "🤖 I didn't catch that. Try asking about **Schedule**, **Gaming**, **Hackathon**, or **Food**!"

# --- MAIN APP ---
def main():
    st.title("⚡ TechFest 2K26 Guide")
    st.caption("Locate events, rooms, and schedules instantly.")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Welcome! 🚀 I have the full schedule and room map. What are you looking for?"}
        ]

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat Input
    if prompt := st.chat_input("Ask me... (e.g. 'Where is the Snow Room?')"):
        # User message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Bot Response
        response = get_bot_response(prompt)
        
        # Assistant message
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()